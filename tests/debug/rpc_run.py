import os
import json
import numpy as np
import argparse
from web_stable_diffusion.rpc_testing import WebGPUDebugSession


def load_checkpt(args, name):
    return np.load(os.path.join(args.artifact_path, "debug", f"{name}.npy"))


def load_metadata(args):
    json_path = os.path.join(args.artifact_path, "params", "ndarray-cache.json")
    return json.load(open(json_path, "r"))["metadata"]


def main_vae(args):
    sess = WebGPUDebugSession(
        os.path.join(args.artifact_path, "stable_diffusion_webgpu.wasm")
    )
    vae_input = load_checkpt(args, "vae_input")
    vae_output = load_checkpt(args, "vae_output")
    nparams = load_metadata(args)["vaeParamSize"]
    vae = sess.get_wrapper("vae", nparams, time_eval=args.time_eval)
    result = vae(vae_input)
    # result are 0-255, set atol=1 so we can avoid relative minor error
    np.testing.assert_allclose(result, vae_output, atol=1)


def main_unet(args):
    sess = WebGPUDebugSession(
        os.path.join(args.artifact_path, "stable_diffusion_webgpu.wasm")
    )
    unet_input = load_checkpt(args, f"unet_input_{args.counter}")
    text_embeddings = load_checkpt(args, f"text_embeddings")
    timestep = load_checkpt(args, f"timestep_{args.counter}")
    unet_output = load_checkpt(args, f"unet_output_{args.counter}")
    nparams = load_metadata(args)["unetParamSize"]
    unet = sess.get_wrapper("unet", nparams, time_eval=args.time_eval)
    result = unet(unet_input, timestep, text_embeddings)
    np.testing.assert_allclose(result, unet_output, atol=4e-5)


def _parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("--artifact-path", type=str, default="dist")
    args.add_argument("--stage", type=str, choices=["unet", "vae"], required=True)
    args.add_argument("--counter", type=int, default=0)
    args.add_argument("--time-eval", default=False, action="store_true")
    parsed = args.parse_args()
    return parsed


if __name__ == "__main__":
    args = _parse_args()
    if args.stage == "vae":
        main_vae(args)
    elif args.stage == "unet":
        main_unet(args)
    else:
        raise ValueError(f"Unknown stage {args.stage}")
    print(f"All pass running stage {args.stage}, counter={args.counter}")
