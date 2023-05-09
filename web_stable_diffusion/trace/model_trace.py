import torch
import torch.fx as fx

from .. import utils as utils
from . import scheduler_trace as scheduler_trace

import tvm
from tvm import relax
from tvm.relax.frontend.torch import dynamo_capture_subgraphs, from_fx
from tvm.script import relax as R


def clip_to_text_embeddings(pipe) -> tvm.IRModule:
    class CLIPModelWrapper(torch.nn.Module):
        def __init__(self, clip):
            super().__init__()
            self.clip = clip

        def forward(self, text_input_ids):
            text_embeddings = self.clip(text_input_ids)[0]
            return text_embeddings

    clip = pipe.text_encoder
    clip_to_text_embeddings = CLIPModelWrapper(clip)

    text_input_ids = torch.rand((1, 77)).to(torch.int32)
    mod = dynamo_capture_subgraphs(
        clip_to_text_embeddings.forward,
        text_input_ids,
        keep_params_as_input=True,
    )
    assert len(mod.functions) == 1

    return tvm.IRModule({"clip": mod["subgraph_0"]})


def unet_latents_to_noise_pred(pipe, device_str: str) -> tvm.IRModule:
    class UNetModelWrapper(torch.nn.Module):
        def __init__(self, unet):
            super().__init__()
            self.unet = unet
            self.guidance_scale = 7.5

        def forward(self, latents, timestep_tensor, text_embeddings):
            latent_model_input = torch.cat([latents] * 2, dim=0)
            noise_pred = self.unet(latent_model_input, timestep_tensor, text_embeddings)
            noise_pred_uncond, noise_pred_text = noise_pred.chunk(2)
            noise_pred = noise_pred_uncond + self.guidance_scale * (
                noise_pred_text - noise_pred_uncond
            )
            return noise_pred

    hidden_size = pipe.unet.config.cross_attention_dim
    attention_head_dim = pipe.unet.config.attention_head_dim
    use_linear_projection = pipe.unet.config.get("use_linear_projection")

    unet = utils.get_unet(
        pipe,
        device_str,
        cross_attention_dim=hidden_size,
        attention_head_dim=attention_head_dim,
        use_linear_projection=use_linear_projection,
    )

    unet_to_noise_pred = UNetModelWrapper(unet)
    graph = fx.symbolic_trace(unet_to_noise_pred)
    mod = from_fx(
        graph,
        [((1, 4, 64, 64), "float32"), ((), "int32"), ((2, 77, hidden_size), "float32")],
        keep_params_as_input=True,
    )
    return tvm.IRModule({"unet": mod["main"]})


def vae_to_image(pipe) -> tvm.IRModule:
    class VAEModelWrapper(torch.nn.Module):
        def __init__(self, vae):
            super().__init__()
            self.vae = vae

        def forward(self, latents):
            latents = 1 / 0.18215 * latents
            z = self.vae.post_quant_conv(latents)
            image = self.vae.decoder(z)
            image = (image / 2 + 0.5).clamp(min=0, max=1)
            image = (image.permute(0, 2, 3, 1) * 255).round()
            return image

    vae = pipe.vae
    vae_to_image = VAEModelWrapper(vae)

    z = torch.rand((1, 4, 64, 64), dtype=torch.float32)
    mod = dynamo_capture_subgraphs(
        vae_to_image.forward,
        z,
        keep_params_as_input=True,
    )
    assert len(mod.functions) == 1

    return tvm.IRModule({"vae": mod["subgraph_0"]})


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
        with bb.dataflow():
            gv = bb.emit_output(
                bb.call_te(f_image_to_rgba, x, primfunc_name_hint="tir_image_to_rgba")
            )
        bb.emit_func_output(gv)
    return bb.get()


def concat_embeddings() -> tvm.IRModule:
    bb = relax.BlockBuilder()
    cond_embeddings = relax.Var("cond_embeddings", R.Tensor([1, 77, 768], "float32"))
    uncond_embeddings = relax.Var(
        "uncond_embeddings", R.Tensor([1, 77, 768], "float32")
    )
    with bb.function("concat_embeddings", [cond_embeddings, uncond_embeddings]):
        with bb.dataflow():
            gv = bb.emit_output(
                relax.op.concat([cond_embeddings, uncond_embeddings], axis=0)
            )
        bb.emit_func_output(gv)
    return bb.get()
