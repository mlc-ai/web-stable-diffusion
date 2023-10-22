from platform import system

import tvm
from tvm import relax
from tvm.relax.frontend.torch import dynamo_capture_subgraphs
from tvm.relax.frontend.torch import from_fx
from tvm.script import relax as R

import torch
from torch import fx

from web_stable_diffusion import trace
from web_stable_diffusion import utils

torch_dev_key = "cpu"

target = tvm.target.Target("apple/m1-gpu")
device = tvm.metal()

def clip_to_text_embeddings(pipe) -> tvm.IRModule:
    # Define the wrapper torch.nn.Module for CLIP.
    class CLIPModelWrapper(torch.nn.Module):
        def __init__(self, clip):
            super().__init__()
            self.clip = clip

        def forward(self, text_input_ids):
            text_embeddings = self.clip(text_input_ids)[0]
            return text_embeddings

    clip = pipe.text_encoder
    clip_to_text_embeddings = CLIPModelWrapper(clip)

    # Create random input (77 is the maximum length).
    text_input_ids = torch.rand((1, 77)).to(torch.int32)
    # Capture CLIP's computational graph.
    mod = dynamo_capture_subgraphs(
        clip_to_text_embeddings.forward,
        text_input_ids,
        keep_params_as_input=True,
    )
    assert len(mod.functions) == 1

    return tvm.IRModule({"clip": mod["subgraph_0"]})


def concat_embeddings() -> tvm.IRModule:
    bb = relax.BlockBuilder()
    cond_embeddings = relax.Var("cond_embeddings", R.Tensor([1, 77, 768], "float32"))
    uncond_embeddings = relax.Var(
        "uncond_embeddings", R.Tensor([1, 77, 768], "float32")
    )
    with bb.function("concat_embeddings", [cond_embeddings, uncond_embeddings]):
        res = bb.emit(
            relax.op.concat([cond_embeddings, uncond_embeddings], axis=0)
        )
        bb.emit_func_output(res)
    return bb.get()


def unet_latents_to_noise_pred(pipe, device_str: str) -> tvm.IRModule:
    class UNetModelWrapper(torch.nn.Module):
        def __init__(self, unet):
            super().__init__()
            self.unet = unet
            # Default guidance scale factor in stable diffusion.
            self.guidance_scale = 7.5

        def forward(self, latents, timestep_tensor, text_embeddings):
            # Latent concatenation.
            latent_model_input = torch.cat([latents] * 2, dim=0)
            # UNet forward.
            noise_pred = self.unet(latent_model_input, timestep_tensor, text_embeddings)
            # Classifier-free guidance.
            noise_pred_uncond, noise_pred_text = noise_pred.chunk(2)
            noise_pred = noise_pred_uncond + self.guidance_scale * (
                noise_pred_text - noise_pred_uncond
            )
            return noise_pred

    unet = utils.get_unet(pipe, device_str)
    unet_to_noise_pred = UNetModelWrapper(unet)
    graph = fx.symbolic_trace(unet_to_noise_pred)
    mod = from_fx(
        graph,
        [((1, 4, 64, 64), "float32"), ((), "int32"), ((2, 77, 768), "float32")],
        keep_params_as_input=True,
    )
    return tvm.IRModule({"unet": mod["main"]})

def dpm_solver_multistep_scheduler_steps() -> tvm.IRModule:
    bb = relax.BlockBuilder()

    # convert_model_output, the first function in multi-step DPM solver.
    sample = relax.Var("sample", R.Tensor((1, 4, 64, 64), "float32"))
    model_output = relax.Var("model_output", R.Tensor((1, 4, 64, 64), "float32"))
    alpha = relax.Var(f"alpha", R.Tensor((), "float32"))
    sigma = relax.Var(f"sigma", R.Tensor((), "float32"))
    with bb.function(
        "dpm_solver_multistep_scheduler_convert_model_output",
        [sample, model_output, alpha, sigma],
    ):
        converted_model_output = bb.emit(
            (sample - sigma * model_output) / alpha, "converted_model_output"
        )
        bb.emit_func_output(converted_model_output)

    # step, the second function.
    sample = relax.Var("sample", R.Tensor((1, 4, 64, 64), "float32"))
    model_output = relax.Var("model_output", R.Tensor((1, 4, 64, 64), "float32"))
    last_model_output = relax.Var(
        "last_model_output", R.Tensor((1, 4, 64, 64), "float32")
    )
    consts = [relax.Var(f"c{i}", R.Tensor((), "float32")) for i in range(3)]

    with bb.function(
        "dpm_solver_multistep_scheduler_step",
        [sample, model_output, last_model_output, *consts],
    ):
        prev_sample = bb.emit(
            consts[0] * sample
            - consts[1] * model_output
            - consts[2] * (model_output - last_model_output),
            "prev_sample",
        )
        bb.emit_func_output(prev_sample)

    return bb.get()


