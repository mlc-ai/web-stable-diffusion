#!/bin/bash
set -euxo pipefail
PROJ_ROOT=`pwd`

rm -rf site/dist
mkdir -p site/dist site/_inlcudes

echo "Copy local configurations.."
cp web/local-config.json site/stable-diffusion-config.json

echo "Copy files..."
cp web/stable_diffusion.html site/_includes
cp web/stable_diffusion.js site/dist


cp dist/scheduler_consts.json site/dist
cp dist/stable_diffusion_webgpu.wasm site/dist

cp dist/tvmjs_runtime.wasi.js site/dist
cp dist/tvmjs.bundle.js site/dist
cp -r dist/tokenizers-wasm site/dist

cd site && jekyll b

echo "symlink parameter location to site.."
ln -s ${PROJ_ROOT}/dist/params _site/dist/webgpu-sd-v1-5

jekyll serve  --skip-initial-build  --baseurl /web-stable-diffusion --port 8888
