from typing import Callable, ClassVar, Dict, List, Type

import tvm
from tvm import relax
from tvm.script import relax as R


class Scheduler:
    consts_json_file_name: ClassVar[str]

    @staticmethod
    def scheduler_steps() -> tvm.IRModule:
        raise NotImplementedError()

    @staticmethod
    def scheduler_steps_func_names() -> List[str]:
        raise NotImplementedError()

    @staticmethod
    def compute_const_dict() -> Dict[str, List[tvm.nd.NDArray]]:
        raise NotImplementedError()


class PNDMScheduler(Scheduler):
    consts_json_file_name = "scheduler_pndm_consts.json"

    @staticmethod
    def get_prev_sample(
        sample: relax.Expr,
        model_output: relax.Expr,
        sample_coeff: relax.Expr,
        alpha_diff: relax.Expr,
        model_output_denom_coeff: relax.Expr,
    ) -> relax.Expr:
        return (
            sample_coeff * sample - alpha_diff * model_output / model_output_denom_coeff
        )

    @staticmethod
    def get_scheduler_step_functions() -> List[Callable]:
        return [
            lambda mo, e0, e1, e2, e3: mo,
            lambda mo, e0, e1, e2, e3: (mo + e3) / relax.const(2, "float32"),
            lambda mo, e0, e1, e2, e3: (relax.const(3, "float32") * e3 - e2)
            / relax.const(2, "float32"),
            lambda mo, e0, e1, e2, e3: (
                relax.const(23, "float32") * e3
                - relax.const(16, "float32") * e2
                + relax.const(5, "float32") * e1
            )
            / relax.const(12, "float32"),
            lambda mo, e0, e1, e2, e3: relax.const(1 / 24, "float32")
            * (
                relax.const(55, "float32") * e3
                - relax.const(59, "float32") * e2
                + relax.const(37, "float32") * e1
                - relax.const(9, "float32") * e0
            ),
        ]

    @staticmethod
    def scheduler_step_wrapper(f_output: Callable):
        def scheduler_step(
            sample: relax.Expr,
            model_output: relax.Expr,
            sample_coeff: relax.Expr,
            alpha_diff: relax.Expr,
            model_output_denom_coeff: relax.Expr,
            ets0: relax.Expr,
            ets1: relax.Expr,
            ets2: relax.Expr,
            ets3: relax.Expr,
        ):
            output = f_output(model_output, ets0, ets1, ets2, ets3)
            return PNDMScheduler.get_prev_sample(
                sample, output, sample_coeff, alpha_diff, model_output_denom_coeff
            )

        return scheduler_step

    @staticmethod
    def scheduler_steps() -> tvm.IRModule:
        bb = relax.BlockBuilder()
        for i, scheduler_step in enumerate(
            PNDMScheduler.get_scheduler_step_functions()
        ):
            sample = relax.Var("sample", R.Tensor((1, 4, 64, 64), "float32"))
            model_output = relax.Var(
                "model_output", R.Tensor((1, 4, 64, 64), "float32")
            )
            sample_coeff = relax.Var("sample_coeff", R.Tensor((), "float32"))
            alpha_diff = relax.Var("alpha_diff", R.Tensor((), "float32"))
            model_output_denom_coeff = relax.Var(
                "model_output_denom_coeff", R.Tensor((), "float32")
            )
            ets = [
                relax.Var(f"ets{i}", R.Tensor((1, 4, 64, 64), "float32"))
                for i in range(4)
            ]

            scheduler_step = PNDMScheduler.scheduler_step_wrapper(scheduler_step)
            with bb.function(
                f"pndm_scheduler_step_{i}",
                [
                    sample,
                    model_output,
                    sample_coeff,
                    alpha_diff,
                    model_output_denom_coeff,
                    *ets,
                ],
            ):
                prev_sample = bb.emit(
                    scheduler_step(
                        sample,
                        model_output,
                        sample_coeff,
                        alpha_diff,
                        model_output_denom_coeff,
                        *ets,
                    ),
                    "prev_sample",
                )
                bb.emit_func_output(prev_sample)

        return bb.get()

    @staticmethod
    def scheduler_steps_func_names() -> List[str]:
        return [f"pndm_scheduler_step_{i}" for i in range(5)]

    @staticmethod
    def compute_const_dict() -> Dict[str, List[tvm.nd.NDArray]]:
        import numpy as np

        num_train_timesteps = 1000
        num_inference_steps = 50
        steps_offset = 1

        beta_start = 0.00085
        beta_end = 0.012

        # this schedule is very specific to the latent diffusion model.
        betas = (
            np.linspace(
                beta_start**0.5, beta_end**0.5, num_train_timesteps, dtype="float32"
            )
            ** 2
        )

        alphas = 1 - betas
        alphas_cumprod = np.cumprod(alphas, axis=0)
        final_alpha_cumprod = alphas_cumprod[0]

        step_ratio = num_train_timesteps // num_inference_steps
        _timesteps = (np.arange(0, num_inference_steps) * step_ratio).round()
        _timesteps += steps_offset

        timesteps = (
            np.concatenate([_timesteps[:-1], _timesteps[-2:-1], _timesteps[-1:]])[::-1]
            .copy()
            .astype(np.int32)
            .tolist()
        )

        ###################################
        list_sample_coeff = []
        list_alpha_diff = []
        list_model_output_denom_coeff = []

        for i, timestep in enumerate(timesteps):
            prev_timestep = timestep - step_ratio

            if i == 1:
                prev_timestep = timestep
                timestep = timestep + step_ratio

            alpha_prod_t = alphas_cumprod[timestep]
            alpha_prod_t_prev = (
                alphas_cumprod[prev_timestep]
                if prev_timestep >= 0
                else final_alpha_cumprod
            )
            beta_prod_t = 1 - alpha_prod_t
            beta_prod_t_prev = 1 - alpha_prod_t_prev

            alpha_diff = alpha_prod_t_prev - alpha_prod_t
            sample_coeff = (alpha_prod_t_prev / alpha_prod_t) ** (0.5)
            model_output_denom_coeff = alpha_prod_t * beta_prod_t_prev ** (0.5) + (
                alpha_prod_t * beta_prod_t * alpha_prod_t_prev
            ) ** (0.5)

            list_sample_coeff.append(sample_coeff.item())
            list_alpha_diff.append(alpha_diff.item())
            list_model_output_denom_coeff.append(model_output_denom_coeff.item())

        return {
            "num_steps": len(timesteps),
            "timesteps": timesteps,
            "sample_coeff": list_sample_coeff,
            "alpha_diff": list_alpha_diff,
            "model_output_denom_coeff": list_model_output_denom_coeff,
        }


