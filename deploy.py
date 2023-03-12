from typing import Type

import argparse
import time

import torch
from transformers import CLIPTokenizer

import web_stable_diffusion.utils as utils
import web_stable_diffusion.runtime as runtime

import os
import tvm
from tvm import relax

from tqdm import tqdm
from PIL import Image


def _parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("--device-name", type=str, default="auto")
    args.add_argument("--debug-dump", action="store_true", default=False)
    args.add_argument("--artifact-path", type=str, default="dist")
    args.add_argument(
        "--prompt", type=str, default="A photo of an astronaut riding a horse on mars."
    )
    args.add_argument("--negative-prompt", type=str, default="")
    args.add_argument(
        "--scheduler",
        type=str,
        choices=[scheduler.scheduler_name for scheduler in runtime.schedulers],
        default=runtime.DPMSolverMultistepScheduler.scheduler_name,
    )
    parsed = args.parse_args()
    if parsed.device_name == "auto":
        if tvm.cuda().exist:
            parsed.device_name = "cuda"
        elif tvm.metal().exist:
            parsed.device_name = "metal"
        else:
            raise ValueError("Cannot auto deduce device-name, please set it")
    return parsed


class TVMSDPipeline:
    def __init__(
        self,
        vm: relax.VirtualMachine,
        tokenizer: CLIPTokenizer,
        scheduler: runtime.Scheduler,
        tvm_device,
        param_dict,
        debug_dump_dir,
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
        self.debug_dump_dir = debug_dump_dir

    def debug_dump(self, name, arr):
        import numpy as np

        if self.debug_dump_dir:
            np.save(f"{self.debug_dump_dir}/{name}.npy", arr.numpy())

    def __call__(self, prompt: str, negative_prompt: str = ""):
        # height = width = 512

        list_text_embeddings = []
        for text in [negative_prompt, prompt]:
            text = [text]
            text_inputs = self.tokenizer(
                text,
                padding="max_length",
                max_length=self.tokenizer.model_max_length,  # 77
                return_tensors="pt",
            )
            text_input_ids = text_inputs.input_ids.to(torch.int32)
            if text_input_ids.shape[-1] > self.tokenizer.model_max_length:
                text_input_ids = text_input_ids[:, : self.tokenizer.model_max_length]

            text_input_ids = tvm.nd.array(text_input_ids.cpu().numpy(), self.tvm_device)
            text_embeddings = self.clip_to_text_embeddings(text_input_ids)
            list_text_embeddings.append(text_embeddings)
        text_embeddings = self.concat_embeddings(*list_text_embeddings)

        self.debug_dump("text_embeddings", text_embeddings)

        latents = torch.randn(
            (1, 4, 64, 64),
            device="cpu",
            dtype=torch.float32,
        )
        latents = tvm.nd.array(latents.numpy(), self.tvm_device)

        for i in tqdm(range(len(self.scheduler.timesteps))):
            t = self.scheduler.timesteps[i]
            self.debug_dump(f"unet_input_{i}", latents)
            self.debug_dump(f"timestep_{i}", t)
            noise_pred = self.unet_latents_to_noise_pred(latents, t, text_embeddings)
            self.debug_dump(f"unet_output_{i}", noise_pred)
            latents = self.scheduler.step(self.vm, noise_pred, latents, i)

        self.debug_dump("vae_input", latents)
        image = self.vae_to_image(latents)
        self.debug_dump("vae_output", image)
        image = self.image_to_rgba(image)
        return Image.fromarray(image.numpy().view("uint8").reshape(512, 512, 4))


def get_scheduler_type(scheduler_name: str) -> Type[runtime.Scheduler]:
    for scheduler in runtime.schedulers:
        if scheduler_name == scheduler.scheduler_name:
            return scheduler

    scheduler_names = [scheduler.scheduler_name for scheduler in runtime.schedulers]
    raise ValueError(
        f'"{scheduler_name}" is an unsupported scheduler name. The list of '
        f"supported scheduler names is {scheduler_names}"
    )


def deploy_to_pipeline(args) -> None:
    device = tvm.device(args.device_name)
    const_params_dict = utils.load_params(args.artifact_path, device)
    ex = tvm.runtime.load_module(
        f"{args.artifact_path}/stable_diffusion_{args.device_name}.so"
    )
    vm = relax.VirtualMachine(ex, device)

    debug_dump_dir = f"{args.artifact_path}/debug/" if args.debug_dump else ""
    if debug_dump_dir:
        os.makedirs(debug_dump_dir, exist_ok=True)

    pipe = TVMSDPipeline(
        vm=vm,
        tokenizer=CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14"),
        scheduler=get_scheduler_type(args.scheduler)(args.artifact_path, device),
        tvm_device=device,
        param_dict=const_params_dict,
        debug_dump_dir=debug_dump_dir,
    )

    start = time.time()
    image = pipe(args.prompt, args.negative_prompt)
    end = time.time()

    img_path = f"{args.artifact_path}/example.png"
    image.save(img_path)
    print(f"Time elapsed: {end - start} seconds, output saved to {img_path}")


if __name__ == "__main__":
    ARGS = _parse_args()
    deploy_to_pipeline(ARGS)
