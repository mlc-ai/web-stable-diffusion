"""Testing utilities through rpc."""
import os
import tvm
import numpy as np

from tvm import relax, rpc

try:
    import torch
except ImportError:
    pass


class RPCBaseDebugSession:
    """A helper class to create debug sessions through rpc.

    Parameters
    ----------
    remote: RPCSession
        The input rpc session.

    rt_mod: runtime.Module
        Runtime module that loads the VM

    device: runtime.Device
        Device to run the vm on.
    """

    def __init__(self, remote, rt_mod, device):
        self.remote = remote
        self.vm = relax.VirtualMachine(rt_mod, device)
        self.device = device

    def get_wrapper(self, func_name, nparam_cached=0, time_eval=False):
        """Get remote debug wrapper.

        Parameters
        ----------
        func_name: str
            The function name

        nparam_cached: int
            Number of extra parameters

        time_eval: bool
            Whether perform time eval

        Returns
        -------
        wrapper: Callable
            The callable that can be used to run related items.
        """
        pfunc = None
        if nparam_cached != 0:
            pfunc_from_cache = self.remote.get_function("tvmjs.param_module_from_cache")
            pfunc = pfunc_from_cache(func_name, nparam_cached)

        if isinstance(time_eval, dict):
            time_eval_kwargs = time_eval
        else:
            time_eval_kwargs = {} if time_eval else None

        time_eval_result = []

        def wrapped_f(*args):
            new_args = []
            ret_kind = None
            ret_device = None

            for arg in args:
                if isinstance(arg, tvm.nd.NDArray):
                    ret_kind = tvm.nd.NDArray
                    ret_device = arg.device
                    if arg.device != self.device:
                        arg = arg.copyto(tvm.cpu()).copyto(self.device)
                elif isinstance(arg, np.ndarray):
                    ret_kind = np.ndarray
                    arg = tvm.nd.array(arg, self.device)
                elif isinstance(arg, torch.Tensor):
                    ret_kind = torch.Tensor
                    ret_device = arg.device
                    arg = tvm.nd.array(arg.numpy(), self.device)
                new_args.append(arg)
            if pfunc:
                new_args.append(pfunc)

            if pfunc:
                self.vm.module["set_input_with_param_module"](func_name, *new_args)
            else:
                self.vm.module["set_input"](func_name, *new_args)

            self.vm.invoke_stateful(func_name)
            if time_eval_kwargs is not None and len(time_eval_result) == 0:
                res = self.vm.time_evaluator("invoke_stateful", self.device)(
                    func_name, **time_eval_kwargs
                )
                time_eval_result.append(res)
                print(f"Remote[{func_name}] on {self.devcice}, {res}")

            outputs = self.vm.get_outputs(func_name)

            def _convert_return(data):
                if isinstance(data, (tvm.ir.Array, list, tuple)):
                    return [_convert_return(x) for x in data]
                if not isinstance(data, tvm.nd.NDArray):
                    return data
                if ret_kind == tvm.nd.NDArray:
                    if ret_device == data.device:
                        return data
                    return data.copyto(tvm.cpu()).copyto(ret_device)
                if ret_kind == torch.Tensor:
                    return torch.from_numpy(data.numpy()).to(ret_device)
                if ret_kind == np.ndarray:
                    return data.numpy()
                raise ValueError(f"Unknown ret kind {ret_kind}")

            return _convert_return(outputs)

        return wrapped_f


class WebGPUDebugSession(RPCBaseDebugSession):
    """Remote debug session to handle webgpu.

    Parameters
    ----------
    wasm_path: str
        The path to the wasm.
    """

    def __init__(self, wasm_path):
        proxy_host = os.environ.get("TVM_RPC_PROXY_HOST", "127.0.0.1")
        proxy_port = int(os.environ.get("TVM_RPC_PROXY_PORT", "9090"))
        wasm_binary = open(wasm_path, "rb").read()
        remote = rpc.connect(
            proxy_host,
            proxy_port,
            key="wasm",
            session_constructor_args=["rpc.WasmSession", wasm_binary],
        )
        super(WebGPUDebugSession, self).__init__(
            remote, remote.system_lib(), remote.webgpu()
        )
