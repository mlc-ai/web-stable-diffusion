from typing import List

import argparse
import os

import numpy as np
import tvm
from tvm import relax
from tvm.relax.testing.lib_comparator import LibCompareVMInstrument
from web_stable_diffusion import utils
from web_stable_diffusion.rpc_testing import connect_to_proxy


def load_checkpt(args, name):
    return np.load(os.path.join(args.artifact_path, "debug", f"{name}.npy"))


class LibCompare(LibCompareVMInstrument):
    def __init__(self, mod, device, time_eval, skip_rounds):
        super().__init__(mod, device, True)
        self.time_eval = time_eval
        self.time_eval_results = {}
        self.skip_rounds = skip_rounds

    def skip_instrument(self, func, name, before_run, ret_val, *args):
        if self.counter < self.skip_rounds:
            self.counter += 1
            print(f"[{self.counter}] Skip validating {name}..")
            return True
        return False

    def compare(self,
                name : str,
                ref_args: List[tvm.nd.NDArray],
                new_args: List[tvm.nd.NDArray],
                ret_indices: List[int]):

        super().compare(name, ref_args, new_args, ret_indices)
        if self.time_eval and name not in self.time_eval_results:
            res = self.mod.time_evaluator(name)(*new_args)
            self.time_eval_results[name] = res
            print(f"Time-eval result {name} on {self.device}: {res}")


class TestState:
    def __init__(self, args):
        assert args.primary_device != "webgpu"
        self.primary_device = tvm.device(args.primary_device)
        ex = tvm.runtime.load_module(
            f"{args.artifact_path}/stable_diffusion_{args.primary_device}.so"
        )
        self.vm = relax.VirtualMachine(ex, self.primary_device)
        if args.cmp_device == "webgpu":
            self.sess = connect_to_proxy(
                f"{args.artifact_path}/stable_diffusion_webgpu.wasm"
            )
            self.lib = self.sess.system_lib()
            self.cmp_device = self.sess.webgpu()
        else:
            self.sess = None
            self.lib = tvm.runtime.load_module(
                f"{args.artifact_path}/stable_diffusion_{args.cmp_device}.so"
            )
            self.cmp_device = tvm.device(args.cmp_device)
        self.const_params_dict = utils.load_params(
            args.artifact_path, self.primary_device)
        self.cmp_instrument = LibCompare(
            self.lib, self.cmp_device,
            time_eval=args.time_eval, skip_rounds=args.skip_rounds)
        self.vm.set_instrument(self.cmp_instrument)


def main_vae(args):
    state = TestState(args)
    vae_input = tvm.nd.array(load_checkpt(args, "vae_input"), state.primary_device)
    state.vm["vae"](vae_input, state.const_params_dict["vae"])


def _parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("--artifact-path", type=str, default="dist")
    args.add_argument("--primary-device", type=str, default="auto")
    args.add_argument("--cmp-device", type=str, required=True)
    args.add_argument("--stage", type=str, choices=["unet", "vae"], required=True)
    args.add_argument("--counter", type=int, default=0)
    args.add_argument("--time-eval", default=False, action="store_true")
    args.add_argument("--skip-rounds", type=int, default=0)
    parsed = args.parse_args()

    if parsed.primary_device == "auto":
        if tvm.cuda().exist:
            parsed.primary_device = "cuda"
        elif tvm.metal().exist:
            parsed.primary_device = "metal"
        else:
            raise ValueError("Cannot auto deduce device-name, please set it")
    return parsed


if __name__ == "__main__":
    args = _parse_args()
    if args.stage == "vae":
        main_vae(args)
    else:
        raise ValueError(f"Unknown stage {args.stage}")
    print(f"All pass running stage {args.stage}, counter={args.counter}")
