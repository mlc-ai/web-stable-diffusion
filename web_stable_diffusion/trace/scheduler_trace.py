from typing import Callable, List

import tvm
from tvm import relax
from tvm.script import relax as R


def get_prev_sample(
    sample: relax.Expr,
    model_output: relax.Expr,
    sample_coeff: relax.Expr,
    alpha_diff: relax.Expr,
    model_output_denom_coeff: relax.Expr,
) -> relax.Expr:
    return sample_coeff * sample - alpha_diff * model_output / model_output_denom_coeff


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
        return get_prev_sample(
            sample, output, sample_coeff, alpha_diff, model_output_denom_coeff
        )

    return scheduler_step


def scheduler_steps() -> tvm.IRModule:
    bb = relax.BlockBuilder()
    for i, scheduler_step in enumerate(get_scheduler_step_functions()):
        sample = relax.Var("sample", R.Tensor((1, 4, 64, 64), "float32"))
        model_output = relax.Var("model_output", R.Tensor((1, 4, 64, 64), "float32"))
        sample_coeff = relax.Var("sample_coeff", R.Tensor((), "float32"))
        alpha_diff = relax.Var("alpha_diff", R.Tensor((), "float32"))
        model_output_denom_coeff = relax.Var(
            "model_output_denom_coeff", R.Tensor((), "float32")
        )
        ets = [
            relax.Var(f"ets{i}", R.Tensor((1, 4, 64, 64), "float32")) for i in range(4)
        ]

        scheduler_step = scheduler_step_wrapper(scheduler_step)
        with bb.function(
            f"scheduler_step_{i}",
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


def compute_save_scheduler_consts(artifact_path: str) -> None:
    import json
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
            alphas_cumprod[prev_timestep] if prev_timestep >= 0 else final_alpha_cumprod
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

    const_dict = {
        "timesteps": timesteps,
        "sample_coeff": list_sample_coeff,
        "alpha_diff": list_alpha_diff,
        "model_output_denom_coeff": list_model_output_denom_coeff,
    }

    jsonstring = json.dumps(const_dict)
    with open(f"{artifact_path}/scheduler_consts.json", "w") as file:
        file.write(jsonstring)