def vae_to_image(pipe) -> tvm.IRModule:
    class VAEModelWrapper(torch.nn.Module):
        def __init__(self, vae):
            super().__init__()
            self.vae = vae

        def forward(self, latents):
            # Scale the latents so that it can be decoded by VAE.
            latents = 1 / 0.13025 * latents
            # VAE decode
            # z = self.vae.post_quant_conv(latents)
            image = self.vae.decode(latents, return_dict=False)[0]
            # Image normalization
            image = (image / 2 + 0.5).clamp(min=0, max=1)
            image = (image.permute(0, 2, 3, 1) * 255).round()
            return image

    vae = utils.get_vae(pipe, "1.5")
    vae_to_image = VAEModelWrapper(vae)

    graph = fx.symbolic_trace(vae_to_image)
    mod = from_fx(
        graph,
        [((1, 4, 64, 64), "float32")],
        keep_params_as_input=True,
    )
    return tvm.IRModule({"vae": mod["main"]})


def image_to_rgba() -> tvm.IRModule:
    from tvm import te

    def f_image_to_rgba(A):
        def fcompute(y, x):
            return (
                A[0, y, x, 0].astype("uint32")
                | (A[0, y, x, 1].astype("uint32") << 8)
                | (A[0, y, x, 2].astype("uint32") << 16)
                | tvm.tir.const(255 << 24, "uint32")
            )

        return te.compute((512, 512), fcompute, name="image_to_rgba")

    bb = relax.BlockBuilder()
    x = relax.Var("x", R.Tensor([1, 512, 512, 3], "float32"))
    with bb.function("image_to_rgba", [x]):
        image = bb.emit(
            bb.call_te(f_image_to_rgba, x, primfunc_name_hint="tir_image_to_rgba")
        )
        bb.emit_func_output(image)
    return bb.get()

from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("SG161222/Realistic_Vision_V5.1_noVAE")
clip = clip_to_text_embeddings(pipe)
unet = unet_latents_to_noise_pred(pipe, torch_dev_key)
vae = vae_to_image(pipe)
concat_embeddings = concat_embeddings()
image_to_rgba = image_to_rgba()
schedulers = [
    dpm_solver_multistep_scheduler_steps(),
    trace.PNDMScheduler.scheduler_steps()
]

mod: tvm.IRModule = utils.merge_irmodules(
    clip,
    unet,
    vae,
    concat_embeddings,
    image_to_rgba,
    *schedulers,
)

mod, params = relax.frontend.detach_params(mod)

mod = relax.pipeline.get_pipeline()(mod)

model_names = ["clip", "unet", "vae"]
scheduler_func_names = [
    name
    for name in trace.DPMSolverMultistepScheduler.scheduler_steps_func_names()
]
entry_funcs = (
    model_names + scheduler_func_names + ["image_to_rgba", "concat_embeddings"]
)

# Clean up unused parts of the IRModule.
mod = relax.transform.DeadCodeElimination(entry_funcs)(mod)


mod = relax.transform.LiftTransformParams()(mod)

mod_transform, mod_deploy = utils.split_transform_deploy_mod(
    mod, model_names, entry_funcs
)

import pickle

with open("mod_deploy_pt1.pkl", "wb") as f:
    pickle.dump(mod_deploy, f)



# trace.compute_save_scheduler_consts(artifact_path="dist")
# # Compute and save the models's weight parameters.
# new_params = utils.transform_params(mod_transform, params)
# utils.save_params(new_params, artifact_path="dist")


# from tvm import meta_schedule as ms

# db = ms.database.create(work_dir="log_db")
# with target, db, tvm.transform.PassContext(opt_level=3):
#     mod_deploy = relax.transform.MetaScheduleApplyDatabase()(mod_deploy)
#     mod_deploy = tvm.tir.transform.DefaultGPUSchedule()(mod_deploy)


# ex = relax.build(mod=mod_deploy, target=target)


# ex.export_library("dist/stable_diffusion.so")
