#!/bin/bash
set -euxo pipefail

if [[ ! -f $1 ]]; then
    echo "cannot find config" $1
fi

rm -rf site/dist
mkdir -p site/dist site/_inlcudes

echo "Copy local configurations.."
cp $1 site/stable-diffusion-config.json
echo "Copy files..."
cp web/stable_diffusion.html site/_includes
cp web/stable_diffusion.js site/dist

cp dist/scheduler_consts.json site/dist
cp dist/stable_diffusion_webgpu.wasm site/dist

cp dist/tvmjs_runtime.wasi.js site/dist
cp dist/tvmjs.bundle.js site/dist
cp -r dist/tokenizers-wasm site/dist

cd site && jekyll b && cd ..
