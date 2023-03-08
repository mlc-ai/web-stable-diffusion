# Web Stable Diffusion

This project brings stable diffusion models onto web browsers. **Everything runs inside the browser with no server support.** To our knowledge, this is the the world’s first stable diffusion completely running on the browser. Please checkout our [demo webpage](https://mlc.ai/web-stable-diffusion/#text-to-image-generation-demo) to try it out.

<img src="site/img/fig/browser-screenshot.png" alt="Browser screenshot"/>

We have been seeing amazing progress through AI models recently. Thanks to the open-source effort, developers can now easily compose open-source models together to produce amazing tasks. Stable diffusion enables the automatic creation of photorealistic images as well as images in various styles based on text input. These models are usually big and compute-heavy, which means we have to pipe through all computation requests to (GPU) servers when developing web applications based on these models. Additionally, most of the workloads have to run on a specific type of GPUs where popular deep-learning frameworks are readily available.

This project takes a step to change that status quo and bring more diversity to the ecosystem. There are a lot of reasons to get some (or all) of the computation to the client side. There are many possible benefits, such as cost reduction on the service provider side, as well as an enhancement for personalization and privacy protection. The development of personal computers (even mobile devices) is going in the direction that enables such possibilities. The client side is getting pretty powerful. For example, the latest MacBook Pro can have up to 96GB of unified RAM that can be used to store the model weights and a reasonably powerful GPU to run many of the workloads.

Building special client apps for those applications is one option (which we also support), but won’t it be even more amazing if we can simply open a browser and directly bring AI natively to your browser tab? There is some level of readiness in the ecosystem. WebAssembly allows us to port more lower-level runtimes onto the web. To solve the compute problem, WebGPU is getting matured lately and enables native GPU executions on the browser.

We are just seeing necessary elements coming together on the client side, both in terms of hardware and browser ecosystem. Still, there are big hurdles to cross, to name a few:
* We need to bring the models somewhere without the relevant GPU-accelerated Python frameworks.
* Most of the AI frameworks have a heavy reliance on optimized computed libraries that are maintained by hardware vendors. We need to start from zero. To get the maximum benefit, we might also need to produce variants per client environment.
* Careful planning of memory usage so we can fit the models into memory.

We do not want to only do it for just one model. Instead, we would like to present a repeatable, hackable, composable workflow that enables anyone to easily develop and optimize these models in a **Python-first** environment and universally **deploy** them everywhere, including the web.

## Get Started

We will later soon update a Jupyter notebook that guides through how to build locally and deploy the stable diffusion model with local GPU runtime.

## How?

The key technology here is machine learning compilation (MLC). Our solution is built on the shoulders of the open-source ecosystem, including PyTorch, Hugging Face diffusers and tokenizers, rust, wasm, and WebGPU. The main flow is built on Apache TVM Unity, an exciting ongoing development in the [Apache TVM Community](https://tvm.apache.org/)

- We take [Runway’s stable diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main) models from the Hugging Face diffuser library.
- We use [TorchDynamo](https://pytorch.org/tutorials/intermediate/dynamo_tutorial.html) and [Torch FX](https://pytorch.org/docs/stable/fx.html) to capture key model components into an IRModule in TVM.
- Each function in TVM’s IRModule can be further transformed and generated with runnable code that can be deployed universally on any environment supported by minimum TVM runtime (javascript being one of them).
- [TensorIR](https://arxiv.org/abs/2207.04296) and [MetaSchedule](https://arxiv.org/abs/2205.13603) are used to build automated solutions to generate optimized programs. These transformations are tuned on a specific device through native GPU runtimes and then used to generate optimized GPU shaders. We provide a database that records these transformations so new builds can be done without tuning.
- We build static memory planning optimizations to reuse memory across multiple layers.
- We use [Emscripten](https://emscripten.org/) and typescript to build a TVM web runtime that can deploy generated modules.
- We also leverage the [wasm port](https://blog.mithrilsecurity.io/porting-tokenizers-to-wasm/) of the [rust tokenizers library](https://github.com/huggingface/tokenizers) from hugging face.

![workflow](site/img/fig/workflow.svg)

All parts of this workflow are done in Python, except, of course, the last part which builds a 400-loc JavaScript app that connects things together. This is also a fun process of interactive development, bringing new models.

All these are made possible by the open-source ecosystem that we leverage. Specifically, we make heavy use of [TVM Unity](https://discuss.tvm.apache.org/t/establish-tvm-unity-connection-a-technical-strategy/13344), an exciting latest development in the TVM project that enables such Python-first interactive MLC development experiences which allows us to easily compose new optimizations, all in Python, and incrementally bring our app to the web. TVM Unity also provides an easy way to compose new solutions in the ecosystem. For example, we can bring in other WebGPU shader generators or shader libraries easily to this workflow in the future.

## Comparison with Native GPU Runtime, Limitations, and Opportunities

Besides the WebGPU runtime, we also provide options for native deployment with local GPU runtime. These options can be used both as a tool to deploy on a native environment as well as a reference point to compare native GPU driver performance and WebGPU.

WebGPU works by translating WGSL (WebGPU Shading Language) shaders to native shaders. So, in theory, we can reach zero gaps between the WebGPU runtime and the native environment. If we directly use Chrome to check the current demo on Apple silicon, however, we can find a performance degradation (about 3x). This is because Chrome’s WebGPU implementation inserts bound clips for all array index access, such that `a[i]` becomes `a[min(i, a.size)]`. Ideally, downstream shader compilers should be able to optimize the bound clipping out, but here unfortunately, it is not the case. This gap can be fixed once WebGPU implementation becomes more mature, checks the index access range, and drops such clipping.

You can get around this by using a special flag to launch Chrome (thanks to Dawn developers for providing the pointers), by exiting Chrome completely, then in the command line, type
```shell
/path/to/chrome-canary --enable-dawn-features=disable_robustness
```
Then you will find that the execution speed is as fast as the native GPU environment. We anticipate this problem will get resolved as WebGPU matures.

We are just seeing the dawn of what we believe to be an eruption. WebGPU is still evolving (though it is getting close to shipping this year), and only available through Chrome Canary, and can be unstable. It also still comes with limitations, such as only support for FP32 (FP16 shader extension is on the spec but not yet implemented). The stable diffusion here would require a GPU with a decent amount of RAM (8GB). We have only tested our solution through Apple silicons so far. There are also opportunities to support advanced optimizations such as [FlashAttention](https://arxiv.org/abs/2205.14135) and quantization to further improve the performance of the system.

These are opportunities to bring several times of performance improvements to the current solutions. We believe many of them can be tackled in the near future. A single component of this solution can still be useful. For example, one can choose just to deploy the text encoder part of the model. Additionally, the same Python-first development, universal deployment workflow can be used to bring ML models to other environments, such as new hardware or mobile cases. Finally, the same machine learning compilation stack is also shared with server class use cases and can be used to optimize server workloads as well.

## Acknowledgement

This project is made possible thanks to collaboration with

<a href="https://www.scs.cmu.edu">
<img src="site/img/logo/cmuscs.png" alt="CMU School of Computer Science" height="50"/>
</a>
<a href="https://catalyst.cs.cmu.edu">
<img src="site/img/logo/catalyst.svg" alt="Catalyst" height="50"/>
</a>
<a href="https://mlc.ai">
<img src="site/img/logo/mlc-logo-with-text-landscape.svg" alt="MLC" height="50"/>
</a>
<a href="https://octoml.ai">
<img src="site/img/logo/octoml.png" alt="OctoML" height="50"/>
</a>

This project is only possible thanks to the shoulders open-source ecosystems that we stand on. We want to thank the Apache TVM community and developers of the TVM Unity effort. We want to thank the open-source ML community members who make these models publicly available, and PyTorch, Hugging Face communities that make these models accessible. We would like to thank the tokenizer wasm port by Mithril Security. We also would like to thank the WebAssembly, Emscripten, Rust, and WebGPU communities. Finally, thanks to Dawn developers, who provide timely answers to questions on Chrome.
