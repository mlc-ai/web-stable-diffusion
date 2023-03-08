/* tslint:disable */
/* eslint-disable */
/**
*/
export class EncodingWasm {
  free(): void;
/**
*/
  readonly input_ids: Uint32Array;
/**
*/
  readonly tokens: Array<any>;
}
/**
*/
export class TokenizerWasm {
  free(): void;
/**
* @param {string} json
*/
  constructor(json: string);
/**
* @param {string} text
* @param {boolean} add_special_tokens
* @returns {EncodingWasm}
*/
  encode(text: string, add_special_tokens: boolean): EncodingWasm;
}

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly __wbg_tokenizerwasm_free: (a: number) => void;
  readonly tokenizerwasm_from_buffer: (a: number, b: number) => number;
  readonly tokenizerwasm_encode: (a: number, b: number, c: number, d: number) => number;
  readonly __wbg_encodingwasm_free: (a: number) => void;
  readonly encodingwasm_get_ids: (a: number) => number;
  readonly encodingwasm_get_tokens: (a: number) => number;
  readonly __wbindgen_malloc: (a: number) => number;
  readonly __wbindgen_realloc: (a: number, b: number, c: number) => number;
  readonly __wbindgen_exn_store: (a: number) => void;
}

export type SyncInitInput = BufferSource | WebAssembly.Module;
/**
* Instantiates the given `module`, which can either be bytes or
* a precompiled `WebAssembly.Module`.
*
* @param {SyncInitInput} module
*
* @returns {InitOutput}
*/
export function initSync(module: SyncInitInput): InitOutput;

/**
* If `module_or_path` is {RequestInfo} or {URL}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {InitInput | Promise<InitInput>} module_or_path
*
* @returns {Promise<InitOutput>}
*/
export default function init (module_or_path?: InitInput | Promise<InitInput>): Promise<InitOutput>;
