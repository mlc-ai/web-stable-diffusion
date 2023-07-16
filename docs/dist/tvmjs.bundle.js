(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
    typeof define === 'function' && define.amd ? define(['exports'], factory) :
    (global = typeof globalThis !== 'undefined' ? globalThis : global || self, factory(global.tvmjs = {}));
})(this, (function (exports) { 'use strict';

    /*! *****************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */

    function __awaiter(thisArg, _arguments, P, generator) {
        function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
        return new (P || (P = Promise))(function (resolve, reject) {
            function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
            function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
            function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
            step((generator = generator.apply(thisArg, _arguments || [])).next());
        });
    }

    /*
     * Licensed to the Apache Software Foundation (ASF) under one
     * or more contributor license agreements.  See the NOTICE file
     * distributed with this work for additional information
     * regarding copyright ownership.  The ASF licenses this file
     * to you under the Apache License, Version 2.0 (the
     * "License"); you may not use this file except in compliance
     * with the License.  You may obtain a copy of the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing,
     * software distributed under the License is distributed on an
     * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
     * KIND, either express or implied.  See the License for the
     * specific language governing permissions and limitations
     * under the License.
     */
    /**
     * Convert string to Uint8array.
     * @param str The string.
     * @returns The corresponding Uint8Array.
     */
    function StringToUint8Array(str) {
        const arr = new Uint8Array(str.length + 1);
        for (let i = 0; i < str.length; ++i) {
            arr[i] = str.charCodeAt(i);
        }
        arr[str.length] = 0;
        return arr;
    }
    /**
     * Convert Uint8array to string.
     * @param array The array.
     * @returns The corresponding string.
     */
    function Uint8ArrayToString(arr) {
        const ret = [];
        for (const ch of arr) {
            ret.push(String.fromCharCode(ch));
        }
        return ret.join("");
    }
    /**
     * Internal assert helper
     * @param condition condition The condition to fail.
     * @param msg msg The message.
     */
    function assert(condition, msg) {
        if (!condition) {
            throw new Error("AssertError:" + (msg || ""));
        }
    }
    /**
     * Get the path to the wasm library in nodejs.
     * @return The wasm path.
     */
    function wasmPath() {
        return __dirname + "/wasm";
    }

    /**
     * Wasm Memory wrapper to perform JS side raw memory access.
     */
    class Memory {
        constructor(memory) {
            this.wasm32 = true;
            this.memory = memory;
            this.buffer = this.memory.buffer;
            this.viewU8 = new Uint8Array(this.buffer);
            this.viewU16 = new Uint16Array(this.buffer);
            this.viewI32 = new Int32Array(this.buffer);
            this.viewU32 = new Uint32Array(this.buffer);
            this.viewF32 = new Float32Array(this.buffer);
            this.viewF64 = new Float64Array(this.buffer);
        }
        loadU8(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            return this.viewU8[ptr >> 0];
        }
        loadU16(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            return this.viewU16[ptr >> 1];
        }
        loadU32(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            return this.viewU32[ptr >> 2];
        }
        loadI32(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            return this.viewI32[ptr >> 2];
        }
        loadI64(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            const base = ptr >> 2;
            // assumes little endian, for now truncate high.
            return this.viewI32[base];
        }
        loadF32(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            return this.viewF32[ptr >> 2];
        }
        loadF64(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            return this.viewF64[ptr >> 3];
        }
        loadPointer(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            if (this.wasm32) {
                return this.loadU32(ptr);
            }
            else {
                return this.loadI64(ptr);
            }
        }
        loadUSize(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            if (this.wasm32) {
                return this.loadU32(ptr);
            }
            else {
                return this.loadI64(ptr);
            }
        }
        sizeofPtr() {
            return this.wasm32 ? 4 /* SizeOf.I32 */ : 8 /* SizeOf.I64 */;
        }
        /**
         * Load raw bytes from ptr.
         * @param ptr The head address
         * @param numBytes The number
         */
        loadRawBytes(ptr, numBytes) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            const result = new Uint8Array(numBytes);
            result.set(this.viewU8.slice(ptr, ptr + numBytes));
            return result;
        }
        /**
         * Load TVMByteArray from ptr.
         *
         * @param ptr The address of the header.
         */
        loadTVMBytes(ptr) {
            const data = this.loadPointer(ptr);
            const length = this.loadUSize(ptr + this.sizeofPtr());
            return this.loadRawBytes(data, length);
        }
        /**
         * Load null-terminated C-string from ptr.
         * @param ptr The head address
         */
        loadCString(ptr) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            // NOTE: the views are still valid for read.
            const ret = [];
            let ch = 1;
            while (ch != 0) {
                ch = this.viewU8[ptr];
                if (ch != 0) {
                    ret.push(String.fromCharCode(ch));
                }
                ++ptr;
            }
            return ret.join("");
        }
        /**
         * Store raw bytes to the ptr.
         * @param ptr The head address.
         * @param bytes The bytes content.
         */
        storeRawBytes(ptr, bytes) {
            if (this.buffer != this.memory.buffer) {
                this.updateViews();
            }
            this.viewU8.set(bytes, ptr);
        }
        /**
         * Update memory view after the memory growth.
         */
        updateViews() {
            this.buffer = this.memory.buffer;
            this.viewU8 = new Uint8Array(this.buffer);
            this.viewU16 = new Uint16Array(this.buffer);
            this.viewI32 = new Int32Array(this.buffer);
            this.viewU32 = new Uint32Array(this.buffer);
            this.viewF32 = new Float32Array(this.buffer);
            this.viewF64 = new Float64Array(this.buffer);
        }
    }
    /**
     * Auxiliary call stack for the FFI calls.
     *
     * Lifecyle of a call stack.
     * - Calls into allocXX to allocate space, mixed with storeXXX to store data.
     * - Calls into ptrFromOffset, no further allocation(as ptrFromOffset can change),
     *   can still call into storeXX
     * - Calls into commitToWasmMemory once.
     * - reset.
     */
    class CachedCallStack {
        constructor(memory, allocSpace, freeSpace) {
            /** List of temporay arguments that can be disposed during reset. */
            this.tempArgs = [];
            this.stackTop = 0;
            this.basePtr = 0;
            this.addressToSetTargetValue = [];
            const initCallStackSize = 128;
            this.memory = memory;
            this.cAllocSpace = allocSpace;
            this.cFreeSpace = freeSpace;
            this.buffer = new ArrayBuffer(initCallStackSize);
            this.basePtr = this.cAllocSpace(initCallStackSize);
            this.viewU8 = new Uint8Array(this.buffer);
            this.viewI32 = new Int32Array(this.buffer);
            this.viewU32 = new Uint32Array(this.buffer);
            this.viewF64 = new Float64Array(this.buffer);
            this.updateViews();
        }
        dispose() {
            if (this.basePtr != 0) {
                this.cFreeSpace(this.basePtr);
                this.basePtr = 0;
            }
        }
        /**
         * Rest the call stack so that it can be reused again.
         */
        reset() {
            this.stackTop = 0;
            assert(this.addressToSetTargetValue.length == 0);
            while (this.tempArgs.length != 0) {
                this.tempArgs.pop().dispose();
            }
        }
        /**
         * Commit all the cached data to WasmMemory.
         * This function can only be called once.
         * No further store function should be called.
         *
         * @param nbytes Number of bytes to be stored.
         */
        commitToWasmMemory(nbytes = this.stackTop) {
            // commit all pointer values.
            while (this.addressToSetTargetValue.length != 0) {
                const [targetOffset, valueOffset] = this.addressToSetTargetValue.pop();
                this.storePtr(targetOffset, this.ptrFromOffset(valueOffset));
            }
            this.memory.storeRawBytes(this.basePtr, this.viewU8.slice(0, nbytes));
        }
        /**
         * Allocate space by number of bytes
         * @param nbytes Number of bytes.
         * @note This function always allocate space that aligns to 64bit.
         */
        allocRawBytes(nbytes) {
            // always aligns to 64bit
            nbytes = ((nbytes + 7) >> 3) << 3;
            if (this.stackTop + nbytes > this.buffer.byteLength) {
                const newSize = Math.max(this.buffer.byteLength * 2, this.stackTop + nbytes);
                const oldU8 = this.viewU8;
                this.buffer = new ArrayBuffer(newSize);
                this.updateViews();
                this.viewU8.set(oldU8);
                if (this.basePtr != 0) {
                    this.cFreeSpace(this.basePtr);
                }
                this.basePtr = this.cAllocSpace(newSize);
            }
            const retOffset = this.stackTop;
            this.stackTop += nbytes;
            return retOffset;
        }
        /**
         * Allocate space for pointers.
         * @param count Number of pointers.
         * @returns The allocated pointer array.
         */
        allocPtrArray(count) {
            return this.allocRawBytes(this.memory.sizeofPtr() * count);
        }
        /**
         * Get the real pointer from offset values.
         * Note that the returned value becomes obsolete if alloc is called on the stack.
         * @param offset The allocated offset.
         */
        ptrFromOffset(offset) {
            return this.basePtr + offset;
        }
        // Store APIs
        storePtr(offset, value) {
            if (this.memory.wasm32) {
                this.storeU32(offset, value);
            }
            else {
                this.storeI64(offset, value);
            }
        }
        storeUSize(offset, value) {
            if (this.memory.wasm32) {
                this.storeU32(offset, value);
            }
            else {
                this.storeI64(offset, value);
            }
        }
        storeI32(offset, value) {
            this.viewI32[offset >> 2] = value;
        }
        storeU32(offset, value) {
            this.viewU32[offset >> 2] = value;
        }
        storeI64(offset, value) {
            // For now, just store as 32bit
            // NOTE: wasm always uses little endian.
            const low = value & 0xffffffff;
            const base = offset >> 2;
            this.viewI32[base] = low;
            // sign extend
            this.viewI32[base + 1] = value < 0 ? -1 : 0;
        }
        storeF64(offset, value) {
            this.viewF64[offset >> 3] = value;
        }
        storeRawBytes(offset, bytes) {
            this.viewU8.set(bytes, offset);
        }
        /**
         * Allocate then set C-String pointer to the offset.
         * This function will call into allocBytes to allocate necessary data.
         * The address won't be set immediately(because the possible change of basePtr)
         * and will be filled when we commit the data.
         *
         * @param offset The offset to set ot data pointer.
         * @param data The string content.
         */
        allocThenSetArgString(offset, data) {
            const strOffset = this.allocRawBytes(data.length + 1);
            this.storeRawBytes(strOffset, StringToUint8Array(data));
            this.addressToSetTargetValue.push([offset, strOffset]);
        }
        /**
         * Allocate then set the argument location with a TVMByteArray.
         * Allocate new temporary space for bytes.
         *
         * @param offset The offset to set ot data pointer.
         * @param data The string content.
         */
        allocThenSetArgBytes(offset, data) {
            // Note: size of size_t equals sizeof ptr.
            const headerOffset = this.allocRawBytes(this.memory.sizeofPtr() * 2);
            const dataOffset = this.allocRawBytes(data.length);
            this.storeRawBytes(dataOffset, data);
            this.storeUSize(headerOffset + this.memory.sizeofPtr(), data.length);
            this.addressToSetTargetValue.push([offset, headerOffset]);
            this.addressToSetTargetValue.push([headerOffset, dataOffset]);
        }
        /**
         * Update internal cache views.
         */
        updateViews() {
            this.viewU8 = new Uint8Array(this.buffer);
            this.viewI32 = new Int32Array(this.buffer);
            this.viewU32 = new Uint32Array(this.buffer);
            this.viewF64 = new Float64Array(this.buffer);
        }
    }

    /**
     * Detect library provider from the importObject.
     *
     * @param importObject The import object.
     */
    function detectLibraryProvider(importObject) {
        if (importObject["wasmLibraryProvider"] &&
            importObject["wasmLibraryProvider"]["start"] &&
            importObject["wasmLibraryProvider"]["imports"] !== undefined) {
            const item = importObject;
            // create provider so that we capture imports in the provider.
            return {
                imports: item.wasmLibraryProvider.imports,
                start: (inst) => {
                    item.wasmLibraryProvider.start(inst);
                },
            };
        }
        else if (importObject["imports"] && importObject["start"] !== undefined) {
            return importObject;
        }
        else if (importObject["wasiImport"] && importObject["start"] !== undefined) {
            // WASI
            return {
                imports: {
                    "wasi_snapshot_preview1": importObject["wasiImport"],
                },
                start: (inst) => {
                    importObject["start"](inst);
                }
            };
        }
        else {
            return undefined;
        }
    }
    /**
     * Environment to impelement most of the JS library functions.
     */
    class Environment {
        constructor(importObject = {}, logger = console.log) {
            /**
             * Maintains a table of FTVMWasmPackedCFunc that the C part
             * can call via TVMWasmPackedCFunc.
             *
             * We maintain a separate table so that we can have un-limited amount
             * of functions that do not maps to the address space.
             */
            this.packedCFuncTable = [
                undefined,
            ];
            /**
             * Free table index that can be recycled.
             */
            this.packedCFuncTableFreeId = [];
            this.logger = logger;
            this.libProvider = detectLibraryProvider(importObject);
            // get imports from the provider
            if (this.libProvider !== undefined) {
                this.imports = this.libProvider.imports;
            }
            else {
                this.imports = importObject;
            }
            // update with more functions
            this.imports.env = this.environment(this.imports.env);
        }
        /** Mark the start of the instance. */
        start(inst) {
            if (this.libProvider !== undefined) {
                this.libProvider.start(inst);
            }
        }
        environment(initEnv) {
            // default env can be be overriden by libraries.
            const defaultEnv = {
                "__cxa_thread_atexit": () => { },
                // eslint-disable-next-line @typescript-eslint/no-unused-vars
                "emscripten_notify_memory_growth": (index) => { }
            };
            const wasmPackedCFunc = (args, typeCodes, nargs, ret, resourceHandle) => {
                const cfunc = this.packedCFuncTable[resourceHandle];
                assert(cfunc !== undefined);
                return cfunc(args, typeCodes, nargs, ret, resourceHandle);
            };
            const wasmPackedCFuncFinalizer = (resourceHandle) => {
                this.packedCFuncTable[resourceHandle] = undefined;
                this.packedCFuncTableFreeId.push(resourceHandle);
            };
            const newEnv = {
                TVMWasmPackedCFunc: wasmPackedCFunc,
                TVMWasmPackedCFuncFinalizer: wasmPackedCFuncFinalizer,
                "__console_log": (msg) => {
                    this.logger(msg);
                }
            };
            return Object.assign(defaultEnv, initEnv, newEnv);
        }
    }

    /**
     * DetectGPU device in the environment.
     */
    function detectGPUDevice() {
        return __awaiter(this, void 0, void 0, function* () {
            if (typeof navigator !== "undefined" && navigator.gpu !== undefined) {
                const adapter = yield navigator.gpu.requestAdapter({ "powerPreference": "high-performance" });
                if (adapter == null) {
                    throw Error("Cannot find adapter that matches the request");
                }
                const computeMB = (value) => {
                    return Math.ceil(value / (1 << 20)) + "MB";
                };
                // more detailed error message
                const requiedMaxBufferSize = 1 << 30;
                if (requiedMaxBufferSize > adapter.limits.maxBufferSize) {
                    throw Error(`Cannot initialize runtime because of requested maxBufferSize ` +
                        `exceeds limit. requested=${computeMB(requiedMaxBufferSize)}, ` +
                        `limit=${computeMB(adapter.limits.maxBufferSize)}. ` +
                        `This error may be caused by an older version of the browser (e.g. Chrome 112). ` +
                        `You can try to upgrade your browser to Chrome 113 or later.`);
                }
                const requiredMaxStorageBufferBindingSize = 1 << 30;
                if (requiredMaxStorageBufferBindingSize > adapter.limits.maxStorageBufferBindingSize) {
                    throw Error(`Cannot initialize runtime because of requested maxStorageBufferBindingSize ` +
                        `exceeds limit. requested=${computeMB(requiredMaxStorageBufferBindingSize)}, ` +
                        `limit=${computeMB(adapter.limits.maxStorageBufferBindingSize)}. `);
                }
                const requiredMaxComputeWorkgroupStorageSize = 32 << 10;
                if (requiredMaxComputeWorkgroupStorageSize > adapter.limits.maxComputeWorkgroupStorageSize) {
                    throw Error(`Cannot initialize runtime because of requested maxComputeWorkgroupStorageSize ` +
                        `exceeds limit. requested=${requiredMaxComputeWorkgroupStorageSize}, ` +
                        `limit=${adapter.limits.maxComputeWorkgroupStorageSize}. `);
                }
                let requiredFeatures = [];
                // Always require f16 if available
                if (adapter.features.has("shader-f16")) {
                    requiredFeatures.push("shader-f16");
                }
                const adapterInfo = yield adapter.requestAdapterInfo();
                const device = yield adapter.requestDevice({
                    requiredLimits: {
                        maxBufferSize: requiedMaxBufferSize,
                        maxStorageBufferBindingSize: requiredMaxStorageBufferBindingSize,
                        maxComputeWorkgroupStorageSize: requiredMaxComputeWorkgroupStorageSize,
                    },
                    requiredFeatures
                });
                return {
                    adapter: adapter,
                    adapterInfo: adapterInfo,
                    device: device
                };
            }
            else {
                return undefined;
            }
        });
    }
    const canvasRenderWGSL = `
@group(0) @binding(0) var my_sampler : sampler;
@group(0) @binding(1) var my_texture : texture_2d<f32>;

struct VertexOutput {
  @builtin(position) position : vec4<f32>,
  @location(0) uv : vec2<f32>,
}

@vertex
fn vertex_main(@builtin(vertex_index) vidx : u32) -> VertexOutput {
  const pos = array(
    vec2( 1.0,  1.0),
    vec2( 1.0, -1.0),
    vec2(-1.0, -1.0),
    vec2( 1.0,  1.0),
    vec2(-1.0, -1.0),
    vec2(-1.0,  1.0),
  );

  const uv = array(
    vec2(1.0, 0.0),
    vec2(1.0, 1.0),
    vec2(0.0, 1.0),
    vec2(1.0, 0.0),
    vec2(0.0, 1.0),
    vec2(0.0, 0.0),
  );

  var output : VertexOutput;
  output.position = vec4(pos[vidx], 0.0, 1.0);
  output.uv = uv[vidx];
  return output;
}

@fragment
fn fragment_main(@location(0) uv : vec2<f32>) -> @location(0) vec4<f32> {
  return textureSample(my_texture, my_sampler, uv);
}

@fragment
fn fragment_clear(@location(0) uv : vec2<f32>) -> @location(0) vec4<f32> {
  return vec4(1.0, 1.0, 1.0, 1.0);
}
`;
    class CanvaRenderManager {
        constructor(device, canvas) {
            this.device = device;
            const ctx = canvas.getContext("webgpu");
            if (ctx == null) {
                throw Error("Cannot bind WebGPU context");
            }
            this.canvasContext = ctx;
            this.canvasTextureFormat = navigator.gpu.getPreferredCanvasFormat();
            this.canvasContext.configure({
                device: this.device,
                format: this.canvasTextureFormat,
                alphaMode: "opaque",
            });
            this.renderPipeline = device.createRenderPipeline({
                layout: "auto",
                vertex: {
                    module: device.createShaderModule({
                        code: canvasRenderWGSL,
                    }),
                    entryPoint: "vertex_main",
                },
                fragment: {
                    module: device.createShaderModule({
                        code: canvasRenderWGSL,
                    }),
                    entryPoint: "fragment_main",
                    targets: [{
                            format: this.canvasTextureFormat,
                        }],
                },
                primitive: {
                    topology: "triangle-list",
                },
            });
            this.clearPipeline = device.createRenderPipeline({
                layout: "auto",
                vertex: {
                    module: device.createShaderModule({
                        code: canvasRenderWGSL,
                    }),
                    entryPoint: "vertex_main",
                },
                fragment: {
                    module: device.createShaderModule({
                        code: canvasRenderWGSL,
                    }),
                    entryPoint: "fragment_clear",
                    targets: [{
                            format: this.canvasTextureFormat,
                        }],
                },
                primitive: {
                    topology: "triangle-list",
                },
            });
            this.renderSampler = device.createSampler({
                magFilter: "linear",
                minFilter: "linear",
            });
            // staging texture always be in RGBA
            this.stagingTexture = device.createTexture({
                size: [canvas.height, canvas.width, 1],
                format: "rgba8unorm",
                usage: GPUTextureUsage.TEXTURE_BINDING |
                    GPUTextureUsage.COPY_DST |
                    GPUTextureUsage.RENDER_ATTACHMENT,
            });
        }
        clear() {
            const commandEncoder = this.device.createCommandEncoder();
            const passEncoder = commandEncoder.beginRenderPass({
                colorAttachments: [
                    {
                        view: this.canvasContext.getCurrentTexture().createView(),
                        clearValue: { r: 0.0, g: 0.0, b: 0.0, a: 1.0 },
                        loadOp: "clear",
                        storeOp: "store",
                    },
                ],
            });
            passEncoder.setPipeline(this.clearPipeline);
            const renderBindingGroup = this.device.createBindGroup({
                layout: this.renderPipeline.getBindGroupLayout(0),
                entries: [
                    { binding: 0, resource: this.renderSampler },
                    { binding: 1, resource: this.stagingTexture.createView() },
                ],
            });
            passEncoder.setBindGroup(0, renderBindingGroup);
            passEncoder.draw(6, 1, 0, 0);
            passEncoder.end();
            this.device.queue.submit([commandEncoder.finish()]);
        }
        draw(buffer, height, width) {
            // resize the staging texture
            if (height != this.stagingTexture.height || width != this.stagingTexture.width) {
                this.stagingTexture.destroy();
                this.stagingTexture = this.device.createTexture({
                    size: [height, width, 1],
                    format: "rgba8unorm",
                    usage: GPUTextureUsage.TEXTURE_BINDING |
                        GPUTextureUsage.COPY_DST |
                        GPUTextureUsage.RENDER_ATTACHMENT,
                });
            }
            const commandEncoder = this.device.createCommandEncoder();
            commandEncoder.copyBufferToTexture({
                buffer: buffer,
                offset: 0,
                bytesPerRow: this.stagingTexture.width * 4
            }, {
                texture: this.stagingTexture
            }, {
                width: this.stagingTexture.width,
                height: this.stagingTexture.height
            });
            const passEncoder = commandEncoder.beginRenderPass({
                colorAttachments: [
                    {
                        view: this.canvasContext.getCurrentTexture().createView(),
                        clearValue: { r: 0.0, g: 0.0, b: 0.0, a: 1.0 },
                        loadOp: "clear",
                        storeOp: "store",
                    },
                ],
            });
            passEncoder.setPipeline(this.renderPipeline);
            const renderBindingGroup = this.device.createBindGroup({
                layout: this.renderPipeline.getBindGroupLayout(0),
                entries: [
                    { binding: 0, resource: this.renderSampler },
                    { binding: 1, resource: this.stagingTexture.createView() },
                ],
            });
            passEncoder.setBindGroup(0, renderBindingGroup);
            passEncoder.draw(6, 1, 0, 0);
            passEncoder.end();
            this.device.queue.submit([commandEncoder.finish()]);
        }
        dispose() {
            this.stagingTexture.destroy();
        }
    }
    /**
     * WebGPU context
     * Manages all the webgpu resources here.
     */
    class WebGPUContext {
        constructor(memory, device) {
            // internal data
            this.bufferTable = [undefined];
            this.bufferTableFreeId = [];
            this.podArgStagingBuffers = [];
            this.canvasRenderManager = undefined;
            // number of pod arg staging buffers
            this.maxNumPodArgsStagingBuffers = 2;
            // flags for debugging
            // stats of the runtime.
            // peak allocation
            this.peakAllocatedBytes = 0;
            // current allocation
            this.currAllocatedBytes = 0;
            // all allocation(ignoring free)
            this.allAllocatedBytes = 0;
            // shader submit counter
            this.shaderSubmitCounter = 0;
            // limite number of shaders to be submitted, useful for debugging, default to -1
            this.debugShaderSubmitLimit = -1;
            // log and sync each step
            this.debugLogFinish = false;
            this.memory = memory;
            this.device = device;
        }
        /**
         * Dispose context.
         */
        dispose() {
            var _a, _b, _c;
            (_a = this.canvasRenderManager) === null || _a === void 0 ? void 0 : _a.dispose();
            this.bufferTableFreeId = [];
            while (this.bufferTable.length != 0) {
                (_b = this.bufferTable.pop()) === null || _b === void 0 ? void 0 : _b.destroy();
            }
            while (this.podArgStagingBuffers.length != 0) {
                (_c = this.podArgStagingBuffers.pop()) === null || _c === void 0 ? void 0 : _c.destroy();
            }
            this.device.destroy();
        }
        /**
         * Wait for all pending GPU tasks to complete
         */
        sync() {
            return __awaiter(this, void 0, void 0, function* () {
                yield this.device.queue.onSubmittedWorkDone();
            });
        }
        /**
         * Obtain the runtime information in readable format.
         */
        runtimeStatsText() {
            let info = "peak-memory=" + Math.ceil(this.peakAllocatedBytes / (1 << 20)) + " MB";
            info += ", all-memory=" + Math.ceil(this.allAllocatedBytes / (1 << 20)) + " MB";
            info += ", shader-submissions=" + this.shaderSubmitCounter;
            return info;
        }
        /**
         * Draw image from data in storage buffer.
         * @param ptr The GPU ptr
         * @param height The height of the image.
         * @param width The width of the image.
         */
        drawImageFromBuffer(ptr, height, width) {
            if (this.canvasRenderManager == undefined) {
                throw Error("Do not have a canvas context, call bindCanvas first");
            }
            this.canvasRenderManager.draw(this.gpuBufferFromPtr(ptr), height, width);
        }
        /**
         * Copy raw bytes into buffer ptr.
         *
         * @param rawBytes The raw bytes
         * @param toPtr The target gpu buffer ptr
         * @param toOffset The beginning offset
         * @param nbytes Number of bytes
         */
        copyRawBytesToBuffer(rawBytes, toPtr, toOffset, nbytes) {
            // Perhaps it would be more useful to use a staging buffer?
            this.device.queue.writeBuffer(this.gpuBufferFromPtr(toPtr), toOffset, rawBytes, 0, nbytes);
        }
        /**
         * Clear canvas
         */
        clearCanvas() {
            var _a;
            (_a = this.canvasRenderManager) === null || _a === void 0 ? void 0 : _a.clear();
        }
        /**
         * Bind a canvas element to the runtime.
         * @param canvas The HTML canvas/
         */
        bindCanvas(canvas) {
            this.canvasRenderManager = new CanvaRenderManager(this.device, canvas);
        }
        /**
         * Create a PackedFunc that runs the given shader
         * via createComputePipeline
         *
         * @param info The function information already parsed as a record.
         * @param code The shader data(in WGSL)
         * @returns The shader
         */
        createShader(finfo, code) {
            return this.createShadeInternal(finfo, code, false);
        }
        /**
         * Create a PackedFunc that runs the given shader asynchrously
         * via createComputePipelineAsync
         *
         * @param info The function information already parsed as a record.
         * @param code The shader data(in WGSL)
         * @returns The shader
         */
        createShaderAsync(finfo, code) {
            return __awaiter(this, void 0, void 0, function* () {
                return yield this.createShadeInternal(finfo, code, true);
            });
        }
        /**
         * Get the pod arg staging buffer
         * \param nbytes The minimum size.
         * \return The allocated buffer
         */
        getPodArgsBuffer(nbytes) {
            let buffer = undefined;
            if (this.podArgStagingBuffers.length >= this.maxNumPodArgsStagingBuffers) {
                buffer = this.podArgStagingBuffers.shift();
            }
            // minimum of 16 bytes
            let allocSize = 16;
            if (buffer !== undefined) {
                allocSize = buffer.size;
                if (buffer.size < nbytes) {
                    buffer.destroy();
                    buffer = undefined;
                }
            }
            while (allocSize < nbytes) {
                allocSize *= 2;
            }
            if (buffer == undefined) {
                // create uniform buffer
                buffer = this.device.createBuffer({
                    size: allocSize,
                    usage: GPUBufferUsage.UNIFORM | GPUBufferUsage.COPY_DST,
                });
            }
            assert(nbytes <= buffer.size);
            return buffer;
        }
        /**
         * Internal impl of createShader for both async and sync mode.
         *
         * @param info The function information already parsed as a record.
         * @param code The shader data(in WGSL)
         * @param asyncMode Whether use async mode.
         * @returns The shader function or promise of shader func.
         */
        createShadeInternal(finfo, code, asyncMode) {
            const dispatchToDim = [];
            let paramWriteAccess = [];
            for (let i = 0; i < finfo.launch_param_tags.length; ++i) {
                const tag = finfo.launch_param_tags[i];
                if (tag.startsWith("blockIdx.")) {
                    const target = tag.charCodeAt(tag.length - 1) - ("x".charCodeAt(0));
                    assert(target >= 0 && target < 3);
                    dispatchToDim.push(target);
                }
                else if (tag.startsWith("threadIdx.")) {
                    const target = tag.charCodeAt(tag.length - 1) - ("x".charCodeAt(0));
                    assert(target >= 0 && target < 3);
                    dispatchToDim.push(target + 3);
                }
                else if (tag.startsWith("paramWriteAccess:")) {
                    paramWriteAccess = JSON.parse(tag.substring(17));
                }
                else {
                    throw new Error("Cannot handle thread_axis " + tag);
                }
            }
            const layoutEntries = [];
            const bufferArgIndices = [];
            const podArgIndices = [];
            for (let i = 0; i < finfo.arg_types.length; ++i) {
                const dtype = finfo.arg_types[i];
                if (dtype == "handle") {
                    layoutEntries.push({
                        binding: bufferArgIndices.length,
                        visibility: GPUShaderStage.COMPUTE,
                        buffer: {
                            type: paramWriteAccess[bufferArgIndices.length] ? "storage" : "read-only-storage"
                        }
                    });
                    bufferArgIndices.push(i);
                }
                else if (dtype.startsWith("int") || dtype.startsWith("uint") || dtype.startsWith("float")) {
                    podArgIndices.push(i);
                }
                else {
                    throw new Error("Cannot handle argument type " + dtype + " in WebGPU shader");
                }
            }
            assert(paramWriteAccess.length == bufferArgIndices.length);
            // POD arguments are pass in the end
            layoutEntries.push({
                binding: bufferArgIndices.length,
                visibility: GPUShaderStage.COMPUTE,
                buffer: {
                    type: "uniform"
                }
            });
            const bindGroupLayout = this.device.createBindGroupLayout({
                entries: layoutEntries
            });
            const pipelineLayout = this.device.createPipelineLayout({
                bindGroupLayouts: [bindGroupLayout]
            });
            // Function to create the pipeline.
            const createShaderFunc = (pipeline) => {
                const submitShader = (...args) => {
                    if (this.debugShaderSubmitLimit != -1 &&
                        this.shaderSubmitCounter >= this.debugShaderSubmitLimit) {
                        this.shaderSubmitCounter += 1;
                        return;
                    }
                    const commandEncoder = this.device.createCommandEncoder();
                    const compute = commandEncoder.beginComputePass();
                    compute.setPipeline(pipeline);
                    const bindGroupEntries = [];
                    const numBufferOrPodArgs = bufferArgIndices.length + podArgIndices.length;
                    assert(args.length == numBufferOrPodArgs + dispatchToDim.length);
                    const workDim = [1, 1, 1, 1, 1, 1];
                    for (let i = 0; i < dispatchToDim.length; ++i) {
                        workDim[dispatchToDim[i]] = args[numBufferOrPodArgs + i];
                    }
                    // get around 65535 restriction of blockIdx.x
                    if (workDim[2] != 1) {
                        throw Error("WebGPU: blockIdx.z is reserved for internal use");
                    }
                    const packDimX = workDim[0];
                    // spread thinsg out into blockIdx.z
                    if (workDim[0] >= (1 << 16)) {
                        let wl_x = workDim[0];
                        let wl_z = workDim[2];
                        while (wl_x >= (1 << 16)) {
                            if (wl_x % 2 == 0) {
                                wl_x = wl_x / 2;
                            }
                            else {
                                // pad up
                                wl_x = (wl_x + 1) / 2;
                            }
                            wl_z *= 2;
                        }
                        workDim[0] = wl_x;
                        workDim[2] = wl_z;
                        assert(wl_x * wl_z >= packDimX);
                    }
                    for (let i = 0; i < bufferArgIndices.length; ++i) {
                        bindGroupEntries.push({
                            binding: i,
                            resource: {
                                buffer: this.gpuBufferFromPtr(args[bufferArgIndices[i]])
                            }
                        });
                    }
                    // push pod buffer
                    const sizeOfI32 = 4;
                    const podArgBuffer = this.getPodArgsBuffer((podArgIndices.length + 1) * sizeOfI32);
                    const i32View = new Int32Array(podArgIndices.length + 1);
                    const u32View = new Uint32Array(i32View.buffer);
                    const f32View = new Float32Array(i32View.buffer);
                    for (let i = 0; i < podArgIndices.length; ++i) {
                        const value = args[podArgIndices[i]];
                        const dtype = finfo.arg_types[podArgIndices[i]];
                        if (dtype.startsWith("int")) {
                            i32View[i] = value;
                        }
                        else if (dtype.startsWith("uint")) {
                            u32View[i] = value;
                        }
                        else if (dtype.startsWith("float")) {
                            f32View[i] = value;
                        }
                        else {
                            throw Error("Unknown pod dtype " + dtype);
                        }
                    }
                    // always pass in dim z launching grid size in
                    u32View[podArgIndices.length] = packDimX;
                    this.device.queue.writeBuffer(podArgBuffer, 0, i32View.buffer);
                    bindGroupEntries.push({
                        binding: bufferArgIndices.length,
                        resource: {
                            buffer: podArgBuffer,
                            size: i32View.buffer.byteLength
                        }
                    });
                    compute.setBindGroup(0, this.device.createBindGroup({
                        layout: bindGroupLayout,
                        entries: bindGroupEntries
                    }));
                    compute.dispatchWorkgroups(workDim[0], workDim[1], workDim[2]);
                    compute.end();
                    const command = commandEncoder.finish();
                    this.device.queue.submit([command]);
                    if (this.debugLogFinish) {
                        const currCounter = this.shaderSubmitCounter;
                        this.device.queue.onSubmittedWorkDone().then(() => {
                            console.log("[" + currCounter + "][Debug] finish shader" + finfo.name);
                        });
                    }
                    this.shaderSubmitCounter += 1;
                };
                return submitShader;
            };
            const shaderModule = this.device.createShaderModule({
                code: code,
                hints: {
                    main: {
                        layout: pipelineLayout
                    }
                }
            });
            if (asyncMode) {
                return this.device.createComputePipelineAsync({
                    layout: pipelineLayout,
                    compute: {
                        module: shaderModule,
                        entryPoint: finfo.name
                    }
                }).then((pipeline) => {
                    return createShaderFunc(pipeline);
                });
            }
            else {
                const pipeline = this.device.createComputePipeline({
                    layout: pipelineLayout,
                    compute: {
                        module: shaderModule,
                        entryPoint: finfo.name
                    }
                });
                return createShaderFunc(pipeline);
            }
        }
        /**
         * Get the device API according to its name
         * @param The name of the API.
         * @returns The corresponding device api.
         */
        getDeviceAPI(name) {
            if (name == "deviceAllocDataSpace") {
                return (nbytes) => {
                    return this.deviceAllocDataSpace(nbytes);
                };
            }
            else if (name == "deviceFreeDataSpace") {
                return (ptr) => {
                    return this.deviceFreeDataSpace(ptr);
                };
            }
            else if (name == "deviceCopyToGPU") {
                return (from, to, toOffset, nbytes) => {
                    this.deviceCopyToGPU(from, to, toOffset, nbytes);
                };
            }
            else if (name == "deviceCopyFromGPU") {
                return (from, fromOffset, to, nbytes) => {
                    this.deviceCopyFromGPU(from, fromOffset, to, nbytes);
                };
            }
            else if (name == "deviceCopyWithinGPU") {
                return (from, fromOffset, to, toOffset, nbytes) => {
                    this.deviceCopyWithinGPU(from, fromOffset, to, toOffset, nbytes);
                };
            }
            else {
                throw new Error("Unknown DeviceAPI function " + name);
            }
        }
        // DeviceAPI
        deviceAllocDataSpace(nbytes) {
            // allocate 0 bytes buffer as 1 bytes buffer.
            if (nbytes == 0) {
                nbytes = 1;
            }
            const buffer = this.device.createBuffer({
                size: nbytes,
                usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_SRC | GPUBufferUsage.COPY_DST,
            });
            this.currAllocatedBytes += nbytes;
            this.allAllocatedBytes += nbytes;
            if (this.currAllocatedBytes > this.peakAllocatedBytes) {
                this.peakAllocatedBytes = this.currAllocatedBytes;
            }
            const ptr = this.attachToBufferTable(buffer);
            return ptr;
        }
        deviceFreeDataSpace(ptr) {
            const idx = ptr;
            const buffer = this.bufferTable[idx];
            this.bufferTable[idx] = undefined;
            assert(buffer !== undefined);
            this.bufferTableFreeId.push(idx);
            this.currAllocatedBytes -= buffer.size;
            buffer.destroy();
        }
        deviceCopyToGPU(from, to, toOffset, nbytes) {
            // Perhaps it would be more useful to use a staging buffer?
            const rawBytes = this.memory.loadRawBytes(from, nbytes);
            this.device.queue.writeBuffer(this.gpuBufferFromPtr(to), toOffset, rawBytes, 0, nbytes);
        }
        deviceCopyFromGPU(from, fromOffset, to, nbytes) {
            // Perhaps it would be more useful to resuse a staging buffer?
            const gpuTemp = this.device.createBuffer({
                size: nbytes,
                usage: GPUBufferUsage.MAP_READ | GPUBufferUsage.COPY_DST,
            });
            const copyEncoder = this.device.createCommandEncoder();
            copyEncoder.copyBufferToBuffer(this.gpuBufferFromPtr(from), fromOffset, gpuTemp, 0, nbytes);
            const copyCommands = copyEncoder.finish();
            this.device.queue.submit([copyCommands]);
            gpuTemp.mapAsync(GPUMapMode.READ).then(() => {
                const data = gpuTemp.getMappedRange();
                this.memory.storeRawBytes(to, new Uint8Array(data));
                gpuTemp.destroy();
            });
        }
        deviceCopyWithinGPU(from, fromOffset, to, toOffset, nbytes) {
            const copyEncoder = this.device.createCommandEncoder();
            copyEncoder.copyBufferToBuffer(this.gpuBufferFromPtr(from), fromOffset, this.gpuBufferFromPtr(to), toOffset, nbytes);
            const copyCommands = copyEncoder.finish();
            this.device.queue.submit([copyCommands]);
        }
        gpuBufferFromPtr(ptr) {
            const buffer = this.bufferTable[ptr];
            assert(buffer !== undefined);
            return buffer;
        }
        attachToBufferTable(buffer) {
            if (this.bufferTableFreeId.length != 0) {
                const idx = this.bufferTableFreeId.pop();
                this.bufferTable[idx] = buffer;
                return idx;
            }
            else {
                const idx = this.bufferTable.length;
                this.bufferTable.push(buffer);
                return idx;
            }
        }
    }

    function EmccWASI() {
    var Module=typeof Module!="undefined"?Module:{};var __wasmLib={};function __wasmLibInstantiateWasm(imports,successCallback){__wasmLib.imports=imports;__wasmLib.successCallback=successCallback;}function __wasmLibStart(wasmInstance){__wasmLib.successCallback(wasmInstance);}__wasmLib.start=__wasmLibStart;var Module={"instantiateWasm":__wasmLibInstantiateWasm,"wasmLibraryProvider":__wasmLib};var moduleOverrides=Object.assign({},Module);var arguments_=[];var thisProgram="./this.program";var quit_=(status,toThrow)=>{throw toThrow};var ENVIRONMENT_IS_WEB=typeof window=="object";var ENVIRONMENT_IS_WORKER=typeof importScripts=="function";var ENVIRONMENT_IS_NODE=typeof process=="object"&&typeof process.versions=="object"&&typeof process.versions.node=="string";var scriptDirectory="";function locateFile(path){if(Module["locateFile"]){return Module["locateFile"](path,scriptDirectory)}return scriptDirectory+path}var read_,readAsync,readBinary;function logExceptionOnExit(e){if(e instanceof ExitStatus)return;let toLog=e;if(e&&typeof e=="object"&&e.stack){toLog=[e,e.stack];}err("exiting due to exception: "+toLog);}if(ENVIRONMENT_IS_NODE){var fs=require("fs");var nodePath=require("path");if(ENVIRONMENT_IS_WORKER){scriptDirectory=nodePath.dirname(scriptDirectory)+"/";}else {scriptDirectory=__dirname+"/";}read_=(filename,binary)=>{filename=isFileURI(filename)?new URL(filename):nodePath.normalize(filename);return fs.readFileSync(filename,binary?undefined:"utf8")};readBinary=filename=>{var ret=read_(filename,true);if(!ret.buffer){ret=new Uint8Array(ret);}return ret};readAsync=(filename,onload,onerror)=>{filename=isFileURI(filename)?new URL(filename):nodePath.normalize(filename);fs.readFile(filename,function(err,data){if(err)onerror(err);else onload(data.buffer);});};if(process.argv.length>1){thisProgram=process.argv[1].replace(/\\/g,"/");}arguments_=process.argv.slice(2);if(typeof module!="undefined"){module["exports"]=Module;}process.on("uncaughtException",function(ex){if(!(ex instanceof ExitStatus)){throw ex}});var nodeMajor=process.versions.node.split(".")[0];if(nodeMajor<15){process.on("unhandledRejection",function(reason){throw reason});}quit_=(status,toThrow)=>{if(keepRuntimeAlive()){process.exitCode=status;throw toThrow}logExceptionOnExit(toThrow);process.exit(status);};Module["inspect"]=function(){return "[Emscripten Module object]"};}else if(ENVIRONMENT_IS_WEB||ENVIRONMENT_IS_WORKER){if(ENVIRONMENT_IS_WORKER){scriptDirectory=self.location.href;}else if(typeof document!="undefined"&&document.currentScript){scriptDirectory=document.currentScript.src;}if(scriptDirectory.indexOf("blob:")!==0){scriptDirectory=scriptDirectory.substr(0,scriptDirectory.replace(/[?#].*/,"").lastIndexOf("/")+1);}else {scriptDirectory="";}{read_=url=>{var xhr=new XMLHttpRequest;xhr.open("GET",url,false);xhr.send(null);return xhr.responseText};if(ENVIRONMENT_IS_WORKER){readBinary=url=>{var xhr=new XMLHttpRequest;xhr.open("GET",url,false);xhr.responseType="arraybuffer";xhr.send(null);return new Uint8Array(xhr.response)};}readAsync=(url,onload,onerror)=>{var xhr=new XMLHttpRequest;xhr.open("GET",url,true);xhr.responseType="arraybuffer";xhr.onload=()=>{if(xhr.status==200||xhr.status==0&&xhr.response){onload(xhr.response);return}onerror();};xhr.onerror=onerror;xhr.send(null);};}}else;var out=Module["print"]||console.log.bind(console);var err=Module["printErr"]||console.warn.bind(console);Object.assign(Module,moduleOverrides);moduleOverrides=null;if(Module["arguments"])arguments_=Module["arguments"];if(Module["thisProgram"])thisProgram=Module["thisProgram"];if(Module["quit"])quit_=Module["quit"];var wasmBinary;if(Module["wasmBinary"])wasmBinary=Module["wasmBinary"];var noExitRuntime=Module["noExitRuntime"]||true;if(typeof WebAssembly!="object"){abort("no native wasm support detected");}var wasmMemory;var ABORT=false;var EXITSTATUS;function assert(condition,text){if(!condition){abort(text);}}var UTF8Decoder=typeof TextDecoder!="undefined"?new TextDecoder("utf8"):undefined;function UTF8ArrayToString(heapOrArray,idx,maxBytesToRead){var endIdx=idx+maxBytesToRead;var endPtr=idx;while(heapOrArray[endPtr]&&!(endPtr>=endIdx))++endPtr;if(endPtr-idx>16&&heapOrArray.buffer&&UTF8Decoder){return UTF8Decoder.decode(heapOrArray.subarray(idx,endPtr))}var str="";while(idx<endPtr){var u0=heapOrArray[idx++];if(!(u0&128)){str+=String.fromCharCode(u0);continue}var u1=heapOrArray[idx++]&63;if((u0&224)==192){str+=String.fromCharCode((u0&31)<<6|u1);continue}var u2=heapOrArray[idx++]&63;if((u0&240)==224){u0=(u0&15)<<12|u1<<6|u2;}else {u0=(u0&7)<<18|u1<<12|u2<<6|heapOrArray[idx++]&63;}if(u0<65536){str+=String.fromCharCode(u0);}else {var ch=u0-65536;str+=String.fromCharCode(55296|ch>>10,56320|ch&1023);}}return str}function UTF8ToString(ptr,maxBytesToRead){return ptr?UTF8ArrayToString(HEAPU8,ptr,maxBytesToRead):""}function stringToUTF8Array(str,heap,outIdx,maxBytesToWrite){if(!(maxBytesToWrite>0))return 0;var startIdx=outIdx;var endIdx=outIdx+maxBytesToWrite-1;for(var i=0;i<str.length;++i){var u=str.charCodeAt(i);if(u>=55296&&u<=57343){var u1=str.charCodeAt(++i);u=65536+((u&1023)<<10)|u1&1023;}if(u<=127){if(outIdx>=endIdx)break;heap[outIdx++]=u;}else if(u<=2047){if(outIdx+1>=endIdx)break;heap[outIdx++]=192|u>>6;heap[outIdx++]=128|u&63;}else if(u<=65535){if(outIdx+2>=endIdx)break;heap[outIdx++]=224|u>>12;heap[outIdx++]=128|u>>6&63;heap[outIdx++]=128|u&63;}else {if(outIdx+3>=endIdx)break;heap[outIdx++]=240|u>>18;heap[outIdx++]=128|u>>12&63;heap[outIdx++]=128|u>>6&63;heap[outIdx++]=128|u&63;}}heap[outIdx]=0;return outIdx-startIdx}function lengthBytesUTF8(str){var len=0;for(var i=0;i<str.length;++i){var c=str.charCodeAt(i);if(c<=127){len++;}else if(c<=2047){len+=2;}else if(c>=55296&&c<=57343){len+=4;++i;}else {len+=3;}}return len}var HEAP8,HEAPU8,HEAP32,HEAPU32;function updateMemoryViews(){var b=wasmMemory.buffer;Module["HEAP8"]=HEAP8=new Int8Array(b);Module["HEAP16"]=new Int16Array(b);Module["HEAP32"]=HEAP32=new Int32Array(b);Module["HEAPU8"]=HEAPU8=new Uint8Array(b);Module["HEAPU16"]=new Uint16Array(b);Module["HEAPU32"]=HEAPU32=new Uint32Array(b);Module["HEAPF32"]=new Float32Array(b);Module["HEAPF64"]=new Float64Array(b);Module["HEAP64"]=new BigInt64Array(b);Module["HEAPU64"]=new BigUint64Array(b);}var __ATPRERUN__=[];var __ATINIT__=[];var __ATMAIN__=[];var __ATPOSTRUN__=[];function keepRuntimeAlive(){return noExitRuntime}function preRun(){if(Module["preRun"]){if(typeof Module["preRun"]=="function")Module["preRun"]=[Module["preRun"]];while(Module["preRun"].length){addOnPreRun(Module["preRun"].shift());}}callRuntimeCallbacks(__ATPRERUN__);}function initRuntime(){if(!Module["noFSInit"]&&!FS.init.initialized)FS.init();FS.ignorePermissions=false;callRuntimeCallbacks(__ATINIT__);}function preMain(){callRuntimeCallbacks(__ATMAIN__);}function postRun(){if(Module["postRun"]){if(typeof Module["postRun"]=="function")Module["postRun"]=[Module["postRun"]];while(Module["postRun"].length){addOnPostRun(Module["postRun"].shift());}}callRuntimeCallbacks(__ATPOSTRUN__);}function addOnPreRun(cb){__ATPRERUN__.unshift(cb);}function addOnPostRun(cb){__ATPOSTRUN__.unshift(cb);}var runDependencies=0;var dependenciesFulfilled=null;function getUniqueRunDependency(id){return id}function addRunDependency(id){runDependencies++;if(Module["monitorRunDependencies"]){Module["monitorRunDependencies"](runDependencies);}}function removeRunDependency(id){runDependencies--;if(Module["monitorRunDependencies"]){Module["monitorRunDependencies"](runDependencies);}if(runDependencies==0){if(dependenciesFulfilled){var callback=dependenciesFulfilled;dependenciesFulfilled=null;callback();}}}function abort(what){if(Module["onAbort"]){Module["onAbort"](what);}what="Aborted("+what+")";err(what);ABORT=true;EXITSTATUS=1;what+=". Build with -sASSERTIONS for more info.";var e=new WebAssembly.RuntimeError(what);throw e}var dataURIPrefix="data:application/octet-stream;base64,";function isDataURI(filename){return filename.startsWith(dataURIPrefix)}function isFileURI(filename){return filename.startsWith("file://")}var wasmBinaryFile;wasmBinaryFile="tvmjs_runtime.wasm";if(!isDataURI(wasmBinaryFile)){wasmBinaryFile=locateFile(wasmBinaryFile);}function getBinary(file){try{if(file==wasmBinaryFile&&wasmBinary){return new Uint8Array(wasmBinary)}if(readBinary){return readBinary(file)}throw "both async and sync fetching of the wasm failed"}catch(err){abort(err);}}function getBinaryPromise(binaryFile){if(!wasmBinary&&(ENVIRONMENT_IS_WEB||ENVIRONMENT_IS_WORKER)){if(typeof fetch=="function"&&!isFileURI(binaryFile)){return fetch(binaryFile,{credentials:"same-origin"}).then(function(response){if(!response["ok"]){throw "failed to load wasm binary file at '"+binaryFile+"'"}return response["arrayBuffer"]()}).catch(function(){return getBinary(binaryFile)})}else {if(readAsync){return new Promise(function(resolve,reject){readAsync(binaryFile,function(response){resolve(new Uint8Array(response));},reject);})}}}return Promise.resolve().then(function(){return getBinary(binaryFile)})}function instantiateArrayBuffer(binaryFile,imports,receiver){return getBinaryPromise(binaryFile).then(function(binary){return WebAssembly.instantiate(binary,imports)}).then(function(instance){return instance}).then(receiver,function(reason){err("failed to asynchronously prepare wasm: "+reason);abort(reason);})}function instantiateAsync(binary,binaryFile,imports,callback){if(!binary&&typeof WebAssembly.instantiateStreaming=="function"&&!isDataURI(binaryFile)&&!isFileURI(binaryFile)&&!ENVIRONMENT_IS_NODE&&typeof fetch=="function"){return fetch(binaryFile,{credentials:"same-origin"}).then(function(response){var result=WebAssembly.instantiateStreaming(response,imports);return result.then(callback,function(reason){err("wasm streaming compile failed: "+reason);err("falling back to ArrayBuffer instantiation");return instantiateArrayBuffer(binaryFile,imports,callback)})})}else {return instantiateArrayBuffer(binaryFile,imports,callback)}}function createWasm(){var info={"env":wasmImports,"wasi_snapshot_preview1":wasmImports};function receiveInstance(instance,module){var exports=instance.exports;Module["asm"]=exports;wasmMemory=Module["asm"]["memory"];updateMemoryViews();Module["asm"]["__indirect_function_table"];removeRunDependency();return exports}addRunDependency();function receiveInstantiationResult(result){receiveInstance(result["instance"]);}if(Module["instantiateWasm"]){try{return Module["instantiateWasm"](info,receiveInstance)}catch(e){err("Module.instantiateWasm callback failed with error: "+e);return false}}instantiateAsync(wasmBinary,wasmBinaryFile,info,receiveInstantiationResult);return {}}var tempDouble;var tempI64;function ExitStatus(status){this.name="ExitStatus";this.message="Program terminated with exit("+status+")";this.status=status;}function callRuntimeCallbacks(callbacks){while(callbacks.length>0){callbacks.shift()(Module);}}function _TVMWasmPackedCFunc(){err("missing function: TVMWasmPackedCFunc");abort(-1);}function _TVMWasmPackedCFuncFinalizer(){err("missing function: TVMWasmPackedCFuncFinalizer");abort(-1);}function __ZN3tvm7runtime9threading10NumThreadsEv(){err("missing function: _ZN3tvm7runtime9threading10NumThreadsEv");abort(-1);}function __ZN3tvm7runtime9threading15ResetThreadPoolEv(){err("missing function: _ZN3tvm7runtime9threading15ResetThreadPoolEv");abort(-1);}var _emscripten_get_now;if(ENVIRONMENT_IS_NODE){_emscripten_get_now=()=>{var t=process.hrtime();return t[0]*1e3+t[1]/1e6};}else _emscripten_get_now=()=>performance.now();function checkWasiClock(clock_id){return clock_id==0||clock_id==1||clock_id==2||clock_id==3}var PATH={isAbs:path=>path.charAt(0)==="/",splitPath:filename=>{var splitPathRe=/^(\/?|)([\s\S]*?)((?:\.{1,2}|[^\/]+?|)(\.[^.\/]*|))(?:[\/]*)$/;return splitPathRe.exec(filename).slice(1)},normalizeArray:(parts,allowAboveRoot)=>{var up=0;for(var i=parts.length-1;i>=0;i--){var last=parts[i];if(last==="."){parts.splice(i,1);}else if(last===".."){parts.splice(i,1);up++;}else if(up){parts.splice(i,1);up--;}}if(allowAboveRoot){for(;up;up--){parts.unshift("..");}}return parts},normalize:path=>{var isAbsolute=PATH.isAbs(path),trailingSlash=path.substr(-1)==="/";path=PATH.normalizeArray(path.split("/").filter(p=>!!p),!isAbsolute).join("/");if(!path&&!isAbsolute){path=".";}if(path&&trailingSlash){path+="/";}return (isAbsolute?"/":"")+path},dirname:path=>{var result=PATH.splitPath(path),root=result[0],dir=result[1];if(!root&&!dir){return "."}if(dir){dir=dir.substr(0,dir.length-1);}return root+dir},basename:path=>{if(path==="/")return "/";path=PATH.normalize(path);path=path.replace(/\/$/,"");var lastSlash=path.lastIndexOf("/");if(lastSlash===-1)return path;return path.substr(lastSlash+1)},join:function(){var paths=Array.prototype.slice.call(arguments);return PATH.normalize(paths.join("/"))},join2:(l,r)=>{return PATH.normalize(l+"/"+r)}};function getRandomDevice(){if(typeof crypto=="object"&&typeof crypto["getRandomValues"]=="function"){var randomBuffer=new Uint8Array(1);return ()=>{crypto.getRandomValues(randomBuffer);return randomBuffer[0]}}else if(ENVIRONMENT_IS_NODE){try{var crypto_module=require("crypto");return ()=>crypto_module["randomBytes"](1)[0]}catch(e){}}return ()=>abort("randomDevice")}var PATH_FS={resolve:function(){var resolvedPath="",resolvedAbsolute=false;for(var i=arguments.length-1;i>=-1&&!resolvedAbsolute;i--){var path=i>=0?arguments[i]:FS.cwd();if(typeof path!="string"){throw new TypeError("Arguments to path.resolve must be strings")}else if(!path){return ""}resolvedPath=path+"/"+resolvedPath;resolvedAbsolute=PATH.isAbs(path);}resolvedPath=PATH.normalizeArray(resolvedPath.split("/").filter(p=>!!p),!resolvedAbsolute).join("/");return (resolvedAbsolute?"/":"")+resolvedPath||"."},relative:(from,to)=>{from=PATH_FS.resolve(from).substr(1);to=PATH_FS.resolve(to).substr(1);function trim(arr){var start=0;for(;start<arr.length;start++){if(arr[start]!=="")break}var end=arr.length-1;for(;end>=0;end--){if(arr[end]!=="")break}if(start>end)return [];return arr.slice(start,end-start+1)}var fromParts=trim(from.split("/"));var toParts=trim(to.split("/"));var length=Math.min(fromParts.length,toParts.length);var samePartsLength=length;for(var i=0;i<length;i++){if(fromParts[i]!==toParts[i]){samePartsLength=i;break}}var outputParts=[];for(var i=samePartsLength;i<fromParts.length;i++){outputParts.push("..");}outputParts=outputParts.concat(toParts.slice(samePartsLength));return outputParts.join("/")}};function intArrayFromString(stringy,dontAddNull,length){var len=length>0?length:lengthBytesUTF8(stringy)+1;var u8array=new Array(len);var numBytesWritten=stringToUTF8Array(stringy,u8array,0,u8array.length);if(dontAddNull)u8array.length=numBytesWritten;return u8array}var TTY={ttys:[],init:function(){},shutdown:function(){},register:function(dev,ops){TTY.ttys[dev]={input:[],output:[],ops:ops};FS.registerDevice(dev,TTY.stream_ops);},stream_ops:{open:function(stream){var tty=TTY.ttys[stream.node.rdev];if(!tty){throw new FS.ErrnoError(43)}stream.tty=tty;stream.seekable=false;},close:function(stream){stream.tty.ops.fsync(stream.tty);},fsync:function(stream){stream.tty.ops.fsync(stream.tty);},read:function(stream,buffer,offset,length,pos){if(!stream.tty||!stream.tty.ops.get_char){throw new FS.ErrnoError(60)}var bytesRead=0;for(var i=0;i<length;i++){var result;try{result=stream.tty.ops.get_char(stream.tty);}catch(e){throw new FS.ErrnoError(29)}if(result===undefined&&bytesRead===0){throw new FS.ErrnoError(6)}if(result===null||result===undefined)break;bytesRead++;buffer[offset+i]=result;}if(bytesRead){stream.node.timestamp=Date.now();}return bytesRead},write:function(stream,buffer,offset,length,pos){if(!stream.tty||!stream.tty.ops.put_char){throw new FS.ErrnoError(60)}try{for(var i=0;i<length;i++){stream.tty.ops.put_char(stream.tty,buffer[offset+i]);}}catch(e){throw new FS.ErrnoError(29)}if(length){stream.node.timestamp=Date.now();}return i}},default_tty_ops:{get_char:function(tty){if(!tty.input.length){var result=null;if(ENVIRONMENT_IS_NODE){var BUFSIZE=256;var buf=Buffer.alloc(BUFSIZE);var bytesRead=0;try{bytesRead=fs.readSync(process.stdin.fd,buf,0,BUFSIZE,-1);}catch(e){if(e.toString().includes("EOF"))bytesRead=0;else throw e}if(bytesRead>0){result=buf.slice(0,bytesRead).toString("utf-8");}else {result=null;}}else if(typeof window!="undefined"&&typeof window.prompt=="function"){result=window.prompt("Input: ");if(result!==null){result+="\n";}}else if(typeof readline=="function"){result=readline();if(result!==null){result+="\n";}}if(!result){return null}tty.input=intArrayFromString(result,true);}return tty.input.shift()},put_char:function(tty,val){if(val===null||val===10){out(UTF8ArrayToString(tty.output,0));tty.output=[];}else {if(val!=0)tty.output.push(val);}},fsync:function(tty){if(tty.output&&tty.output.length>0){out(UTF8ArrayToString(tty.output,0));tty.output=[];}}},default_tty1_ops:{put_char:function(tty,val){if(val===null||val===10){err(UTF8ArrayToString(tty.output,0));tty.output=[];}else {if(val!=0)tty.output.push(val);}},fsync:function(tty){if(tty.output&&tty.output.length>0){err(UTF8ArrayToString(tty.output,0));tty.output=[];}}}};function mmapAlloc(size){abort();}var MEMFS={ops_table:null,mount:function(mount){return MEMFS.createNode(null,"/",16384|511,0)},createNode:function(parent,name,mode,dev){if(FS.isBlkdev(mode)||FS.isFIFO(mode)){throw new FS.ErrnoError(63)}if(!MEMFS.ops_table){MEMFS.ops_table={dir:{node:{getattr:MEMFS.node_ops.getattr,setattr:MEMFS.node_ops.setattr,lookup:MEMFS.node_ops.lookup,mknod:MEMFS.node_ops.mknod,rename:MEMFS.node_ops.rename,unlink:MEMFS.node_ops.unlink,rmdir:MEMFS.node_ops.rmdir,readdir:MEMFS.node_ops.readdir,symlink:MEMFS.node_ops.symlink},stream:{llseek:MEMFS.stream_ops.llseek}},file:{node:{getattr:MEMFS.node_ops.getattr,setattr:MEMFS.node_ops.setattr},stream:{llseek:MEMFS.stream_ops.llseek,read:MEMFS.stream_ops.read,write:MEMFS.stream_ops.write,allocate:MEMFS.stream_ops.allocate,mmap:MEMFS.stream_ops.mmap,msync:MEMFS.stream_ops.msync}},link:{node:{getattr:MEMFS.node_ops.getattr,setattr:MEMFS.node_ops.setattr,readlink:MEMFS.node_ops.readlink},stream:{}},chrdev:{node:{getattr:MEMFS.node_ops.getattr,setattr:MEMFS.node_ops.setattr},stream:FS.chrdev_stream_ops}};}var node=FS.createNode(parent,name,mode,dev);if(FS.isDir(node.mode)){node.node_ops=MEMFS.ops_table.dir.node;node.stream_ops=MEMFS.ops_table.dir.stream;node.contents={};}else if(FS.isFile(node.mode)){node.node_ops=MEMFS.ops_table.file.node;node.stream_ops=MEMFS.ops_table.file.stream;node.usedBytes=0;node.contents=null;}else if(FS.isLink(node.mode)){node.node_ops=MEMFS.ops_table.link.node;node.stream_ops=MEMFS.ops_table.link.stream;}else if(FS.isChrdev(node.mode)){node.node_ops=MEMFS.ops_table.chrdev.node;node.stream_ops=MEMFS.ops_table.chrdev.stream;}node.timestamp=Date.now();if(parent){parent.contents[name]=node;parent.timestamp=node.timestamp;}return node},getFileDataAsTypedArray:function(node){if(!node.contents)return new Uint8Array(0);if(node.contents.subarray)return node.contents.subarray(0,node.usedBytes);return new Uint8Array(node.contents)},expandFileStorage:function(node,newCapacity){var prevCapacity=node.contents?node.contents.length:0;if(prevCapacity>=newCapacity)return;var CAPACITY_DOUBLING_MAX=1024*1024;newCapacity=Math.max(newCapacity,prevCapacity*(prevCapacity<CAPACITY_DOUBLING_MAX?2:1.125)>>>0);if(prevCapacity!=0)newCapacity=Math.max(newCapacity,256);var oldContents=node.contents;node.contents=new Uint8Array(newCapacity);if(node.usedBytes>0)node.contents.set(oldContents.subarray(0,node.usedBytes),0);},resizeFileStorage:function(node,newSize){if(node.usedBytes==newSize)return;if(newSize==0){node.contents=null;node.usedBytes=0;}else {var oldContents=node.contents;node.contents=new Uint8Array(newSize);if(oldContents){node.contents.set(oldContents.subarray(0,Math.min(newSize,node.usedBytes)));}node.usedBytes=newSize;}},node_ops:{getattr:function(node){var attr={};attr.dev=FS.isChrdev(node.mode)?node.id:1;attr.ino=node.id;attr.mode=node.mode;attr.nlink=1;attr.uid=0;attr.gid=0;attr.rdev=node.rdev;if(FS.isDir(node.mode)){attr.size=4096;}else if(FS.isFile(node.mode)){attr.size=node.usedBytes;}else if(FS.isLink(node.mode)){attr.size=node.link.length;}else {attr.size=0;}attr.atime=new Date(node.timestamp);attr.mtime=new Date(node.timestamp);attr.ctime=new Date(node.timestamp);attr.blksize=4096;attr.blocks=Math.ceil(attr.size/attr.blksize);return attr},setattr:function(node,attr){if(attr.mode!==undefined){node.mode=attr.mode;}if(attr.timestamp!==undefined){node.timestamp=attr.timestamp;}if(attr.size!==undefined){MEMFS.resizeFileStorage(node,attr.size);}},lookup:function(parent,name){throw FS.genericErrors[44]},mknod:function(parent,name,mode,dev){return MEMFS.createNode(parent,name,mode,dev)},rename:function(old_node,new_dir,new_name){if(FS.isDir(old_node.mode)){var new_node;try{new_node=FS.lookupNode(new_dir,new_name);}catch(e){}if(new_node){for(var i in new_node.contents){throw new FS.ErrnoError(55)}}}delete old_node.parent.contents[old_node.name];old_node.parent.timestamp=Date.now();old_node.name=new_name;new_dir.contents[new_name]=old_node;new_dir.timestamp=old_node.parent.timestamp;old_node.parent=new_dir;},unlink:function(parent,name){delete parent.contents[name];parent.timestamp=Date.now();},rmdir:function(parent,name){var node=FS.lookupNode(parent,name);for(var i in node.contents){throw new FS.ErrnoError(55)}delete parent.contents[name];parent.timestamp=Date.now();},readdir:function(node){var entries=[".",".."];for(var key in node.contents){if(!node.contents.hasOwnProperty(key)){continue}entries.push(key);}return entries},symlink:function(parent,newname,oldpath){var node=MEMFS.createNode(parent,newname,511|40960,0);node.link=oldpath;return node},readlink:function(node){if(!FS.isLink(node.mode)){throw new FS.ErrnoError(28)}return node.link}},stream_ops:{read:function(stream,buffer,offset,length,position){var contents=stream.node.contents;if(position>=stream.node.usedBytes)return 0;var size=Math.min(stream.node.usedBytes-position,length);if(size>8&&contents.subarray){buffer.set(contents.subarray(position,position+size),offset);}else {for(var i=0;i<size;i++)buffer[offset+i]=contents[position+i];}return size},write:function(stream,buffer,offset,length,position,canOwn){if(buffer.buffer===HEAP8.buffer){canOwn=false;}if(!length)return 0;var node=stream.node;node.timestamp=Date.now();if(buffer.subarray&&(!node.contents||node.contents.subarray)){if(canOwn){node.contents=buffer.subarray(offset,offset+length);node.usedBytes=length;return length}else if(node.usedBytes===0&&position===0){node.contents=buffer.slice(offset,offset+length);node.usedBytes=length;return length}else if(position+length<=node.usedBytes){node.contents.set(buffer.subarray(offset,offset+length),position);return length}}MEMFS.expandFileStorage(node,position+length);if(node.contents.subarray&&buffer.subarray){node.contents.set(buffer.subarray(offset,offset+length),position);}else {for(var i=0;i<length;i++){node.contents[position+i]=buffer[offset+i];}}node.usedBytes=Math.max(node.usedBytes,position+length);return length},llseek:function(stream,offset,whence){var position=offset;if(whence===1){position+=stream.position;}else if(whence===2){if(FS.isFile(stream.node.mode)){position+=stream.node.usedBytes;}}if(position<0){throw new FS.ErrnoError(28)}return position},allocate:function(stream,offset,length){MEMFS.expandFileStorage(stream.node,offset+length);stream.node.usedBytes=Math.max(stream.node.usedBytes,offset+length);},mmap:function(stream,length,position,prot,flags){if(!FS.isFile(stream.node.mode)){throw new FS.ErrnoError(43)}var ptr;var allocated;var contents=stream.node.contents;if(!(flags&2)&&contents.buffer===HEAP8.buffer){allocated=false;ptr=contents.byteOffset;}else {if(position>0||position+length<contents.length){if(contents.subarray){contents=contents.subarray(position,position+length);}else {contents=Array.prototype.slice.call(contents,position,position+length);}}allocated=true;ptr=mmapAlloc();if(!ptr){throw new FS.ErrnoError(48)}HEAP8.set(contents,ptr);}return {ptr:ptr,allocated:allocated}},msync:function(stream,buffer,offset,length,mmapFlags){MEMFS.stream_ops.write(stream,buffer,0,length,offset,false);return 0}}};function asyncLoad(url,onload,onerror,noRunDep){var dep=!noRunDep?getUniqueRunDependency("al "+url):"";readAsync(url,arrayBuffer=>{assert(arrayBuffer,'Loading data file "'+url+'" failed (no arrayBuffer).');onload(new Uint8Array(arrayBuffer));if(dep)removeRunDependency();},event=>{if(onerror){onerror();}else {throw 'Loading data file "'+url+'" failed.'}});if(dep)addRunDependency();}var FS={root:null,mounts:[],devices:{},streams:[],nextInode:1,nameTable:null,currentPath:"/",initialized:false,ignorePermissions:true,ErrnoError:null,genericErrors:{},filesystems:null,syncFSRequests:0,lookupPath:(path,opts={})=>{path=PATH_FS.resolve(path);if(!path)return {path:"",node:null};var defaults={follow_mount:true,recurse_count:0};opts=Object.assign(defaults,opts);if(opts.recurse_count>8){throw new FS.ErrnoError(32)}var parts=path.split("/").filter(p=>!!p);var current=FS.root;var current_path="/";for(var i=0;i<parts.length;i++){var islast=i===parts.length-1;if(islast&&opts.parent){break}current=FS.lookupNode(current,parts[i]);current_path=PATH.join2(current_path,parts[i]);if(FS.isMountpoint(current)){if(!islast||islast&&opts.follow_mount){current=current.mounted.root;}}if(!islast||opts.follow){var count=0;while(FS.isLink(current.mode)){var link=FS.readlink(current_path);current_path=PATH_FS.resolve(PATH.dirname(current_path),link);var lookup=FS.lookupPath(current_path,{recurse_count:opts.recurse_count+1});current=lookup.node;if(count++>40){throw new FS.ErrnoError(32)}}}}return {path:current_path,node:current}},getPath:node=>{var path;while(true){if(FS.isRoot(node)){var mount=node.mount.mountpoint;if(!path)return mount;return mount[mount.length-1]!=="/"?mount+"/"+path:mount+path}path=path?node.name+"/"+path:node.name;node=node.parent;}},hashName:(parentid,name)=>{var hash=0;for(var i=0;i<name.length;i++){hash=(hash<<5)-hash+name.charCodeAt(i)|0;}return (parentid+hash>>>0)%FS.nameTable.length},hashAddNode:node=>{var hash=FS.hashName(node.parent.id,node.name);node.name_next=FS.nameTable[hash];FS.nameTable[hash]=node;},hashRemoveNode:node=>{var hash=FS.hashName(node.parent.id,node.name);if(FS.nameTable[hash]===node){FS.nameTable[hash]=node.name_next;}else {var current=FS.nameTable[hash];while(current){if(current.name_next===node){current.name_next=node.name_next;break}current=current.name_next;}}},lookupNode:(parent,name)=>{var errCode=FS.mayLookup(parent);if(errCode){throw new FS.ErrnoError(errCode,parent)}var hash=FS.hashName(parent.id,name);for(var node=FS.nameTable[hash];node;node=node.name_next){var nodeName=node.name;if(node.parent.id===parent.id&&nodeName===name){return node}}return FS.lookup(parent,name)},createNode:(parent,name,mode,rdev)=>{var node=new FS.FSNode(parent,name,mode,rdev);FS.hashAddNode(node);return node},destroyNode:node=>{FS.hashRemoveNode(node);},isRoot:node=>{return node===node.parent},isMountpoint:node=>{return !!node.mounted},isFile:mode=>{return (mode&61440)===32768},isDir:mode=>{return (mode&61440)===16384},isLink:mode=>{return (mode&61440)===40960},isChrdev:mode=>{return (mode&61440)===8192},isBlkdev:mode=>{return (mode&61440)===24576},isFIFO:mode=>{return (mode&61440)===4096},isSocket:mode=>{return (mode&49152)===49152},flagModes:{"r":0,"r+":2,"w":577,"w+":578,"a":1089,"a+":1090},modeStringToFlags:str=>{var flags=FS.flagModes[str];if(typeof flags=="undefined"){throw new Error("Unknown file open mode: "+str)}return flags},flagsToPermissionString:flag=>{var perms=["r","w","rw"][flag&3];if(flag&512){perms+="w";}return perms},nodePermissions:(node,perms)=>{if(FS.ignorePermissions){return 0}if(perms.includes("r")&&!(node.mode&292)){return 2}else if(perms.includes("w")&&!(node.mode&146)){return 2}else if(perms.includes("x")&&!(node.mode&73)){return 2}return 0},mayLookup:dir=>{var errCode=FS.nodePermissions(dir,"x");if(errCode)return errCode;if(!dir.node_ops.lookup)return 2;return 0},mayCreate:(dir,name)=>{try{var node=FS.lookupNode(dir,name);return 20}catch(e){}return FS.nodePermissions(dir,"wx")},mayDelete:(dir,name,isdir)=>{var node;try{node=FS.lookupNode(dir,name);}catch(e){return e.errno}var errCode=FS.nodePermissions(dir,"wx");if(errCode){return errCode}if(isdir){if(!FS.isDir(node.mode)){return 54}if(FS.isRoot(node)||FS.getPath(node)===FS.cwd()){return 10}}else {if(FS.isDir(node.mode)){return 31}}return 0},mayOpen:(node,flags)=>{if(!node){return 44}if(FS.isLink(node.mode)){return 32}else if(FS.isDir(node.mode)){if(FS.flagsToPermissionString(flags)!=="r"||flags&512){return 31}}return FS.nodePermissions(node,FS.flagsToPermissionString(flags))},MAX_OPEN_FDS:4096,nextfd:(fd_start=0,fd_end=FS.MAX_OPEN_FDS)=>{for(var fd=fd_start;fd<=fd_end;fd++){if(!FS.streams[fd]){return fd}}throw new FS.ErrnoError(33)},getStream:fd=>FS.streams[fd],createStream:(stream,fd_start,fd_end)=>{if(!FS.FSStream){FS.FSStream=function(){this.shared={};};FS.FSStream.prototype={};Object.defineProperties(FS.FSStream.prototype,{object:{get:function(){return this.node},set:function(val){this.node=val;}},isRead:{get:function(){return (this.flags&2097155)!==1}},isWrite:{get:function(){return (this.flags&2097155)!==0}},isAppend:{get:function(){return this.flags&1024}},flags:{get:function(){return this.shared.flags},set:function(val){this.shared.flags=val;}},position:{get:function(){return this.shared.position},set:function(val){this.shared.position=val;}}});}stream=Object.assign(new FS.FSStream,stream);var fd=FS.nextfd(fd_start,fd_end);stream.fd=fd;FS.streams[fd]=stream;return stream},closeStream:fd=>{FS.streams[fd]=null;},chrdev_stream_ops:{open:stream=>{var device=FS.getDevice(stream.node.rdev);stream.stream_ops=device.stream_ops;if(stream.stream_ops.open){stream.stream_ops.open(stream);}},llseek:()=>{throw new FS.ErrnoError(70)}},major:dev=>dev>>8,minor:dev=>dev&255,makedev:(ma,mi)=>ma<<8|mi,registerDevice:(dev,ops)=>{FS.devices[dev]={stream_ops:ops};},getDevice:dev=>FS.devices[dev],getMounts:mount=>{var mounts=[];var check=[mount];while(check.length){var m=check.pop();mounts.push(m);check.push.apply(check,m.mounts);}return mounts},syncfs:(populate,callback)=>{if(typeof populate=="function"){callback=populate;populate=false;}FS.syncFSRequests++;if(FS.syncFSRequests>1){err("warning: "+FS.syncFSRequests+" FS.syncfs operations in flight at once, probably just doing extra work");}var mounts=FS.getMounts(FS.root.mount);var completed=0;function doCallback(errCode){FS.syncFSRequests--;return callback(errCode)}function done(errCode){if(errCode){if(!done.errored){done.errored=true;return doCallback(errCode)}return}if(++completed>=mounts.length){doCallback(null);}}mounts.forEach(mount=>{if(!mount.type.syncfs){return done(null)}mount.type.syncfs(mount,populate,done);});},mount:(type,opts,mountpoint)=>{var root=mountpoint==="/";var pseudo=!mountpoint;var node;if(root&&FS.root){throw new FS.ErrnoError(10)}else if(!root&&!pseudo){var lookup=FS.lookupPath(mountpoint,{follow_mount:false});mountpoint=lookup.path;node=lookup.node;if(FS.isMountpoint(node)){throw new FS.ErrnoError(10)}if(!FS.isDir(node.mode)){throw new FS.ErrnoError(54)}}var mount={type:type,opts:opts,mountpoint:mountpoint,mounts:[]};var mountRoot=type.mount(mount);mountRoot.mount=mount;mount.root=mountRoot;if(root){FS.root=mountRoot;}else if(node){node.mounted=mount;if(node.mount){node.mount.mounts.push(mount);}}return mountRoot},unmount:mountpoint=>{var lookup=FS.lookupPath(mountpoint,{follow_mount:false});if(!FS.isMountpoint(lookup.node)){throw new FS.ErrnoError(28)}var node=lookup.node;var mount=node.mounted;var mounts=FS.getMounts(mount);Object.keys(FS.nameTable).forEach(hash=>{var current=FS.nameTable[hash];while(current){var next=current.name_next;if(mounts.includes(current.mount)){FS.destroyNode(current);}current=next;}});node.mounted=null;var idx=node.mount.mounts.indexOf(mount);node.mount.mounts.splice(idx,1);},lookup:(parent,name)=>{return parent.node_ops.lookup(parent,name)},mknod:(path,mode,dev)=>{var lookup=FS.lookupPath(path,{parent:true});var parent=lookup.node;var name=PATH.basename(path);if(!name||name==="."||name===".."){throw new FS.ErrnoError(28)}var errCode=FS.mayCreate(parent,name);if(errCode){throw new FS.ErrnoError(errCode)}if(!parent.node_ops.mknod){throw new FS.ErrnoError(63)}return parent.node_ops.mknod(parent,name,mode,dev)},create:(path,mode)=>{mode=mode!==undefined?mode:438;mode&=4095;mode|=32768;return FS.mknod(path,mode,0)},mkdir:(path,mode)=>{mode=mode!==undefined?mode:511;mode&=511|512;mode|=16384;return FS.mknod(path,mode,0)},mkdirTree:(path,mode)=>{var dirs=path.split("/");var d="";for(var i=0;i<dirs.length;++i){if(!dirs[i])continue;d+="/"+dirs[i];try{FS.mkdir(d,mode);}catch(e){if(e.errno!=20)throw e}}},mkdev:(path,mode,dev)=>{if(typeof dev=="undefined"){dev=mode;mode=438;}mode|=8192;return FS.mknod(path,mode,dev)},symlink:(oldpath,newpath)=>{if(!PATH_FS.resolve(oldpath)){throw new FS.ErrnoError(44)}var lookup=FS.lookupPath(newpath,{parent:true});var parent=lookup.node;if(!parent){throw new FS.ErrnoError(44)}var newname=PATH.basename(newpath);var errCode=FS.mayCreate(parent,newname);if(errCode){throw new FS.ErrnoError(errCode)}if(!parent.node_ops.symlink){throw new FS.ErrnoError(63)}return parent.node_ops.symlink(parent,newname,oldpath)},rename:(old_path,new_path)=>{var old_dirname=PATH.dirname(old_path);var new_dirname=PATH.dirname(new_path);var old_name=PATH.basename(old_path);var new_name=PATH.basename(new_path);var lookup,old_dir,new_dir;lookup=FS.lookupPath(old_path,{parent:true});old_dir=lookup.node;lookup=FS.lookupPath(new_path,{parent:true});new_dir=lookup.node;if(!old_dir||!new_dir)throw new FS.ErrnoError(44);if(old_dir.mount!==new_dir.mount){throw new FS.ErrnoError(75)}var old_node=FS.lookupNode(old_dir,old_name);var relative=PATH_FS.relative(old_path,new_dirname);if(relative.charAt(0)!=="."){throw new FS.ErrnoError(28)}relative=PATH_FS.relative(new_path,old_dirname);if(relative.charAt(0)!=="."){throw new FS.ErrnoError(55)}var new_node;try{new_node=FS.lookupNode(new_dir,new_name);}catch(e){}if(old_node===new_node){return}var isdir=FS.isDir(old_node.mode);var errCode=FS.mayDelete(old_dir,old_name,isdir);if(errCode){throw new FS.ErrnoError(errCode)}errCode=new_node?FS.mayDelete(new_dir,new_name,isdir):FS.mayCreate(new_dir,new_name);if(errCode){throw new FS.ErrnoError(errCode)}if(!old_dir.node_ops.rename){throw new FS.ErrnoError(63)}if(FS.isMountpoint(old_node)||new_node&&FS.isMountpoint(new_node)){throw new FS.ErrnoError(10)}if(new_dir!==old_dir){errCode=FS.nodePermissions(old_dir,"w");if(errCode){throw new FS.ErrnoError(errCode)}}FS.hashRemoveNode(old_node);try{old_dir.node_ops.rename(old_node,new_dir,new_name);}catch(e){throw e}finally{FS.hashAddNode(old_node);}},rmdir:path=>{var lookup=FS.lookupPath(path,{parent:true});var parent=lookup.node;var name=PATH.basename(path);var node=FS.lookupNode(parent,name);var errCode=FS.mayDelete(parent,name,true);if(errCode){throw new FS.ErrnoError(errCode)}if(!parent.node_ops.rmdir){throw new FS.ErrnoError(63)}if(FS.isMountpoint(node)){throw new FS.ErrnoError(10)}parent.node_ops.rmdir(parent,name);FS.destroyNode(node);},readdir:path=>{var lookup=FS.lookupPath(path,{follow:true});var node=lookup.node;if(!node.node_ops.readdir){throw new FS.ErrnoError(54)}return node.node_ops.readdir(node)},unlink:path=>{var lookup=FS.lookupPath(path,{parent:true});var parent=lookup.node;if(!parent){throw new FS.ErrnoError(44)}var name=PATH.basename(path);var node=FS.lookupNode(parent,name);var errCode=FS.mayDelete(parent,name,false);if(errCode){throw new FS.ErrnoError(errCode)}if(!parent.node_ops.unlink){throw new FS.ErrnoError(63)}if(FS.isMountpoint(node)){throw new FS.ErrnoError(10)}parent.node_ops.unlink(parent,name);FS.destroyNode(node);},readlink:path=>{var lookup=FS.lookupPath(path);var link=lookup.node;if(!link){throw new FS.ErrnoError(44)}if(!link.node_ops.readlink){throw new FS.ErrnoError(28)}return PATH_FS.resolve(FS.getPath(link.parent),link.node_ops.readlink(link))},stat:(path,dontFollow)=>{var lookup=FS.lookupPath(path,{follow:!dontFollow});var node=lookup.node;if(!node){throw new FS.ErrnoError(44)}if(!node.node_ops.getattr){throw new FS.ErrnoError(63)}return node.node_ops.getattr(node)},lstat:path=>{return FS.stat(path,true)},chmod:(path,mode,dontFollow)=>{var node;if(typeof path=="string"){var lookup=FS.lookupPath(path,{follow:!dontFollow});node=lookup.node;}else {node=path;}if(!node.node_ops.setattr){throw new FS.ErrnoError(63)}node.node_ops.setattr(node,{mode:mode&4095|node.mode&~4095,timestamp:Date.now()});},lchmod:(path,mode)=>{FS.chmod(path,mode,true);},fchmod:(fd,mode)=>{var stream=FS.getStream(fd);if(!stream){throw new FS.ErrnoError(8)}FS.chmod(stream.node,mode);},chown:(path,uid,gid,dontFollow)=>{var node;if(typeof path=="string"){var lookup=FS.lookupPath(path,{follow:!dontFollow});node=lookup.node;}else {node=path;}if(!node.node_ops.setattr){throw new FS.ErrnoError(63)}node.node_ops.setattr(node,{timestamp:Date.now()});},lchown:(path,uid,gid)=>{FS.chown(path,uid,gid,true);},fchown:(fd,uid,gid)=>{var stream=FS.getStream(fd);if(!stream){throw new FS.ErrnoError(8)}FS.chown(stream.node,uid,gid);},truncate:(path,len)=>{if(len<0){throw new FS.ErrnoError(28)}var node;if(typeof path=="string"){var lookup=FS.lookupPath(path,{follow:true});node=lookup.node;}else {node=path;}if(!node.node_ops.setattr){throw new FS.ErrnoError(63)}if(FS.isDir(node.mode)){throw new FS.ErrnoError(31)}if(!FS.isFile(node.mode)){throw new FS.ErrnoError(28)}var errCode=FS.nodePermissions(node,"w");if(errCode){throw new FS.ErrnoError(errCode)}node.node_ops.setattr(node,{size:len,timestamp:Date.now()});},ftruncate:(fd,len)=>{var stream=FS.getStream(fd);if(!stream){throw new FS.ErrnoError(8)}if((stream.flags&2097155)===0){throw new FS.ErrnoError(28)}FS.truncate(stream.node,len);},utime:(path,atime,mtime)=>{var lookup=FS.lookupPath(path,{follow:true});var node=lookup.node;node.node_ops.setattr(node,{timestamp:Math.max(atime,mtime)});},open:(path,flags,mode)=>{if(path===""){throw new FS.ErrnoError(44)}flags=typeof flags=="string"?FS.modeStringToFlags(flags):flags;mode=typeof mode=="undefined"?438:mode;if(flags&64){mode=mode&4095|32768;}else {mode=0;}var node;if(typeof path=="object"){node=path;}else {path=PATH.normalize(path);try{var lookup=FS.lookupPath(path,{follow:!(flags&131072)});node=lookup.node;}catch(e){}}var created=false;if(flags&64){if(node){if(flags&128){throw new FS.ErrnoError(20)}}else {node=FS.mknod(path,mode,0);created=true;}}if(!node){throw new FS.ErrnoError(44)}if(FS.isChrdev(node.mode)){flags&=~512;}if(flags&65536&&!FS.isDir(node.mode)){throw new FS.ErrnoError(54)}if(!created){var errCode=FS.mayOpen(node,flags);if(errCode){throw new FS.ErrnoError(errCode)}}if(flags&512&&!created){FS.truncate(node,0);}flags&=~(128|512|131072);var stream=FS.createStream({node:node,path:FS.getPath(node),flags:flags,seekable:true,position:0,stream_ops:node.stream_ops,ungotten:[],error:false});if(stream.stream_ops.open){stream.stream_ops.open(stream);}if(Module["logReadFiles"]&&!(flags&1)){if(!FS.readFiles)FS.readFiles={};if(!(path in FS.readFiles)){FS.readFiles[path]=1;}}return stream},close:stream=>{if(FS.isClosed(stream)){throw new FS.ErrnoError(8)}if(stream.getdents)stream.getdents=null;try{if(stream.stream_ops.close){stream.stream_ops.close(stream);}}catch(e){throw e}finally{FS.closeStream(stream.fd);}stream.fd=null;},isClosed:stream=>{return stream.fd===null},llseek:(stream,offset,whence)=>{if(FS.isClosed(stream)){throw new FS.ErrnoError(8)}if(!stream.seekable||!stream.stream_ops.llseek){throw new FS.ErrnoError(70)}if(whence!=0&&whence!=1&&whence!=2){throw new FS.ErrnoError(28)}stream.position=stream.stream_ops.llseek(stream,offset,whence);stream.ungotten=[];return stream.position},read:(stream,buffer,offset,length,position)=>{if(length<0||position<0){throw new FS.ErrnoError(28)}if(FS.isClosed(stream)){throw new FS.ErrnoError(8)}if((stream.flags&2097155)===1){throw new FS.ErrnoError(8)}if(FS.isDir(stream.node.mode)){throw new FS.ErrnoError(31)}if(!stream.stream_ops.read){throw new FS.ErrnoError(28)}var seeking=typeof position!="undefined";if(!seeking){position=stream.position;}else if(!stream.seekable){throw new FS.ErrnoError(70)}var bytesRead=stream.stream_ops.read(stream,buffer,offset,length,position);if(!seeking)stream.position+=bytesRead;return bytesRead},write:(stream,buffer,offset,length,position,canOwn)=>{if(length<0||position<0){throw new FS.ErrnoError(28)}if(FS.isClosed(stream)){throw new FS.ErrnoError(8)}if((stream.flags&2097155)===0){throw new FS.ErrnoError(8)}if(FS.isDir(stream.node.mode)){throw new FS.ErrnoError(31)}if(!stream.stream_ops.write){throw new FS.ErrnoError(28)}if(stream.seekable&&stream.flags&1024){FS.llseek(stream,0,2);}var seeking=typeof position!="undefined";if(!seeking){position=stream.position;}else if(!stream.seekable){throw new FS.ErrnoError(70)}var bytesWritten=stream.stream_ops.write(stream,buffer,offset,length,position,canOwn);if(!seeking)stream.position+=bytesWritten;return bytesWritten},allocate:(stream,offset,length)=>{if(FS.isClosed(stream)){throw new FS.ErrnoError(8)}if(offset<0||length<=0){throw new FS.ErrnoError(28)}if((stream.flags&2097155)===0){throw new FS.ErrnoError(8)}if(!FS.isFile(stream.node.mode)&&!FS.isDir(stream.node.mode)){throw new FS.ErrnoError(43)}if(!stream.stream_ops.allocate){throw new FS.ErrnoError(138)}stream.stream_ops.allocate(stream,offset,length);},mmap:(stream,length,position,prot,flags)=>{if((prot&2)!==0&&(flags&2)===0&&(stream.flags&2097155)!==2){throw new FS.ErrnoError(2)}if((stream.flags&2097155)===1){throw new FS.ErrnoError(2)}if(!stream.stream_ops.mmap){throw new FS.ErrnoError(43)}return stream.stream_ops.mmap(stream,length,position,prot,flags)},msync:(stream,buffer,offset,length,mmapFlags)=>{if(!stream.stream_ops.msync){return 0}return stream.stream_ops.msync(stream,buffer,offset,length,mmapFlags)},munmap:stream=>0,ioctl:(stream,cmd,arg)=>{if(!stream.stream_ops.ioctl){throw new FS.ErrnoError(59)}return stream.stream_ops.ioctl(stream,cmd,arg)},readFile:(path,opts={})=>{opts.flags=opts.flags||0;opts.encoding=opts.encoding||"binary";if(opts.encoding!=="utf8"&&opts.encoding!=="binary"){throw new Error('Invalid encoding type "'+opts.encoding+'"')}var ret;var stream=FS.open(path,opts.flags);var stat=FS.stat(path);var length=stat.size;var buf=new Uint8Array(length);FS.read(stream,buf,0,length,0);if(opts.encoding==="utf8"){ret=UTF8ArrayToString(buf,0);}else if(opts.encoding==="binary"){ret=buf;}FS.close(stream);return ret},writeFile:(path,data,opts={})=>{opts.flags=opts.flags||577;var stream=FS.open(path,opts.flags,opts.mode);if(typeof data=="string"){var buf=new Uint8Array(lengthBytesUTF8(data)+1);var actualNumBytes=stringToUTF8Array(data,buf,0,buf.length);FS.write(stream,buf,0,actualNumBytes,undefined,opts.canOwn);}else if(ArrayBuffer.isView(data)){FS.write(stream,data,0,data.byteLength,undefined,opts.canOwn);}else {throw new Error("Unsupported data type")}FS.close(stream);},cwd:()=>FS.currentPath,chdir:path=>{var lookup=FS.lookupPath(path,{follow:true});if(lookup.node===null){throw new FS.ErrnoError(44)}if(!FS.isDir(lookup.node.mode)){throw new FS.ErrnoError(54)}var errCode=FS.nodePermissions(lookup.node,"x");if(errCode){throw new FS.ErrnoError(errCode)}FS.currentPath=lookup.path;},createDefaultDirectories:()=>{FS.mkdir("/tmp");FS.mkdir("/home");FS.mkdir("/home/web_user");},createDefaultDevices:()=>{FS.mkdir("/dev");FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length});FS.mkdev("/dev/null",FS.makedev(1,3));TTY.register(FS.makedev(5,0),TTY.default_tty_ops);TTY.register(FS.makedev(6,0),TTY.default_tty1_ops);FS.mkdev("/dev/tty",FS.makedev(5,0));FS.mkdev("/dev/tty1",FS.makedev(6,0));var random_device=getRandomDevice();FS.createDevice("/dev","random",random_device);FS.createDevice("/dev","urandom",random_device);FS.mkdir("/dev/shm");FS.mkdir("/dev/shm/tmp");},createSpecialDirectories:()=>{FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mkdir("/proc/self/fd");FS.mount({mount:()=>{var node=FS.createNode(proc_self,"fd",16384|511,73);node.node_ops={lookup:(parent,name)=>{var fd=+name;var stream=FS.getStream(fd);if(!stream)throw new FS.ErrnoError(8);var ret={parent:null,mount:{mountpoint:"fake"},node_ops:{readlink:()=>stream.path}};ret.parent=ret;return ret}};return node}},{},"/proc/self/fd");},createStandardStreams:()=>{if(Module["stdin"]){FS.createDevice("/dev","stdin",Module["stdin"]);}else {FS.symlink("/dev/tty","/dev/stdin");}if(Module["stdout"]){FS.createDevice("/dev","stdout",null,Module["stdout"]);}else {FS.symlink("/dev/tty","/dev/stdout");}if(Module["stderr"]){FS.createDevice("/dev","stderr",null,Module["stderr"]);}else {FS.symlink("/dev/tty1","/dev/stderr");}FS.open("/dev/stdin",0);FS.open("/dev/stdout",1);FS.open("/dev/stderr",1);},ensureErrnoError:()=>{if(FS.ErrnoError)return;FS.ErrnoError=function ErrnoError(errno,node){this.name="ErrnoError";this.node=node;this.setErrno=function(errno){this.errno=errno;};this.setErrno(errno);this.message="FS error";};FS.ErrnoError.prototype=new Error;FS.ErrnoError.prototype.constructor=FS.ErrnoError;[44].forEach(code=>{FS.genericErrors[code]=new FS.ErrnoError(code);FS.genericErrors[code].stack="<generic error, no stack>";});},staticInit:()=>{FS.ensureErrnoError();FS.nameTable=new Array(4096);FS.mount(MEMFS,{},"/");FS.createDefaultDirectories();FS.createDefaultDevices();FS.createSpecialDirectories();FS.filesystems={"MEMFS":MEMFS};},init:(input,output,error)=>{FS.init.initialized=true;FS.ensureErrnoError();Module["stdin"]=input||Module["stdin"];Module["stdout"]=output||Module["stdout"];Module["stderr"]=error||Module["stderr"];FS.createStandardStreams();},quit:()=>{FS.init.initialized=false;for(var i=0;i<FS.streams.length;i++){var stream=FS.streams[i];if(!stream){continue}FS.close(stream);}},getMode:(canRead,canWrite)=>{var mode=0;if(canRead)mode|=292|73;if(canWrite)mode|=146;return mode},findObject:(path,dontResolveLastLink)=>{var ret=FS.analyzePath(path,dontResolveLastLink);if(!ret.exists){return null}return ret.object},analyzePath:(path,dontResolveLastLink)=>{try{var lookup=FS.lookupPath(path,{follow:!dontResolveLastLink});path=lookup.path;}catch(e){}var ret={isRoot:false,exists:false,error:0,name:null,path:null,object:null,parentExists:false,parentPath:null,parentObject:null};try{var lookup=FS.lookupPath(path,{parent:true});ret.parentExists=true;ret.parentPath=lookup.path;ret.parentObject=lookup.node;ret.name=PATH.basename(path);lookup=FS.lookupPath(path,{follow:!dontResolveLastLink});ret.exists=true;ret.path=lookup.path;ret.object=lookup.node;ret.name=lookup.node.name;ret.isRoot=lookup.path==="/";}catch(e){ret.error=e.errno;}return ret},createPath:(parent,path,canRead,canWrite)=>{parent=typeof parent=="string"?parent:FS.getPath(parent);var parts=path.split("/").reverse();while(parts.length){var part=parts.pop();if(!part)continue;var current=PATH.join2(parent,part);try{FS.mkdir(current);}catch(e){}parent=current;}return current},createFile:(parent,name,properties,canRead,canWrite)=>{var path=PATH.join2(typeof parent=="string"?parent:FS.getPath(parent),name);var mode=FS.getMode(canRead,canWrite);return FS.create(path,mode)},createDataFile:(parent,name,data,canRead,canWrite,canOwn)=>{var path=name;if(parent){parent=typeof parent=="string"?parent:FS.getPath(parent);path=name?PATH.join2(parent,name):parent;}var mode=FS.getMode(canRead,canWrite);var node=FS.create(path,mode);if(data){if(typeof data=="string"){var arr=new Array(data.length);for(var i=0,len=data.length;i<len;++i)arr[i]=data.charCodeAt(i);data=arr;}FS.chmod(node,mode|146);var stream=FS.open(node,577);FS.write(stream,data,0,data.length,0,canOwn);FS.close(stream);FS.chmod(node,mode);}return node},createDevice:(parent,name,input,output)=>{var path=PATH.join2(typeof parent=="string"?parent:FS.getPath(parent),name);var mode=FS.getMode(!!input,!!output);if(!FS.createDevice.major)FS.createDevice.major=64;var dev=FS.makedev(FS.createDevice.major++,0);FS.registerDevice(dev,{open:stream=>{stream.seekable=false;},close:stream=>{if(output&&output.buffer&&output.buffer.length){output(10);}},read:(stream,buffer,offset,length,pos)=>{var bytesRead=0;for(var i=0;i<length;i++){var result;try{result=input();}catch(e){throw new FS.ErrnoError(29)}if(result===undefined&&bytesRead===0){throw new FS.ErrnoError(6)}if(result===null||result===undefined)break;bytesRead++;buffer[offset+i]=result;}if(bytesRead){stream.node.timestamp=Date.now();}return bytesRead},write:(stream,buffer,offset,length,pos)=>{for(var i=0;i<length;i++){try{output(buffer[offset+i]);}catch(e){throw new FS.ErrnoError(29)}}if(length){stream.node.timestamp=Date.now();}return i}});return FS.mkdev(path,mode,dev)},forceLoadFile:obj=>{if(obj.isDevice||obj.isFolder||obj.link||obj.contents)return true;if(typeof XMLHttpRequest!="undefined"){throw new Error("Lazy loading should have been performed (contents set) in createLazyFile, but it was not. Lazy loading only works in web workers. Use --embed-file or --preload-file in emcc on the main thread.")}else if(read_){try{obj.contents=intArrayFromString(read_(obj.url),true);obj.usedBytes=obj.contents.length;}catch(e){throw new FS.ErrnoError(29)}}else {throw new Error("Cannot load without read() or XMLHttpRequest.")}},createLazyFile:(parent,name,url,canRead,canWrite)=>{function LazyUint8Array(){this.lengthKnown=false;this.chunks=[];}LazyUint8Array.prototype.get=function LazyUint8Array_get(idx){if(idx>this.length-1||idx<0){return undefined}var chunkOffset=idx%this.chunkSize;var chunkNum=idx/this.chunkSize|0;return this.getter(chunkNum)[chunkOffset]};LazyUint8Array.prototype.setDataGetter=function LazyUint8Array_setDataGetter(getter){this.getter=getter;};LazyUint8Array.prototype.cacheLength=function LazyUint8Array_cacheLength(){var xhr=new XMLHttpRequest;xhr.open("HEAD",url,false);xhr.send(null);if(!(xhr.status>=200&&xhr.status<300||xhr.status===304))throw new Error("Couldn't load "+url+". Status: "+xhr.status);var datalength=Number(xhr.getResponseHeader("Content-length"));var header;var hasByteServing=(header=xhr.getResponseHeader("Accept-Ranges"))&&header==="bytes";var usesGzip=(header=xhr.getResponseHeader("Content-Encoding"))&&header==="gzip";var chunkSize=1024*1024;if(!hasByteServing)chunkSize=datalength;var doXHR=(from,to)=>{if(from>to)throw new Error("invalid range ("+from+", "+to+") or no bytes requested!");if(to>datalength-1)throw new Error("only "+datalength+" bytes available! programmer error!");var xhr=new XMLHttpRequest;xhr.open("GET",url,false);if(datalength!==chunkSize)xhr.setRequestHeader("Range","bytes="+from+"-"+to);xhr.responseType="arraybuffer";if(xhr.overrideMimeType){xhr.overrideMimeType("text/plain; charset=x-user-defined");}xhr.send(null);if(!(xhr.status>=200&&xhr.status<300||xhr.status===304))throw new Error("Couldn't load "+url+". Status: "+xhr.status);if(xhr.response!==undefined){return new Uint8Array(xhr.response||[])}return intArrayFromString(xhr.responseText||"",true)};var lazyArray=this;lazyArray.setDataGetter(chunkNum=>{var start=chunkNum*chunkSize;var end=(chunkNum+1)*chunkSize-1;end=Math.min(end,datalength-1);if(typeof lazyArray.chunks[chunkNum]=="undefined"){lazyArray.chunks[chunkNum]=doXHR(start,end);}if(typeof lazyArray.chunks[chunkNum]=="undefined")throw new Error("doXHR failed!");return lazyArray.chunks[chunkNum]});if(usesGzip||!datalength){chunkSize=datalength=1;datalength=this.getter(0).length;chunkSize=datalength;out("LazyFiles on gzip forces download of the whole file when length is accessed");}this._length=datalength;this._chunkSize=chunkSize;this.lengthKnown=true;};if(typeof XMLHttpRequest!="undefined"){if(!ENVIRONMENT_IS_WORKER)throw "Cannot do synchronous binary XHRs outside webworkers in modern browsers. Use --embed-file or --preload-file in emcc";var lazyArray=new LazyUint8Array;Object.defineProperties(lazyArray,{length:{get:function(){if(!this.lengthKnown){this.cacheLength();}return this._length}},chunkSize:{get:function(){if(!this.lengthKnown){this.cacheLength();}return this._chunkSize}}});var properties={isDevice:false,contents:lazyArray};}else {var properties={isDevice:false,url:url};}var node=FS.createFile(parent,name,properties,canRead,canWrite);if(properties.contents){node.contents=properties.contents;}else if(properties.url){node.contents=null;node.url=properties.url;}Object.defineProperties(node,{usedBytes:{get:function(){return this.contents.length}}});var stream_ops={};var keys=Object.keys(node.stream_ops);keys.forEach(key=>{var fn=node.stream_ops[key];stream_ops[key]=function forceLoadLazyFile(){FS.forceLoadFile(node);return fn.apply(null,arguments)};});function writeChunks(stream,buffer,offset,length,position){var contents=stream.node.contents;if(position>=contents.length)return 0;var size=Math.min(contents.length-position,length);if(contents.slice){for(var i=0;i<size;i++){buffer[offset+i]=contents[position+i];}}else {for(var i=0;i<size;i++){buffer[offset+i]=contents.get(position+i);}}return size}stream_ops.read=(stream,buffer,offset,length,position)=>{FS.forceLoadFile(node);return writeChunks(stream,buffer,offset,length,position)};stream_ops.mmap=(stream,length,position,prot,flags)=>{FS.forceLoadFile(node);var ptr=mmapAlloc();if(!ptr){throw new FS.ErrnoError(48)}writeChunks(stream,HEAP8,ptr,length,position);return {ptr:ptr,allocated:true}};node.stream_ops=stream_ops;return node},createPreloadedFile:(parent,name,url,canRead,canWrite,onload,onerror,dontCreateFile,canOwn,preFinish)=>{var fullname=name?PATH_FS.resolve(PATH.join2(parent,name)):parent;function processData(byteArray){function finish(byteArray){if(preFinish)preFinish();if(!dontCreateFile){FS.createDataFile(parent,name,byteArray,canRead,canWrite,canOwn);}if(onload)onload();removeRunDependency();}if(Browser.handledByPreloadPlugin(byteArray,fullname,finish,()=>{if(onerror)onerror();removeRunDependency();})){return}finish(byteArray);}addRunDependency();if(typeof url=="string"){asyncLoad(url,byteArray=>processData(byteArray),onerror);}else {processData(url);}},indexedDB:()=>{return window.indexedDB||window.mozIndexedDB||window.webkitIndexedDB||window.msIndexedDB},DB_NAME:()=>{return "EM_FS_"+window.location.pathname},DB_VERSION:20,DB_STORE_NAME:"FILE_DATA",saveFilesToDB:(paths,onload=(()=>{}),onerror=(()=>{}))=>{var indexedDB=FS.indexedDB();try{var openRequest=indexedDB.open(FS.DB_NAME(),FS.DB_VERSION);}catch(e){return onerror(e)}openRequest.onupgradeneeded=()=>{out("creating db");var db=openRequest.result;db.createObjectStore(FS.DB_STORE_NAME);};openRequest.onsuccess=()=>{var db=openRequest.result;var transaction=db.transaction([FS.DB_STORE_NAME],"readwrite");var files=transaction.objectStore(FS.DB_STORE_NAME);var ok=0,fail=0,total=paths.length;function finish(){if(fail==0)onload();else onerror();}paths.forEach(path=>{var putRequest=files.put(FS.analyzePath(path).object.contents,path);putRequest.onsuccess=()=>{ok++;if(ok+fail==total)finish();};putRequest.onerror=()=>{fail++;if(ok+fail==total)finish();};});transaction.onerror=onerror;};openRequest.onerror=onerror;},loadFilesFromDB:(paths,onload=(()=>{}),onerror=(()=>{}))=>{var indexedDB=FS.indexedDB();try{var openRequest=indexedDB.open(FS.DB_NAME(),FS.DB_VERSION);}catch(e){return onerror(e)}openRequest.onupgradeneeded=onerror;openRequest.onsuccess=()=>{var db=openRequest.result;try{var transaction=db.transaction([FS.DB_STORE_NAME],"readonly");}catch(e){onerror(e);return}var files=transaction.objectStore(FS.DB_STORE_NAME);var ok=0,fail=0,total=paths.length;function finish(){if(fail==0)onload();else onerror();}paths.forEach(path=>{var getRequest=files.get(path);getRequest.onsuccess=()=>{if(FS.analyzePath(path).exists){FS.unlink(path);}FS.createDataFile(PATH.dirname(path),PATH.basename(path),getRequest.result,true,true,true);ok++;if(ok+fail==total)finish();};getRequest.onerror=()=>{fail++;if(ok+fail==total)finish();};});transaction.onerror=onerror;};openRequest.onerror=onerror;}};var SYSCALLS={DEFAULT_POLLMASK:5,calculateAt:function(dirfd,path,allowEmpty){if(PATH.isAbs(path)){return path}var dir;if(dirfd===-100){dir=FS.cwd();}else {var dirstream=SYSCALLS.getStreamFromFD(dirfd);dir=dirstream.path;}if(path.length==0){if(!allowEmpty){throw new FS.ErrnoError(44)}return dir}return PATH.join2(dir,path)},doStat:function(func,path,buf){try{var stat=func(path);}catch(e){if(e&&e.node&&PATH.normalize(path)!==PATH.normalize(FS.getPath(e.node))){return -54}throw e}HEAP32[buf>>2]=stat.dev;HEAP32[buf+8>>2]=stat.ino;HEAP32[buf+12>>2]=stat.mode;HEAPU32[buf+16>>2]=stat.nlink;HEAP32[buf+20>>2]=stat.uid;HEAP32[buf+24>>2]=stat.gid;HEAP32[buf+28>>2]=stat.rdev;tempI64=[stat.size>>>0,(tempDouble=stat.size,+Math.abs(tempDouble)>=1?tempDouble>0?(Math.min(+Math.floor(tempDouble/4294967296),4294967295)|0)>>>0:~~+Math.ceil((tempDouble-+(~~tempDouble>>>0))/4294967296)>>>0:0)],HEAP32[buf+40>>2]=tempI64[0],HEAP32[buf+44>>2]=tempI64[1];HEAP32[buf+48>>2]=4096;HEAP32[buf+52>>2]=stat.blocks;var atime=stat.atime.getTime();var mtime=stat.mtime.getTime();var ctime=stat.ctime.getTime();tempI64=[Math.floor(atime/1e3)>>>0,(tempDouble=Math.floor(atime/1e3),+Math.abs(tempDouble)>=1?tempDouble>0?(Math.min(+Math.floor(tempDouble/4294967296),4294967295)|0)>>>0:~~+Math.ceil((tempDouble-+(~~tempDouble>>>0))/4294967296)>>>0:0)],HEAP32[buf+56>>2]=tempI64[0],HEAP32[buf+60>>2]=tempI64[1];HEAPU32[buf+64>>2]=atime%1e3*1e3;tempI64=[Math.floor(mtime/1e3)>>>0,(tempDouble=Math.floor(mtime/1e3),+Math.abs(tempDouble)>=1?tempDouble>0?(Math.min(+Math.floor(tempDouble/4294967296),4294967295)|0)>>>0:~~+Math.ceil((tempDouble-+(~~tempDouble>>>0))/4294967296)>>>0:0)],HEAP32[buf+72>>2]=tempI64[0],HEAP32[buf+76>>2]=tempI64[1];HEAPU32[buf+80>>2]=mtime%1e3*1e3;tempI64=[Math.floor(ctime/1e3)>>>0,(tempDouble=Math.floor(ctime/1e3),+Math.abs(tempDouble)>=1?tempDouble>0?(Math.min(+Math.floor(tempDouble/4294967296),4294967295)|0)>>>0:~~+Math.ceil((tempDouble-+(~~tempDouble>>>0))/4294967296)>>>0:0)],HEAP32[buf+88>>2]=tempI64[0],HEAP32[buf+92>>2]=tempI64[1];HEAPU32[buf+96>>2]=ctime%1e3*1e3;tempI64=[stat.ino>>>0,(tempDouble=stat.ino,+Math.abs(tempDouble)>=1?tempDouble>0?(Math.min(+Math.floor(tempDouble/4294967296),4294967295)|0)>>>0:~~+Math.ceil((tempDouble-+(~~tempDouble>>>0))/4294967296)>>>0:0)],HEAP32[buf+104>>2]=tempI64[0],HEAP32[buf+108>>2]=tempI64[1];return 0},doMsync:function(addr,stream,len,flags,offset){if(!FS.isFile(stream.node.mode)){throw new FS.ErrnoError(43)}if(flags&2){return 0}var buffer=HEAPU8.slice(addr,addr+len);FS.msync(stream,buffer,offset,len,flags);},varargs:undefined,get:function(){SYSCALLS.varargs+=4;var ret=HEAP32[SYSCALLS.varargs-4>>2];return ret},getStr:function(ptr){var ret=UTF8ToString(ptr);return ret},getStreamFromFD:function(fd){var stream=FS.getStream(fd);if(!stream)throw new FS.ErrnoError(8);return stream}};function _clock_time_get(clk_id,ignored_precision,ptime){if(!checkWasiClock(clk_id)){return 28}var now;if(clk_id===0){now=Date.now();}else {now=_emscripten_get_now();}var nsec=Math.round(now*1e3*1e3);HEAP32[ptime>>2]=nsec>>>0;HEAP32[ptime+4>>2]=nsec/Math.pow(2,32)>>>0;return 0}function _emscripten_notify_memory_growth(memoryIndex){updateMemoryViews();}var ENV={};function getExecutableName(){return thisProgram||"./this.program"}function getEnvStrings(){if(!getEnvStrings.strings){var lang=(typeof navigator=="object"&&navigator.languages&&navigator.languages[0]||"C").replace("-","_")+".UTF-8";var env={"USER":"web_user","LOGNAME":"web_user","PATH":"/","PWD":"/","HOME":"/home/web_user","LANG":lang,"_":getExecutableName()};for(var x in ENV){if(ENV[x]===undefined)delete env[x];else env[x]=ENV[x];}var strings=[];for(var x in env){strings.push(x+"="+env[x]);}getEnvStrings.strings=strings;}return getEnvStrings.strings}function writeAsciiToMemory(str,buffer,dontAddNull){for(var i=0;i<str.length;++i){HEAP8[buffer++>>0]=str.charCodeAt(i);}if(!dontAddNull)HEAP8[buffer>>0]=0;}function _environ_get(__environ,environ_buf){var bufSize=0;getEnvStrings().forEach(function(string,i){var ptr=environ_buf+bufSize;HEAPU32[__environ+i*4>>2]=ptr;writeAsciiToMemory(string,ptr);bufSize+=string.length+1;});return 0}function _environ_sizes_get(penviron_count,penviron_buf_size){var strings=getEnvStrings();HEAPU32[penviron_count>>2]=strings.length;var bufSize=0;strings.forEach(function(string){bufSize+=string.length+1;});HEAPU32[penviron_buf_size>>2]=bufSize;return 0}function _fd_close(fd){try{var stream=SYSCALLS.getStreamFromFD(fd);FS.close(stream);return 0}catch(e){if(typeof FS=="undefined"||!(e.name==="ErrnoError"))throw e;return e.errno}}function doReadv(stream,iov,iovcnt,offset){var ret=0;for(var i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2];var len=HEAPU32[iov+4>>2];iov+=8;var curr=FS.read(stream,HEAP8,ptr,len,offset);if(curr<0)return -1;ret+=curr;if(curr<len)break;if(typeof offset!=="undefined"){offset+=curr;}}return ret}function _fd_read(fd,iov,iovcnt,pnum){try{var stream=SYSCALLS.getStreamFromFD(fd);var num=doReadv(stream,iov,iovcnt);HEAPU32[pnum>>2]=num;return 0}catch(e){if(typeof FS=="undefined"||!(e.name==="ErrnoError"))throw e;return e.errno}}var MAX_INT53=9007199254740992;var MIN_INT53=-9007199254740992;function bigintToI53Checked(num){return num<MIN_INT53||num>MAX_INT53?NaN:Number(num)}function _fd_seek(fd,offset,whence,newOffset){try{offset=bigintToI53Checked(offset);if(isNaN(offset))return 61;var stream=SYSCALLS.getStreamFromFD(fd);FS.llseek(stream,offset,whence);tempI64=[stream.position>>>0,(tempDouble=stream.position,+Math.abs(tempDouble)>=1?tempDouble>0?(Math.min(+Math.floor(tempDouble/4294967296),4294967295)|0)>>>0:~~+Math.ceil((tempDouble-+(~~tempDouble>>>0))/4294967296)>>>0:0)],HEAP32[newOffset>>2]=tempI64[0],HEAP32[newOffset+4>>2]=tempI64[1];if(stream.getdents&&offset===0&&whence===0)stream.getdents=null;return 0}catch(e){if(typeof FS=="undefined"||!(e.name==="ErrnoError"))throw e;return e.errno}}function doWritev(stream,iov,iovcnt,offset){var ret=0;for(var i=0;i<iovcnt;i++){var ptr=HEAPU32[iov>>2];var len=HEAPU32[iov+4>>2];iov+=8;var curr=FS.write(stream,HEAP8,ptr,len,offset);if(curr<0)return -1;ret+=curr;if(typeof offset!=="undefined"){offset+=curr;}}return ret}function _fd_write(fd,iov,iovcnt,pnum){try{var stream=SYSCALLS.getStreamFromFD(fd);var num=doWritev(stream,iov,iovcnt);HEAPU32[pnum>>2]=num;return 0}catch(e){if(typeof FS=="undefined"||!(e.name==="ErrnoError"))throw e;return e.errno}}function _proc_exit(code){EXITSTATUS=code;if(!keepRuntimeAlive()){if(Module["onExit"])Module["onExit"](code);ABORT=true;}quit_(code,new ExitStatus(code));}function exitJS(status,implicit){EXITSTATUS=status;_proc_exit(status);}function handleException(e){if(e instanceof ExitStatus||e=="unwind"){return EXITSTATUS}quit_(1,e);}var FSNode=function(parent,name,mode,rdev){if(!parent){parent=this;}this.parent=parent;this.mount=parent.mount;this.mounted=null;this.id=FS.nextInode++;this.name=name;this.mode=mode;this.node_ops={};this.stream_ops={};this.rdev=rdev;};var readMode=292|73;var writeMode=146;Object.defineProperties(FSNode.prototype,{read:{get:function(){return (this.mode&readMode)===readMode},set:function(val){val?this.mode|=readMode:this.mode&=~readMode;}},write:{get:function(){return (this.mode&writeMode)===writeMode},set:function(val){val?this.mode|=writeMode:this.mode&=~writeMode;}},isFolder:{get:function(){return FS.isDir(this.mode)}},isDevice:{get:function(){return FS.isChrdev(this.mode)}}});FS.FSNode=FSNode;FS.staticInit();var wasmImports={"TVMWasmPackedCFunc":_TVMWasmPackedCFunc,"TVMWasmPackedCFuncFinalizer":_TVMWasmPackedCFuncFinalizer,"_ZN3tvm7runtime9threading10NumThreadsEv":__ZN3tvm7runtime9threading10NumThreadsEv,"_ZN3tvm7runtime9threading15ResetThreadPoolEv":__ZN3tvm7runtime9threading15ResetThreadPoolEv,"clock_time_get":_clock_time_get,"emscripten_notify_memory_growth":_emscripten_notify_memory_growth,"environ_get":_environ_get,"environ_sizes_get":_environ_sizes_get,"fd_close":_fd_close,"fd_read":_fd_read,"fd_seek":_fd_seek,"fd_write":_fd_write,"proc_exit":_proc_exit};createWasm();Module["__ZN3tvm7runtime17GetCustomTypeNameEh"]=function(){return (Module["__ZN3tvm7runtime17GetCustomTypeNameEh"]=Module["asm"]["_ZN3tvm7runtime17GetCustomTypeNameEh"]).apply(null,arguments)};Module["__ZN3tvm7runtime8Registry3GetERKNS0_6StringE"]=function(){return (Module["__ZN3tvm7runtime8Registry3GetERKNS0_6StringE"]=Module["asm"]["_ZN3tvm7runtime8Registry3GetERKNS0_6StringE"]).apply(null,arguments)};Module["__ZN3tvm7runtime23GetCustomTypeRegisteredEh"]=function(){return (Module["__ZN3tvm7runtime23GetCustomTypeRegisteredEh"]=Module["asm"]["_ZN3tvm7runtime23GetCustomTypeRegisteredEh"]).apply(null,arguments)};Module["__ZN3tvm7runtime19ParseCustomDatatypeERKNSt3__212basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPKc"]=function(){return (Module["__ZN3tvm7runtime19ParseCustomDatatypeERKNSt3__212basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPKc"]=Module["asm"]["_ZN3tvm7runtime19ParseCustomDatatypeERKNSt3__212basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPKc"]).apply(null,arguments)};Module["_TVMGetLastError"]=function(){return (Module["_TVMGetLastError"]=Module["asm"]["TVMGetLastError"]).apply(null,arguments)};Module["_TVMAPISetLastError"]=function(){return (Module["_TVMAPISetLastError"]=Module["asm"]["TVMAPISetLastError"]).apply(null,arguments)};Module["_TVMModLoadFromFile"]=function(){return (Module["_TVMModLoadFromFile"]=Module["asm"]["TVMModLoadFromFile"]).apply(null,arguments)};Module["__ZN3tvm7runtime6Module12LoadFromFileERKNS0_6StringES4_"]=function(){return (Module["__ZN3tvm7runtime6Module12LoadFromFileERKNS0_6StringES4_"]=Module["asm"]["_ZN3tvm7runtime6Module12LoadFromFileERKNS0_6StringES4_"]).apply(null,arguments)};Module["_TVMModImport"]=function(){return (Module["_TVMModImport"]=Module["asm"]["TVMModImport"]).apply(null,arguments)};Module["_TVMModGetFunction"]=function(){return (Module["_TVMModGetFunction"]=Module["asm"]["TVMModGetFunction"]).apply(null,arguments)};Module["_TVMModFree"]=function(){return (Module["_TVMModFree"]=Module["asm"]["TVMModFree"]).apply(null,arguments)};Module["_TVMObjectFree"]=function(){return (Module["_TVMObjectFree"]=Module["asm"]["TVMObjectFree"]).apply(null,arguments)};Module["_TVMBackendGetFuncFromEnv"]=function(){return (Module["_TVMBackendGetFuncFromEnv"]=Module["asm"]["TVMBackendGetFuncFromEnv"]).apply(null,arguments)};Module["_TVMBackendAllocWorkspace"]=function(){return (Module["_TVMBackendAllocWorkspace"]=Module["asm"]["TVMBackendAllocWorkspace"]).apply(null,arguments)};Module["_TVMBackendFreeWorkspace"]=function(){return (Module["_TVMBackendFreeWorkspace"]=Module["asm"]["TVMBackendFreeWorkspace"]).apply(null,arguments)};Module["_TVMBackendRunOnce"]=function(){return (Module["_TVMBackendRunOnce"]=Module["asm"]["TVMBackendRunOnce"]).apply(null,arguments)};Module["_TVMFuncFree"]=function(){return (Module["_TVMFuncFree"]=Module["asm"]["TVMFuncFree"]).apply(null,arguments)};Module["_TVMByteArrayFree"]=function(){return (Module["_TVMByteArrayFree"]=Module["asm"]["TVMByteArrayFree"]).apply(null,arguments)};Module["_TVMFuncCall"]=function(){return (Module["_TVMFuncCall"]=Module["asm"]["TVMFuncCall"]).apply(null,arguments)};Module["_TVMCFuncSetReturn"]=function(){return (Module["_TVMCFuncSetReturn"]=Module["asm"]["TVMCFuncSetReturn"]).apply(null,arguments)};Module["_TVMFuncCreateFromCFunc"]=function(){return (Module["_TVMFuncCreateFromCFunc"]=Module["asm"]["TVMFuncCreateFromCFunc"]).apply(null,arguments)};Module["_TVMStreamCreate"]=function(){return (Module["_TVMStreamCreate"]=Module["asm"]["TVMStreamCreate"]).apply(null,arguments)};Module["_TVMStreamFree"]=function(){return (Module["_TVMStreamFree"]=Module["asm"]["TVMStreamFree"]).apply(null,arguments)};Module["_TVMSetStream"]=function(){return (Module["_TVMSetStream"]=Module["asm"]["TVMSetStream"]).apply(null,arguments)};Module["_TVMSynchronize"]=function(){return (Module["_TVMSynchronize"]=Module["asm"]["TVMSynchronize"]).apply(null,arguments)};Module["_TVMStreamStreamSynchronize"]=function(){return (Module["_TVMStreamStreamSynchronize"]=Module["asm"]["TVMStreamStreamSynchronize"]).apply(null,arguments)};Module["_TVMCbArgToReturn"]=function(){return (Module["_TVMCbArgToReturn"]=Module["asm"]["TVMCbArgToReturn"]).apply(null,arguments)};Module["_TVMDeviceAllocDataSpace"]=function(){return (Module["_TVMDeviceAllocDataSpace"]=Module["asm"]["TVMDeviceAllocDataSpace"]).apply(null,arguments)};Module["_TVMDeviceAllocDataSpaceWithScope"]=function(){return (Module["_TVMDeviceAllocDataSpaceWithScope"]=Module["asm"]["TVMDeviceAllocDataSpaceWithScope"]).apply(null,arguments)};Module["_TVMDeviceFreeDataSpace"]=function(){return (Module["_TVMDeviceFreeDataSpace"]=Module["asm"]["TVMDeviceFreeDataSpace"]).apply(null,arguments)};Module["_TVMDeviceCopyDataFromTo"]=function(){return (Module["_TVMDeviceCopyDataFromTo"]=Module["asm"]["TVMDeviceCopyDataFromTo"]).apply(null,arguments)};Module["__ZN3tvm7runtime8Registry8RegisterERKNS0_6StringEb"]=function(){return (Module["__ZN3tvm7runtime8Registry8RegisterERKNS0_6StringEb"]=Module["asm"]["_ZN3tvm7runtime8Registry8RegisterERKNS0_6StringEb"]).apply(null,arguments)};Module["_TVMBackendParallelLaunch"]=function(){return (Module["_TVMBackendParallelLaunch"]=Module["asm"]["TVMBackendParallelLaunch"]).apply(null,arguments)};Module["_TVMBackendParallelBarrier"]=function(){return (Module["_TVMBackendParallelBarrier"]=Module["asm"]["TVMBackendParallelBarrier"]).apply(null,arguments)};Module["__ZN3tvm7runtime8Registry9ListNamesEv"]=function(){return (Module["__ZN3tvm7runtime8Registry9ListNamesEv"]=Module["asm"]["_ZN3tvm7runtime8Registry9ListNamesEv"]).apply(null,arguments)};Module["__ZN3tvm7runtime9BacktraceEv"]=function(){return (Module["__ZN3tvm7runtime9BacktraceEv"]=Module["asm"]["_ZN3tvm7runtime9BacktraceEv"]).apply(null,arguments)};Module["__ZN3tvm7runtime14RuntimeEnabledERKNS0_6StringE"]=function(){return (Module["__ZN3tvm7runtime14RuntimeEnabledERKNS0_6StringE"]=Module["asm"]["_ZN3tvm7runtime14RuntimeEnabledERKNS0_6StringE"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray10CreateViewENS0_10ShapeTupleE10DLDataType"]=function(){return (Module["__ZN3tvm7runtime7NDArray10CreateViewENS0_10ShapeTupleE10DLDataType"]=Module["asm"]["_ZN3tvm7runtime7NDArray10CreateViewENS0_10ShapeTupleE10DLDataType"]).apply(null,arguments)};Module["__ZNK3tvm7runtime7NDArray8ToDLPackEv"]=function(){return (Module["__ZNK3tvm7runtime7NDArray8ToDLPackEv"]=Module["asm"]["_ZNK3tvm7runtime7NDArray8ToDLPackEv"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray5EmptyENS0_10ShapeTupleE10DLDataType8DLDeviceNS0_8OptionalINS0_6StringEEE"]=function(){return (Module["__ZN3tvm7runtime7NDArray5EmptyENS0_10ShapeTupleE10DLDataType8DLDeviceNS0_8OptionalINS0_6StringEEE"]=Module["asm"]["_ZN3tvm7runtime7NDArray5EmptyENS0_10ShapeTupleE10DLDataType8DLDeviceNS0_8OptionalINS0_6StringEEE"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray20FromExternalDLTensorERK8DLTensor"]=function(){return (Module["__ZN3tvm7runtime7NDArray20FromExternalDLTensorERK8DLTensor"]=Module["asm"]["_ZN3tvm7runtime7NDArray20FromExternalDLTensorERK8DLTensor"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray9IsAlignedERK8DLTensor"]=function(){return (Module["__ZN3tvm7runtime7NDArray9IsAlignedERK8DLTensor"]=Module["asm"]["_ZN3tvm7runtime7NDArray9IsAlignedERK8DLTensor"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray15NewFromDLTensorEP8DLTensorRK8DLDevice"]=function(){return (Module["__ZN3tvm7runtime7NDArray15NewFromDLTensorEP8DLTensorRK8DLDevice"]=Module["asm"]["_ZN3tvm7runtime7NDArray15NewFromDLTensorEP8DLTensorRK8DLDevice"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray10FromDLPackEP15DLManagedTensor"]=function(){return (Module["__ZN3tvm7runtime7NDArray10FromDLPackEP15DLManagedTensor"]=Module["asm"]["_ZN3tvm7runtime7NDArray10FromDLPackEP15DLManagedTensor"]).apply(null,arguments)};Module["__ZNK3tvm7runtime7NDArray11CopyToBytesEPvm"]=function(){return (Module["__ZNK3tvm7runtime7NDArray11CopyToBytesEPvm"]=Module["asm"]["_ZNK3tvm7runtime7NDArray11CopyToBytesEPvm"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray13CopyFromBytesEPKvm"]=function(){return (Module["__ZN3tvm7runtime7NDArray13CopyFromBytesEPKvm"]=Module["asm"]["_ZN3tvm7runtime7NDArray13CopyFromBytesEPKvm"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray10CopyFromToEPK8DLTensorPS2_Pv"]=function(){return (Module["__ZN3tvm7runtime7NDArray10CopyFromToEPK8DLTensorPS2_Pv"]=Module["asm"]["_ZN3tvm7runtime7NDArray10CopyFromToEPK8DLTensorPS2_Pv"]).apply(null,arguments)};Module["__ZNK3tvm7runtime7NDArray5ShapeEv"]=function(){return (Module["__ZNK3tvm7runtime7NDArray5ShapeEv"]=Module["asm"]["_ZNK3tvm7runtime7NDArray5ShapeEv"]).apply(null,arguments)};Module["__ZNK3tvm7runtime7NDArray8DataTypeEv"]=function(){return (Module["__ZNK3tvm7runtime7NDArray8DataTypeEv"]=Module["asm"]["_ZNK3tvm7runtime7NDArray8DataTypeEv"]).apply(null,arguments)};Module["__ZN3tvm7runtime7NDArray28AbilityOfZeroCopyForDLTensorEP8DLTensorRK8DLDevice"]=function(){return (Module["__ZN3tvm7runtime7NDArray28AbilityOfZeroCopyForDLTensorEP8DLTensorRK8DLDevice"]=Module["asm"]["_ZN3tvm7runtime7NDArray28AbilityOfZeroCopyForDLTensorEP8DLTensorRK8DLDevice"]).apply(null,arguments)};Module["_TVMArrayGetTypeIndex"]=function(){return (Module["_TVMArrayGetTypeIndex"]=Module["asm"]["TVMArrayGetTypeIndex"]).apply(null,arguments)};Module["_TVMArrayAlloc"]=function(){return (Module["_TVMArrayAlloc"]=Module["asm"]["TVMArrayAlloc"]).apply(null,arguments)};Module["_TVMArrayFree"]=function(){return (Module["_TVMArrayFree"]=Module["asm"]["TVMArrayFree"]).apply(null,arguments)};Module["_TVMArrayCopyFromTo"]=function(){return (Module["_TVMArrayCopyFromTo"]=Module["asm"]["TVMArrayCopyFromTo"]).apply(null,arguments)};Module["_TVMArrayFromDLPack"]=function(){return (Module["_TVMArrayFromDLPack"]=Module["asm"]["TVMArrayFromDLPack"]).apply(null,arguments)};Module["_TVMArrayToDLPack"]=function(){return (Module["_TVMArrayToDLPack"]=Module["asm"]["TVMArrayToDLPack"]).apply(null,arguments)};Module["_TVMDLManagedTensorCallDeleter"]=function(){return (Module["_TVMDLManagedTensorCallDeleter"]=Module["asm"]["TVMDLManagedTensorCallDeleter"]).apply(null,arguments)};Module["_TVMArrayCopyFromBytes"]=function(){return (Module["_TVMArrayCopyFromBytes"]=Module["asm"]["TVMArrayCopyFromBytes"]).apply(null,arguments)};Module["_TVMArrayCopyToBytes"]=function(){return (Module["_TVMArrayCopyToBytes"]=Module["asm"]["TVMArrayCopyToBytes"]).apply(null,arguments)};Module["_TVMObjectGetTypeIndex"]=function(){return (Module["_TVMObjectGetTypeIndex"]=Module["asm"]["TVMObjectGetTypeIndex"]).apply(null,arguments)};Module["_TVMObjectRetain"]=function(){return (Module["_TVMObjectRetain"]=Module["asm"]["TVMObjectRetain"]).apply(null,arguments)};Module["_TVMObjectDerivedFrom"]=function(){return (Module["_TVMObjectDerivedFrom"]=Module["asm"]["TVMObjectDerivedFrom"]).apply(null,arguments)};Module["_TVMObjectTypeKey2Index"]=function(){return (Module["_TVMObjectTypeKey2Index"]=Module["asm"]["TVMObjectTypeKey2Index"]).apply(null,arguments)};Module["_TVMObjectTypeIndex2Key"]=function(){return (Module["_TVMObjectTypeIndex2Key"]=Module["asm"]["TVMObjectTypeIndex2Key"]).apply(null,arguments)};Module["__ZN3tvm7runtime5Timer5StartE8DLDevice"]=function(){return (Module["__ZN3tvm7runtime5Timer5StartE8DLDevice"]=Module["asm"]["_ZN3tvm7runtime5Timer5StartE8DLDevice"]).apply(null,arguments)};Module["__ZN3tvm7runtime8Registry8set_bodyENS0_10PackedFuncE"]=function(){return (Module["__ZN3tvm7runtime8Registry8set_bodyENS0_10PackedFuncE"]=Module["asm"]["_ZN3tvm7runtime8Registry8set_bodyENS0_10PackedFuncE"]).apply(null,arguments)};Module["__ZN3tvm7runtime8Registry6RemoveERKNS0_6StringE"]=function(){return (Module["__ZN3tvm7runtime8Registry6RemoveERKNS0_6StringE"]=Module["asm"]["_ZN3tvm7runtime8Registry6RemoveERKNS0_6StringE"]).apply(null,arguments)};Module["__ZN3tvm7runtime15EnvCheckSignalsEv"]=function(){return (Module["__ZN3tvm7runtime15EnvCheckSignalsEv"]=Module["asm"]["_ZN3tvm7runtime15EnvCheckSignalsEv"]).apply(null,arguments)};Module["_TVMFuncRegisterGlobal"]=function(){return (Module["_TVMFuncRegisterGlobal"]=Module["asm"]["TVMFuncRegisterGlobal"]).apply(null,arguments)};Module["_TVMFuncGetGlobal"]=function(){return (Module["_TVMFuncGetGlobal"]=Module["asm"]["TVMFuncGetGlobal"]).apply(null,arguments)};Module["_TVMFuncListGlobalNames"]=function(){return (Module["_TVMFuncListGlobalNames"]=Module["asm"]["TVMFuncListGlobalNames"]).apply(null,arguments)};Module["_TVMFuncRemoveGlobal"]=function(){return (Module["_TVMFuncRemoveGlobal"]=Module["asm"]["TVMFuncRemoveGlobal"]).apply(null,arguments)};Module["_TVMBackendRegisterEnvCAPI"]=function(){return (Module["_TVMBackendRegisterEnvCAPI"]=Module["asm"]["TVMBackendRegisterEnvCAPI"]).apply(null,arguments)};Module["_TVMBackendRegisterSystemLibSymbol"]=function(){return (Module["_TVMBackendRegisterSystemLibSymbol"]=Module["asm"]["TVMBackendRegisterSystemLibSymbol"]).apply(null,arguments)};Module["_TVMBackendAnyListSetPackedArg"]=function(){return (Module["_TVMBackendAnyListSetPackedArg"]=Module["asm"]["TVMBackendAnyListSetPackedArg"]).apply(null,arguments)};Module["_TVMBackendAnyListResetItem"]=function(){return (Module["_TVMBackendAnyListResetItem"]=Module["asm"]["TVMBackendAnyListResetItem"]).apply(null,arguments)};Module["_TVMBackendAnyListMoveFromPackedReturn"]=function(){return (Module["_TVMBackendAnyListMoveFromPackedReturn"]=Module["asm"]["TVMBackendAnyListMoveFromPackedReturn"]).apply(null,arguments)};Module["__ZN3tvm7runtime6detail12LogFatalImplERKNSt3__212basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiSA_"]=function(){return (Module["__ZN3tvm7runtime6detail12LogFatalImplERKNSt3__212basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiSA_"]=Module["asm"]["_ZN3tvm7runtime6detail12LogFatalImplERKNSt3__212basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiSA_"]).apply(null,arguments)};Module["__ZN3tvm7runtime6detail14LogMessageImplERKNSt3__212basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiiSA_"]=function(){return (Module["__ZN3tvm7runtime6detail14LogMessageImplERKNSt3__212basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiiSA_"]=Module["asm"]["_ZN3tvm7runtime6detail14LogMessageImplERKNSt3__212basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEiiSA_"]).apply(null,arguments)};Module["_TVMWasmAllocSpace"]=function(){return (Module["_TVMWasmAllocSpace"]=Module["asm"]["TVMWasmAllocSpace"]).apply(null,arguments)};Module["_TVMWasmFreeSpace"]=function(){return (Module["_TVMWasmFreeSpace"]=Module["asm"]["TVMWasmFreeSpace"]).apply(null,arguments)};Module["_TVMWasmFuncCreateFromCFunc"]=function(){return (Module["_TVMWasmFuncCreateFromCFunc"]=Module["asm"]["TVMWasmFuncCreateFromCFunc"]).apply(null,arguments)};var __initialize=Module["__initialize"]=function(){return (__initialize=Module["__initialize"]=Module["asm"]["_initialize"]).apply(null,arguments)};var calledRun;dependenciesFulfilled=function runCaller(){if(!calledRun)run();if(!calledRun)dependenciesFulfilled=runCaller;};function callMain(args=[]){var entryFunction=__initialize;try{entryFunction();var ret=0;exitJS(ret,true);return ret}catch(e){return handleException(e)}}function run(args=arguments_){if(runDependencies>0){return}preRun();if(runDependencies>0){return}function doRun(){if(calledRun)return;calledRun=true;Module["calledRun"]=true;if(ABORT)return;initRuntime();preMain();if(Module["onRuntimeInitialized"])Module["onRuntimeInitialized"]();if(shouldRunNow)callMain(args);postRun();}if(Module["setStatus"]){Module["setStatus"]("Running...");setTimeout(function(){setTimeout(function(){Module["setStatus"]("");},1);doRun();},1);}else {doRun();}}if(Module["preInit"]){if(typeof Module["preInit"]=="function")Module["preInit"]=[Module["preInit"]];while(Module["preInit"].length>0){Module["preInit"].pop()();}}var shouldRunNow=true;if(Module["noInitialRun"])shouldRunNow=false;run();

        this.Module = Module;
        this.start = Module.wasmLibraryProvider.start;
        this.imports = Module.wasmLibraryProvider.imports;
        this.wasiImport = this.imports["wasi_snapshot_preview1"];
    }

    /**
     * Get performance measurement.
     */
    function getPerformance() {
        if (typeof performance == "undefined") {
            // eslint-disable-next-line @typescript-eslint/no-var-requires
            const performanceNode = require("perf_hooks");
            return performanceNode.performance;
        }
        else {
            return performance;
        }
    }
    /**
     * Create a new websocket for a given URL
     * @param url The url.
     */
    function createWebSocket(url) {
        if (typeof WebSocket == "undefined") {
            // eslint-disable-next-line @typescript-eslint/no-var-requires
            const WebSocket = require("ws");
            return new WebSocket(url);
        }
        else {
            return new WebSocket(url);
        }
    }
    /**
     * Create a WASI based on current environment.
     *
     * @return A wasi that can run on broswer or local.
     */
    function createPolyfillWASI() {
        return new EmccWASI();
    }

    /*
     * Licensed to the Apache Software Foundation (ASF) under one
     * or more contributor license agreements.  See the NOTICE file
     * distributed with this work for additional information
     * regarding copyright ownership.  The ASF licenses this file
     * to you under the Apache License, Version 2.0 (the
     * "License"); you may not use this file except in compliance
     * with the License.  You may obtain a copy of the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing,
     * software distributed under the License is distributed on an
     * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
     * KIND, either express or implied.  See the License for the
     * specific language governing permissions and limitations
     * under the License.
     */
    /**
     * @internal
     * FFI Library wrapper, maintains most runtime states.
     */
    class FFILibrary {
        constructor(wasmInstance, imports) {
            this.recycledCallStacks = [];
            this.wasmInstance = wasmInstance;
            this.memory = new Memory(this.detectWasmMemory(this.wasmInstance, imports));
            assert(this.wasmInstance.exports !== undefined, "Expect the library module contains exports");
            this.exports = this.wasmInstance.exports;
            this.wasm32 = this.memory.wasm32;
            this.validateInstance();
        }
        dispose() {
            var _a;
            while (this.recycledCallStacks.length != 0) {
                this.recycledCallStacks.pop().dispose();
            }
            (_a = this.webGPUContext) === null || _a === void 0 ? void 0 : _a.dispose();
        }
        sizeofPtr() {
            return this.memory.sizeofPtr();
        }
        checkCall(code) {
            if (code != 0) {
                const msgPtr = this.exports
                    .TVMGetLastError();
                throw new Error("TVMError: " + this.memory.loadCString(msgPtr));
            }
        }
        getOrAllocCallStack() {
            if (this.recycledCallStacks.length != 0) {
                return this.recycledCallStacks.pop();
            }
            return new CachedCallStack(this.memory, this.exports.TVMWasmAllocSpace, this.exports.TVMWasmFreeSpace);
        }
        recycleCallStack(callstack) {
            callstack.reset();
            this.recycledCallStacks.push(callstack);
        }
        validateInstance() {
            this.checkExports(["TVMWasmAllocSpace", "TVMWasmFreeSpace", "TVMFuncFree"]);
        }
        checkExports(funcNames) {
            const missList = [];
            for (const name of funcNames) {
                const f = this.exports[name];
                if (!(f instanceof Function)) {
                    missList.push(name);
                }
            }
            if (missList.length != 0) {
                throw new Error("Cannot find " + missList + " in exports");
            }
        }
        detectWasmMemory(instance, imports) {
            if (instance.exports.memory instanceof WebAssembly.Memory) {
                return instance.exports.memory;
            }
            if (imports.env && imports.env.memory instanceof WebAssembly.Memory) {
                return imports.env.memory;
            }
            throw new Error("Cannt detect wasm memory from imports " +
                imports +
                " or exports" +
                instance.exports);
        }
    }
    /**
     * @internal
     * Manages extra runtime context for the runtime.
     */
    class RuntimeContext {
        constructor(getGlobalFunc) {
            this.autoDisposeScope = [];
            this.arrayGetItem = getGlobalFunc("runtime.ArrayGetItem");
            this.arrayGetSize = getGlobalFunc("runtime.ArraySize");
            this.arrayMake = getGlobalFunc("runtime.Array");
            this.stringMake = getGlobalFunc("runtime.String");
            this.getFFIString = getGlobalFunc("runtime.GetFFIString");
            this.getSysLib = getGlobalFunc("runtime.SystemLib");
            this.arrayCacheGet = getGlobalFunc("vm.builtin.ndarray_cache.get");
            this.arrayCacheRemove = getGlobalFunc("vm.builtin.ndarray_cache.remove");
            this.arrayCacheUpdate = getGlobalFunc("vm.builtin.ndarray_cache.update");
            this.arrayCacheClear = getGlobalFunc("vm.builtin.ndarray_cache.clear");
            this.arrayDecodeStorage = getGlobalFunc("tvmjs.array.decode_storage");
            this.paramModuleFromCache = getGlobalFunc("vm.builtin.param_module_from_cache");
            this.makeShapeTuple = getGlobalFunc("runtime.ShapeTuple");
            this.ndarrayCreateView = getGlobalFunc("runtime.TVMArrayCreateView");
            this.sampleTopPFromLogits = getGlobalFunc("vm.builtin.sample_top_p_from_logits");
            this.applyRepetitionPenalty = getGlobalFunc("vm.builtin.apply_repetition_penalty");
            this.applySoftmaxWithTemperature = getGlobalFunc("vm.builtin.apply_softmax_with_temperature");
        }
        dispose() {
            // call array cache clear to clear all cached items
            this.arrayCacheClear.dispose();
            this.arrayGetItem.dispose();
            this.arrayGetSize.dispose();
            this.arrayMake.dispose();
            this.stringMake.dispose();
            this.getFFIString.dispose();
            this.arrayCacheGet.dispose();
            this.arrayCacheRemove.dispose();
            this.arrayCacheUpdate.dispose();
            this.arrayCacheClear.dispose();
            this.arrayDecodeStorage.dispose();
            this.paramModuleFromCache.dispose();
            this.makeShapeTuple.dispose();
            this.ndarrayCreateView.dispose();
            this.sampleTopPFromLogits.dispose();
            this.applyRepetitionPenalty.dispose();
            this.applySoftmaxWithTemperature.dispose();
        }
        beginScope() {
            this.autoDisposeScope.push([]);
        }
        endScope() {
            if (this.autoDisposeScope.length == 0) {
                throw Error("tvm.endScope called when the stack is empty.");
            }
            // automatically dispose all the tracked values in the current scope.
            const currScope = this.autoDisposeScope.pop();
            for (let i = 0; i < currScope.length; ++i) {
                const val = currScope[i];
                if (val !== undefined) {
                    val.dispose();
                }
            }
        }
        /**
         * Track object for dispose in current scope.
         *
         * @param obj The object to be tracked.
         * @returns the same object.
         * @note This function only needs to be called for raw system C API values.
         *       The return value of PackedFunc will be automatically tracked.
         */
        attachToCurrentScope(obj) {
            if (this.autoDisposeScope.length == 0) {
                throw Error("Must call beginScope to use functions that returns TVM objects");
            }
            const currScope = this.autoDisposeScope[this.autoDisposeScope.length - 1];
            currScope.push(obj);
            return obj;
        }
        moveToParentScope(obj) {
            this.detachFromCurrentScope(obj);
            if (this.autoDisposeScope.length < 2) {
                throw Error("moveToParentScope: Parent scope do not exist");
            }
            const parentScope = this.autoDisposeScope[this.autoDisposeScope.length - 2];
            parentScope.push(obj);
            return obj;
        }
        detachFromCurrentScope(obj) {
            const currScope = this.autoDisposeScope[this.autoDisposeScope.length - 1];
            let occurance = 0;
            for (let i = 0; i < currScope.length; ++i) {
                if (currScope[i] === obj) {
                    occurance += 1;
                    currScope[i] = undefined;
                }
            }
            if (occurance == 0) {
                throw Error("Cannot find obj in the current auto conversion pool");
            }
            if (occurance > 1) {
                throw Error("Value attached to scope multiple times");
            }
            return obj;
        }
    }
    /**
     * A typed scalar constant used to represent a typed number
     * argument to PackedFunc calls.
     */
    class Scalar {
        constructor(value, dtype) {
            this.value = value;
            this.dtype = dtype;
        }
    }
    /**
     * Cell holds the PackedFunc object.
     */
    class PackedFuncCell {
        constructor(handle, lib) {
            this.handle = handle;
            this.lib = lib;
        }
        dispose() {
            if (this.handle != 0) {
                this.lib.checkCall(this.lib.exports.TVMFuncFree(this.handle));
                this.handle = 0;
            }
        }
        getHandle(requireNotNull = true) {
            if (requireNotNull && this.handle == 0) {
                throw Error("PackedFunc has already been disposed");
            }
            return this.handle;
        }
    }
    const DeviceEnumToStr = {
        1: "cpu",
        2: "cuda",
        4: "opencl",
        8: "metal",
        15: "webgpu"
    };
    const DeviceStrToEnum = {
        cpu: 1,
        cuda: 2,
        cl: 4,
        opencl: 4,
        vulkan: 7,
        metal: 8,
        webgpu: 15
    };
    /**
     * Represent a runtime context where a NDArray can reside.
     */
    class DLDevice {
        constructor(deviceType, deviceId, lib) {
            const tp = typeof deviceType;
            if (tp == "string") {
                this.deviceType = DeviceStrToEnum[deviceType];
                if (this.deviceType == undefined) {
                    throw new Error("Cannot recogonize deviceType " + deviceType);
                }
            }
            else if (tp == "number") {
                this.deviceType = deviceType;
            }
            else {
                throw new Error("Cannot take type " + tp + " as deviceType");
            }
            this.deviceId = deviceId;
            this.lib = lib;
        }
        /**
         * Synchronize the device
         */
        sync() {
            return __awaiter(this, void 0, void 0, function* () {
                if (this.deviceType == DeviceStrToEnum.webgpu) {
                    assert(this.lib.webGPUContext !== undefined);
                    yield this.lib.webGPUContext.sync();
                }
            });
        }
        toString() {
            return (DeviceEnumToStr[this.deviceType] + "(" + this.deviceId.toString() + ")");
        }
    }
    const DLDataTypeCodeToStr = {
        0: "int",
        1: "uint",
        2: "float",
        3: "handle",
    };
    /**
     * Runtime data type of NDArray.
     */
    class DLDataType {
        constructor(code, bits, lanes) {
            this.code = code;
            this.bits = bits;
            this.lanes = lanes;
        }
        toString() {
            const ret = DLDataTypeCodeToStr[this.code] + this.bits.toString();
            if (this.lanes != 1) {
                return ret + "x" + this.lanes.toString();
            }
            else {
                return ret;
            }
        }
        numStorageBytes() {
            return (this.bits * this.lanes + 7) >> 3;
        }
    }
    /**
     * n-dimnesional array.
     */
    class NDArray {
        constructor(handle, isView, lib, ctx) {
            this.handle = handle;
            this.isView = isView;
            this.lib = lib;
            this.ctx = ctx;
            if (this.isView) {
                this.dltensor = handle;
            }
            else {
                this.dltensor = this.getDLTensorFromArrayHandle(this.handle);
            }
            // constant offsets.
            const arrayOffsetData = 0;
            const arrayOffsetContext = arrayOffsetData + this.lib.sizeofPtr();
            const arrayOffsetDevType = arrayOffsetContext;
            const arrayOffsetDevId = arrayOffsetContext + 4 /* SizeOf.I32 */;
            const arrayOffsetNdim = arrayOffsetContext + 8 /* SizeOf.DLDevice */;
            const arrayOffsetDtype = arrayOffsetNdim + 4 /* SizeOf.I32 */;
            const arrayOffsetDtypeCode = arrayOffsetDtype;
            const arrayOffsetDtypeBits = arrayOffsetDtype + 1 /* SizeOf.U8 */;
            const arrayOffsetDtypeLanes = arrayOffsetDtypeBits + 1 /* SizeOf.U8 */;
            const arrayOffsetShape = arrayOffsetDtype + 4 /* SizeOf.DLDataType */;
            const arrayOffsetStrides = arrayOffsetShape + this.lib.sizeofPtr();
            const arrayOffsetByteOffset = arrayOffsetStrides + this.lib.sizeofPtr();
            // dataPtr
            this.dataPtr = lib.memory.loadPointer(this.dltensor);
            // ndim
            this.ndim = lib.memory.loadI32(this.dltensor + arrayOffsetNdim);
            // shape
            const cshapePtr = lib.memory.loadPointer(this.dltensor + arrayOffsetShape);
            this.shape = [];
            for (let i = 0; i < this.ndim; ++i) {
                this.shape.push(lib.memory.loadI64(cshapePtr + i * 8 /* SizeOf.I64 */));
            }
            // dtype
            const code = lib.memory.loadU8(this.dltensor + arrayOffsetDtypeCode);
            const bits = lib.memory.loadU8(this.dltensor + arrayOffsetDtypeBits);
            const lanes = lib.memory.loadU16(this.dltensor + arrayOffsetDtypeLanes);
            this.dlDataType = new DLDataType(code, bits, lanes);
            this.dtype = this.dlDataType.toString();
            // device
            const deviceType = lib.memory.loadI32(this.dltensor + arrayOffsetDevType);
            const deviceId = lib.memory.loadI32(this.dltensor + arrayOffsetDevId);
            this.device = new DLDevice(deviceType, deviceId, lib);
            // byte_offset
            this.byteOffset = lib.memory.loadI64(this.dltensor + arrayOffsetByteOffset);
        }
        /**
         * Create a view of the array.
         * @param shape The shape of the view.
         * @returns The new sliced ndarray.
         */
        view(shape) {
            const shapeArray = shape.map((value) => new Scalar(value, "int"));
            return this.ctx.ndarrayCreateView(this, this.ctx.makeShapeTuple(...shapeArray));
        }
        /**
         * Get handle of ndarray, check it is not null.
         *
         * @param requireNotNull require handle is not null.
         * @returns The handle.
         */
        getHandle(requireNotNull = true) {
            if (requireNotNull && this.handle == 0) {
                throw Error("NDArray has already been disposed");
            }
            return this.handle;
        }
        /**
         * Get dataPtr of NDarray
         *
         * @returns The handle.
         */
        getDataPtr() {
            if (this.handle == 0) {
                throw Error("NDArray has already been disposed");
            }
            return this.dataPtr;
        }
        dispose() {
            if (this.handle != 0 && !this.isView) {
                this.lib.checkCall(this.lib.exports.TVMArrayFree(this.handle));
                this.handle = 0;
            }
        }
        /**
         * Copy data from another NDArray or javascript array.
         * The number of elements must match.
         *
         * @param data The source data array.
         * @returns this
         */
        copyFrom(data) {
            if (data instanceof NDArray) {
                this.lib.checkCall(this.lib.exports.TVMArrayCopyFromTo(data.getHandle(), this.getHandle(), 0));
                return this;
            }
            else {
                const size = this.shape.reduce((a, b) => {
                    return a * b;
                }, 1);
                if (data.length != size) {
                    throw new Error("data size and shape mismatch data.length" +
                        data.length +
                        " vs " +
                        size);
                }
                let buffer;
                if (this.dtype == "float32") {
                    buffer = Float32Array.from(data).buffer;
                }
                else if (this.dtype == "float64") {
                    buffer = Float64Array.from(data).buffer;
                }
                else if (this.dtype == "int32") {
                    buffer = Int32Array.from(data).buffer;
                }
                else if (this.dtype == "int8") {
                    buffer = Int8Array.from(data).buffer;
                }
                else if (this.dtype == "uint8") {
                    buffer = Uint8Array.from(data).buffer;
                }
                else {
                    throw new Error("Unsupported data type " + this.dtype);
                }
                return this.copyFromRawBytes(new Uint8Array(buffer));
            }
        }
        /**
         * Copy data from raw bytes.
         * @param data Uint8Array of bytes.
         * @returns this
         */
        copyFromRawBytes(data) {
            var _a;
            // short cut for gpu copy
            if (this.device.deviceType == DeviceStrToEnum.webgpu) {
                (_a = this.lib.webGPUContext) === null || _a === void 0 ? void 0 : _a.copyRawBytesToBuffer(data, this.getDataPtr(), 0, data.length);
                return this;
            }
            // CPU copy
            const size = this.shape.reduce((a, b) => {
                return a * b;
            }, 1);
            const nbytes = this.dlDataType.numStorageBytes() * size;
            if (nbytes != data.length) {
                throw new Error("Expect the data's length equals nbytes=" + nbytes);
            }
            const stack = this.lib.getOrAllocCallStack();
            const tempOffset = stack.allocRawBytes(nbytes);
            const tempPtr = stack.ptrFromOffset(tempOffset);
            this.lib.memory.storeRawBytes(tempPtr, data);
            this.lib.checkCall(this.lib.exports.TVMArrayCopyFromBytes(this.getHandle(), tempPtr, nbytes));
            this.lib.recycleCallStack(stack);
            return this;
        }
        /**
         * Return a copied Uint8Array of the raw bytes in the NDArray.
         * @returns The result array.
         */
        toRawBytes() {
            if (this.device.deviceType != DeviceStrToEnum.cpu) {
                throw new Error("Can only sync copy CPU array, use cpu_arr.copyfrom(gpu_arr) then sync instead.");
            }
            const size = this.shape.reduce((a, b) => {
                return a * b;
            }, 1);
            const nbytes = this.dlDataType.numStorageBytes() * size;
            const stack = this.lib.getOrAllocCallStack();
            const tempOffset = stack.allocRawBytes(nbytes);
            const tempPtr = stack.ptrFromOffset(tempOffset);
            this.lib.checkCall(this.lib.exports.TVMArrayCopyToBytes(this.getHandle(), tempPtr, nbytes));
            const ret = this.lib.memory.loadRawBytes(tempPtr, nbytes);
            this.lib.recycleCallStack(stack);
            return ret;
        }
        /**
         * Return a TypedArray copy of the NDArray, the specific type depends on
         * the dtype of the NDArray.
         * @returns The result array.
         */
        toArray() {
            const stype = this.dtype;
            if (stype == "float32") {
                return new Float32Array(this.toRawBytes().buffer);
            }
            else if (stype == "float64") {
                return new Float64Array(this.toRawBytes().buffer);
            }
            else if (stype == "int32") {
                return new Int32Array(this.toRawBytes().buffer);
            }
            else if (stype == "int8") {
                return new Int8Array(this.toRawBytes().buffer);
            }
            else if (stype == "uint8") {
                return new Uint8Array(this.toRawBytes().buffer);
            }
            else {
                throw new Error("Unsupported data type " + this.dtype);
            }
        }
        getDLTensorFromArrayHandle(handle) {
            // Note: this depends on the NDArray C ABI.
            // keep this function in case of ABI change.
            return handle;
        }
    }
    /**
     * Runtime Module.
     */
    class Module {
        constructor(handle, lib, makePackedFunc) {
            this.handle = handle;
            this.lib = lib;
            this.makePackedFunc = makePackedFunc;
        }
        dispose() {
            if (this.handle != 0) {
                this.lib.checkCall(this.lib.exports.TVMModFree(this.handle));
                this.handle = 0;
            }
        }
        /**
         * Get handle of module, check it is not null.
         *
         * @param requireNotNull require handle is not null.
         * @returns The handle.
         */
        getHandle(requireNotNull = true) {
            if (requireNotNull && this.handle == 0) {
                throw Error("Module has already been disposed");
            }
            return this.handle;
        }
        /**
         * Get a function in the module.
         * @param name The name of the function.
         * @param queryImports Whether to also query imports
         * @returns The result function.
         */
        getFunction(name, queryImports = true) {
            if (this.handle == 0) {
                throw Error("Module has already been disposed");
            }
            const stack = this.lib.getOrAllocCallStack();
            const nameOffset = stack.allocRawBytes(name.length + 1);
            stack.storeRawBytes(nameOffset, StringToUint8Array(name));
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            stack.commitToWasmMemory(outOffset);
            this.lib.checkCall(this.lib.exports.TVMModGetFunction(this.getHandle(), stack.ptrFromOffset(nameOffset), queryImports ? 1 : 0, outPtr));
            const handle = this.lib.memory.loadPointer(outPtr);
            this.lib.recycleCallStack(stack);
            if (handle == 0) {
                throw Error("Cannot find function " + name);
            }
            const ret = this.makePackedFunc(handle);
            return ret;
        }
        /**
         * Import another module into the current runtime module.
         * @param mod The module to be imported.
         */
        importModule(mod) {
            this.lib.checkCall(this.lib.exports.TVMModImport(this.getHandle(), mod.getHandle()));
        }
    }
    /**
     * Generic object base
     */
    class TVMObject {
        constructor(handle, lib, ctx) {
            this.handle = handle;
            this.lib = lib;
            this.ctx = ctx;
        }
        dispose() {
            if (this.handle != 0) {
                this.lib.checkCall(this.lib.exports.TVMObjectFree(this.handle));
                this.handle = 0;
            }
        }
        /**
         * Get handle of module, check it is not null.
         *
         * @param requireNotNull require handle is not null.
         * @returns The handle.
         */
        getHandle(requireNotNull = true) {
            if (requireNotNull && this.handle == 0) {
                throw Error("Module has already been disposed");
            }
            return this.handle;
        }
        /** get the type index of the object */
        typeIndex() {
            if (this.handle == 0) {
                throw Error("The current Object has already been disposed");
            }
            const stack = this.lib.getOrAllocCallStack();
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            this.lib.checkCall(this.lib.exports.TVMObjectGetTypeIndex(this.getHandle(), outPtr));
            const result = this.lib.memory.loadU32(outPtr);
            this.lib.recycleCallStack(stack);
            return result;
        }
        /** get the type key of the object */
        typeKey() {
            const type_index = this.typeIndex();
            const stack = this.lib.getOrAllocCallStack();
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            this.lib.checkCall(this.lib.exports.TVMObjectTypeIndex2Key(type_index, outPtr));
            const result = this.lib.memory.loadCString(this.lib.memory.loadPointer(outPtr));
            this.lib.recycleCallStack(stack);
            return result;
        }
    }
    /** Runtime array object. */
    class TVMArray extends TVMObject {
        constructor(handle, lib, ctx) {
            super(handle, lib, ctx);
        }
        /**
         * @returns the size of the array.
         */
        size() {
            return this.ctx.arrayGetSize(this);
        }
        /**
         * Get index-th element of the array
         * @param index the array index.
         * @returns The element.
         */
        get(index) {
            return this.ctx.arrayGetItem(this, new Scalar(index, "int32"));
        }
    }
    /** Runtime string object. */
    class TVMString extends TVMObject {
        constructor(handle, lib, ctx) {
            super(handle, lib, ctx);
        }
        /**
         * @returns the size of the array.
         */
        toString() {
            return this.ctx.getFFIString(this);
        }
    }
    /**
     *  VirtualMachine Executor.
     *
     *  This is a thin wrapper of the underlying TVM module.
     *  you can also directly call set_input, run, and get_output
     *  of underlying module functions
     */
    class VirtualMachine {
        /**
         * Constructor
         * @param mod The underlying module, need to be detached.
         * @param device The main device ro run VM on.
         */
        constructor(mod, device) {
            this.mod = mod;
            this.mod.getFunction("vm_initialization")(new Scalar(device.deviceType, "int"), new Scalar(device.deviceId, "int"), new Scalar(2 /* VMAllocatorKind.POOLED_ALLOCATOR */, "int"), 
            // explicitly specify host device type
            new Scalar(DeviceStrToEnum.cpu, "int"), new Scalar(0, "int"), new Scalar(2 /* VMAllocatorKind.POOLED_ALLOCATOR */, "int"));
        }
        dispose() {
            this.mod.dispose();
        }
        /**
         * Get a function in the VM module.
         * @param name The name of the function.
         * @returns The result function.
         */
        getFunction(name) {
            return this.mod.getFunction(name);
        }
        /**
         * Get the internal module.
         */
        getInternalModule() {
            return this.mod;
        }
    }
    /**
     * Cache to store model related data.
     */
    class ArtifactCache {
        constructor(scope) {
            this.scope = scope;
        }
        fetchWithCache(url) {
            return __awaiter(this, void 0, void 0, function* () {
                const request = new Request(url);
                if (this.cache === undefined) {
                    this.cache = yield caches.open(this.scope);
                }
                let result = yield this.cache.match(request);
                if (result === undefined) {
                    yield this.cache.add(request);
                    result = yield this.cache.match(request);
                }
                if (result == undefined) {
                    throw Error("Cannot fetch " + url);
                }
                return result;
            });
        }
    }
    /**
     * TVM runtime instance.
     *
     * All objects(NDArray, Module, PackedFunc) returned by TVM runtim function call
     * and PackedFunc instance are tracked through a scope mechanism that will get
     * auto-released when we call EndScope.
     *
     * This is necessarily to be able to release the underlying WASM and WebGPU memory that
     * are not tracked through JS native garbage collection mechanism.
     *
     * This does mean that we have to get familar with the following functions:
     * - {@link beginScope}
     * - {@link endScope}
     * - {@link withNewScope}
     * - {@link attachToCurrentScope}
     * - {@link detachFromCurrentScope}
     */
    class Instance {
        /**
         * Constructor
         *
         * importObject can also be a {@link LibraryProvider} object,
         * a WASI object, or an object containing wasmLibraryProvider field.
         *
         * @param wasmModule The input module or instance.
         * @param importObject The imports to initialize the wasmInstance if it is not provided.
         * @param wasmInstance Additional wasm instance argument for deferred construction.
         * @param env Directly specified environment module.
         *
         * @see Please use the async version {@link instantiate} when targeting browsers.
         */
        constructor(wasmModule, importObject = {}, wasmInstance, env) {
            this.cacheMetadata = {};
            this.initProgressCallback = [];
            if (wasmInstance instanceof WebAssembly.Instance) {
                assert(env instanceof Environment, "env must be provided when passing in instance");
            }
            else {
                assert(env === undefined);
                env = new Environment(importObject);
                wasmInstance = new WebAssembly.Instance(wasmModule, env.imports);
            }
            env.start(wasmInstance);
            this.env = env;
            this.lib = new FFILibrary(wasmInstance, env.imports);
            this.memory = this.lib.memory;
            this.exports = this.lib.exports;
            this.objFactory = new Map();
            this.ctx = new RuntimeContext((name) => {
                const autoAttachToScope = false;
                // runtime context function do not auto-release.
                return this.getGlobalFuncInternal(name, autoAttachToScope);
            });
            this.registerEnvGlobalPackedFuncs();
            this.registerObjectFactoryFuncs();
        }
        /**
         * Benchmark stable execution of the run function.
         *
         * @params run The run function
         * @params dev The device to sync during each run.
         * @number The number of times to compute the average.
         * @repeat The number of times to repeat the run.
         */
        benchmark(run, dev, number = 10, repeat = 1) {
            return __awaiter(this, void 0, void 0, function* () {
                // Skip first run as it can involve GPU warmup and module loading time.
                const perf = getPerformance();
                const results = [];
                // run with new scope
                this.withNewScope(run);
                yield dev.sync();
                for (let k = 0; k < repeat; ++k) {
                    const tstart = perf.now();
                    for (let i = 0; i < number; ++i) {
                        this.withNewScope(run);
                    }
                    yield dev.sync();
                    const tend = perf.now();
                    results.push((tend - tstart) / number);
                }
                return results;
            });
        }
        dispose() {
            // order matters
            // ctx release goes back into lib.
            this.ctx.dispose();
            this.lib.dispose();
        }
        /**
         * Obtain the runtime information in readable format.
         */
        runtimeStatsText() {
            if (this.lib.webGPUContext !== undefined) {
                return this.lib.webGPUContext.runtimeStatsText();
            }
            else {
                return "";
            }
        }
        /**
         * Begin a new scope for tracking object disposal.
         */
        beginScope() {
            this.ctx.beginScope();
        }
        /**
         * End a scope and release all created TVM objects
         * under the current scope.
         *
         * Exception: one can call {@link moveToParentScope} to move
         * a value to parent scope.
         */
        endScope() {
            this.ctx.endScope();
        }
        /**
         * Perform action under a new scope.
         *
         * @param action The action function.
         * @returns The result value.
         *
         * @note For action to return a valid value,
         *       we will need to call {@link moveToParentScope}
         *       for the objects that are created in the scope.
         */
        withNewScope(action) {
            this.beginScope();
            const val = action();
            this.endScope();
            return val;
        }
        /**
         * Attach a detached obj to the auto-release pool of the current scope.
         *
         * @param obj The input obj.
         * @note Normally user do not need to call this function explicitly, as
         *       all library call return values are explicitly attached to
         *       the current scope. You only need to do so when you call
         *       {@link detachFromCurrentScope} to create a detached object.
         */
        attachToCurrentScope(obj) {
            return this.ctx.attachToCurrentScope(obj);
        }
        /**
         * Move obj's attachment to the parent scope.
         *
         * This function is useful to make sure objects are still
         * alive when exit the current scope.
         *
         * @param obj The object to be moved.
         * @returns The input obj.
         */
        moveToParentScope(obj) {
            return this.ctx.moveToParentScope(obj);
        }
        /**
         * Detach the object from the current scope
         * so it won't be released via auto-release during endscope.
         *
         * User needs to either explicitly call obj.dispose(), or
         * {@link attachToCurrentScope} to re-attach to the current scope.
         *
         * This function can be used to return values to the parent scope.
         * @param obj The object.
         */
        detachFromCurrentScope(obj) {
            return this.ctx.detachFromCurrentScope(obj);
        }
        /**
         * Get system-wide library module in the wasm.
         * System lib is a global module that contains self register functions in startup.
         * @returns The system library module.
         */
        systemLib() {
            return this.ctx.getSysLib();
        }
        /**
         * List all the global function names registered in the runtime.
         * @returns The name list.
         */
        listGlobalFuncNames() {
            const stack = this.lib.getOrAllocCallStack();
            const outSizeOffset = stack.allocPtrArray(2);
            const outSizePtr = stack.ptrFromOffset(outSizeOffset);
            const outArrayPtr = stack.ptrFromOffset(outSizeOffset + this.lib.sizeofPtr());
            this.lib.checkCall(this.exports.TVMFuncListGlobalNames(outSizePtr, outArrayPtr));
            const size = this.memory.loadI32(outSizePtr);
            const array = this.memory.loadPointer(outArrayPtr);
            const names = [];
            for (let i = 0; i < size; ++i) {
                names.push(this.memory.loadCString(this.memory.loadPointer(array + this.lib.sizeofPtr() * i)));
            }
            this.lib.recycleCallStack(stack);
            return names;
        }
        /**
         * Register function to be global function in tvm runtime.
         * @param name The name of the function.
         * @param f function to be registered.
         * @param override Whether overwrite function in existing registry.
         */
        registerFunc(name, func, override = false) {
            this.withNewScope(() => {
                const autoAttachToScope = true;
                // packed func can be released once it is registered
                const packedFunc = this.toPackedFuncInternal(func, autoAttachToScope);
                const ioverride = override ? 1 : 0;
                const stack = this.lib.getOrAllocCallStack();
                const nameOffset = stack.allocRawBytes(name.length + 1);
                stack.storeRawBytes(nameOffset, StringToUint8Array(name));
                stack.commitToWasmMemory();
                this.lib.checkCall(this.lib.exports.TVMFuncRegisterGlobal(stack.ptrFromOffset(nameOffset), packedFunc._tvmPackedCell.getHandle(), ioverride));
                this.lib.recycleCallStack(stack);
            });
        }
        /**
         * Get global PackedFunc from the runtime.
         * @param name The name of the function.
         * @param autoAttachToScope Whether to track it via autoDispose
         * @returns The result function.
         */
        getGlobalFunc(name) {
            return this.getGlobalFuncInternal(name, true);
        }
        getGlobalFuncInternal(name, autoAttachToScope = true) {
            const stack = this.lib.getOrAllocCallStack();
            const nameOffset = stack.allocRawBytes(name.length + 1);
            stack.storeRawBytes(nameOffset, StringToUint8Array(name));
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            stack.commitToWasmMemory(outOffset);
            this.lib.checkCall(this.exports.TVMFuncGetGlobal(stack.ptrFromOffset(nameOffset), outPtr));
            const handle = this.memory.loadPointer(outPtr);
            this.lib.recycleCallStack(stack);
            if (handle == 0) {
                throw Error("Cannot find global function " + name);
            }
            const ret = this.makePackedFunc(handle);
            if (autoAttachToScope)
                this.ctx.attachToCurrentScope(ret);
            return ret;
        }
        /**
         * Check if func is PackedFunc.
         *
         * @param func The input.
         * @returns The check result.
         */
        isPackedFunc(func) {
            // eslint-disable-next-line no-prototype-builtins
            return typeof func == "function" && func.hasOwnProperty("_tvmPackedCell");
        }
        /**
         * Convert func to PackedFunc
         *
         * @param func Input function.
         * @returns The converted function.
         */
        toPackedFunc(func) {
            return this.toPackedFuncInternal(func, true);
        }
        toPackedFuncInternal(func, autoAttachToScope) {
            if (this.isPackedFunc(func))
                return func;
            const ret = this.createPackedFuncFromCFunc(this.wrapJSFuncAsPackedCFunc(func));
            if (autoAttachToScope)
                return this.ctx.attachToCurrentScope(ret);
            return ret;
        }
        /**
        * Setup a virtual machine module with given device.
        *
        * @param dev DLDevice the device.
        * @returns The created virtual machime.
        */
        createVirtualMachine(dev) {
            const mod = this.ctx.detachFromCurrentScope(this.systemLib().getFunction("vm_load_executable")());
            return this.ctx.attachToCurrentScope(new VirtualMachine(mod, dev));
        }
        //-----------------------------------------------
        // Native NDArray Cache Support
        //-----------------------------------------------
        /**
         * Register a call back for fetch progress.
        *
         * @param cb the fetch progress callback.
         */
        registerInitProgressCallback(cb) {
            this.initProgressCallback.push(cb);
        }
        /**
         * Get parameters in the form of prefix_i
         *
         * @param prefix The parameter prefix.
         * @param numParams  Number of parameters.
         * @returns
         */
        getParamsFromCache(prefix, numParams) {
            return this.ctx.paramModuleFromCache(prefix, new Scalar(numParams, "int32")).getFunction("get_params")();
        }
        /**
         * Get NDArray from cache.
         * @param name  The name of array.
         * @returns  The result.
         */
        ndarrayCacheGet(name) {
            return this.ctx.arrayCacheGet(name);
        }
        /**
         * Get NDArray from cache.
         * @param name  The name of array.
         * @returns  The result.
         */
        ndarrayCacheRemove(name) {
            return this.ctx.arrayCacheRemove(name);
        }
        /**
         * Update the ndarray cache.
         * @param name The name of the array.
         * @param arr The content.
         */
        ndarrayCacheUpdate(name, arr, override = false) {
            this.ctx.arrayCacheUpdate(name, arr, this.scalar(override ? 1 : 0, "int32"));
        }
        /**
         * Update the ndarray cache.
         * @param name The name of the array.
         * @param arr The content.
         */
        ndarrayCacheClear() {
            this.ctx.arrayCacheClear();
        }
        /**
         * Fetch NDArray cache from url.
         *
         * @param ndarrayCacheUrl The cache url.
         * @param device The device to be fetched to.
         * @param cacheScope The scope identifier of the cache
         * @returns The meta data
         */
        fetchNDArrayCache(ndarrayCacheUrl, device, cacheScope = "tvmjs") {
            return __awaiter(this, void 0, void 0, function* () {
                const artifactCache = new ArtifactCache(cacheScope);
                const jsonUrl = new URL("ndarray-cache.json", ndarrayCacheUrl).href;
                const result = yield artifactCache.fetchWithCache(jsonUrl);
                let list;
                if (result instanceof Response) {
                    list = yield result.json();
                }
                yield this.fetchNDArrayCacheInternal(ndarrayCacheUrl, list["records"], device, artifactCache);
                this.cacheMetadata = Object.assign(Object.assign({}, this.cacheMetadata), list["metadata"]);
            });
        }
        /**
         * Fetch list of NDArray into the NDArrayCache.
         *
         * @param ndarrayCacheUrl The cache url.
         * @param list The list of array data.
         * @param device The device to store the data to.
         * @param artifactCache The artifact cache
         */
        fetchNDArrayCacheInternal(ndarrayCacheUrl, list, device, artifactCache) {
            return __awaiter(this, void 0, void 0, function* () {
                const perf = getPerformance();
                let tstart = perf.now();
                let totalBytes = 0;
                for (let i = 0; i < list.length; ++i) {
                    totalBytes += list[i].nbytes;
                }
                let fetchedBytes = 0;
                let timeElapsed = 0;
                const reportCallback = (iter) => {
                    // report
                    for (let j = 0; j < this.initProgressCallback.length; ++j) {
                        let text = "Fetching param cache[" + iter + "/" + list.length + "]: ";
                        text += Math.ceil(fetchedBytes / (1024 * 1024)).toString() + "MB fetched. ";
                        text += Math.floor(fetchedBytes * 100 / totalBytes).toString() + "% completed, ";
                        text += timeElapsed + " secs elapsed.";
                        text += " It can take a while when we first visit this page to populate the cache.";
                        text += " Later refreshes will become faster.";
                        this.initProgressCallback[j]({
                            progress: fetchedBytes / totalBytes,
                            timeElapsed: timeElapsed,
                            text: text
                        });
                    }
                };
                for (let j = 0; j < this.initProgressCallback.length; ++j) {
                    this.initProgressCallback[j]({
                        progress: fetchedBytes / totalBytes,
                        timeElapsed: 0,
                        text: "Start to fetch params",
                    });
                }
                for (let i = 0; i < list.length; ++i) {
                    reportCallback(i);
                    fetchedBytes += list[i].nbytes;
                    const dataUrl = new URL(list[i].dataPath, ndarrayCacheUrl).href;
                    let buffer;
                    try {
                        buffer = yield (yield artifactCache.fetchWithCache(dataUrl)).arrayBuffer();
                    }
                    catch (err) {
                        this.env.logger("Error: Cannot fetch " + dataUrl + " err= " + err);
                        throw err;
                    }
                    const shardRecords = list[i].records;
                    for (let j = 0; j < shardRecords.length; ++j) {
                        const rec = shardRecords[j];
                        const cpu_arr = this.withNewScope(() => {
                            return this.detachFromCurrentScope(this.empty(rec.shape, rec.dtype, this.cpu()));
                        });
                        const recSource = buffer.slice(rec.byteOffset, rec.byteOffset + rec.nbytes);
                        // first sync copy to cpu.
                        this.ctx.arrayDecodeStorage(cpu_arr, new Uint8Array(recSource), rec.format);
                        // then async stream into GPU if needed
                        if (device.deviceType == DeviceStrToEnum.cpu) {
                            this.ndarrayCacheUpdate(rec.name, cpu_arr, false);
                            cpu_arr.dispose();
                        }
                        else {
                            // allocate a gpu arr and async copy to it.
                            const gpu_arr = this.withNewScope(() => {
                                return this.detachFromCurrentScope(this.empty(rec.shape, rec.dtype, device));
                            });
                            gpu_arr.copyFrom(cpu_arr);
                            yield device.sync();
                            this.ndarrayCacheUpdate(rec.name, gpu_arr, false);
                            cpu_arr.dispose();
                            gpu_arr.dispose();
                        }
                    }
                    timeElapsed = Math.ceil((perf.now() - tstart) / 1000);
                }
                reportCallback(list.length);
            });
        }
        /**
         * Convert dtype to {@link DLDataType}
         *
         * @param dtype The input dtype string or DLDataType.
         * @returns The converted result.
         */
        toDLDataType(dtype) {
            if (dtype instanceof DLDataType)
                return dtype;
            if (typeof dtype == "string") {
                let pattern = dtype;
                let code, bits = 32, lanes = 1;
                if (pattern.substring(0, 5) == "float") {
                    pattern = pattern.substring(5, pattern.length);
                    code = 2 /* DLDataTypeCode.Float */;
                }
                else if (pattern.substring(0, 3) == "int") {
                    pattern = pattern.substring(3, pattern.length);
                    code = 0 /* DLDataTypeCode.Int */;
                }
                else if (pattern.substring(0, 4) == "uint") {
                    pattern = pattern.substring(4, pattern.length);
                    code = 1 /* DLDataTypeCode.UInt */;
                }
                else if (pattern.substring(0, 6) == "handle") {
                    pattern = pattern.substring(5, pattern.length);
                    code = 3 /* DLDataTypeCode.OpaqueHandle */;
                    bits = 64;
                }
                else {
                    throw new Error("Unknown dtype " + dtype);
                }
                const arr = pattern.split("x");
                if (arr.length >= 1) {
                    const parsed = parseInt(arr[0]);
                    if (parsed + "" == arr[0]) {
                        bits = parsed;
                    }
                }
                if (arr.length >= 2) {
                    lanes = parseInt(arr[1]);
                }
                return new DLDataType(code, bits, lanes);
            }
            else {
                throw new Error("Unknown dtype " + dtype);
            }
        }
        /**
         * Create a new {@link Scalar} that can be passed to a PackedFunc.
         * @param value The number value.
         * @param dtype The dtype string.
         * @returns The created scalar.
         */
        scalar(value, dtype) {
            return new Scalar(value, dtype);
        }
        /**
         * Create a new {@link DLDevice}
         * @param deviceType The device type.
         * @param deviceId The device index.
         * @returns The created device.
         */
        device(deviceType, deviceId = 0) {
            return new DLDevice(deviceType, deviceId, this.lib);
        }
        /**
         * Create a new cpu {@link DLDevice}
         * @param deviceId The device index.
         */
        cpu(deviceId = 0) {
            return this.device("cpu", deviceId);
        }
        /**
         * Create a new webgpu {@link DLDevice}
         * @param deviceId The device index.
         */
        webgpu(deviceId = 0) {
            return this.device("webgpu", deviceId);
        }
        /**
         * Create an empty {@link NDArray} with given shape and dtype.
         *
         * @param shape The shape of the array.
         * @param dtype The data type of the array.
         * @param dev The device of the ndarray.
         * @returns The created ndarray.
         */
        empty(shape, dtype = "float32", dev = this.device("cpu", 0)) {
            dtype = this.toDLDataType(dtype);
            shape = typeof shape == "number" ? [shape] : shape;
            const stack = this.lib.getOrAllocCallStack();
            const shapeOffset = stack.allocRawBytes(shape.length * 8 /* SizeOf.I64 */);
            for (let i = 0; i < shape.length; ++i) {
                stack.storeI64(shapeOffset + i * 8 /* SizeOf.I64 */, shape[i]);
            }
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            stack.commitToWasmMemory(outOffset);
            this.lib.checkCall(this.exports.TVMArrayAlloc(stack.ptrFromOffset(shapeOffset), shape.length, dtype.code, dtype.bits, dtype.lanes, dev.deviceType, dev.deviceId, outPtr));
            const ret = this.ctx.attachToCurrentScope(new NDArray(this.memory.loadPointer(outPtr), false, this.lib, this.ctx));
            this.lib.recycleCallStack(stack);
            return ret;
        }
        /**
         * Create am uniform {@link NDArray} with given shape.
         *
         * @param shape The shape of the array.
         * @param low The low value.
         * @param high The high value.
         * @param dev The device of the ndarray.
         * @returns The created ndarray.
         */
        uniform(shape, low, high, dev) {
            const ret = this.empty(shape, "float32", dev);
            const size = shape.reduce((a, b) => {
                return a * b;
            }, 1);
            const scale = high - low;
            const input = new Float32Array(size);
            for (let i = 0; i < input.length; ++i) {
                input[i] = low + Math.random() * scale;
            }
            return ret.copyFrom(input);
        }
        /**
         * Sample index via top-p sampling.
         *
         * @param logits The input logits before normalization.
         * @param temperature  The temperature factor, will take argmax if temperature = 0.0
         * @param top_p The top_p
         * @returns The sampled index.
         */
        sampleTopPFromLogits(logits, temperature, top_p) {
            return this.ctx.sampleTopPFromLogits(logits, temperature, top_p, Math.random());
        }
        /**
         * Apply repetition penalty to the logits.
         * @param logits The input logits before penalty.
         * @param token_ids The appeared token ids.
         * @param penalty The penalty factor.
         */
        applyRepetitionPenalty(logits, token_ids, penalty) {
            return this.ctx.applyRepetitionPenalty(logits, token_ids, penalty);
        }
        /**
         * Apply softmax with temperature to the logits.
         * @param logits The input logits before softmax w/ temperature.
         * @param temperature The temperature factor.
         */
        applySoftmaxWithTemperature(logits, temperature) {
            return this.ctx.applySoftmaxWithTemperature(logits, temperature);
        }
        /**
         * Bind canvas to the current WebGPU context
         * @param canvas The canvas.
         */
        bindCanvas(canvas) {
            var _a;
            (_a = this.lib.webGPUContext) === null || _a === void 0 ? void 0 : _a.bindCanvas(canvas);
        }
        /**
         * Show image in canvas.
         *
         * @param dataRGBA Image array in height x width uint32 NDArray RGBA format on GPU.
         */
        showImage(dataRGBA) {
            var _a;
            if (dataRGBA.shape.length != 2) {
                throw Error("Require a height x width uint32 NDArray in RGBA" +
                    "get shape=" + dataRGBA.shape.toString() + " instead.");
            }
            if (dataRGBA.device.deviceType != DeviceStrToEnum.webgpu) {
                throw new Error("Can only run showImage on WebGPU array, " +
                    "get " + DeviceEnumToStr[dataRGBA.device.deviceType] + " instead.");
            }
            if (dataRGBA.dtype != "uint32") {
                throw Error("Require a height x width uint32 NDArray in RGBA, " +
                    "get " + dataRGBA.dtype + " instead.");
            }
            (_a = this.lib.webGPUContext) === null || _a === void 0 ? void 0 : _a.drawImageFromBuffer(dataRGBA.getDataPtr(), dataRGBA.shape[0], dataRGBA.shape[1]);
        }
        /**
         * Clear canvas
         */
        clearCanvas() {
            var _a;
            (_a = this.lib.webGPUContext) === null || _a === void 0 ? void 0 : _a.clearCanvas();
        }
        /**
         * Create an tuple {@link TVMArray} input array.
         *
         * The input array can be passed to tvm runtime function
         * and needs to b explicitly disposed.
         *
         * @param inputs The input array
         * @returns The result array.
         */
        makeTVMArray(inputs) {
            return this.ctx.arrayMake(...inputs);
        }
        /**
         * Create a {@link TVMString} that can be consumed by runtime.
         *
         * @param input The string.
         * @returns The result TVMString.
         */
        makeString(input) {
            return this.ctx.stringMake(input);
        }
        /**
         * Create a shape tuple to pass to runtime.
         * @param shape The shape .
         * @returns The created shape tuple.
         */
        makeShapeTuple(shape) {
            const shapeArray = shape.map((value) => new Scalar(value, "int"));
            return this.ctx.makeShapeTuple(...shapeArray);
        }
        /**
         * Get type index from type key.
         * @param typeKey The type key.
         * @returns The corresponding type index.
         */
        typeKey2Index(typeKey) {
            const stack = this.lib.getOrAllocCallStack();
            const typeKeyOffset = stack.allocRawBytes(typeKey.length + 1);
            stack.storeRawBytes(typeKeyOffset, StringToUint8Array(typeKey));
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            stack.commitToWasmMemory(outOffset);
            this.lib.checkCall(this.lib.exports.TVMObjectTypeKey2Index(stack.ptrFromOffset(typeKeyOffset), outPtr));
            const typeIndex = this.memory.loadU32(outPtr);
            this.lib.recycleCallStack(stack);
            return typeIndex;
        }
        /**
         * Register an object constructor.
         * @param typeKey The name of the function.
         * @param func function to be registered.
         * @param override Whether overwrite function in existing registry.
         */
        registerObjectConstructor(typeKey, func, override = false) {
            const typeIndex = this.typeKey2Index(typeKey);
            if (this.objFactory.has(typeIndex)) {
                if (!override) {
                    throw new Error("Type " + typeKey + " already registered");
                }
            }
            this.objFactory.set(typeIndex, func);
        }
        /**
         * Register an asyncfunction to be global function in the server.
         * @param name The name of the function.
         * @param func function to be registered.
         * @param override Whether overwrite function in existing registry.
         *
         * @note The async function will only be used for serving remote calls in the rpc.
         */
        registerAsyncServerFunc(name, func, override = false) {
            const asyncVariant = (...args) => {
                const fargs = args.slice(0, args.length - 1);
                // need to keep it alive until callback is fulfilled.
                const callback = this.detachFromCurrentScope(args[args.length - 1]);
                const promise = func(...fargs);
                promise.then((rv) => {
                    callback(this.scalar(4 /* AyncCallbackCode.kReturn */, "int32"), rv);
                    callback.dispose();
                });
            };
            this.registerFunc("__async." + name, asyncVariant, override);
        }
        /**
         * Asynchrously load webgpu pipelines when possible.
         * @param mod The input module.
         */
        asyncLoadWebGPUPiplines(mod) {
            return __awaiter(this, void 0, void 0, function* () {
                if (this.lib.webGPUContext == undefined)
                    throw Error("WebGPU not initialied");
                const webgpuContext = this.lib.webGPUContext;
                this.beginScope();
                const fmap_str = mod.getFunction("webgpu.get_fmap", true)();
                const fmap = JSON.parse(fmap_str);
                const fGetShader = this.detachFromCurrentScope(mod.getFunction("webgpu.get_shader"));
                const fUpdatePrebuild = this.detachFromCurrentScope(mod.getFunction("webgpu.update_prebuild"));
                this.endScope();
                const perf = getPerformance();
                const tstart = perf.now();
                let tlastReport = tstart;
                let finishCounter = 0;
                const fmapEntries = Object.entries(fmap);
                let allEvents = Promise.resolve();
                for (const [key, finfo] of fmapEntries) {
                    const code = fGetShader(key);
                    assert(key == finfo.name);
                    const event = webgpuContext.createShaderAsync(finfo, code).then((func) => {
                        this.beginScope();
                        fUpdatePrebuild(key, func);
                        this.endScope();
                    }).then(() => {
                        finishCounter += 1;
                        const tend = perf.now();
                        // skip report if gap is smaller than 1000
                        if ((tend - tlastReport) < 1000 && finishCounter != fmapEntries.length) {
                            return;
                        }
                        tlastReport = tend;
                        const timeElapsed = Math.ceil((perf.now() - tstart) / 1000);
                        // report
                        for (let j = 0; j < this.initProgressCallback.length; ++j) {
                            const progress = finishCounter / fmapEntries.length;
                            let text = "Loading GPU shader modules[" + finishCounter + "/" + fmapEntries.length + "]: ";
                            text += Math.floor(progress * 100).toString() + "% completed, ";
                            text += timeElapsed + " secs elapsed.";
                            this.initProgressCallback[j]({
                                progress: progress,
                                timeElapsed: timeElapsed,
                                text: text
                            });
                        }
                    });
                    allEvents = Promise.all([allEvents, event]).then(() => { });
                }
                yield allEvents;
                assert(finishCounter == fmapEntries.length);
            });
        }
        /**
         * Initialize webgpu in the runtime.
         * @param device The given GPU device.
         */
        initWebGPU(device) {
            const webGPUContext = new WebGPUContext(this.memory, device);
            this.registerFunc("wasm.WebGPUDeviceAPI", (name) => {
                return webGPUContext.getDeviceAPI(name);
            });
            this.registerFunc("wasm.WebGPUCreateShader", (info, code) => {
                const finfo = JSON.parse(info);
                return webGPUContext.createShader(finfo, code);
            });
            this.registerAsyncServerFunc("wasm.WebGPUWaitForTasks", () => __awaiter(this, void 0, void 0, function* () {
                yield webGPUContext.sync();
            }));
            this.lib.webGPUContext = webGPUContext;
        }
        /** Register all object factory */
        registerObjectFactoryFuncs() {
            this.registerObjectConstructor("Array", (handle, lib, ctx) => {
                return new TVMArray(handle, lib, ctx);
            });
            this.registerObjectConstructor("runtime.String", (handle, lib, ctx) => {
                return new TVMString(handle, lib, ctx);
            });
        }
        /** Register global packed functions needed by the backend to the env. */
        registerEnvGlobalPackedFuncs() {
            // Register the timer function to enable the time_evaluator.
            const perf = getPerformance();
            // Helper function to time the finvoke
            const timeExecution = (finvoke, dev, nstep, repeat, minRepeatMs, limitZeroTimeIterations, cooldownIntervalMs, repeatsToCooldown) => __awaiter(this, void 0, void 0, function* () {
                // detach and explicit dispose when tasks is fullfilled
                // the promise will immediately return and we need to makesure
                // finvoke do not get recycled.
                this.ctx.detachFromCurrentScope(finvoke);
                finvoke(this.scalar(1, "int32"));
                yield dev.sync();
                const result = [];
                let setupNumber = nstep;
                for (let i = 0; i < repeat; ++i) {
                    let durationMs = 0.0;
                    let absoluteZeroTimes = 0;
                    do {
                        if (durationMs > 0.0) {
                            let golden_ratio = 1.618;
                            setupNumber = Math.floor(Math.max(minRepeatMs / (durationMs / setupNumber) + 1, setupNumber * golden_ratio));
                        }
                        const tstart = perf.now();
                        finvoke(this.scalar(setupNumber, "int32"));
                        yield dev.sync();
                        const tend = perf.now();
                        durationMs = tend - tstart;
                        if (durationMs == 0) {
                            absoluteZeroTimes++;
                        }
                    } while (durationMs < minRepeatMs && absoluteZeroTimes < limitZeroTimeIterations);
                    const speed = durationMs / setupNumber / 1000;
                    result.push(speed);
                    if (cooldownIntervalMs > 0.0 && (i % repeatsToCooldown) == 0) {
                        yield new Promise(r => setTimeout(r, cooldownIntervalMs));
                    }
                }
                const ret = new Float64Array(result.length);
                ret.set(result);
                // dispose finvoke
                finvoke.dispose();
                return new Uint8Array(ret.buffer);
            });
            const addOne = (x) => __awaiter(this, void 0, void 0, function* () {
                yield new Promise(resolve => setTimeout(resolve, 100));
                return x + 1;
            });
            this.registerAsyncServerFunc("wasm.TimeExecution", timeExecution);
            this.registerAsyncServerFunc("testing.asyncAddOne", addOne);
        }
        createPackedFuncFromCFunc(func) {
            let findex = this.env.packedCFuncTable.length;
            if (this.env.packedCFuncTableFreeId.length != 0) {
                findex = this.env.packedCFuncTableFreeId.pop();
            }
            else {
                this.env.packedCFuncTable.push(undefined);
            }
            this.env.packedCFuncTable[findex] = func;
            const stack = this.lib.getOrAllocCallStack();
            const outOffset = stack.allocPtrArray(1);
            const outPtr = stack.ptrFromOffset(outOffset);
            this.lib.checkCall(this.exports
                .TVMWasmFuncCreateFromCFunc(findex, outPtr));
            const ret = this.makePackedFunc(this.memory.loadPointer(outPtr));
            this.lib.recycleCallStack(stack);
            return ret;
        }
        /**
         * Set packed function arguments into the location indicated by argsValue and argsCode.
         * Allocate new temporary space from the stack if necessary.
         *
         * @parma stack The call stack
         * @param args  The input arguments.
         * @param argsValue The offset of argsValue.
         * @param argsCode The offset of argsCode.
         */
        setPackedArguments(stack, args, argsValue, argsCode) {
            for (let i = 0; i < args.length; ++i) {
                let val = args[i];
                const tp = typeof val;
                const valueOffset = argsValue + i * 8 /* SizeOf.TVMValue */;
                const codeOffset = argsCode + i * 4 /* SizeOf.I32 */;
                if (val instanceof NDArray) {
                    if (!val.isView) {
                        stack.storePtr(valueOffset, val.getHandle());
                        stack.storeI32(codeOffset, 13 /* ArgTypeCode.TVMNDArrayHandle */);
                    }
                    else {
                        stack.storePtr(valueOffset, val.getHandle());
                        stack.storeI32(codeOffset, 7 /* ArgTypeCode.TVMDLTensorHandle */);
                    }
                }
                else if (val instanceof Scalar) {
                    if (val.dtype.startsWith("int") || val.dtype.startsWith("uint")) {
                        stack.storeI64(valueOffset, val.value);
                        stack.storeI32(codeOffset, 0 /* ArgTypeCode.Int */);
                    }
                    else if (val.dtype.startsWith("float")) {
                        stack.storeF64(valueOffset, val.value);
                        stack.storeI32(codeOffset, 2 /* ArgTypeCode.Float */);
                    }
                    else {
                        assert(val.dtype == "handle", "Expect handle");
                        stack.storePtr(valueOffset, val.value);
                        stack.storeI32(codeOffset, 3 /* ArgTypeCode.TVMOpaqueHandle */);
                    }
                }
                else if (val instanceof DLDevice) {
                    stack.storeI32(valueOffset, val.deviceType);
                    stack.storeI32(valueOffset + 4 /* SizeOf.I32 */, val.deviceType);
                    stack.storeI32(codeOffset, 6 /* ArgTypeCode.DLDevice */);
                }
                else if (tp == "number") {
                    stack.storeF64(valueOffset, val);
                    stack.storeI32(codeOffset, 2 /* ArgTypeCode.Float */);
                    // eslint-disable-next-line no-prototype-builtins
                }
                else if (tp == "function" && val.hasOwnProperty("_tvmPackedCell")) {
                    stack.storePtr(valueOffset, val._tvmPackedCell.getHandle());
                    stack.storeI32(codeOffset, 10 /* ArgTypeCode.TVMPackedFuncHandle */);
                }
                else if (val === null || val == undefined) {
                    stack.storePtr(valueOffset, 0);
                    stack.storeI32(codeOffset, 4 /* ArgTypeCode.Null */);
                }
                else if (tp == "string") {
                    stack.allocThenSetArgString(valueOffset, val);
                    stack.storeI32(codeOffset, 11 /* ArgTypeCode.TVMStr */);
                }
                else if (val instanceof Uint8Array) {
                    stack.allocThenSetArgBytes(valueOffset, val);
                    stack.storeI32(codeOffset, 12 /* ArgTypeCode.TVMBytes */);
                }
                else if (val instanceof Function) {
                    val = this.toPackedFuncInternal(val, false);
                    stack.tempArgs.push(val);
                    stack.storePtr(valueOffset, val._tvmPackedCell.getHandle());
                    stack.storeI32(codeOffset, 10 /* ArgTypeCode.TVMPackedFuncHandle */);
                }
                else if (val instanceof Module) {
                    stack.storePtr(valueOffset, val.getHandle());
                    stack.storeI32(codeOffset, 9 /* ArgTypeCode.TVMModuleHandle */);
                }
                else if (val instanceof TVMObject) {
                    stack.storePtr(valueOffset, val.getHandle());
                    stack.storeI32(codeOffset, 8 /* ArgTypeCode.TVMObjectHandle */);
                }
                else {
                    throw new Error("Unsupported argument type " + tp);
                }
            }
        }
        wrapJSFuncAsPackedCFunc(func) {
            const lib = this.lib;
            return (argValues, argCodes, nargs, ret, 
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            _handle) => {
                const jsArgs = [];
                // use scope to track js values.
                this.ctx.beginScope();
                for (let i = 0; i < nargs; ++i) {
                    const valuePtr = argValues + i * 8 /* SizeOf.TVMValue */;
                    const codePtr = argCodes + i * 4 /* SizeOf.I32 */;
                    let tcode = lib.memory.loadI32(codePtr);
                    if (tcode == 8 /* ArgTypeCode.TVMObjectHandle */ ||
                        tcode == 14 /* ArgTypeCode.TVMObjectRValueRefArg */ ||
                        tcode == 10 /* ArgTypeCode.TVMPackedFuncHandle */ ||
                        tcode == 13 /* ArgTypeCode.TVMNDArrayHandle */ ||
                        tcode == 9 /* ArgTypeCode.TVMModuleHandle */) {
                        lib.checkCall(lib.exports.TVMCbArgToReturn(valuePtr, codePtr));
                    }
                    tcode = lib.memory.loadI32(codePtr);
                    jsArgs.push(this.retValueToJS(valuePtr, tcode, true));
                }
                const rv = func(...jsArgs);
                // recycle all js object value in function unless we want to retain them.
                this.ctx.endScope();
                if (rv !== undefined && rv !== null) {
                    const stack = lib.getOrAllocCallStack();
                    const valueOffset = stack.allocRawBytes(8 /* SizeOf.TVMValue */);
                    const codeOffset = stack.allocRawBytes(4 /* SizeOf.I32 */);
                    this.setPackedArguments(stack, [rv], valueOffset, codeOffset);
                    const valuePtr = stack.ptrFromOffset(valueOffset);
                    const codePtr = stack.ptrFromOffset(codeOffset);
                    stack.commitToWasmMemory();
                    lib.checkCall(lib.exports.TVMCFuncSetReturn(ret, valuePtr, codePtr, 1));
                    lib.recycleCallStack(stack);
                }
                return 0;
            };
        }
        makePackedFunc(handle) {
            const cell = new PackedFuncCell(handle, this.lib);
            const packedFunc = (...args) => {
                const stack = this.lib.getOrAllocCallStack();
                const valueOffset = stack.allocRawBytes(8 /* SizeOf.TVMValue */ * args.length);
                const tcodeOffset = stack.allocRawBytes(4 /* SizeOf.I32 */ * args.length);
                this.setPackedArguments(stack, args, valueOffset, tcodeOffset);
                const rvalueOffset = stack.allocRawBytes(8 /* SizeOf.TVMValue */);
                const rcodeOffset = stack.allocRawBytes(4 /* SizeOf.I32 */);
                const rvaluePtr = stack.ptrFromOffset(rvalueOffset);
                const rcodePtr = stack.ptrFromOffset(rcodeOffset);
                // commit to wasm memory, till rvalueOffset (the return value don't need to be committed)
                stack.commitToWasmMemory(rvalueOffset);
                this.lib.checkCall(this.exports.TVMFuncCall(cell.getHandle(), stack.ptrFromOffset(valueOffset), stack.ptrFromOffset(tcodeOffset), args.length, rvaluePtr, rcodePtr));
                const ret = this.retValueToJS(rvaluePtr, this.memory.loadI32(rcodePtr), false);
                this.lib.recycleCallStack(stack);
                return ret;
            };
            // Attach attributes to the function type.
            // This is because javascript do not allow us to overload call.
            const ret = packedFunc;
            ret.dispose = () => {
                cell.dispose();
            };
            ret._tvmPackedCell = cell;
            return ret;
        }
        /**
         * Creaye return value of the packed func. The value us auto-tracked for dispose.
         * @param rvaluePtr The location of rvalue
         * @param tcode     The type code.
         * @param callbackArg Whether it is being used in callbackArg.
         * @returns The JS value.
         */
        retValueToJS(rvaluePtr, tcode, callbackArg) {
            switch (tcode) {
                case 0 /* ArgTypeCode.Int */:
                case 1 /* ArgTypeCode.UInt */:
                    return this.memory.loadI64(rvaluePtr);
                case 2 /* ArgTypeCode.Float */:
                    return this.memory.loadF64(rvaluePtr);
                case 3 /* ArgTypeCode.TVMOpaqueHandle */: {
                    return this.memory.loadPointer(rvaluePtr);
                }
                case 13 /* ArgTypeCode.TVMNDArrayHandle */: {
                    return this.ctx.attachToCurrentScope(new NDArray(this.memory.loadPointer(rvaluePtr), false, this.lib, this.ctx));
                }
                case 7 /* ArgTypeCode.TVMDLTensorHandle */: {
                    assert(callbackArg);
                    // no need to attach as we are only looking at view
                    return new NDArray(this.memory.loadPointer(rvaluePtr), true, this.lib, this.ctx);
                }
                case 10 /* ArgTypeCode.TVMPackedFuncHandle */: {
                    return this.ctx.attachToCurrentScope(this.makePackedFunc(this.memory.loadPointer(rvaluePtr)));
                }
                case 9 /* ArgTypeCode.TVMModuleHandle */: {
                    return this.ctx.attachToCurrentScope(new Module(this.memory.loadPointer(rvaluePtr), this.lib, (ptr) => {
                        return this.ctx.attachToCurrentScope(this.makePackedFunc(ptr));
                    }));
                }
                case 8 /* ArgTypeCode.TVMObjectHandle */: {
                    const obj = new TVMObject(this.memory.loadPointer(rvaluePtr), this.lib, this.ctx);
                    const func = this.objFactory.get(obj.typeIndex());
                    if (func != undefined) {
                        return this.ctx.attachToCurrentScope(func(obj.getHandle(), this.lib, this.ctx));
                    }
                    else {
                        return this.ctx.attachToCurrentScope(obj);
                    }
                }
                case 4 /* ArgTypeCode.Null */: return undefined;
                case 6 /* ArgTypeCode.DLDevice */: {
                    const deviceType = this.memory.loadI32(rvaluePtr);
                    const deviceId = this.memory.loadI32(rvaluePtr + 4 /* SizeOf.I32 */);
                    return this.device(deviceType, deviceId);
                }
                case 11 /* ArgTypeCode.TVMStr */: {
                    const ret = this.memory.loadCString(this.memory.loadPointer(rvaluePtr));
                    return ret;
                }
                case 12 /* ArgTypeCode.TVMBytes */: {
                    return this.memory.loadTVMBytes(this.memory.loadPointer(rvaluePtr));
                }
                default:
                    throw new Error("Unsupported return type code=" + tcode);
            }
        }
    }
    /**
     * Asynchrously instantiate a new {@link Instance}.
     *
     * importObject can also be a {@link LibraryProvider} object,
     * a WASI object, or an object containing wasmLibraryProvider field.
     * We can take benefit of syslib implementations from the Emscripten
     * by passing its generated js Module as the imports.
     *
     * @param bufferSource The source to be compiled.
     * @param importObject The import objects.
     * @param logger The system logger.
     */
    function instantiate(bufferSource, importObject = {}, logger = console.log) {
        const env = new Environment(importObject, logger);
        return WebAssembly.instantiate(bufferSource, env.imports).then((result) => {
            return new Instance(result.module, {}, result.instance, env);
        });
    }

    /*
     * Licensed to the Apache Software Foundation (ASF) under one
     * or more contributor license agreements.  See the NOTICE file
     * distributed with this work for additional information
     * regarding copyright ownership.  The ASF licenses this file
     * to you under the Apache License, Version 2.0 (the
     * "License"); you may not use this file except in compliance
     * with the License.  You may obtain a copy of the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing,
     * software distributed under the License is distributed on an
     * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
     * KIND, either express or implied.  See the License for the
     * specific language governing permissions and limitations
     * under the License.
     */
    var RPCServerState;
    (function (RPCServerState) {
        RPCServerState[RPCServerState["InitHeader"] = 0] = "InitHeader";
        RPCServerState[RPCServerState["InitHeaderKey"] = 1] = "InitHeaderKey";
        RPCServerState[RPCServerState["InitServer"] = 2] = "InitServer";
        RPCServerState[RPCServerState["WaitForCallback"] = 3] = "WaitForCallback";
        RPCServerState[RPCServerState["ReceivePacketHeader"] = 4] = "ReceivePacketHeader";
        RPCServerState[RPCServerState["ReceivePacketBody"] = 5] = "ReceivePacketBody";
    })(RPCServerState || (RPCServerState = {}));
    /** RPC magic header */
    const RPC_MAGIC = 0xff271;
    /**
     * An utility class to read from binary bytes.
     */
    class ByteStreamReader {
        constructor(bytes) {
            this.offset = 0;
            this.bytes = bytes;
        }
        readU32() {
            const i = this.offset;
            const b = this.bytes;
            const val = b[i] | (b[i + 1] << 8) | (b[i + 2] << 16) | (b[i + 3] << 24);
            this.offset += 4;
            return val;
        }
        readU64() {
            const val = this.readU32();
            this.offset += 4;
            return val;
        }
        readByteArray() {
            const len = this.readU64();
            assert(this.offset + len <= this.bytes.byteLength);
            const ret = new Uint8Array(len);
            ret.set(this.bytes.slice(this.offset, this.offset + len));
            this.offset += len;
            return ret;
        }
    }
    /**
     * A websocket based RPC
     */
    class RPCServer {
        constructor(url, key, getImports, logger = console.log, ndarrayCacheUrl = "", ndarrayCacheDevice = "cpu", initProgressCallback = undefined, asyncOnServerLoad = undefined) {
            this.state = RPCServerState.InitHeader;
            this.pendingSend = Promise.resolve();
            this.inst = undefined;
            this.globalObjects = [];
            this.currPacketLength = 0;
            this.remoteKeyLength = 0;
            this.pendingBytes = 0;
            this.buffredBytes = 0;
            this.messageQueue = [];
            this.url = url;
            this.key = key;
            this.name = "WebSocketRPCServer[" + this.key + "]: ";
            this.getImports = getImports;
            this.logger = logger;
            this.ndarrayCacheUrl = ndarrayCacheUrl;
            this.ndarrayCacheDevice = ndarrayCacheDevice;
            this.initProgressCallback = initProgressCallback;
            this.asyncOnServerLoad = asyncOnServerLoad;
            this.checkLittleEndian();
            this.socket = createWebSocket(url);
            this.socket.binaryType = "arraybuffer";
            this.socket.addEventListener("open", (event) => {
                return this.onOpen(event);
            });
            this.socket.addEventListener("message", (event) => {
                return this.onMessage(event);
            });
            this.socket.addEventListener("close", (event) => {
                return this.onClose(event);
            });
        }
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        onClose(_event) {
            if (this.inst !== undefined) {
                this.globalObjects.forEach(obj => {
                    obj.dispose();
                });
                this.log(this.inst.runtimeStatsText());
                this.inst.dispose();
            }
            if (this.state == RPCServerState.ReceivePacketHeader) {
                this.log("Closing the server in clean state");
                this.log("Automatic reconnecting..");
                new RPCServer(this.url, this.key, this.getImports, this.logger, this.ndarrayCacheUrl, this.ndarrayCacheDevice, this.initProgressCallback, this.asyncOnServerLoad);
            }
            else {
                this.log("Closing the server, final state=" + this.state);
            }
        }
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        onOpen(_event) {
            // Send the headers
            let bkey = StringToUint8Array("server:" + this.key);
            bkey = bkey.slice(0, bkey.length - 1);
            const intbuf = new Int32Array(1);
            intbuf[0] = RPC_MAGIC;
            this.socket.send(intbuf);
            intbuf[0] = bkey.length;
            this.socket.send(intbuf);
            this.socket.send(bkey);
            this.log("connected...");
            // request bytes: magic + keylen
            this.requestBytes(4 /* SizeOf.I32 */ + 4 /* SizeOf.I32 */);
            this.state = RPCServerState.InitHeader;
        }
        /** Handler for raw message. */
        onMessage(event) {
            const buffer = event.data;
            this.buffredBytes += buffer.byteLength;
            this.messageQueue.push(new Uint8Array(buffer));
            this.processEvents();
        }
        /** Process ready events. */
        processEvents() {
            while (this.buffredBytes >= this.pendingBytes && this.pendingBytes != 0) {
                this.onDataReady();
            }
        }
        /** State machine to handle each request */
        onDataReady() {
            switch (this.state) {
                case RPCServerState.InitHeader: {
                    this.handleInitHeader();
                    break;
                }
                case RPCServerState.InitHeaderKey: {
                    this.handleInitHeaderKey();
                    break;
                }
                case RPCServerState.ReceivePacketHeader: {
                    this.currPacketHeader = this.readFromBuffer(8 /* SizeOf.I64 */);
                    const reader = new ByteStreamReader(this.currPacketHeader);
                    this.currPacketLength = reader.readU64();
                    assert(this.pendingBytes == 0);
                    this.requestBytes(this.currPacketLength);
                    this.state = RPCServerState.ReceivePacketBody;
                    break;
                }
                case RPCServerState.ReceivePacketBody: {
                    const body = this.readFromBuffer(this.currPacketLength);
                    assert(this.pendingBytes == 0);
                    assert(this.currPacketHeader !== undefined);
                    this.onPacketReady(this.currPacketHeader, body);
                    break;
                }
                case RPCServerState.WaitForCallback: {
                    assert(this.pendingBytes == 0);
                    break;
                }
                default: {
                    throw new Error("Cannot handle state " + this.state);
                }
            }
        }
        onPacketReady(header, body) {
            if (this.inst === undefined) {
                // initialize server.
                const reader = new ByteStreamReader(body);
                // eslint-disable-next-line @typescript-eslint/no-unused-vars
                reader.readU32();
                // eslint-disable-next-line @typescript-eslint/no-unused-vars
                Uint8ArrayToString(reader.readByteArray());
                const nargs = reader.readU32();
                const tcodes = [];
                const args = [];
                for (let i = 0; i < nargs; ++i) {
                    tcodes.push(reader.readU32());
                }
                for (let i = 0; i < nargs; ++i) {
                    const tcode = tcodes[i];
                    if (tcode == 11 /* ArgTypeCode.TVMStr */) {
                        const str = Uint8ArrayToString(reader.readByteArray());
                        args.push(str);
                    }
                    else if (tcode == 12 /* ArgTypeCode.TVMBytes */) {
                        args.push(reader.readByteArray());
                    }
                    else {
                        throw new Error("cannot support type code " + tcode);
                    }
                }
                this.onInitServer(args, header, body);
            }
            else {
                assert(this.serverRecvData !== undefined);
                this.serverRecvData(header, body);
                this.requestBytes(8 /* SizeOf.I64 */);
                this.state = RPCServerState.ReceivePacketHeader;
            }
        }
        /** Event handler during server initialization. */
        onInitServer(args, header, body) {
            // start the server
            assert(args[0] == "rpc.WasmSession");
            assert(this.pendingBytes == 0);
            const asyncInitServer = () => __awaiter(this, void 0, void 0, function* () {
                assert(args[1] instanceof Uint8Array);
                const inst = yield instantiate(args[1].buffer, this.getImports(), this.logger);
                try {
                    const output = yield detectGPUDevice();
                    if (output !== undefined) {
                        const label = "WebGPU: " + output.adapterInfo.description;
                        this.log("Initialize GPU device: " + label);
                        inst.initWebGPU(output.device);
                    }
                    else {
                        this.log("Cannot find WebGPU device in the env");
                    }
                }
                catch (err) {
                    this.log("Cannnot initialize WebGPU, " + err.toString());
                }
                this.inst = inst;
                // begin scope to allow handling of objects
                this.inst.beginScope();
                if (this.initProgressCallback !== undefined) {
                    this.inst.registerInitProgressCallback(this.initProgressCallback);
                }
                if (this.ndarrayCacheUrl.length != 0) {
                    if (this.ndarrayCacheDevice == "cpu") {
                        yield this.inst.fetchNDArrayCache(this.ndarrayCacheUrl, this.inst.cpu());
                    }
                    else {
                        assert(this.ndarrayCacheDevice == "webgpu");
                        yield this.inst.fetchNDArrayCache(this.ndarrayCacheUrl, this.inst.webgpu());
                    }
                }
                assert(this.inst !== undefined);
                if (this.asyncOnServerLoad !== undefined) {
                    yield this.asyncOnServerLoad(this.inst);
                }
                const fcreate = this.inst.getGlobalFunc("rpc.CreateEventDrivenServer");
                const messageHandler = fcreate((cbytes) => {
                    assert(this.inst !== undefined);
                    if (this.socket.readyState == 1) {
                        // WebSocket will automatically close the socket
                        // if we burst send data that exceeds its internal buffer
                        // wait a bit before we send next one.
                        const sendDataWithCongestionControl = () => __awaiter(this, void 0, void 0, function* () {
                            const packetSize = 4 << 10;
                            const maxBufferAmount = 4 * packetSize;
                            const waitTimeMs = 20;
                            for (let offset = 0; offset < cbytes.length; offset += packetSize) {
                                const end = Math.min(offset + packetSize, cbytes.length);
                                while (this.socket.bufferedAmount >= maxBufferAmount) {
                                    yield new Promise((r) => setTimeout(r, waitTimeMs));
                                }
                                this.socket.send(cbytes.slice(offset, end));
                            }
                        });
                        // Chain up the pending send so that the async send is always in-order.
                        this.pendingSend = this.pendingSend.then(sendDataWithCongestionControl);
                        // Directly return since the data are "sent" from the caller's pov.
                        return this.inst.scalar(cbytes.length, "int32");
                    }
                    else {
                        return this.inst.scalar(0, "int32");
                    }
                }, this.name, this.key);
                // message handler should persist across RPC runs
                this.globalObjects.push(this.inst.detachFromCurrentScope(messageHandler));
                const writeFlag = this.inst.scalar(3, "int32");
                this.serverRecvData = (header, body) => {
                    if (messageHandler(header, writeFlag) == 0) {
                        this.socket.close();
                    }
                    if (messageHandler(body, writeFlag) == 0) {
                        this.socket.close();
                    }
                };
                // Forward the same init sequence to the wasm RPC.
                // The RPC will look for "rpc.wasmSession"
                // and we will redirect it to the correct local session.
                // register the callback to redirect the session to local.
                const flocal = this.inst.getGlobalFunc("wasm.LocalSession");
                const localSession = flocal();
                assert(localSession instanceof Module);
                // eslint-disable-next-line @typescript-eslint/no-unused-vars
                this.inst.registerFunc("rpc.WasmSession", 
                // eslint-disable-next-line @typescript-eslint/no-unused-vars
                (_args) => {
                    return localSession;
                });
                messageHandler(header, writeFlag);
                messageHandler(body, writeFlag);
                this.log("Finish initializing the Wasm Server..");
                this.requestBytes(8 /* SizeOf.I64 */);
                this.state = RPCServerState.ReceivePacketHeader;
                // call process events in case there are bufferred data.
                this.processEvents();
                // recycle all values.
                this.inst.endScope();
            });
            this.state = RPCServerState.WaitForCallback;
            asyncInitServer();
        }
        log(msg) {
            this.logger(this.name + msg);
        }
        handleInitHeader() {
            const reader = new ByteStreamReader(this.readFromBuffer(4 /* SizeOf.I32 */ * 2));
            const magic = reader.readU32();
            if (magic == RPC_MAGIC + 1) {
                throw new Error("key: " + this.key + " has already been used in proxy");
            }
            else if (magic == RPC_MAGIC + 2) {
                throw new Error("RPCProxy do not have matching client key " + this.key);
            }
            assert(magic == RPC_MAGIC, this.url + " is not an RPC Proxy");
            this.remoteKeyLength = reader.readU32();
            assert(this.pendingBytes == 0);
            this.requestBytes(this.remoteKeyLength);
            this.state = RPCServerState.InitHeaderKey;
        }
        handleInitHeaderKey() {
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            Uint8ArrayToString(this.readFromBuffer(this.remoteKeyLength));
            assert(this.pendingBytes == 0);
            this.requestBytes(8 /* SizeOf.I64 */);
            this.state = RPCServerState.ReceivePacketHeader;
        }
        checkLittleEndian() {
            const a = new ArrayBuffer(4);
            const b = new Uint8Array(a);
            const c = new Uint32Array(a);
            b[0] = 0x11;
            b[1] = 0x22;
            b[2] = 0x33;
            b[3] = 0x44;
            assert(c[0] === 0x44332211, "RPCServer little endian to work");
        }
        requestBytes(nbytes) {
            this.pendingBytes += nbytes;
        }
        readFromBuffer(nbytes) {
            const ret = new Uint8Array(nbytes);
            let ptr = 0;
            while (ptr < nbytes) {
                assert(this.messageQueue.length != 0);
                const nleft = nbytes - ptr;
                if (this.messageQueue[0].byteLength <= nleft) {
                    const buffer = this.messageQueue.shift();
                    ret.set(buffer, ptr);
                    ptr += buffer.byteLength;
                }
                else {
                    const buffer = this.messageQueue[0];
                    ret.set(buffer.slice(0, nleft), ptr);
                    this.messageQueue[0] = buffer.slice(nleft, buffer.byteLength);
                    ptr += nleft;
                }
            }
            this.buffredBytes -= nbytes;
            this.pendingBytes -= nbytes;
            return ret;
        }
    }

    exports.ArtifactCache = ArtifactCache;
    exports.DLDataType = DLDataType;
    exports.DLDevice = DLDevice;
    exports.Instance = Instance;
    exports.Module = Module;
    exports.NDArray = NDArray;
    exports.RPCServer = RPCServer;
    exports.Scalar = Scalar;
    exports.TVMArray = TVMArray;
    exports.TVMObject = TVMObject;
    exports.VirtualMachine = VirtualMachine;
    exports.assert = assert;
    exports.createPolyfillWASI = createPolyfillWASI;
    exports.detectGPUDevice = detectGPUDevice;
    exports.instantiate = instantiate;
    exports.wasmPath = wasmPath;

    Object.defineProperty(exports, '__esModule', { value: true });

}));
