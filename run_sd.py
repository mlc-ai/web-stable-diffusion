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

if system() == "Darwin":
    target = tvm.target.Target("apple/m1-gpu")
    device = tvm.metal()
else:
    target = tvm.target.Target("cuda" if has_gpu else "llvm")
    device = tvm.cuda() if has_gpu else tvm.cpu()


# Load the model weight parameters back.
const_params_dict = utils.load_params(artifact_path="dist", device=device)
# Load the model executable back from the shared library.
ex = tvm.runtime.load_module("dist/stable_diffusion.so")


vm = relax.VirtualMachine(rt_mod=ex, device=device)


import json
import numpy as np

from web_stable_diffusion import runtime


class DPMSolverMultistepScheduler(runtime.Scheduler):
    scheduler_name = "multistep-dpm-solver"

    def __init__(self, artifact_path: str, device) -> None:
        # Load the scheduler constants.
        with open(
            f"{artifact_path}/scheduler_dpm_solver_multistep_consts.json", "r"
        ) as file:
            jsoncontent = file.read()
        scheduler_consts = json.loads(jsoncontent)

        def f_convert(data, dtype):
            return [tvm.nd.array(np.array(t, dtype=dtype), device) for t in data]

        self.timesteps = f_convert(scheduler_consts["timesteps"], "int32")
        self.alpha = f_convert(scheduler_consts["alpha"], "float32")
        self.sigma = f_convert(scheduler_consts["sigma"], "float32")
        self.c0 = f_convert(scheduler_consts["c0"], "float32")
        self.c1 = f_convert(scheduler_consts["c1"], "float32")
        self.c2 = f_convert(scheduler_consts["c2"], "float32")

        # Initialize the model_output history.
        self.last_model_output: tvm.nd.NDArray = tvm.nd.empty(
            (1, 4, 64, 64), "float32", device
        )

    def step(
        self,
        vm: relax.VirtualMachine,
        model_output: tvm.nd.NDArray,
        sample: tvm.nd.NDArray,
        counter: int,
    ) -> tvm.nd.NDArray:
        # Invoke the functions through VM.
        model_output = vm["dpm_solver_multistep_scheduler_convert_model_output"](
            sample, model_output, self.alpha[counter], self.sigma[counter]
        )
        prev_latents = vm["dpm_solver_multistep_scheduler_step"](
            sample,
            model_output,
            self.last_model_output,
            self.c0[counter],
            self.c1[counter],
            self.c2[counter],
        )
        self.last_model_output = model_output
        return prev_latents
    

from PIL import Image
from tqdm import tqdm
from transformers import CLIPTokenizer


class TVMSDPipeline:
    def __init__(
        self,
        vm: relax.VirtualMachine,
        tokenizer: CLIPTokenizer,
        scheduler: runtime.Scheduler,
        tvm_device,
        param_dict,
    ):
        def wrapper(f, params):
            def wrapped_f(*args):
                return f(*args, params)

            return wrapped_f

        self.vm = vm
        self.clip_to_text_embeddings = wrapper(vm["clip"], param_dict["clip"])
        self.unet_latents_to_noise_pred = wrapper(vm["unet"], param_dict["unet"])
        self.vae_to_image = wrapper(vm["vae"], param_dict["vae"])
        self.concat_embeddings = vm["concat_embeddings"]
        self.image_to_rgba = vm["image_to_rgba"]
        self.tokenizer = tokenizer
        self.scheduler = scheduler
        self.tvm_device = tvm_device
        self.param_dict = param_dict

    def __call__(self, prompt: str, negative_prompt: str = ""):
        # The height and width are fixed to 512.

        # Compute the embeddings for the prompt and negative prompt.
        list_text_embeddings = []
        for text in [negative_prompt, prompt]:
            text = [text]
            # Tokenize the text.
            text_inputs = self.tokenizer(
                text,
                padding="max_length",
                max_length=self.tokenizer.model_max_length,  # 77
                return_tensors="pt",
            )
            text_input_ids = text_inputs.input_ids.to(torch.int32)
            # Clip the text if the length exceeds the maximum allowed length.
            if text_input_ids.shape[-1] > self.tokenizer.model_max_length:
                text_input_ids = text_input_ids[:, : self.tokenizer.model_max_length]

            # Compute text embeddings.
            text_input_ids = tvm.nd.array(text_input_ids.cpu().numpy(), self.tvm_device)
            print("text input id", text_input_ids)
            print("data type", text_input_ids.dtype)
            text_embeddings = self.clip_to_text_embeddings(text_input_ids)
            list_text_embeddings.append(text_embeddings)
        
        # Concatenate the text embeddings.
        text_embeddings = self.concat_embeddings(*list_text_embeddings)

        print("text embedding")

        # Randomly initialize the latents.
        latents = torch.randn(
            (1, 4, 64, 64),
            device="cpu",
            dtype=torch.float32,
        )
        latents = tvm.nd.array(latents.numpy(), self.tvm_device)

        # UNet iteration.
        for i in tqdm(range(len(self.scheduler.timesteps))):
            t = self.scheduler.timesteps[i]
            noise_pred = self.unet_latents_to_noise_pred(latents, t, text_embeddings)
            latents = self.scheduler.step(self.vm, noise_pred, latents, i)

        # VAE decode.
        image = self.vae_to_image(latents)

        # Transform generated image to RGBA mode.
        image = self.image_to_rgba(image)
        return Image.fromarray(image.numpy().view("uint8").reshape(512, 512, 4))
    

pipe = TVMSDPipeline(
    vm=vm,
    tokenizer=CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14"),
    scheduler=runtime.DPMSolverMultistepScheduler(artifact_path="dist", device=device),
    tvm_device=device,
    param_dict=const_params_dict,
)


import time

prompt = "A photo of an astronaut riding a horse on mars"
neg_prompt = ""

start = time.time()
image = pipe(prompt, negative_prompt=neg_prompt)
end = time.time()

print(f"Time elapsed: {end - start} seconds.")