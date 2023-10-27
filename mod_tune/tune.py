from tvm.script import ir as I
from tvm.script import tir as T
from tvm.script import relax as R
import tvm
import pickle

with open("mod_deploy.pkl", "rb") as f:
    mod = pickle.load(f)




def tune(mod: tvm.IRModule) -> None:
    from tvm import meta_schedule as ms

    ms.relax_integration.tune_relax(
        mod=mod,
        target=tvm.target.Target("apple/m1-gpu-restricted"),
        params={},
        builder=ms.builder.LocalBuilder(
            max_workers=6,
            timeout_sec = 300
        ),
        runner=ms.runner.LocalRunner(timeout_sec = 300),
        work_dir="log_db_tuning",
        max_trials_global=117500,
        max_trials_per_task=500,
        strategy=ms.search_strategy.EvolutionarySearch(init_min_unmeasured=10, max_fail_count=20),
    )

tune(mod)