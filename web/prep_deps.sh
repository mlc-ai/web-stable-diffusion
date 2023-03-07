#!/bin/bash
# This file prepares all the necessary dependencies for the web build.
set -euxo pipefail

export TVM_HOME="${TVM_HOME:-3rdparty/tvm}"
export TOKENZIER_WASM_HOME="3rdparty/tokenizers-wasm"

npm --version
cargo --version

mkdir -p dist
cd ${TVM_HOME}/web && make && npm install && npm run bundle && cd -
cd ${TOKENZIER_WASM_HOME} && wasm-pack build --target web && cd -
rm -rf dist/tokenizers-wasm
cp -r ${TOKENZIER_WASM_HOME}/pkg dist/tokenizers-wasm
