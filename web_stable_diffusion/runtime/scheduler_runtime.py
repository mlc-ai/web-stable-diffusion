from typing import ClassVar, List, Type

import json
import numpy as np

import tvm
from tvm import relax


class Scheduler:
    scheduler_name: ClassVar[str]
    timesteps: List[tvm.nd.NDArray]

    def __init__(self, artifact_path: str, device) -> None:
        raise NotImplementedError()

    def step(
        self,
        vm: relax.VirtualMachine,
        model_output: tvm.nd.NDArray,
        sample: tvm.nd.NDArray,
        counter: int,
    ) -> tvm.nd.NDArray:
        raise NotImplementedError()


class PNDMScheduler(Scheduler):
    scheduler_name = "pndm"

    def __init__(self, artifact_path: str, device) -> None:
        with open(f"{artifact_path}/scheduler_pndm_consts.json", "r") as file:
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

        prev_latents = vm[f"pndm_scheduler_step_{min(counter, 4)}"](
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


class DPMSolverMultistepScheduler(Scheduler):
    scheduler_name = "multistep-dpm-solver"

    def __init__(self, artifact_path: str, device) -> None:
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


########################################################################

schedulers: List[Type[Scheduler]] = [DPMSolverMultistepScheduler, PNDMScheduler]
