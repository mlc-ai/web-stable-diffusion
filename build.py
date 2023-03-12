from typing import Dict, List, Tuple

import os
import argparse
import pickle
import web_stable_diffusion.trace as trace
import web_stable_diffusion.utils as utils

import tvm
from tvm import relax
from tvm.contrib import tvmjs


def _parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("--target", type=str, default="apple/m2-gpu")
    args.add_argument("--db-path", type=str, default="log_db/")
    args.add_argument("--artifact-path", type=str, default="dist")
    args.add_argument(
        "--use-cache",
        type=int,
        default=1,
        help="Whether to use previously pickled IRModule and skip trace.",
    )
    args.add_argument("--debug-dump", action="store_true", default=False)

    parsed = args.parse_args()

    if parsed.target == "webgpu":
        parsed.target = tvm.target.Target(
            "webgpu", host="llvm -mtriple=wasm32-unknown-unknown-wasm"
        )
    else:
        parsed.target = tvm.target.Target(parsed.target, host="llvm")
    return parsed


def debug_dump(mod, name, args):
    """Debug dump mode"""
    if not args.debug_dump:
        return
    dump_path = os.path.join(args.artifact_path, "debug", name)
    with open(dump_path, "w") as outfile:
        outfile.write(mod.script(show_meta=True))
    print(f"Dump mod to {dump_path}")


def trace_models(
    device_str: str,
) -> Tuple[tvm.IRModule, Dict[str, List[tvm.nd.NDArray]]]:
    from diffusers import StableDiffusionPipeline

    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    clip = trace.clip_to_text_embeddings(pipe)
    unet = trace.unet_latents_to_noise_pred(pipe, device_str)
    vae = trace.vae_to_image(pipe)
    concat_embeddings = trace.concat_embeddings()
    image_to_rgba = trace.image_to_rgba()
    schedulers = [scheduler.scheduler_steps() for scheduler in trace.schedulers]

    mod = utils.merge_irmodules(
        clip,
        unet,
        vae,
        concat_embeddings,
        image_to_rgba,
        *schedulers,
    )
    return relax.frontend.detach_params(mod)


def legalize_and_lift_params(
    mod: tvm.IRModule, model_params: Dict[str, List[tvm.nd.NDArray]], args: Dict
) -> tvm.IRModule:
    """First-stage: Legalize ops and trace"""
    model_names = ["clip", "unet", "vae"]
    scheduler_func_names = [
        name
        for scheduler in trace.schedulers
        for name in scheduler.scheduler_steps_func_names()
    ]
    entry_funcs = (
        model_names + scheduler_func_names + ["image_to_rgba", "concat_embeddings"]
    )

    mod = relax.pipeline.get_pipeline()(mod)
    mod = relax.transform.RemoveUnusedFunctions(entry_funcs)(mod)
    mod = relax.transform.LiftTransformParams()(mod)

    mod_transform, mod_deploy = utils.split_transform_deploy_mod(
        mod, model_names, entry_funcs
    )

    debug_dump(mod_transform, "mod_lift_params.py", args)

    trace.compute_save_scheduler_consts(args.artifact_path)
    new_params = utils.transform_params(mod_transform, model_params)
    utils.save_params(new_params, args.artifact_path)
    return mod_deploy


def build(mod: tvm.IRModule, args: Dict) -> None:
    from tvm import meta_schedule as ms

    db = ms.database.create(work_dir=args.db_path)
    with args.target, db, tvm.transform.PassContext(opt_level=3):
        mod_deploy = relax.transform.MetaScheduleApplyDatabase()(mod)

    debug_dump(mod_deploy, "mod_build_stage.py", args)

    ex = relax.build(mod_deploy, args.target)

    target_kind = args.target.kind.default_keys[0]

    if target_kind == "webgpu":
        output_filename = f"stable_diffusion_{target_kind}.wasm"
        tvmjs.export_runtime(f"{args.artifact_path}")
    else:
        output_filename = f"stable_diffusion_{target_kind}.so"
    ex.export_library(os.path.join(args.artifact_path, output_filename))


if __name__ == "__main__":
    ARGS = _parse_args()
    os.makedirs(ARGS.artifact_path, exist_ok=True)
    os.makedirs(os.path.join(ARGS.artifact_path, "debug"), exist_ok=True)
    torch_dev_key = utils.detect_available_torch_device()
    cache_path = os.path.join(ARGS.artifact_path, "mod_cache_before_build.pkl")
    use_cache = ARGS.use_cache and os.path.isfile(cache_path)
    if not use_cache:
        mod, params = trace_models(torch_dev_key)
        mod = legalize_and_lift_params(mod, params, ARGS)
        with open(cache_path, "wb") as outfile:
            pickle.dump(mod, outfile)
        print(f"Save a cached module to {cache_path}.")
    else:
        print(
            f"Load cached module from {cache_path} and skip tracing. "
            "You can use --use-cache=0 to retrace"
        )
        mod = pickle.load(open(cache_path, "rb"))
    build(mod, ARGS)
