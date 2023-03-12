#!/bin/bash
set -euxo pipefail

TVM_HOME_SET="${TVM_HOME:-}"

if [[ -z ${TVM_HOME_SET} ]]; then
    echo "Require TVM_HOME to be set"
    exit 255
fi

echo "Copy files..."
mkdir -p ${TVM_HOME}/web/dist/www/dist/
cp web/stable_diffusion.html ${TVM_HOME}/web/dist/www/rpc_plugin.html
cp web/stable_diffusion.js ${TVM_HOME}/web/dist/www/dist/
cp web/local-config.json ${TVM_HOME}/web/dist/www/stable-diffusion-config.json

cp dist/scheduler_pndm_consts.json ${TVM_HOME}/web/dist/www/dist/
cp dist/scheduler_dpm_solver_multistep_consts.json ${TVM_HOME}/web/dist/www/dist/
cp dist/stable_diffusion_webgpu.wasm ${TVM_HOME}/web/dist/www/dist/
cp -rf dist/tokenizers-wasm ${TVM_HOME}/web/dist/www/dist/

rm -rf ${TVM_HOME}/web/.ndarray_cache/web-sd-shards-v1-5
ln -s `pwd`/dist/params ${TVM_HOME}/web/.ndarray_cache/web-sd-shards-v1-5
