#!/bin/bash
# This file prepares all the necessary dependencies for the web build.
set -euxo pipefail

emcc --version
npm --version
cargo --version

TEMP_TVM_HOME_SET="${TEMP_TVM_HOME:-}"

if [[ -z ${TEMP_TVM_HOME_SET} ]]; then
    if [[ ! -d "3rdparty/tvm" ]]; then
        echo "Do not find TEMP_TVM_HOME env variable, cloning a version as source".
        git clone https://github.com/apache/tvm 3rdparty/tvm --branch unity --recursive
    fi
    export TEMP_TVM_HOME="${TEMP_TVM_HOME:-3rdparty/tvm}"
fi

export TOKENZIER_WASM_HOME="3rdparty/tokenizers-wasm"

mkdir -p dist
cd ${TEMP_TVM_HOME}/web && make && npm install && npm run bundle && cd -
git submodule update --init
cd ${TOKENZIER_WASM_HOME} && wasm-pack build --target web && cd -
rm -rf dist/tokenizers-wasm
cp -r ${TOKENZIER_WASM_HOME}/pkg dist/tokenizers-wasm

echo "Exporting tvmjs runtime dist files"
python -c "from tvm.contrib import tvmjs; tvmjs.export_runtime(\"dist\")"
