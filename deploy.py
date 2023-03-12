from typing import List

import argparse
import time

import torch
from transformers import CLIPTokenizer

import web_stable_diffusion.utils as utils

import os
import json
import tvm
import numpy as np
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
    parsed = args.parse_args()
    if parsed.device_name == "auto":
        if tvm.cuda().exist:
            parsed.device_name = "cuda"
        elif tvm.metal().exist:
            parsed.device_name = "metal"
        else:
            raise ValueError("Cannot auto deduce device-name, please set it")
    return parsed


class PNDMScheduler:
    def __init__(self, artifact_path: str, device) -> None:
        with open(f"{artifact_path}/scheduler_consts.json", "r") as file:
            jsoncontent = file.read()
        scheduler_consts = json.loads(jsoncontent)

        def f_convert(data, dtype):
            return [tvm.nd.array(np.array(t, dtype=dtype), device) for t in data]

        self.timesteps = f_convert(scheduler_consts["timesteps"], "int32")
        self.sample_coeff = f_convert(scheduler_consts["sample_coeff"], "float32")
        self.alpha_diff = f_convert(scheduler_consts["alpha_diff"], "float32")
        self.model_output_denom_coeff = f_convert(
            scheduler_consts["model_output_denom_coeff"], "float32"
        )

        self.ets: List[tvm.nd.NDArray] = [
            tvm.nd.empty((1, 4, 64, 64), "float32", device)
        ] * 4
        self.cur_sample: tvm.nd.NDArray

    def step(
        self,
        vm: relax.VirtualMachine,
        model_output: tvm.nd.NDArray,
        sample: tvm.nd.NDArray,
        counter: int,
    ) -> tvm.nd.NDArray:
        if counter != 1:
            self.ets = self.ets[-3:]
            self.ets.append(model_output)

        if counter == 0:
            self.cur_sample = sample
        elif counter == 1:
            sample = self.cur_sample

        prev_latents = vm[f"scheduler_step_{min(counter, 4)}"](
            sample,
            model_output,
            self.sample_coeff[counter],
            self.alpha_diff[counter],
            self.model_output_denom_coeff[counter],
            self.ets[0],
            self.ets[1],
            self.ets[2],
            self.ets[3],
        )

        return prev_latents


class TVMSDPipeline:
    def __init__(
        self,
        vm: relax.VirtualMachine,
        tokenizer: CLIPTokenizer,
        scheduler: PNDMScheduler,
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
        if self.debug_dump_dir:
            np.save(f"{self.debug_dump_dir}/{name}.npy", arr.numpy())

    def __call__(self, prompt: str, negative_prompt: str = ""):
        # height = width = 512
        num_inference_steps = 50

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

        for i in tqdm(range(num_inference_steps)):
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
        scheduler=PNDMScheduler(args.artifact_path, device),
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