class DPMSolverMultistepScheduler(Scheduler):
    consts_json_file_name = "scheduler_dpm_solver_multistep_consts.json"

    @staticmethod
    def scheduler_steps() -> tvm.IRModule:
        bb = relax.BlockBuilder()

        # Scheduler convert_model_output
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

        # Scheduler step
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

    @staticmethod
    def scheduler_steps_func_names() -> List[str]:
        return [
            "dpm_solver_multistep_scheduler_convert_model_output",
            "dpm_solver_multistep_scheduler_step",
        ]

    @staticmethod
    def compute_const_dict() -> Dict[str, List[tvm.nd.NDArray]]:
        import numpy as np

        num_train_timesteps = 1000
        num_inference_steps = 20

        beta_start = 0.00085
        beta_end = 0.012

        betas = (
            np.linspace(
                beta_start**0.5, beta_end**0.5, num_train_timesteps, dtype="float32"
            )
            ** 2
        )

        alphas = 1 - betas
        alphas_cumprod = np.cumprod(alphas, axis=0)
        alpha_t = np.sqrt(alphas_cumprod)
        sigma_t = np.sqrt(1 - alphas_cumprod)
        lambda_t = np.log(alpha_t) - np.log(sigma_t)
        timesteps = (
            np.linspace(0, num_train_timesteps - 1, num_inference_steps + 1)
            .round()[::-1][:-1]
            .copy()
            .astype(np.int32)
            .tolist()
        )

        ###################################
        list_alpha = []
        list_sigma = []
        list_c0 = []
        list_c1 = []
        list_c2 = []

        for i, timestep in enumerate(timesteps):
            t = timesteps[i + 1] if i < len(timesteps) - 1 else 0
            s0 = timesteps[i]
            s1 = timesteps[i - 1] if i > 0 else None

            c0 = sigma_t[t] / sigma_t[s0]
            c1 = alpha_t[t] * (np.exp(-(lambda_t[t] - lambda_t[s0])) - 1)
            c2 = (
                0.5
                * c1
                * (
                    ((lambda_t[t] - lambda_t[s0]) / (lambda_t[s0] - lambda_t[s1]))
                    if i > 0
                    else np.array(0.0, dtype="float32")
                )
            )

            list_alpha.append(alpha_t[timestep].item())
            list_sigma.append(sigma_t[timestep].item())
            list_c0.append(c0.item())
            list_c1.append(c1.item())
            list_c2.append(c2.item())

        return {
            "num_steps": len(timesteps),
            "timesteps": timesteps,
            "alpha": list_alpha,
            "sigma": list_sigma,
            "c0": list_c0,
            "c1": list_c1,
            "c2": list_c2,
        }


########################################################################

schedulers: List[Type[Scheduler]] = [DPMSolverMultistepScheduler, PNDMScheduler]


def compute_save_scheduler_consts(artifact_path: str) -> None:
    import json

    for scheduler in schedulers:
        jsonstring = json.dumps(scheduler.compute_const_dict())
        with open(f"{artifact_path}/{scheduler.consts_json_file_name}", "w") as file:
            file.write(jsonstring)
