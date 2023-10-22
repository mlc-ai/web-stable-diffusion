from tvm.script import ir as I
from tvm.script import tir as T
from tvm.script import relax as R
import tvm

metadata = tvm.ir.load_json("""{
  \"root\": 1, 
  \"nodes\": [
    {
      \"type_key\": \"\"
    }, 
    {
      \"type_key\": \"Map\", 
      \"keys\": [
        \"relax.expr.Constant\"
      ], 
      \"data\": [2]
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [3, 14]
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"13\", 
        \"data\": \"0\", 
        \"span\": \"0\", 
        \"struct_info_\": \"4\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"float32\", 
        \"ndim\": \"4\", 
        \"shape\": \"5\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"12\", 
        \"span\": \"0\", 
        \"struct_info_\": \"11\", 
        \"values\": \"6\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [7, 8, 9, 10]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"77\"
      }
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"77\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"4\", 
        \"span\": \"0\", 
        \"values\": \"6\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"4\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"float32\", 
        \"ndim\": \"4\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"22\", 
        \"data\": \"1\", 
        \"span\": \"0\", 
        \"struct_info_\": \"15\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"float32\", 
        \"ndim\": \"2\", 
        \"shape\": \"16\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"21\", 
        \"span\": \"0\", 
        \"struct_info_\": \"20\", 
        \"values\": \"17\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [18, 19]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"160\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"2\", 
        \"span\": \"0\", 
        \"values\": \"17\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"2\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"float32\", 
        \"ndim\": \"2\", 
        \"span\": \"0\"
      }
    }
  ], 
  \"b64ndarrays\": [
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAABAAAAAIgAQABAAAAAAAAAAEAAAAAAAAATQAAAAAAAABNAAAAAAAAAKRcAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9/////f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3////9//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f////3//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//f/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAgAAAAIgAQABAAAAAAAAAKAAAAAAAAAAgAIAAAAAAAAAAIA/+a1xPwUpZD+sZVc/GFlLPxH5Pz/vOzU/lhgrP2yGIT9QfRg/mvUPPwvoBz/PTQA/4UDyPrez5D6a6Nc+tNTLPsJtwD4ZqrU+l4CrPpvooT4C2pg+HE2QPqg6iD7Mm4A+ItRyPro+ZT7Ya1g+nFBMPrviQD6HGDY+1ugrPgZLIj7sNhk+0qQQPneNCD756QA+wGfzPRTK5T1o79g9zMzMPflXwT03h7Y9VVGsPa2toj0NlJk9wPyQPXjgiD1XOIE9s/tzPcFVZj1Ec1k9SUlNPYHNQT0q9jY9FbosPZIQIz1p8Rk94VQRPaozCT3ihgE9BJD0PMLh5jxx99k8FMbNPFFDwjxjZbc8EyOtPK1zozz7Tpo8Oa2RPBKHiTyd1YE8qCR1PCBuZzzxe1o8J0NOPGO5Qjzf1Dc8U4wtPArXIzzHrBo8wwUSPKzaCTyKJAI8rbn1O8j65zvCANs7isDOO8IvwzuaRLg7zfWtO6M6pDvOCps7iF6SO3Uuijunc4I7Dk92O82HaDvdhVs7Mz5PO2mmQzuetDg7jV8uO3OeJDsNaRs7grcSO3WCCjvwwgI7weT2OigV6TpQC9w6NbzPOlkdxDrmJLk6iMmuOoUCpTqCx5s6rhCTOqjWijpuEoM633p3OtmiaToTkVw6cDpQOoqURDptlTk6yTMvOtVmJTo1Jhw6GWoTOg8rCzobYgM6QRH4Odkw6jkhF905BbnQOQsMxTk+Bro5UJ6vOWHLpTkhhZw5scOTOaR/izn1sYM5Dah4OS6/ajmPnV057TdROdODRTlTdzo5DAkwOSUwJjlC5Bw5gB0UOW3UCzkIAgQ5PT/5OOpN6zhAJN44\"
  ], 
  \"attrs\": {\"tvm_version\": \"0.14.dev0\"}
}""")


@I.ir_module
class Module:
    @T.prim_func(private=True)
    def add(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_add: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3], B[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = A[v_ax0, v_ax1, v_ax2, v_ax3] + B[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def concatenate(A: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), B: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(77), T.int64(768)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(B[v_ax0 - T.int64(1), v_ax1, v_ax2], A[v_ax0, v_ax1, v_ax2])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2])
                T_concat[v_ax0, v_ax1, v_ax2] = T.if_then_else(T.int64(1) <= v_ax0, B[v_ax0 - T.int64(1), v_ax1, v_ax2], A[v_ax0, v_ax1, v_ax2])

    @T.prim_func(private=True)
    def concatenate1(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0 - T.int64(1), v_ax1, v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(1) <= v_ax0, B[v_ax0 - T.int64(1), v_ax1, v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate10(A: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(320), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(320) <= v_ax1, B[v_ax0, v_ax1 - T.int64(320), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate3(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), B: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(2560), T.int64(8), T.int64(8)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(1280) <= v_ax1, B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate4(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), B: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(2560), T.int64(16), T.int64(16)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(1280) <= v_ax1, B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate5(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), B: T.Buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1920), T.int64(16), T.int64(16)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(1280) <= v_ax1, B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate6(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32"), B: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1920), T.int64(32), T.int64(32)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(1280) <= v_ax1, B[v_ax0, v_ax1 - T.int64(1280), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate7(A: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), B: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(640), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(640) <= v_ax1, B[v_ax0, v_ax1 - T.int64(640), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate8(A: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), B: T.Buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(960), T.int64(32), T.int64(32)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(640), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(640) <= v_ax1, B[v_ax0, v_ax1 - T.int64(640), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def concatenate9(A: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), T_concat: T.Buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(960), T.int64(64), T.int64(64)):
            with T.block("T_concat"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[v_ax0, v_ax1 - T.int64(640), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_concat[v_ax0, v_ax1, v_ax2, v_ax3])
                T_concat[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(640) <= v_ax1, B[v_ax0, v_ax1 - T.int64(640), v_ax2, v_ax3], A[v_ax0, v_ax1, v_ax2, v_ax3])

    @T.prim_func(private=True)
    def divide(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((), "float32"), T_divide: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3], B[()])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = A[v_ax0, v_ax1, v_ax2, v_ax3] / B[()]

    @T.prim_func(private=True)
    def divide1(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_divide: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = A[v_ax0, v_ax1, v_ax2, v_ax3] * T.float32(0.083333333333333329)

    @T.prim_func(private=True)
    def divide2(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_divide: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = A[v_ax0, v_ax1, v_ax2, v_ax3] * T.float32(0.5)

    @T.prim_func(private=True)
    def fused_broadcast_to1_strided_slice_reshape20_cast3_multiply11_multiply12_tir_sin_tir_cos_concatenate2_strided_slice1_reshape21_strided_slice2_reshape21_concatenate2(inp_1: T.Buffer((), "int32"), param_0: T.Buffer((T.int64(1), T.int64(160)), "float32"), var_T_concat_intermediate: T.Buffer((T.int64(2), T.int64(320)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_broadcast_to_intermediate = T.alloc_buffer((T.int64(2),), "int32")
        var_T_strided_slice_with_axes_intermediate = T.alloc_buffer((T.int64(2),), "int32")
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1)), "int32")
        var_compute_intermediate = T.alloc_buffer((T.int64(2), T.int64(1)))
        var_T_multiply_intermediate = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_T_multiply_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_compute_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_compute_intermediate_2 = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_T_concat_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(320)))
        var_T_strided_slice_with_axes_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_T_strided_slice_with_axes_intermediate_2 = T.alloc_buffer((T.int64(2), T.int64(160)))
        var_T_reshape_intermediate_2 = T.alloc_buffer((T.int64(2), T.int64(160)))
        for ax0 in range(T.int64(2)):
            with T.block("T_broadcast_to"):
                v_ax0 = T.axis.spatial(T.int64(2), ax0)
                T.reads(inp_1[()])
                T.writes(var_T_broadcast_to_intermediate[v_ax0])
                var_T_broadcast_to_intermediate[v_ax0] = inp_1[()]
        for ax0 in range(T.int64(2)):
            with T.block("T_strided_slice_with_axes"):
                v_ax0 = T.axis.spatial(T.int64(2), ax0)
                T.reads(var_T_broadcast_to_intermediate[v_ax0])
                T.writes(var_T_strided_slice_with_axes_intermediate[v_ax0])
                var_T_strided_slice_with_axes_intermediate[v_ax0] = var_T_broadcast_to_intermediate[v_ax0]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_strided_slice_with_axes_intermediate[(v_ax0 + v_ax1) % T.int64(2)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1])
                var_T_reshape_intermediate[v_ax0, v_ax1] = var_T_strided_slice_with_axes_intermediate[(v_ax0 + v_ax1) % T.int64(2)]
        for i0, i1 in T.grid(T.int64(2), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1 = T.axis.remap("SS", [i0, i1])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1])
                T.writes(var_compute_intermediate[v_i0, v_i1])
                var_compute_intermediate[v_i0, v_i1] = T.Cast("float32", var_T_reshape_intermediate[v_i0, v_i1])
        for ax0, ax1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("T_multiply"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_compute_intermediate[v_ax0, T.int64(0)], param_0[T.int64(0), v_ax1])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1])
                var_T_multiply_intermediate[v_ax0, v_ax1] = var_compute_intermediate[v_ax0, T.int64(0)] * param_0[T.int64(0), v_ax1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("T_multiply_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_multiply_intermediate[v_ax0, v_ax1])
                T.writes(var_T_multiply_intermediate_1[v_ax0, v_ax1])
                var_T_multiply_intermediate_1[v_ax0, v_ax1] = var_T_multiply_intermediate[v_ax0, v_ax1]
        for i0, i1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("compute_1"):
                v_i0, v_i1 = T.axis.remap("SS", [i0, i1])
                T.reads(var_T_multiply_intermediate_1[v_i0, v_i1])
                T.writes(var_compute_intermediate_1[v_i0, v_i1])
                var_compute_intermediate_1[v_i0, v_i1] = T.sin(var_T_multiply_intermediate_1[v_i0, v_i1])
        for i0, i1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("compute_2"):
                v_i0, v_i1 = T.axis.remap("SS", [i0, i1])
                T.reads(var_T_multiply_intermediate_1[v_i0, v_i1])
                T.writes(var_compute_intermediate_2[v_i0, v_i1])
                var_compute_intermediate_2[v_i0, v_i1] = T.cos(var_T_multiply_intermediate_1[v_i0, v_i1])
        for ax0, ax1 in T.grid(T.int64(2), T.int64(320)):
            with T.block("T_concat"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_compute_intermediate_2[v_ax0, v_ax1 - T.int64(160)], var_compute_intermediate_1[v_ax0, v_ax1])
                T.writes(var_T_concat_intermediate_1[v_ax0, v_ax1])
                var_T_concat_intermediate_1[v_ax0, v_ax1] = T.if_then_else(T.int64(160) <= v_ax1, var_compute_intermediate_2[v_ax0, v_ax1 - T.int64(160)], var_compute_intermediate_1[v_ax0, v_ax1])
        for ax0, ax1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("T_strided_slice_with_axes_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_concat_intermediate_1[v_ax0, v_ax1 + T.int64(160)])
                T.writes(var_T_strided_slice_with_axes_intermediate_1[v_ax0, v_ax1])
                var_T_strided_slice_with_axes_intermediate_1[v_ax0, v_ax1] = var_T_concat_intermediate_1[v_ax0, v_ax1 + T.int64(160)]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_strided_slice_with_axes_intermediate_1[(v_ax1 // T.int64(160) + v_ax0) % T.int64(2), v_ax1 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1])
                var_T_reshape_intermediate_1[v_ax0, v_ax1] = var_T_strided_slice_with_axes_intermediate_1[(v_ax1 // T.int64(160) + v_ax0) % T.int64(2), v_ax1 % T.int64(160)]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("T_strided_slice_with_axes_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_concat_intermediate_1[v_ax0, v_ax1])
                T.writes(var_T_strided_slice_with_axes_intermediate_2[v_ax0, v_ax1])
                var_T_strided_slice_with_axes_intermediate_2[v_ax0, v_ax1] = var_T_concat_intermediate_1[v_ax0, v_ax1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(160)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_strided_slice_with_axes_intermediate_2[(v_ax1 // T.int64(160) + v_ax0) % T.int64(2), v_ax1 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_2[v_ax0, v_ax1])
                var_T_reshape_intermediate_2[v_ax0, v_ax1] = var_T_strided_slice_with_axes_intermediate_2[(v_ax1 // T.int64(160) + v_ax0) % T.int64(2), v_ax1 % T.int64(160)]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(320)):
            with T.block("T_concat_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_reshape_intermediate_2[v_ax0, v_ax1 - T.int64(160)], var_T_reshape_intermediate_1[v_ax0, v_ax1])
                T.writes(var_T_concat_intermediate[v_ax0, v_ax1])
                var_T_concat_intermediate[v_ax0, v_ax1] = T.if_then_else(T.int64(160) <= v_ax1, var_T_reshape_intermediate_2[v_ax0, v_ax1 - T.int64(160)], var_T_reshape_intermediate_1[v_ax0, v_ax1])

    @T.prim_func(private=True)
    def fused_conv2d10_add11(lv207: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_3_resnets_1_conv1_weight: T.Buffer((T.int64(128), T.int64(128), T.int64(3), T.int64(3)), "float32"), lv209: T.Buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(514), T.int64(514)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(514), T.int64(514)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv207[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(513) and T.int64(1) <= v_i3 and v_i3 < T.int64(513), lv207[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512), T.int64(128), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_3_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_3_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv209[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv209[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d10_add11_add12_divide7(lv197: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_3_resnets_0_conv2_weight: T.Buffer((T.int64(128), T.int64(128), T.int64(3), T.int64(3)), "float32"), lv199: T.Buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)), "float32"), lv203: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(514), T.int64(514)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(514), T.int64(514)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv197[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(513) and T.int64(1) <= v_i3 and v_i3 < T.int64(513), lv197[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512), T.int64(128), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_3_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_3_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv199[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv199[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv203[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv203[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d11_add11(lv190: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_3_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(128), T.int64(256), T.int64(1), T.int64(1)), "float32"), lv202: T.Buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv190[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv190[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_3_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_3_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv202[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv202[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d12_add13_divide8_add14_tir_clip(lv231: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32"), vae_decoder_conv_out_weight: T.Buffer((T.int64(3), T.int64(128), T.int64(3), T.int64(3)), "float32"), lv233: T.Buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)), "float32"), var_compute_intermediate: T.Buffer((T.int64(1), T.int64(3), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(514), T.int64(514)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(512), T.int64(512)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(512), T.int64(512)))
        var_T_divide_intermediate = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(512), T.int64(512)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(512), T.int64(512)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(514), T.int64(514)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv231[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(513) and T.int64(1) <= v_i3 and v_i3 < T.int64(513), lv231[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(3), T.int64(512), T.int64(512), T.int64(128), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_conv_out_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_conv_out_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(512), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv233[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv233[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(512), T.int64(512)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * T.float32(0.5)
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(512), T.int64(512)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(0.5)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(3), T.int64(512), T.int64(512)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_add_intermediate_1[v_i0, v_i1, v_i2, v_i3])
                T.writes(var_compute_intermediate[v_i0, v_i1, v_i2, v_i3])
                var_compute_intermediate[v_i0, v_i1, v_i2, v_i3] = T.max(T.min(var_T_add_intermediate_1[v_i0, v_i1, v_i2, v_i3], T.float32(1)), T.float32(0))

    @T.prim_func(private=True)
    def fused_conv2d13_add21(lv: T.Buffer((T.int64(2), T.int64(4), T.int64(64), T.int64(64)), "float32"), unet_conv_in_weight: T.Buffer((T.int64(320), T.int64(4), T.int64(3), T.int64(3)), "float32"), lv23: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(4), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(4), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(4), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_conv_in_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_conv_in_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv23[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv23[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d14_add21_add23(lv26: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_down_blocks_0_resnets_0_conv1_weight: T.Buffer((T.int64(320), T.int64(320), T.int64(3), T.int64(3)), "float32"), lv28: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv35: T.Buffer((T.int64(2), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv26[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv26[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(320), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_0_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_0_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv28[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv28[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv35[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv35[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d14_add21_add24_divide9(lv38: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_down_blocks_0_resnets_0_conv2_weight: T.Buffer((T.int64(320), T.int64(320), T.int64(3), T.int64(3)), "float32"), lv40: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv24: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv38[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv38[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(320), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_0_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_0_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv40[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv40[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv24[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv24[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d15_add21(lv44: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_down_blocks_0_attentions_0_proj_in_weight: T.Buffer((T.int64(320), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv46: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv44[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv44[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(320), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_0_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_0_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv46[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv46[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d15_add21_add24(lv120: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_down_blocks_0_attentions_0_proj_out_weight: T.Buffer((T.int64(320), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv122: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv43: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv120[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv120[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(320), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_0_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_0_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv122[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv122[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv43[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv43[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d16_add28(lv224: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_down_blocks_0_downsamplers_0_conv_weight: T.Buffer((T.int64(320), T.int64(320), T.int64(3), T.int64(3)), "float32"), lv226: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv224[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv224[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(32), T.int64(32), T.int64(320), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], unet_down_blocks_0_downsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * unet_down_blocks_0_downsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv226[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv226[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d17_add29_add31(lv229: T.Buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_resnets_0_conv1_weight: T.Buffer((T.int64(640), T.int64(320), T.int64(3), T.int64(3)), "float32"), lv231: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv238: T.Buffer((T.int64(2), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv229[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv229[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(320), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_1_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_1_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv231[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv231[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv238[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv238[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d18_add29_add31(lv332: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_resnets_1_conv1_weight: T.Buffer((T.int64(640), T.int64(640), T.int64(3), T.int64(3)), "float32"), lv334: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv341: T.Buffer((T.int64(2), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv332[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv332[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(640), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_1_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_1_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv334[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv334[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv341[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv341[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d18_add29_add32_divide10(lv241: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_resnets_0_conv2_weight: T.Buffer((T.int64(640), T.int64(640), T.int64(3), T.int64(3)), "float32"), lv243: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv247: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv241[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv241[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(640), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_1_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_1_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv243[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv243[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv247[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv247[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d19_add29(lv227: T.Buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(640), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv246: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(32), T.int64(32)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv227[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv227[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(320), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_1_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_1_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv246[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv246[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d1_add2(lv3: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), vae_decoder_conv_in_weight: T.Buffer((T.int64(512), T.int64(4), T.int64(3), T.int64(3)), "float32"), lv5: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(4), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv3[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv3[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64), T.int64(4), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_conv_in_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_conv_in_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv5[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv5[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d20_add29(lv250: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_attentions_0_proj_in_weight: T.Buffer((T.int64(640), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv252: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv250[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv250[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(640), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_1_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_1_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv252[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv252[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d20_add29_add32(lv326: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_attentions_0_proj_out_weight: T.Buffer((T.int64(640), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv328: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv249: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv326[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv326[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(640), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_1_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_1_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv328[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv328[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv249[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv249[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d21_add36(lv430: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_downsamplers_0_conv_weight: T.Buffer((T.int64(640), T.int64(640), T.int64(3), T.int64(3)), "float32"), lv432: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv430[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv430[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(16), T.int64(16), T.int64(640), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], unet_down_blocks_1_downsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * unet_down_blocks_1_downsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv432[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv432[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d22_add37_add38(lv435: T.Buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_resnets_0_conv1_weight: T.Buffer((T.int64(1280), T.int64(640), T.int64(3), T.int64(3)), "float32"), lv437: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv444: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv435[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv435[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(640), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_2_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_2_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv437[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv437[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv444[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv444[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d23_add37(lv866: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_0_upsamplers_0_conv_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv868: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv866[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv866[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_0_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_0_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv868[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv868[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d23_add37_add38(lv538: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_resnets_1_conv1_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv540: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv547: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv538[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv538[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_2_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_2_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv540[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv540[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv547[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv547[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d23_add37_add39_divide11(lv447: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_resnets_0_conv2_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv449: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv453: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv447[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv447[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_2_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_2_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv449[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv449[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv453[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv453[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d24_add37(lv433: T.Buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(1280), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv452: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv433[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv433[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(640), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_2_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_2_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv452[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv452[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d25_add37(lv456: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_attentions_0_proj_in_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv458: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv456[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv456[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1280), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_2_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_2_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv458[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv458[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d25_add37_add39(lv532: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_attentions_0_proj_out_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv534: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv455: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv532[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv532[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1280), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_2_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_2_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv534[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv534[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv455[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv455[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d26_add43(lv636: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_downsamplers_0_conv_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv638: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv636[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv636[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], unet_down_blocks_2_downsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * unet_down_blocks_2_downsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv638[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv638[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d27_add43_add44(lv641: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), unet_down_blocks_3_resnets_0_conv1_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv643: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv650: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(10), T.int64(10)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(10), T.int64(10)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv641[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(9) and T.int64(1) <= v_i3 and v_i3 < T.int64(9), lv641[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_3_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_3_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv643[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv643[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv650[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv650[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d27_add43_add45_divide12(lv653: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), unet_down_blocks_3_resnets_0_conv2_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv655: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv639: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(10), T.int64(10)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(10), T.int64(10)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv653[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(9) and T.int64(1) <= v_i3 and v_i3 < T.int64(9), lv653[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_down_blocks_3_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_down_blocks_3_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv655[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv655[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv639[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv639[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d28_add43(lv697: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), unet_mid_block_attentions_0_proj_in_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv699: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv697[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv697[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(1280), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_mid_block_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_mid_block_attentions_0_proj_in_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv699[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv699[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d28_add43_add45(lv773: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), unet_mid_block_attentions_0_proj_out_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv775: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv696: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv773[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv773[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(1280), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_mid_block_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_mid_block_attentions_0_proj_out_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv775[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv775[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv696[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv696[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d29_add43_add44(lv799: T.Buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)), "float32"), unet_up_blocks_0_resnets_0_conv1_weight: T.Buffer((T.int64(1280), T.int64(2560), T.int64(3), T.int64(3)), "float32"), lv801: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv808: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(10), T.int64(10)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(2560), T.int64(10), T.int64(10)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv799[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(9) and T.int64(1) <= v_i3 and v_i3 < T.int64(9), lv799[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(2560), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_0_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_0_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv801[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv801[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv808[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv808[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d2_add2(lv8: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), vae_decoder_mid_block_resnets_0_conv1_weight: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv10: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv8[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv8[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_mid_block_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_mid_block_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv10[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv10[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d2_add2_add3_divide3(lv13: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), vae_decoder_mid_block_resnets_0_conv2_weight: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv15: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), lv6: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv13[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv13[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_mid_block_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_mid_block_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv15[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv15[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv6[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv6[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d2_add2_add3_divide3_divide3(lv61: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), vae_decoder_mid_block_resnets_1_conv2_weight: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv63: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), lv54: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        var_T_divide_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv61[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv61[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_mid_block_resnets_1_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_mid_block_resnets_1_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv63[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv63[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv54[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv54[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_divide_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_divide_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_divide_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d30_add43(lv797: T.Buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)), "float32"), unet_up_blocks_0_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(1280), T.int64(2560), T.int64(1), T.int64(1)), "float32"), lv816: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(2560), T.int64(8), T.int64(8)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv797[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv797[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8), T.int64(2560), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_0_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_0_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv816[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv816[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d31_add37_add38(lv872: T.Buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_1_resnets_0_conv1_weight: T.Buffer((T.int64(1280), T.int64(2560), T.int64(3), T.int64(3)), "float32"), lv874: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv881: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(2560), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv872[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv872[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(2560), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_1_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_1_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv874[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv874[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv881[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv881[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d32_add37(lv870: T.Buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_1_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(1280), T.int64(2560), T.int64(1), T.int64(1)), "float32"), lv889: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(2560), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv870[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv870[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(2560), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_1_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_1_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv889[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv889[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d33_add37_add38(lv1080: T.Buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_1_resnets_2_conv1_weight: T.Buffer((T.int64(1280), T.int64(1920), T.int64(3), T.int64(3)), "float32"), lv1082: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv1089: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(18), T.int64(18)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1920), T.int64(18), T.int64(18)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1080[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(17) and T.int64(1) <= v_i3 and v_i3 < T.int64(17), lv1080[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1920), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_1_resnets_2_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_1_resnets_2_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1082[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1082[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv1089[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv1089[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d34_add37(lv1078: T.Buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_1_resnets_2_conv_shortcut_weight: T.Buffer((T.int64(1280), T.int64(1920), T.int64(1), T.int64(1)), "float32"), lv1097: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1920), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1078[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv1078[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16), T.int64(1920), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_1_resnets_2_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_1_resnets_2_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1097[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1097[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d35_add49(lv1182: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_1_upsamplers_0_conv_weight: T.Buffer((T.int64(1280), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv1184: T.Buffer((T.int64(1), T.int64(1280), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1182[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv1182[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_1_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_1_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1184[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1184[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d36_add29_add31(lv1188: T.Buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_0_conv1_weight: T.Buffer((T.int64(640), T.int64(1920), T.int64(3), T.int64(3)), "float32"), lv1190: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv1197: T.Buffer((T.int64(2), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1920), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1188[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv1188[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(1920), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1190[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1190[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv1197[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv1197[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d37_add29(lv1186: T.Buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(640), T.int64(1920), T.int64(1), T.int64(1)), "float32"), lv1205: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1920), T.int64(32), T.int64(32)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1186[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv1186[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(1920), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1205[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1205[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d38_add29_add31(lv1292: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_1_conv1_weight: T.Buffer((T.int64(640), T.int64(1280), T.int64(3), T.int64(3)), "float32"), lv1294: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv1301: T.Buffer((T.int64(2), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1292[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv1292[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(1280), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1294[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1294[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv1301[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv1301[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d39_add29(lv1290: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_1_conv_shortcut_weight: T.Buffer((T.int64(640), T.int64(1280), T.int64(1), T.int64(1)), "float32"), lv1309: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1290[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv1290[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(1280), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_resnets_1_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_resnets_1_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1309[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1309[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d3_add5(lv104: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32"), vae_decoder_up_blocks_0_upsamplers_0_conv_weight: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv106: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(130), T.int64(130)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(130), T.int64(130)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv104[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(129) and T.int64(1) <= v_i3 and v_i3 < T.int64(129), lv104[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_0_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_0_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv106[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv106[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d3_add5_add6_divide5(lv114: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32"), vae_decoder_up_blocks_1_resnets_0_conv2_weight: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv116: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), lv107: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(130), T.int64(130)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(130), T.int64(130)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv114[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(129) and T.int64(1) <= v_i3 and v_i3 < T.int64(129), lv114[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_1_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_1_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv116[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv116[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv107[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv107[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d40_add29_add31(lv1396: T.Buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_2_conv1_weight: T.Buffer((T.int64(640), T.int64(960), T.int64(3), T.int64(3)), "float32"), lv1398: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv1405: T.Buffer((T.int64(2), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(34), T.int64(34)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(960), T.int64(34), T.int64(34)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1396[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(33) and T.int64(1) <= v_i3 and v_i3 < T.int64(33), lv1396[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(960), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_resnets_2_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_resnets_2_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1398[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1398[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv1405[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv1405[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d41_add29(lv1394: T.Buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_2_conv_shortcut_weight: T.Buffer((T.int64(640), T.int64(960), T.int64(1), T.int64(1)), "float32"), lv1413: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(960), T.int64(32), T.int64(32)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1394[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv1394[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32), T.int64(960), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_resnets_2_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_resnets_2_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1413[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1413[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d42_add50(lv1498: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_2_upsamplers_0_conv_weight: T.Buffer((T.int64(640), T.int64(640), T.int64(3), T.int64(3)), "float32"), lv1500: T.Buffer((T.int64(1), T.int64(640), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1498[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv1498[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64), T.int64(640), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_2_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_2_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1500[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1500[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d43_add21_add23(lv1504: T.Buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_3_resnets_0_conv1_weight: T.Buffer((T.int64(320), T.int64(960), T.int64(3), T.int64(3)), "float32"), lv1506: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv1513: T.Buffer((T.int64(2), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(960), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1504[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv1504[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(960), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_3_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_3_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1506[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1506[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv1513[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv1513[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d44_add21(lv1502: T.Buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_3_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(320), T.int64(960), T.int64(1), T.int64(1)), "float32"), lv1521: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(960), T.int64(64), T.int64(64)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1502[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv1502[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(960), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_3_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_3_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1521[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1521[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d45_add21_add23(lv1608: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_3_resnets_1_conv1_weight: T.Buffer((T.int64(320), T.int64(640), T.int64(3), T.int64(3)), "float32"), lv1610: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), lv1617: T.Buffer((T.int64(2), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1608[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv1608[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(640), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_3_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_3_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1610[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1610[T.int64(0), v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], lv1617[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + lv1617[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d46_add21(lv1606: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_3_resnets_1_conv_shortcut_weight: T.Buffer((T.int64(320), T.int64(640), T.int64(1), T.int64(1)), "float32"), lv1625: T.Buffer((T.int64(1), T.int64(320), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1606[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv1606[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64), T.int64(640), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_up_blocks_3_resnets_1_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_up_blocks_3_resnets_1_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1625[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1625[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d47_add51(lv1815: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_conv_out_weight: T.Buffer((T.int64(4), T.int64(320), T.int64(3), T.int64(3)), "float32"), lv1817: T.Buffer((T.int64(1), T.int64(4), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(66), T.int64(66)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(2), T.int64(4), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(66), T.int64(66)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1815[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(65) and T.int64(1) <= v_i3 and v_i3 < T.int64(65), lv1815[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(2), T.int64(4), T.int64(64), T.int64(64), T.int64(320), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], unet_conv_out_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * unet_conv_out_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv1817[T.int64(0), v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv1817[T.int64(0), v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d4_add7(lv144: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_1_upsamplers_0_conv_weight: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv146: T.Buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(258), T.int64(258)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(258), T.int64(258)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv144[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(257) and T.int64(1) <= v_i3 and v_i3 < T.int64(257), lv144[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_1_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_1_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv146[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv146[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d5_add8(lv149: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_2_resnets_0_conv1_weight: T.Buffer((T.int64(256), T.int64(512), T.int64(3), T.int64(3)), "float32"), lv151: T.Buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(258), T.int64(258)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(258), T.int64(258)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv149[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(257) and T.int64(1) <= v_i3 and v_i3 < T.int64(257), lv149[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_2_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_2_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv151[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv151[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d6_add8(lv164: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_2_resnets_1_conv1_weight: T.Buffer((T.int64(256), T.int64(256), T.int64(3), T.int64(3)), "float32"), lv166: T.Buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(258), T.int64(258)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(258), T.int64(258)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv164[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(257) and T.int64(1) <= v_i3 and v_i3 < T.int64(257), lv164[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256), T.int64(256), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_2_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_2_resnets_1_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv166[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv166[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d6_add8_add9_divide6(lv154: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_2_resnets_0_conv2_weight: T.Buffer((T.int64(256), T.int64(256), T.int64(3), T.int64(3)), "float32"), lv156: T.Buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)), "float32"), lv160: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(258), T.int64(258)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(258), T.int64(258)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv154[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(257) and T.int64(1) <= v_i3 and v_i3 < T.int64(257), lv154[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256), T.int64(256), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_2_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_2_resnets_0_conv2_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv156[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv156[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv160[v_ax0, v_ax1, v_ax2, v_ax3], var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv160[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_conv2d7_add8(lv147: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_2_resnets_0_conv_shortcut_weight: T.Buffer((T.int64(256), T.int64(512), T.int64(1), T.int64(1)), "float32"), lv159: T.Buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv147[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv147[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_2_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_2_resnets_0_conv_shortcut_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv159[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv159[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d8_add10(lv187: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_2_upsamplers_0_conv_weight: T.Buffer((T.int64(256), T.int64(256), T.int64(3), T.int64(3)), "float32"), lv189: T.Buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(514), T.int64(514)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(514), T.int64(514)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv187[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(513) and T.int64(1) <= v_i3 and v_i3 < T.int64(513), lv187[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512), T.int64(256), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_2_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_2_upsamplers_0_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv189[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv189[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d9_add11(lv192: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_3_resnets_0_conv1_weight: T.Buffer((T.int64(128), T.int64(256), T.int64(3), T.int64(3)), "float32"), lv194: T.Buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(514), T.int64(514)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(514), T.int64(514)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv192[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(513) and T.int64(1) <= v_i3 and v_i3 < T.int64(513), lv192[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512), T.int64(256), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_decoder_up_blocks_3_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_decoder_up_blocks_3_resnets_0_conv1_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv194[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv194[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv2d_add1(lv: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), vae_post_quant_conv_weight: T.Buffer((T.int64(4), T.int64(4), T.int64(1), T.int64(1)), "float32"), lv2: T.Buffer((T.int64(1), T.int64(4), T.int64(1), T.int64(1)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)))
        var_conv2d_nchw_intermediate = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64), T.int64(4), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], vae_post_quant_conv_weight[v_ff, v_rc, v_ry, v_rx])
                T.writes(var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = T.float32(0)
                var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] = var_conv2d_nchw_intermediate[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * vae_post_quant_conv_weight[v_ff, v_rc, v_ry, v_rx]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_conv2d_nchw_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv2[v_ax0, v_ax1, T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def fused_group_norm10_silu9(lv239: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_resnets_0_norm2_weight: T.Buffer((T.int64(640),), "float32"), unet_down_blocks_1_resnets_0_norm2_bias: T.Buffer((T.int64(640),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        compute = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv239[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(640), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv239[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(640), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_1_resnets_0_norm2_weight[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_down_blocks_1_resnets_0_norm2_weight[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_1_resnets_0_norm2_bias[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_down_blocks_1_resnets_0_norm2_bias[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(20), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(20), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm12_silu10(lv433: T.Buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_resnets_0_norm1_weight: T.Buffer((T.int64(640),), "float32"), unet_down_blocks_2_resnets_0_norm1_bias: T.Buffer((T.int64(640),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(16), T.int64(16)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(16), T.int64(16)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)))
        compute = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(16), T.int64(16)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(16), T.int64(16)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv433[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(640), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv433[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(640), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(16), T.int64(16)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_2_resnets_0_norm1_weight[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_down_blocks_2_resnets_0_norm1_weight[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_2_resnets_0_norm1_bias[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_down_blocks_2_resnets_0_norm1_bias[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(16), T.int64(16)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00019531250000000001)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.00019531250000000001) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00019531250000000001) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00019531250000000001)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(16), T.int64(16)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(20), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(20), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(16), T.int64(16)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(16), T.int64(16)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm13_silu11(lv445: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), unet_down_blocks_2_resnets_0_norm2_weight: T.Buffer((T.int64(1280),), "float32"), unet_down_blocks_2_resnets_0_norm2_bias: T.Buffer((T.int64(1280),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv445[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv445[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_2_resnets_0_norm2_weight[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_down_blocks_2_resnets_0_norm2_weight[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_2_resnets_0_norm2_bias[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_down_blocks_2_resnets_0_norm2_bias[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(40), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(40), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm15_silu12(lv639: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), unet_down_blocks_3_resnets_0_norm1_weight: T.Buffer((T.int64(1280),), "float32"), unet_down_blocks_3_resnets_0_norm1_bias: T.Buffer((T.int64(1280),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv639[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(8) + v_ax3) % T.int64(8), v_ax4 % T.int64(8)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv639[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(8) + v_ax3) % T.int64(8), v_ax4 % T.int64(8)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_3_resnets_0_norm1_weight[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_down_blocks_3_resnets_0_norm1_weight[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_3_resnets_0_norm1_bias[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_down_blocks_3_resnets_0_norm1_bias[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00039062500000000002)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.00039062500000000002) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00039062500000000002) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00039062500000000002)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(40), (v_ax3 // T.int64(8) + v_ax2) % T.int64(8), v_ax3 % T.int64(8)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(40), (v_ax3 // T.int64(8) + v_ax2) % T.int64(8), v_ax3 % T.int64(8)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm17_silu13(lv797: T.Buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)), "float32"), unet_up_blocks_0_resnets_0_norm1_weight: T.Buffer((T.int64(2560),), "float32"), unet_up_blocks_0_resnets_0_norm1_bias: T.Buffer((T.int64(2560),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(80), T.int64(8), T.int64(8)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(80)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(80)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(80), T.int64(8), T.int64(8)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)))
        compute = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(8), T.int64(8)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(80), T.int64(8), T.int64(8)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv797[((v_ax1 * T.int64(80) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) // T.int64(2560) + v_ax0) % T.int64(2), (v_ax1 * T.int64(80) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) % T.int64(2560), (v_ax4 // T.int64(8) + v_ax3) % T.int64(8), v_ax4 % T.int64(8)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv797[((v_ax1 * T.int64(80) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) // T.int64(2560) + v_ax0) % T.int64(2), (v_ax1 * T.int64(80) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) % T.int64(2560), (v_ax4 // T.int64(8) + v_ax3) % T.int64(8), v_ax4 % T.int64(8)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(80), T.int64(8), T.int64(8)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(80)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_0_resnets_0_norm1_weight[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_0_resnets_0_norm1_weight[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(80)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_0_resnets_0_norm1_bias[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_0_resnets_0_norm1_bias[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(80), T.int64(8), T.int64(8)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00019531250000000001)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.00019531250000000001) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00019531250000000001) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00019531250000000001)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(2560), T.int64(8), T.int64(8)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) // T.int64(2560) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(2560) // T.int64(80), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(80), (v_ax3 // T.int64(8) + v_ax2) % T.int64(8), v_ax3 % T.int64(8)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) // T.int64(2560) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(2560) // T.int64(80), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(80), (v_ax3 // T.int64(8) + v_ax2) % T.int64(8), v_ax3 % T.int64(8)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(2560), T.int64(8), T.int64(8)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(2560), T.int64(8), T.int64(8)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm18_silu14(lv870: T.Buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_1_resnets_0_norm1_weight: T.Buffer((T.int64(2560),), "float32"), unet_up_blocks_1_resnets_0_norm1_bias: T.Buffer((T.int64(2560),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(80), T.int64(16), T.int64(16)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(80)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(80)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(80), T.int64(16), T.int64(16)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)))
        compute = T.alloc_buffer((T.int64(2), T.int64(2560), T.int64(16), T.int64(16)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(80), T.int64(16), T.int64(16)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv870[((v_ax1 * T.int64(80) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(2560) + v_ax0) % T.int64(2), (v_ax1 * T.int64(80) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(2560), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv870[((v_ax1 * T.int64(80) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(2560) + v_ax0) % T.int64(2), (v_ax1 * T.int64(80) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(2560), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(80), T.int64(16), T.int64(16)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(80)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_1_resnets_0_norm1_weight[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_1_resnets_0_norm1_weight[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(80)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_1_resnets_0_norm1_bias[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_1_resnets_0_norm1_bias[(v_ax0 * T.int64(80) + v_ax1) % T.int64(2560)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(80), T.int64(16), T.int64(16)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(2560), T.int64(16), T.int64(16)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(2560) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(2560) // T.int64(80), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(80), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(2560) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(2560) // T.int64(80), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(80), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(2560), T.int64(16), T.int64(16)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(2560), T.int64(16), T.int64(16)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm19_silu15(lv1078: T.Buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)), "float32"), unet_up_blocks_1_resnets_2_norm1_weight: T.Buffer((T.int64(1920),), "float32"), unet_up_blocks_1_resnets_2_norm1_bias: T.Buffer((T.int64(1920),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(60), T.int64(16), T.int64(16)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(60)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(60)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(60), T.int64(16), T.int64(16)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(16), T.int64(16)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(60), T.int64(16), T.int64(16)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv1078[((v_ax1 * T.int64(60) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(1920) + v_ax0) % T.int64(2), (v_ax1 * T.int64(60) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(1920), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv1078[((v_ax1 * T.int64(60) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(1920) + v_ax0) % T.int64(2), (v_ax1 * T.int64(60) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(1920), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(60), T.int64(16), T.int64(16)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(60)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_1_resnets_2_norm1_weight[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_1_resnets_2_norm1_weight[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(60)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_1_resnets_2_norm1_bias[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_1_resnets_2_norm1_bias[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(60), T.int64(16), T.int64(16)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(6.5104166666666666e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(6.5104166666666666e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(6.5104166666666666e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(6.5104166666666666e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1920), T.int64(16), T.int64(16)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(1920) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(1920) // T.int64(60), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(60), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(1920) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(1920) // T.int64(60), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(60), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1920), T.int64(16), T.int64(16)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1920), T.int64(16), T.int64(16)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm20_silu16(lv1186: T.Buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_0_norm1_weight: T.Buffer((T.int64(1920),), "float32"), unet_up_blocks_2_resnets_0_norm1_bias: T.Buffer((T.int64(1920),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(60), T.int64(32), T.int64(32)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(60)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(60)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(60), T.int64(32), T.int64(32)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1920), T.int64(32), T.int64(32)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(60), T.int64(32), T.int64(32)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv1186[((v_ax1 * T.int64(60) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(1920) + v_ax0) % T.int64(2), (v_ax1 * T.int64(60) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(1920), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv1186[((v_ax1 * T.int64(60) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(1920) + v_ax0) % T.int64(2), (v_ax1 * T.int64(60) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(1920), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(60), T.int64(32), T.int64(32)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(60)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_2_resnets_0_norm1_weight[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_2_resnets_0_norm1_weight[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(60)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_2_resnets_0_norm1_bias[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_2_resnets_0_norm1_bias[(v_ax0 * T.int64(60) + v_ax1) % T.int64(1920)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(60), T.int64(32), T.int64(32)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.6276041666666666e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(1.6276041666666666e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.6276041666666666e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.6276041666666666e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1920), T.int64(32), T.int64(32)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(1920) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(1920) // T.int64(60), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(60), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(1920) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(1920) // T.int64(60), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(60), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1920), T.int64(32), T.int64(32)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1920), T.int64(32), T.int64(32)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm21_silu17(lv1290: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_1_norm1_weight: T.Buffer((T.int64(1280),), "float32"), unet_up_blocks_2_resnets_1_norm1_bias: T.Buffer((T.int64(1280),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(32), T.int64(32)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(32), T.int64(32)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(32), T.int64(32)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv1290[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv1290[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(32), T.int64(32)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_2_resnets_1_norm1_weight[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_2_resnets_1_norm1_weight[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_2_resnets_1_norm1_bias[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_2_resnets_1_norm1_bias[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(32), T.int64(32)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(40), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(40), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm22_silu18(lv1394: T.Buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)), "float32"), unet_up_blocks_2_resnets_2_norm1_weight: T.Buffer((T.int64(960),), "float32"), unet_up_blocks_2_resnets_2_norm1_bias: T.Buffer((T.int64(960),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(30), T.int64(32), T.int64(32)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(30)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(30)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(30), T.int64(32), T.int64(32)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)))
        compute = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(32), T.int64(32)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(30), T.int64(32), T.int64(32)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv1394[((v_ax1 * T.int64(30) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(960) + v_ax0) % T.int64(2), (v_ax1 * T.int64(30) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(960), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv1394[((v_ax1 * T.int64(30) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(960) + v_ax0) % T.int64(2), (v_ax1 * T.int64(30) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(960), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(30), T.int64(32), T.int64(32)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(30)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_2_resnets_2_norm1_weight[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_2_resnets_2_norm1_weight[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(30)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_2_resnets_2_norm1_bias[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_2_resnets_2_norm1_bias[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(30), T.int64(32), T.int64(32)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(3.2552083333333333e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(3.2552083333333333e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(3.2552083333333333e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(3.2552083333333333e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(960), T.int64(32), T.int64(32)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(960) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(960) // T.int64(30), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(30), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(960) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(960) // T.int64(30), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(30), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(960), T.int64(32), T.int64(32)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(960), T.int64(32), T.int64(32)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm23_silu19(lv1502: T.Buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_3_resnets_0_norm1_weight: T.Buffer((T.int64(960),), "float32"), unet_up_blocks_3_resnets_0_norm1_bias: T.Buffer((T.int64(960),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(30), T.int64(64), T.int64(64)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(30)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(30)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(30), T.int64(64), T.int64(64)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)))
        compute = T.alloc_buffer((T.int64(2), T.int64(960), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(30), T.int64(64), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv1502[((v_ax1 * T.int64(30) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(960) + v_ax0) % T.int64(2), (v_ax1 * T.int64(30) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(960), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv1502[((v_ax1 * T.int64(30) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(960) + v_ax0) % T.int64(2), (v_ax1 * T.int64(30) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(960), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(30), T.int64(64), T.int64(64)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(30)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_3_resnets_0_norm1_weight[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_3_resnets_0_norm1_weight[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(30)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_3_resnets_0_norm1_bias[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_3_resnets_0_norm1_bias[(v_ax0 * T.int64(30) + v_ax1) % T.int64(960)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(30), T.int64(64), T.int64(64)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(8.1380208333333332e-06)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(8.1380208333333332e-06) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(8.1380208333333332e-06) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(8.1380208333333332e-06)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(960), T.int64(64), T.int64(64)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(960) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(960) // T.int64(30), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(30), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(960) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(960) // T.int64(30), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(30), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(960), T.int64(64), T.int64(64)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(960), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm24_silu20(lv1606: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32"), unet_up_blocks_3_resnets_1_norm1_weight: T.Buffer((T.int64(640),), "float32"), unet_up_blocks_3_resnets_1_norm1_bias: T.Buffer((T.int64(640),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(64), T.int64(64)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(64), T.int64(64)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)))
        compute = T.alloc_buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(64), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv1606[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(640), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv1606[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(640), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(64), T.int64(64)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_3_resnets_1_norm1_weight[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_up_blocks_3_resnets_1_norm1_weight[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_up_blocks_3_resnets_1_norm1_bias[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_up_blocks_3_resnets_1_norm1_bias[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(64), T.int64(64)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.2207031250000001e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(1.2207031250000001e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.2207031250000001e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.2207031250000001e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(20), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(20), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm2_silu1(lv107: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32"), vae_decoder_up_blocks_1_resnets_0_norm1_weight: T.Buffer((T.int64(512),), "float32"), vae_decoder_up_blocks_1_resnets_0_norm1_bias: T.Buffer((T.int64(512),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(128), T.int64(128)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(128), T.int64(128)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)))
        compute = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(128), T.int64(128)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv107[T.int64(0), (v_ax1 * T.int64(16) + (v_ax4 // T.int64(128) + v_ax3) // T.int64(128) + v_ax2) % T.int64(512), (v_ax4 // T.int64(128) + v_ax3) % T.int64(128), v_ax4 % T.int64(128)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv107[T.int64(0), (v_ax1 * T.int64(16) + (v_ax4 // T.int64(128) + v_ax3) // T.int64(128) + v_ax2) % T.int64(512), (v_ax4 // T.int64(128) + v_ax3) % T.int64(128), v_ax4 % T.int64(128)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(128), T.int64(128)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_1_resnets_0_norm1_weight[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = vae_decoder_up_blocks_1_resnets_0_norm1_weight[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_1_resnets_0_norm1_bias[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = vae_decoder_up_blocks_1_resnets_0_norm1_bias[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(128), T.int64(128)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(3.814697265625e-06)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(3.814697265625e-06) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(3.814697265625e-06) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(3.814697265625e-06)) + T.float32(9.9999999999999995e-07)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[T.int64(0), ((v_ax3 // T.int64(128) + v_ax2) // T.int64(128) + v_ax1) % T.int64(512) // T.int64(16), ((v_ax3 // T.int64(128) + v_ax2) // T.int64(128) + v_ax1) % T.int64(16), (v_ax3 // T.int64(128) + v_ax2) % T.int64(128), v_ax3 % T.int64(128)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[T.int64(0), ((v_ax3 // T.int64(128) + v_ax2) // T.int64(128) + v_ax1) % T.int64(512) // T.int64(16), ((v_ax3 // T.int64(128) + v_ax2) // T.int64(128) + v_ax1) % T.int64(16), (v_ax3 // T.int64(128) + v_ax2) % T.int64(128), v_ax3 % T.int64(128)]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm3_silu2(lv147: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_2_resnets_0_norm1_weight: T.Buffer((T.int64(512),), "float32"), vae_decoder_up_blocks_2_resnets_0_norm1_bias: T.Buffer((T.int64(512),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(256), T.int64(256)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(256), T.int64(256)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)))
        compute = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv147[T.int64(0), (v_ax1 * T.int64(16) + (v_ax4 // T.int64(256) + v_ax3) // T.int64(256) + v_ax2) % T.int64(512), (v_ax4 // T.int64(256) + v_ax3) % T.int64(256), v_ax4 % T.int64(256)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv147[T.int64(0), (v_ax1 * T.int64(16) + (v_ax4 // T.int64(256) + v_ax3) // T.int64(256) + v_ax2) % T.int64(512), (v_ax4 // T.int64(256) + v_ax3) % T.int64(256), v_ax4 % T.int64(256)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(256), T.int64(256)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_2_resnets_0_norm1_weight[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = vae_decoder_up_blocks_2_resnets_0_norm1_weight[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_2_resnets_0_norm1_bias[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = vae_decoder_up_blocks_2_resnets_0_norm1_bias[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.5367431640625e-07)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(9.5367431640625e-07) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.5367431640625e-07) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.5367431640625e-07)) + T.float32(9.9999999999999995e-07)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[T.int64(0), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(512) // T.int64(16), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(16), (v_ax3 // T.int64(256) + v_ax2) % T.int64(256), v_ax3 % T.int64(256)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[T.int64(0), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(512) // T.int64(16), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(16), (v_ax3 // T.int64(256) + v_ax2) % T.int64(256), v_ax3 % T.int64(256)]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm4_silu3(lv152: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32"), vae_decoder_up_blocks_2_resnets_0_norm2_weight: T.Buffer((T.int64(256),), "float32"), vae_decoder_up_blocks_2_resnets_0_norm2_bias: T.Buffer((T.int64(256),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(8), T.int64(256), T.int64(256)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(8)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(8)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(8), T.int64(256), T.int64(256)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        compute = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(8), T.int64(256), T.int64(256)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv152[T.int64(0), (v_ax1 * T.int64(8) + (v_ax4 // T.int64(256) + v_ax3) // T.int64(256) + v_ax2) % T.int64(256), (v_ax4 // T.int64(256) + v_ax3) % T.int64(256), v_ax4 % T.int64(256)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv152[T.int64(0), (v_ax1 * T.int64(8) + (v_ax4 // T.int64(256) + v_ax3) // T.int64(256) + v_ax2) % T.int64(256), (v_ax4 // T.int64(256) + v_ax3) % T.int64(256), v_ax4 % T.int64(256)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(1), T.int64(32), T.int64(8), T.int64(256), T.int64(256)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(8)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_2_resnets_0_norm2_weight[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = vae_decoder_up_blocks_2_resnets_0_norm2_weight[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(8)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_2_resnets_0_norm2_bias[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = vae_decoder_up_blocks_2_resnets_0_norm2_bias[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(8), T.int64(256), T.int64(256)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.9073486328125e-06)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(1.9073486328125e-06) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.9073486328125e-06) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.9073486328125e-06)) + T.float32(9.9999999999999995e-07)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[T.int64(0), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(256) // T.int64(8), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(8), (v_ax3 // T.int64(256) + v_ax2) % T.int64(256), v_ax3 % T.int64(256)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[T.int64(0), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(256) // T.int64(8), ((v_ax3 // T.int64(256) + v_ax2) // T.int64(256) + v_ax1) % T.int64(8), (v_ax3 // T.int64(256) + v_ax2) % T.int64(256), v_ax3 % T.int64(256)]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(256), T.int64(256)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm5_silu4(lv190: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_3_resnets_0_norm1_weight: T.Buffer((T.int64(256),), "float32"), vae_decoder_up_blocks_3_resnets_0_norm1_bias: T.Buffer((T.int64(256),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(8), T.int64(512), T.int64(512)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(8)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(8)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(8), T.int64(512), T.int64(512)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)))
        compute = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(8), T.int64(512), T.int64(512)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv190[T.int64(0), (v_ax1 * T.int64(8) + (v_ax4 // T.int64(512) + v_ax3) // T.int64(512) + v_ax2) % T.int64(256), (v_ax4 // T.int64(512) + v_ax3) % T.int64(512), v_ax4 % T.int64(512)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv190[T.int64(0), (v_ax1 * T.int64(8) + (v_ax4 // T.int64(512) + v_ax3) // T.int64(512) + v_ax2) % T.int64(256), (v_ax4 // T.int64(512) + v_ax3) % T.int64(512), v_ax4 % T.int64(512)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(1), T.int64(32), T.int64(8), T.int64(512), T.int64(512)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(8)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_3_resnets_0_norm1_weight[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = vae_decoder_up_blocks_3_resnets_0_norm1_weight[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(8)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_3_resnets_0_norm1_bias[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = vae_decoder_up_blocks_3_resnets_0_norm1_bias[(v_ax0 * T.int64(8) + v_ax1) % T.int64(256)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(8), T.int64(512), T.int64(512)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.76837158203125e-07)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(4.76837158203125e-07) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.76837158203125e-07) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.76837158203125e-07)) + T.float32(9.9999999999999995e-07)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[T.int64(0), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(256) // T.int64(8), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(8), (v_ax3 // T.int64(512) + v_ax2) % T.int64(512), v_ax3 % T.int64(512)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[T.int64(0), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(256) // T.int64(8), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(8), (v_ax3 // T.int64(512) + v_ax2) % T.int64(512), v_ax3 % T.int64(512)]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm6_silu5(lv195: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32"), vae_decoder_up_blocks_3_resnets_0_norm2_weight: T.Buffer((T.int64(128),), "float32"), vae_decoder_up_blocks_3_resnets_0_norm2_bias: T.Buffer((T.int64(128),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(4), T.int64(512), T.int64(512)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(4)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(4)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(4), T.int64(512), T.int64(512)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        compute = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(512), T.int64(512)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(4), T.int64(512), T.int64(512)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv195[T.int64(0), (v_ax1 * T.int64(4) + (v_ax4 // T.int64(512) + v_ax3) // T.int64(512) + v_ax2) % T.int64(128), (v_ax4 // T.int64(512) + v_ax3) % T.int64(512), v_ax4 % T.int64(512)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv195[T.int64(0), (v_ax1 * T.int64(4) + (v_ax4 // T.int64(512) + v_ax3) // T.int64(512) + v_ax2) % T.int64(128), (v_ax4 // T.int64(512) + v_ax3) % T.int64(512), v_ax4 % T.int64(512)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(1), T.int64(32), T.int64(4), T.int64(512), T.int64(512)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(4)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_3_resnets_0_norm2_weight[(v_ax0 * T.int64(4) + v_ax1) % T.int64(128)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = vae_decoder_up_blocks_3_resnets_0_norm2_weight[(v_ax0 * T.int64(4) + v_ax1) % T.int64(128)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(4)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_up_blocks_3_resnets_0_norm2_bias[(v_ax0 * T.int64(4) + v_ax1) % T.int64(128)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = vae_decoder_up_blocks_3_resnets_0_norm2_bias[(v_ax0 * T.int64(4) + v_ax1) % T.int64(128)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(4), T.int64(512), T.int64(512)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.5367431640625e-07)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(9.5367431640625e-07) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.5367431640625e-07) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.5367431640625e-07)) + T.float32(9.9999999999999995e-07)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[T.int64(0), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(128) // T.int64(4), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(4), (v_ax3 // T.int64(512) + v_ax2) % T.int64(512), v_ax3 % T.int64(512)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[T.int64(0), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(128) // T.int64(4), ((v_ax3 // T.int64(512) + v_ax2) // T.int64(512) + v_ax1) % T.int64(4), (v_ax3 // T.int64(512) + v_ax2) % T.int64(512), v_ax3 % T.int64(512)]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(512), T.int64(512)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm7_silu7(lv24: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), unet_down_blocks_0_resnets_0_norm1_weight: T.Buffer((T.int64(320),), "float32"), unet_down_blocks_0_resnets_0_norm1_bias: T.Buffer((T.int64(320),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(10)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(10)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        compute = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv24[((v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(320), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv24[((v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(320), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(10)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_0_resnets_0_norm1_weight[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_down_blocks_0_resnets_0_norm1_weight[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(10)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_0_resnets_0_norm1_bias[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_down_blocks_0_resnets_0_norm1_bias[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(320) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(320) // T.int64(10), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(10), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(320) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(320) // T.int64(10), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(10), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm9_silu8(lv227: T.Buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)), "float32"), unet_down_blocks_1_resnets_0_norm1_weight: T.Buffer((T.int64(320),), "float32"), unet_down_blocks_1_resnets_0_norm1_bias: T.Buffer((T.int64(320),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(10), T.int64(32), T.int64(32)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(10)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(10)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(10), T.int64(32), T.int64(32)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)))
        compute = T.alloc_buffer((T.int64(2), T.int64(320), T.int64(32), T.int64(32)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(32), T.int64(32)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv227[((v_ax1 * T.int64(10) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 * T.int64(10) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(320), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv227[((v_ax1 * T.int64(10) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 * T.int64(10) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(320), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(32), T.int64(32)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(10)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_1_resnets_0_norm1_weight[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = unet_down_blocks_1_resnets_0_norm1_weight[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(10)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(unet_down_blocks_1_resnets_0_norm1_bias[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = unet_down_blocks_1_resnets_0_norm1_bias[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(32), T.int64(32)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05)) + T.float32(1.0000000000000001e-05)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(32), T.int64(32)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(320) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(320) // T.int64(10), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(10), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(320) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(320) // T.int64(10), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(10), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)]
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(320), T.int64(32), T.int64(32)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(32), T.int64(32)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_group_norm_silu(lv6: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), vae_decoder_mid_block_resnets_0_norm1_weight: T.Buffer((T.int64(512),), "float32"), vae_decoder_mid_block_resnets_0_norm1_bias: T.Buffer((T.int64(512),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(64), T.int64(64)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_1 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(64), T.int64(64)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        compute = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(lv6[T.int64(0), (v_ax1 * T.int64(16) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(512), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = lv6[T.int64(0), (v_ax1 * T.int64(16) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(512), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(64), T.int64(64)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_mid_block_resnets_0_norm1_weight[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_1[v_ax0, v_ax1])
                T_reshape_1[v_ax0, v_ax1] = vae_decoder_mid_block_resnets_0_norm1_weight[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(vae_decoder_mid_block_resnets_0_norm1_bias[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = vae_decoder_mid_block_resnets_0_norm1_bias[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_1[v_ax1, v_ax2], T_reshape_2[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.52587890625e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(1.52587890625e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.52587890625e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.52587890625e-05)) + T.float32(9.9999999999999995e-07)) * T_reshape_1[v_ax1, v_ax2] + T_reshape_2[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[T.int64(0), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(512) // T.int64(16), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(16), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[T.int64(0), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(512) // T.int64(16), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(16), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sigmoid(var_T_reshape_intermediate[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * compute[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_matmul10_add22_strided_slice3(lv30: T.Buffer((T.int64(2), T.int64(1280)), "float32"), lv31: T.Buffer((T.int64(1280), T.int64(320)), "float32"), unet_down_blocks_0_resnets_0_time_emb_proj_bias: T.Buffer((T.int64(320),), "float32"), var_T_strided_slice_with_axes_intermediate: T.Buffer((T.int64(2), T.int64(320)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(320)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(320)))
        for i0, i1, k in T.grid(T.int64(2), T.int64(320), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(lv30[v_i0, v_k], lv31[v_k, v_i1])
                T.writes(var_matmul_intermediate[v_i0, v_i1])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1] = var_matmul_intermediate[v_i0, v_i1] + lv30[v_i0, v_k] * lv31[v_k, v_i1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(320)):
            with T.block("T_add"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1], unet_down_blocks_0_resnets_0_time_emb_proj_bias[v_ax1])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1])
                var_T_add_intermediate[v_ax0, v_ax1] = var_matmul_intermediate[v_ax0, v_ax1] + unet_down_blocks_0_resnets_0_time_emb_proj_bias[v_ax1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(320)):
            with T.block("T_strided_slice_with_axes"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1])
                T.writes(var_T_strided_slice_with_axes_intermediate[v_ax0, v_ax1])
                var_T_strided_slice_with_axes_intermediate[v_ax0, v_ax1] = var_T_add_intermediate[v_ax0, v_ax1]

    @T.prim_func(private=True)
    def fused_matmul11_add25_add26(lv73: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), lv74: T.Buffer((T.int64(320), T.int64(320)), "float32"), unet_down_blocks_0_attentions_0_transformer_blocks_0_attn1_to_out_0_bias: T.Buffer((T.int64(320),), "float32"), lv49: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(320)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(320)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(4096), T.int64(320), T.int64(320)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv73[v_i0, v_i1, v_k], lv74[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv73[v_i0, v_i1, v_k] * lv74[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_0_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_0_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv49[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv49[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul12_multiply13(lv59: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32"), lv66: T.Buffer((T.int64(16), T.int64(40), T.int64(4096)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(4096), T.int64(4096)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(4096), T.int64(4096)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(4096), T.int64(4096), T.int64(40)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv59[v_i0, v_i1, v_k], lv66[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv59[v_i0, v_i1, v_k] * lv66[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(4096), T.int64(4096)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.15811388194561005)

    @T.prim_func(private=True)
    def fused_matmul15_multiply14(lv87: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32"), lv94: T.Buffer((T.int64(16), T.int64(40), T.int64(77)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(4096), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(4096), T.int64(77)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(4096), T.int64(77), T.int64(40)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv87[v_i0, v_i1, v_k], lv94[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv87[v_i0, v_i1, v_k] * lv94[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(4096), T.int64(77)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.15811388194561005)

    @T.prim_func(private=True)
    def fused_matmul17_add27_gelu(lv106: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), lv110: T.Buffer((T.int64(320), T.int64(1280)), "float32"), unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias: T.Buffer((T.int64(1280),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(4096), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        T_multiply = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        compute = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        T_multiply_1 = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        T_add = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(4096), T.int64(1280), T.int64(320)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv106[v_i0, v_i1, v_k], lv110[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv106[v_i0, v_i1, v_k] * lv110[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2])
                T_multiply[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.70710678118654757)
        for i0, i1, i2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("compute"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_multiply[v_i0, v_i1, v_i2])
                T.writes(compute[v_i0, v_i1, v_i2])
                compute[v_i0, v_i1, v_i2] = T.erf(T_multiply[v_i0, v_i1, v_i2])
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_multiply_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(compute[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T_multiply_1[v_ax0, v_ax1, v_ax2] = compute[v_ax0, v_ax1, v_ax2] * T.float32(0.5)
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T.writes(T_add[v_ax0, v_ax1, v_ax2])
                T_add[v_ax0, v_ax1, v_ax2] = T.float32(0.5) + T_multiply_1[v_ax0, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_multiply_2"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], T_add[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T_add[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul17_add27_multiply15(lv106: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), lv107: T.Buffer((T.int64(320), T.int64(1280)), "float32"), unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias: T.Buffer((T.int64(1280),), "float32"), lv113: T.Buffer((T.int64(2), T.int64(4096), T.int64(1280)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(4096), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(1280)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(4096), T.int64(1280), T.int64(320)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv106[v_i0, v_i1, v_k], lv107[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv106[v_i0, v_i1, v_k] * lv107[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(1280)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], lv113[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * lv113[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul18_add25_add26(lv114: T.Buffer((T.int64(2), T.int64(4096), T.int64(1280)), "float32"), lv115: T.Buffer((T.int64(1280), T.int64(320)), "float32"), unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_2_bias: T.Buffer((T.int64(320),), "float32"), lv105: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(320)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(320)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(4096), T.int64(320), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv114[v_i0, v_i1, v_k], lv115[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv114[v_i0, v_i1, v_k] * lv115[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_0_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv105[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv105[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul19_add30_strided_slice4(lv233: T.Buffer((T.int64(2), T.int64(1280)), "float32"), lv234: T.Buffer((T.int64(1280), T.int64(640)), "float32"), unet_down_blocks_1_resnets_0_time_emb_proj_bias: T.Buffer((T.int64(640),), "float32"), var_T_strided_slice_with_axes_intermediate: T.Buffer((T.int64(2), T.int64(640)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(640)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(640)))
        for i0, i1, k in T.grid(T.int64(2), T.int64(640), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(lv233[v_i0, v_k], lv234[v_k, v_i1])
                T.writes(var_matmul_intermediate[v_i0, v_i1])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1] = var_matmul_intermediate[v_i0, v_i1] + lv233[v_i0, v_k] * lv234[v_k, v_i1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(640)):
            with T.block("T_add"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1], unet_down_blocks_1_resnets_0_time_emb_proj_bias[v_ax1])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1])
                var_T_add_intermediate[v_ax0, v_ax1] = var_matmul_intermediate[v_ax0, v_ax1] + unet_down_blocks_1_resnets_0_time_emb_proj_bias[v_ax1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(640)):
            with T.block("T_strided_slice_with_axes"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1])
                T.writes(var_T_strided_slice_with_axes_intermediate[v_ax0, v_ax1])
                var_T_strided_slice_with_axes_intermediate[v_ax0, v_ax1] = var_T_add_intermediate[v_ax0, v_ax1]

    @T.prim_func(private=True)
    def fused_matmul1_multiply5(lv34: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(512)), "float32"), lv41: T.Buffer((T.int64(1), T.int64(1), T.int64(512), T.int64(4096)), "float32"), param_0: T.Buffer((), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)))
        for i0, i1, i2, i3, k in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(4096), T.int64(512)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_i3, v_k = T.axis.remap("SSSSR", [i0, i1, i2, i3, k])
                T.reads(lv34[v_i0, v_i1, v_i2, v_k], lv41[v_i0, v_i1, v_k, v_i3])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2, v_i3])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2, v_i3] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2, v_i3] = var_matmul_intermediate[v_i0, v_i1, v_i2, v_i3] + lv34[v_i0, v_i1, v_i2, v_k] * lv41[v_i0, v_i1, v_k, v_i3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], param_0[()])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * param_0[()]

    @T.prim_func(private=True)
    def fused_matmul20_add33_add34(lv279: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), lv280: T.Buffer((T.int64(640), T.int64(640)), "float32"), unet_down_blocks_1_attentions_0_transformer_blocks_0_attn1_to_out_0_bias: T.Buffer((T.int64(640),), "float32"), lv255: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(640)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(640)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(1024), T.int64(640), T.int64(640)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv279[v_i0, v_i1, v_k], lv280[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv279[v_i0, v_i1, v_k] * lv280[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_1_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_1_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv255[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv255[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul21_multiply16(lv265: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32"), lv272: T.Buffer((T.int64(16), T.int64(80), T.int64(1024)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(1024), T.int64(1024)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(1024), T.int64(1024)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(1024), T.int64(1024), T.int64(80)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv265[v_i0, v_i1, v_k], lv272[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv265[v_i0, v_i1, v_k] * lv272[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(1024), T.int64(1024)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.11180339753627777)

    @T.prim_func(private=True)
    def fused_matmul24_multiply17(lv293: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32"), lv300: T.Buffer((T.int64(16), T.int64(80), T.int64(77)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(1024), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(1024), T.int64(77)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(1024), T.int64(77), T.int64(80)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv293[v_i0, v_i1, v_k], lv300[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv293[v_i0, v_i1, v_k] * lv300[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(1024), T.int64(77)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.11180339753627777)

    @T.prim_func(private=True)
    def fused_matmul26_add35_gelu1(lv312: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), lv316: T.Buffer((T.int64(640), T.int64(2560)), "float32"), unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias: T.Buffer((T.int64(2560),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1024), T.int64(2560)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        T_multiply = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        T_multiply_1 = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        T_add = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(1024), T.int64(2560), T.int64(640)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv312[v_i0, v_i1, v_k], lv316[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv312[v_i0, v_i1, v_k] * lv316[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2])
                T_multiply[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.70710678118654757)
        for i0, i1, i2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("compute"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_multiply[v_i0, v_i1, v_i2])
                T.writes(compute[v_i0, v_i1, v_i2])
                compute[v_i0, v_i1, v_i2] = T.erf(T_multiply[v_i0, v_i1, v_i2])
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_multiply_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(compute[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T_multiply_1[v_ax0, v_ax1, v_ax2] = compute[v_ax0, v_ax1, v_ax2] * T.float32(0.5)
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T.writes(T_add[v_ax0, v_ax1, v_ax2])
                T_add[v_ax0, v_ax1, v_ax2] = T.float32(0.5) + T_multiply_1[v_ax0, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_multiply_2"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], T_add[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T_add[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul26_add35_multiply18(lv312: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), lv313: T.Buffer((T.int64(640), T.int64(2560)), "float32"), unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias: T.Buffer((T.int64(2560),), "float32"), lv319: T.Buffer((T.int64(2), T.int64(1024), T.int64(2560)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1024), T.int64(2560)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(2560)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(1024), T.int64(2560), T.int64(640)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv312[v_i0, v_i1, v_k], lv313[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv312[v_i0, v_i1, v_k] * lv313[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(2560)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], lv319[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * lv319[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul27_add33_add34(lv320: T.Buffer((T.int64(2), T.int64(1024), T.int64(2560)), "float32"), lv321: T.Buffer((T.int64(2560), T.int64(640)), "float32"), unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_2_bias: T.Buffer((T.int64(640),), "float32"), lv311: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(640)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(640)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(1024), T.int64(640), T.int64(2560)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv320[v_i0, v_i1, v_k], lv321[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv320[v_i0, v_i1, v_k] * lv321[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_1_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv311[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv311[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul28_add40_add41(lv485: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), lv486: T.Buffer((T.int64(1280), T.int64(1280)), "float32"), unet_down_blocks_2_attentions_0_transformer_blocks_0_attn1_to_out_0_bias: T.Buffer((T.int64(1280),), "float32"), lv461: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(1280)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(1280)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(256), T.int64(1280), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv485[v_i0, v_i1, v_k], lv486[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv485[v_i0, v_i1, v_k] * lv486[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_2_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_2_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv461[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv461[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul29_multiply19(lv471: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32"), lv478: T.Buffer((T.int64(16), T.int64(160), T.int64(256)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(256), T.int64(256)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(256), T.int64(256), T.int64(160)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv471[v_i0, v_i1, v_k], lv478[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv471[v_i0, v_i1, v_k] * lv478[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.079056940972805023)

    @T.prim_func(private=True)
    def fused_matmul32_multiply20(lv499: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32"), lv506: T.Buffer((T.int64(16), T.int64(160), T.int64(77)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(256), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(256), T.int64(77)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(256), T.int64(77), T.int64(160)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv499[v_i0, v_i1, v_k], lv506[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv499[v_i0, v_i1, v_k] * lv506[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(256), T.int64(77)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.079056940972805023)

    @T.prim_func(private=True)
    def fused_matmul34_add42_gelu2(lv518: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), lv522: T.Buffer((T.int64(1280), T.int64(5120)), "float32"), unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias: T.Buffer((T.int64(5120),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(256), T.int64(5120)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        T_multiply = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        compute = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        T_multiply_1 = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        T_add = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(256), T.int64(5120), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv518[v_i0, v_i1, v_k], lv522[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv518[v_i0, v_i1, v_k] * lv522[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2])
                T_multiply[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.70710678118654757)
        for i0, i1, i2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("compute"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_multiply[v_i0, v_i1, v_i2])
                T.writes(compute[v_i0, v_i1, v_i2])
                compute[v_i0, v_i1, v_i2] = T.erf(T_multiply[v_i0, v_i1, v_i2])
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_multiply_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(compute[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T_multiply_1[v_ax0, v_ax1, v_ax2] = compute[v_ax0, v_ax1, v_ax2] * T.float32(0.5)
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T.writes(T_add[v_ax0, v_ax1, v_ax2])
                T_add[v_ax0, v_ax1, v_ax2] = T.float32(0.5) + T_multiply_1[v_ax0, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_multiply_2"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], T_add[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T_add[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul34_add42_multiply21(lv518: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), lv519: T.Buffer((T.int64(1280), T.int64(5120)), "float32"), unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias: T.Buffer((T.int64(5120),), "float32"), lv525: T.Buffer((T.int64(2), T.int64(256), T.int64(5120)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(256), T.int64(5120)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(5120)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(256), T.int64(5120), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv518[v_i0, v_i1, v_k], lv519[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv518[v_i0, v_i1, v_k] * lv519[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(5120)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], lv525[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * lv525[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul35_add40_add41(lv526: T.Buffer((T.int64(2), T.int64(256), T.int64(5120)), "float32"), lv527: T.Buffer((T.int64(5120), T.int64(1280)), "float32"), unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_2_bias: T.Buffer((T.int64(1280),), "float32"), lv517: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(1280)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(1280)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(256), T.int64(1280), T.int64(5120)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv526[v_i0, v_i1, v_k], lv527[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv526[v_i0, v_i1, v_k] * lv527[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_down_blocks_2_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv517[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv517[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul36_add46_add47(lv726: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), lv727: T.Buffer((T.int64(1280), T.int64(1280)), "float32"), unet_mid_block_attentions_0_transformer_blocks_0_attn1_to_out_0_bias: T.Buffer((T.int64(1280),), "float32"), lv702: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(1280)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(1280)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(64), T.int64(1280), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv726[v_i0, v_i1, v_k], lv727[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv726[v_i0, v_i1, v_k] * lv727[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_mid_block_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_mid_block_attentions_0_transformer_blocks_0_attn1_to_out_0_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv702[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv702[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul37_multiply22(lv712: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32"), lv719: T.Buffer((T.int64(16), T.int64(160), T.int64(64)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(64), T.int64(64)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(64), T.int64(64), T.int64(160)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv712[v_i0, v_i1, v_k], lv719[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv712[v_i0, v_i1, v_k] * lv719[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.079056940972805023)

    @T.prim_func(private=True)
    def fused_matmul39_multiply23(lv740: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32"), lv747: T.Buffer((T.int64(16), T.int64(160), T.int64(77)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(16), T.int64(64), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(16), T.int64(64), T.int64(77)))
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(64), T.int64(77), T.int64(160)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv740[v_i0, v_i1, v_k], lv747[v_i0, v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv740[v_i0, v_i1, v_k] * lv747[v_i0, v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(64), T.int64(77)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.079056940972805023)

    @T.prim_func(private=True)
    def fused_matmul3_add17(lv21: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), lv26: T.Buffer((T.int64(768), T.int64(768)), "float32"), self_clip_text_model_encoder_layers_0_self_attn_k_proj_bias: T.Buffer((T.int64(768),), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(77), T.int64(768), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv21[v_i0, v_i1, v_k], lv26[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv21[v_i0, v_i1, v_k] * lv26[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], self_clip_text_model_encoder_layers_0_self_attn_k_proj_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + self_clip_text_model_encoder_layers_0_self_attn_k_proj_bias[v_ax2]

    @T.prim_func(private=True)
    def fused_matmul3_add17_add15(lv50: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), lv51: T.Buffer((T.int64(768), T.int64(768)), "float32"), self_clip_text_model_encoder_layers_0_self_attn_out_proj_bias: T.Buffer((T.int64(768),), "float32"), lv9: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(77), T.int64(768), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv50[v_i0, v_i1, v_k], lv51[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv50[v_i0, v_i1, v_k] * lv51[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], self_clip_text_model_encoder_layers_0_self_attn_out_proj_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + self_clip_text_model_encoder_layers_0_self_attn_out_proj_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(lv9[v_ax0, v_ax1, v_ax2], var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = lv9[v_ax0, v_ax1, v_ax2] + var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul3_add17_multiply7(lv21: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), lv22: T.Buffer((T.int64(768), T.int64(768)), "float32"), self_clip_text_model_encoder_layers_0_self_attn_q_proj_bias: T.Buffer((T.int64(768),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(77), T.int64(768), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv21[v_i0, v_i1, v_k], lv22[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv21[v_i0, v_i1, v_k] * lv22[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], self_clip_text_model_encoder_layers_0_self_attn_q_proj_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + self_clip_text_model_encoder_layers_0_self_attn_q_proj_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.125)

    @T.prim_func(private=True)
    def fused_matmul41_add48_gelu3(lv759: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), lv763: T.Buffer((T.int64(1280), T.int64(5120)), "float32"), unet_mid_block_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias: T.Buffer((T.int64(5120),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(64), T.int64(5120)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        T_multiply = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        compute = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        T_multiply_1 = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        T_add = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(64), T.int64(5120), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv759[v_i0, v_i1, v_k], lv763[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv759[v_i0, v_i1, v_k] * lv763[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_mid_block_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_mid_block_attentions_0_transformer_blocks_0_ff_net_0_proj2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2])
                T_multiply[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T.float32(0.70710678118654757)
        for i0, i1, i2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("compute"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_multiply[v_i0, v_i1, v_i2])
                T.writes(compute[v_i0, v_i1, v_i2])
                compute[v_i0, v_i1, v_i2] = T.erf(T_multiply[v_i0, v_i1, v_i2])
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_multiply_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(compute[v_ax0, v_ax1, v_ax2])
                T.writes(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T_multiply_1[v_ax0, v_ax1, v_ax2] = compute[v_ax0, v_ax1, v_ax2] * T.float32(0.5)
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(T_multiply_1[v_ax0, v_ax1, v_ax2])
                T.writes(T_add[v_ax0, v_ax1, v_ax2])
                T_add[v_ax0, v_ax1, v_ax2] = T.float32(0.5) + T_multiply_1[v_ax0, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_multiply_2"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], T_add[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * T_add[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul41_add48_multiply24(lv759: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), lv760: T.Buffer((T.int64(1280), T.int64(5120)), "float32"), unet_mid_block_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias: T.Buffer((T.int64(5120),), "float32"), lv766: T.Buffer((T.int64(2), T.int64(64), T.int64(5120)), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(64), T.int64(5120)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(5120)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(64), T.int64(5120), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv759[v_i0, v_i1, v_k], lv760[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv759[v_i0, v_i1, v_k] * lv760[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_mid_block_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_mid_block_attentions_0_transformer_blocks_0_ff_net_0_proj1_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(5120)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], lv766[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * lv766[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul42_add46_add47(lv767: T.Buffer((T.int64(2), T.int64(64), T.int64(5120)), "float32"), lv768: T.Buffer((T.int64(5120), T.int64(1280)), "float32"), unet_mid_block_attentions_0_transformer_blocks_0_ff_net_2_bias: T.Buffer((T.int64(1280),), "float32"), lv758: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(1280)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(1280)))
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(64), T.int64(1280), T.int64(5120)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv767[v_i0, v_i1, v_k], lv768[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv767[v_i0, v_i1, v_k] * lv768[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], unet_mid_block_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + unet_mid_block_attentions_0_transformer_blocks_0_ff_net_2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2], lv758[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] + lv758[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul6_add19_multiply8_tir_sigmoid_multiply9(lv55: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), lv56: T.Buffer((T.int64(768), T.int64(3072)), "float32"), self_clip_text_model_encoder_layers_0_mlp_fc1_bias: T.Buffer((T.int64(3072),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(3072)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(3072)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(3072)))
        var_T_multiply_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(3072)))
        var_compute_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(3072)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(77), T.int64(3072), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv55[v_i0, v_i1, v_k], lv56[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv55[v_i0, v_i1, v_k] * lv56[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(3072)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], self_clip_text_model_encoder_layers_0_mlp_fc1_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + self_clip_text_model_encoder_layers_0_mlp_fc1_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(3072)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate_1[v_ax0, v_ax1, v_ax2] = T.float32(1.7020000219345093) * var_T_add_intermediate[v_ax0, v_ax1, v_ax2]
        for i0, i1, i2 in T.grid(T.int64(1), T.int64(77), T.int64(3072)):
            with T.block("compute"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(var_T_multiply_intermediate_1[v_i0, v_i1, v_i2])
                T.writes(var_compute_intermediate[v_i0, v_i1, v_i2])
                var_compute_intermediate[v_i0, v_i1, v_i2] = T.sigmoid(var_T_multiply_intermediate_1[v_i0, v_i1, v_i2])
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(3072)):
            with T.block("T_multiply_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2], var_compute_intermediate[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2] * var_compute_intermediate[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul7_add17_add15(lv61: T.Buffer((T.int64(1), T.int64(77), T.int64(3072)), "float32"), lv62: T.Buffer((T.int64(3072), T.int64(768)), "float32"), self_clip_text_model_encoder_layers_0_mlp_fc2_bias: T.Buffer((T.int64(768),), "float32"), lv54: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        var_T_add_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(77), T.int64(768), T.int64(3072)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv61[v_i0, v_i1, v_k], lv62[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv61[v_i0, v_i1, v_k] * lv62[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], self_clip_text_model_encoder_layers_0_mlp_fc2_bias[v_ax2])
                T.writes(var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + self_clip_text_model_encoder_layers_0_mlp_fc2_bias[v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(lv54[v_ax0, v_ax1, v_ax2], var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = lv54[v_ax0, v_ax1, v_ax2] + var_T_add_intermediate_1[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_matmul8_add20_silu6(lv14: T.Buffer((T.int64(2), T.int64(320)), "float32"), lv15: T.Buffer((T.int64(320), T.int64(1280)), "float32"), unet_time_embedding_linear_1_bias: T.Buffer((T.int64(1280),), "float32"), var_T_multiply_intermediate: T.Buffer((T.int64(2), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280)))
        compute = T.alloc_buffer((T.int64(2), T.int64(1280)))
        for i0, i1, k in T.grid(T.int64(2), T.int64(1280), T.int64(320)):
            with T.block("matmul"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(lv14[v_i0, v_k], lv15[v_k, v_i1])
                T.writes(var_matmul_intermediate[v_i0, v_i1])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1] = var_matmul_intermediate[v_i0, v_i1] + lv14[v_i0, v_k] * lv15[v_k, v_i1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1], unet_time_embedding_linear_1_bias[v_ax1])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1])
                var_T_add_intermediate[v_ax0, v_ax1] = var_matmul_intermediate[v_ax0, v_ax1] + unet_time_embedding_linear_1_bias[v_ax1]
        for i0, i1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("compute"):
                v_i0, v_i1 = T.axis.remap("SS", [i0, i1])
                T.reads(var_T_add_intermediate[v_i0, v_i1])
                T.writes(compute[v_i0, v_i1])
                compute[v_i0, v_i1] = T.sigmoid(var_T_add_intermediate[v_i0, v_i1])
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("T_multiply"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1], compute[v_ax0, v_ax1])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1])
                var_T_multiply_intermediate[v_ax0, v_ax1] = var_T_add_intermediate[v_ax0, v_ax1] * compute[v_ax0, v_ax1]

    @T.prim_func(private=True)
    def fused_matmul9_add20(lv18: T.Buffer((T.int64(2), T.int64(1280)), "float32"), lv19: T.Buffer((T.int64(1280), T.int64(1280)), "float32"), unet_time_embedding_linear_2_bias: T.Buffer((T.int64(1280),), "float32"), var_T_add_intermediate: T.Buffer((T.int64(2), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280)))
        for i0, i1, k in T.grid(T.int64(2), T.int64(1280), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(lv18[v_i0, v_k], lv19[v_k, v_i1])
                T.writes(var_matmul_intermediate[v_i0, v_i1])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1] = var_matmul_intermediate[v_i0, v_i1] + lv18[v_i0, v_k] * lv19[v_k, v_i1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1], unet_time_embedding_linear_2_bias[v_ax1])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1])
                var_T_add_intermediate[v_ax0, v_ax1] = var_matmul_intermediate[v_ax0, v_ax1] + unet_time_embedding_linear_2_bias[v_ax1]

    @T.prim_func(private=True)
    def fused_matmul9_add20_strided_slice5(lv439: T.Buffer((T.int64(2), T.int64(1280)), "float32"), lv440: T.Buffer((T.int64(1280), T.int64(1280)), "float32"), unet_down_blocks_2_resnets_0_time_emb_proj_bias: T.Buffer((T.int64(1280),), "float32"), var_T_strided_slice_with_axes_intermediate: T.Buffer((T.int64(2), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(2), T.int64(1280)))
        for i0, i1, k in T.grid(T.int64(2), T.int64(1280), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(lv439[v_i0, v_k], lv440[v_k, v_i1])
                T.writes(var_matmul_intermediate[v_i0, v_i1])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1] = var_matmul_intermediate[v_i0, v_i1] + lv439[v_i0, v_k] * lv440[v_k, v_i1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("T_add"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1], unet_down_blocks_2_resnets_0_time_emb_proj_bias[v_ax1])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1])
                var_T_add_intermediate[v_ax0, v_ax1] = var_matmul_intermediate[v_ax0, v_ax1] + unet_down_blocks_2_resnets_0_time_emb_proj_bias[v_ax1]
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("T_strided_slice_with_axes"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1])
                T.writes(var_T_strided_slice_with_axes_intermediate[v_ax0, v_ax1])
                var_T_strided_slice_with_axes_intermediate[v_ax0, v_ax1] = var_T_add_intermediate[v_ax0, v_ax1]

    @T.prim_func(private=True)
    def fused_matmul_add4(lv23: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32"), lv24: T.Buffer((T.int64(512), T.int64(512)), "float32"), vae_decoder_mid_block_attentions_0_to_q_bias: T.Buffer((T.int64(512),), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_matmul_intermediate = T.alloc_buffer((T.int64(1), T.int64(4096), T.int64(512)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(4096), T.int64(512), T.int64(512)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(lv23[v_i0, v_i1, v_k], lv24[v_k, v_i2])
                T.writes(var_matmul_intermediate[v_i0, v_i1, v_i2])
                with T.init():
                    var_matmul_intermediate[v_i0, v_i1, v_i2] = T.float32(0)
                var_matmul_intermediate[v_i0, v_i1, v_i2] = var_matmul_intermediate[v_i0, v_i1, v_i2] + lv23[v_i0, v_i1, v_k] * lv24[v_k, v_i2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(4096), T.int64(512)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_matmul_intermediate[v_ax0, v_ax1, v_ax2], vae_decoder_mid_block_attentions_0_to_q_bias[v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_matmul_intermediate[v_ax0, v_ax1, v_ax2] + vae_decoder_mid_block_attentions_0_to_q_bias[v_ax2]

    @T.prim_func(private=True)
    def fused_reshape11_reshape11_add15(lv3: T.Buffer((T.int64(77), T.int64(768)), "float32"), lv7: T.Buffer((T.int64(77), T.int64(768)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(768)))
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(lv3[(v_ax2 // T.int64(768) + v_ax1) % T.int64(77), v_ax2 % T.int64(768)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = lv3[(v_ax2 // T.int64(768) + v_ax1) % T.int64(77), v_ax2 % T.int64(768)]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(lv7[(v_ax2 // T.int64(768) + v_ax1) % T.int64(77), v_ax2 % T.int64(768)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = lv7[(v_ax2 // T.int64(768) + v_ax1) % T.int64(77), v_ax2 % T.int64(768)]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2], var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] + var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def fused_reshape14_transpose8_reshape15(lv33: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(12), T.int64(77), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(12), T.int64(64)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(1), T.int64(12), T.int64(77), T.int64(64)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(77), T.int64(12), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv33[T.int64(0), ((v_ax2 * T.int64(64) + v_ax3) // T.int64(768) + v_ax1) % T.int64(77), (v_ax2 * T.int64(64) + v_ax3) % T.int64(768)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv33[T.int64(0), ((v_ax2 * T.int64(64) + v_ax3) // T.int64(768) + v_ax1) % T.int64(77), (v_ax2 * T.int64(64) + v_ax3) % T.int64(768)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(12), T.int64(77), T.int64(64)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(12), T.int64(77), T.int64(64)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[T.int64(0), ((v_ax2 // T.int64(64) + v_ax1) // T.int64(77) + v_ax0) % T.int64(12), (v_ax2 // T.int64(64) + v_ax1) % T.int64(77), v_ax2 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[T.int64(0), ((v_ax2 // T.int64(64) + v_ax1) // T.int64(77) + v_ax0) % T.int64(12), (v_ax2 // T.int64(64) + v_ax1) % T.int64(77), v_ax2 % T.int64(64)]

    @T.prim_func(private=True)
    def fused_reshape14_transpose8_reshape15_transpose9(lv28: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(12), T.int64(64), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(12), T.int64(64)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(12), T.int64(77), T.int64(64)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(12), T.int64(77), T.int64(64)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(77), T.int64(12), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv28[T.int64(0), ((v_ax2 * T.int64(64) + v_ax3) // T.int64(768) + v_ax1) % T.int64(77), (v_ax2 * T.int64(64) + v_ax3) % T.int64(768)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv28[T.int64(0), ((v_ax2 * T.int64(64) + v_ax3) // T.int64(768) + v_ax1) % T.int64(77), (v_ax2 * T.int64(64) + v_ax3) % T.int64(768)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(12), T.int64(77), T.int64(64)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(12), T.int64(77), T.int64(64)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[T.int64(0), ((v_ax2 // T.int64(64) + v_ax1) // T.int64(77) + v_ax0) % T.int64(12), (v_ax2 // T.int64(64) + v_ax1) % T.int64(77), v_ax2 % T.int64(64)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[T.int64(0), ((v_ax2 // T.int64(64) + v_ax1) // T.int64(77) + v_ax0) % T.int64(12), (v_ax2 // T.int64(64) + v_ax1) % T.int64(77), v_ax2 % T.int64(64)]
        for ax0, ax1, ax2 in T.grid(T.int64(12), T.int64(64), T.int64(77)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape16_add18_reshape17(lv42: T.Buffer((T.int64(12), T.int64(77), T.int64(77)), "float32"), param_0: T.Buffer((T.int64(1), T.int64(1), T.int64(77), T.int64(77)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(12), T.int64(77), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(12), T.int64(77), T.int64(77)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(12), T.int64(77), T.int64(77)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv42[((v_ax3 // T.int64(77) + v_ax2) // T.int64(77) + v_ax1) % T.int64(12), (v_ax3 // T.int64(77) + v_ax2) % T.int64(77), v_ax3 % T.int64(77)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv42[((v_ax3 // T.int64(77) + v_ax2) // T.int64(77) + v_ax1) % T.int64(12), (v_ax3 // T.int64(77) + v_ax2) % T.int64(77), v_ax3 % T.int64(77)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], param_0[v_ax0, T.int64(0), v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] + param_0[v_ax0, T.int64(0), v_ax2, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_add_intermediate[T.int64(0), ((v_ax2 // T.int64(77) + v_ax1) // T.int64(77) + v_ax0) % T.int64(12), (v_ax2 // T.int64(77) + v_ax1) % T.int64(77), v_ax2 % T.int64(77)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_add_intermediate[T.int64(0), ((v_ax2 // T.int64(77) + v_ax1) // T.int64(77) + v_ax0) % T.int64(12), (v_ax2 // T.int64(77) + v_ax1) % T.int64(77), v_ax2 % T.int64(77)]

    @T.prim_func(private=True)
    def fused_reshape18_transpose10_reshape19(lv47: T.Buffer((T.int64(12), T.int64(77), T.int64(64)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(12), T.int64(77), T.int64(64)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(1), T.int64(77), T.int64(12), T.int64(64)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(12), T.int64(77), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv47[((v_ax3 // T.int64(64) + v_ax2) // T.int64(77) + v_ax1) % T.int64(12), (v_ax3 // T.int64(64) + v_ax2) % T.int64(77), v_ax3 % T.int64(64)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv47[((v_ax3 // T.int64(64) + v_ax2) // T.int64(77) + v_ax1) % T.int64(12), (v_ax3 // T.int64(64) + v_ax2) % T.int64(77), v_ax3 % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(77), T.int64(12), T.int64(64)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[T.int64(0), (v_ax2 // T.int64(768) + v_ax1) % T.int64(77), v_ax2 % T.int64(768) // T.int64(64), v_ax2 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[T.int64(0), (v_ax2 // T.int64(768) + v_ax1) % T.int64(77), v_ax2 % T.int64(768) // T.int64(64), v_ax2 % T.int64(64)]

    @T.prim_func(private=True)
    def fused_reshape25_transpose18_reshape26(lv52: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(8), T.int64(40)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(4096), T.int64(40)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(4096), T.int64(8), T.int64(40)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv52[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(4096), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv52[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(4096), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(4096), T.int64(40)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(4096), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(4096), v_ax2 % T.int64(40)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(4096), v_ax2 % T.int64(40)]

    @T.prim_func(private=True)
    def fused_reshape25_transpose18_reshape26_transpose19(lv54: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(40), T.int64(4096)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(8), T.int64(40)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(4096), T.int64(40)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(4096), T.int64(40)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(4096), T.int64(8), T.int64(40)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv54[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(4096), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv54[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(4096), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(4096), T.int64(40)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(4096), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(4096), v_ax2 % T.int64(40)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(4096), v_ax2 % T.int64(40)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(40), T.int64(4096)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape27_transpose20_reshape28(lv70: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(4096), T.int64(40)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(4096), T.int64(8), T.int64(40)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(4096), T.int64(40)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv70[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(40) + v_ax2) // T.int64(4096) + v_ax1) % T.int64(16), (v_ax3 // T.int64(40) + v_ax2) % T.int64(4096), v_ax3 % T.int64(40)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv70[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(40) + v_ax2) // T.int64(4096) + v_ax1) % T.int64(16), (v_ax3 // T.int64(40) + v_ax2) % T.int64(4096), v_ax3 % T.int64(40)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(4096), T.int64(8), T.int64(40)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), (v_ax2 // T.int64(320) + v_ax1) % T.int64(4096), v_ax2 % T.int64(320) // T.int64(40), v_ax2 % T.int64(40)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), (v_ax2 // T.int64(320) + v_ax1) % T.int64(4096), v_ax2 % T.int64(320) // T.int64(40), v_ax2 % T.int64(40)]

    @T.prim_func(private=True)
    def fused_reshape29_transpose22_reshape30(lv84: T.Buffer((T.int64(2), T.int64(77), T.int64(320)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(77), T.int64(40)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(77), T.int64(8), T.int64(40)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(77), T.int64(40)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(77), T.int64(8), T.int64(40)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv84[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(77), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv84[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(77), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(77), T.int64(40)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(77), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(77), v_ax2 % T.int64(40)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(77), v_ax2 % T.int64(40)]

    @T.prim_func(private=True)
    def fused_reshape29_transpose22_reshape30_transpose23(lv82: T.Buffer((T.int64(2), T.int64(77), T.int64(320)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(40), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(77), T.int64(8), T.int64(40)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(77), T.int64(40)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(77), T.int64(40)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(77), T.int64(8), T.int64(40)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv82[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(77), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv82[(((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(40) + v_ax3) // T.int64(320) + v_ax1) % T.int64(77), (v_ax2 * T.int64(40) + v_ax3) % T.int64(320)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(77), T.int64(40)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(77), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(77), v_ax2 % T.int64(40)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(40) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(40) + v_ax1) % T.int64(77), v_ax2 % T.int64(40)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(40), T.int64(77)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape2_transpose_transpose1(lv18: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(4096)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(4096)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(4096), T.int64(512)))
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(512), T.int64(4096)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(lv18[T.int64(0), (v_ax2 // T.int64(4096) + v_ax1) % T.int64(512), v_ax2 % T.int64(4096) // T.int64(64), v_ax2 % T.int64(64)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = lv18[T.int64(0), (v_ax2 // T.int64(4096) + v_ax1) % T.int64(512), v_ax2 % T.int64(4096) // T.int64(64), v_ax2 % T.int64(64)]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(4096), T.int64(512)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(512), T.int64(4096)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape31_transpose24(lv118: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(64), T.int64(320)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(64), T.int64(64), T.int64(320)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv118[((v_ax1 * T.int64(64) + v_ax3 // T.int64(320) + v_ax2) // T.int64(4096) + v_ax0) % T.int64(2), (v_ax1 * T.int64(64) + v_ax3 // T.int64(320) + v_ax2) % T.int64(4096), v_ax3 % T.int64(320)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv118[((v_ax1 * T.int64(64) + v_ax3 // T.int64(320) + v_ax2) // T.int64(4096) + v_ax0) % T.int64(2), (v_ax1 * T.int64(64) + v_ax3 // T.int64(320) + v_ax2) % T.int64(4096), v_ax3 % T.int64(320)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape35_transpose28_reshape36(lv258: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(8), T.int64(80)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(1024), T.int64(80)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1024), T.int64(8), T.int64(80)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv258[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(1024), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv258[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(1024), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(1024), T.int64(80)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(1024), T.int64(80)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(1024), v_ax2 % T.int64(80)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(1024), v_ax2 % T.int64(80)]

    @T.prim_func(private=True)
    def fused_reshape35_transpose28_reshape36_transpose29(lv260: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(80), T.int64(1024)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(8), T.int64(80)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(1024), T.int64(80)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(1024), T.int64(80)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1024), T.int64(8), T.int64(80)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv260[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(1024), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv260[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(1024), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(1024), T.int64(80)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(1024), T.int64(80)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(1024), v_ax2 % T.int64(80)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(1024), v_ax2 % T.int64(80)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(80), T.int64(1024)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape37_transpose30_reshape38(lv276: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(1024), T.int64(80)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(1024), T.int64(8), T.int64(80)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(1024), T.int64(80)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv276[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(80) + v_ax2) // T.int64(1024) + v_ax1) % T.int64(16), (v_ax3 // T.int64(80) + v_ax2) % T.int64(1024), v_ax3 % T.int64(80)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv276[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(80) + v_ax2) // T.int64(1024) + v_ax1) % T.int64(16), (v_ax3 // T.int64(80) + v_ax2) % T.int64(1024), v_ax3 % T.int64(80)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1024), T.int64(8), T.int64(80)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), (v_ax2 // T.int64(640) + v_ax1) % T.int64(1024), v_ax2 % T.int64(640) // T.int64(80), v_ax2 % T.int64(80)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), (v_ax2 // T.int64(640) + v_ax1) % T.int64(1024), v_ax2 % T.int64(640) // T.int64(80), v_ax2 % T.int64(80)]

    @T.prim_func(private=True)
    def fused_reshape39_transpose32_reshape40(lv290: T.Buffer((T.int64(2), T.int64(77), T.int64(640)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(77), T.int64(80)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(77), T.int64(8), T.int64(80)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(77), T.int64(80)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(77), T.int64(8), T.int64(80)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv290[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(77), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv290[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(77), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(77), T.int64(80)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(77), T.int64(80)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(77), v_ax2 % T.int64(80)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(77), v_ax2 % T.int64(80)]

    @T.prim_func(private=True)
    def fused_reshape39_transpose32_reshape40_transpose33(lv288: T.Buffer((T.int64(2), T.int64(77), T.int64(640)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(80), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(77), T.int64(8), T.int64(80)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(77), T.int64(80)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(77), T.int64(80)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(77), T.int64(8), T.int64(80)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv288[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(77), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv288[(((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(80) + v_ax3) // T.int64(640) + v_ax1) % T.int64(77), (v_ax2 * T.int64(80) + v_ax3) % T.int64(640)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(77), T.int64(80)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(77), T.int64(80)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(77), v_ax2 % T.int64(80)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(80) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(80) + v_ax1) % T.int64(77), v_ax2 % T.int64(80)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(80), T.int64(77)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape3_transpose3(lv26: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(4096), T.int64(1), T.int64(512)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4096), T.int64(1), T.int64(512)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv26[T.int64(0), (v_ax3 // T.int64(512) + v_ax1 + v_ax2) % T.int64(4096), v_ax3 % T.int64(512)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv26[T.int64(0), (v_ax3 // T.int64(512) + v_ax1 + v_ax2) % T.int64(4096), v_ax3 % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(512)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]

    @T.prim_func(private=True)
    def fused_reshape3_transpose3_transpose4(lv29: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(1), T.int64(1), T.int64(512), T.int64(4096)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(4096), T.int64(1), T.int64(512)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(512)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4096), T.int64(1), T.int64(512)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv29[T.int64(0), (v_ax3 // T.int64(512) + v_ax1 + v_ax2) % T.int64(4096), v_ax3 % T.int64(512)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv29[T.int64(0), (v_ax3 // T.int64(512) + v_ax1 + v_ax2) % T.int64(4096), v_ax3 % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(512)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1), T.int64(512), T.int64(4096)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax3, v_ax2])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax3, v_ax2]

    @T.prim_func(private=True)
    def fused_reshape41_transpose36(lv324: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(32), T.int64(640)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(32), T.int64(32), T.int64(640)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv324[((v_ax1 * T.int64(32) + v_ax3 // T.int64(640) + v_ax2) // T.int64(1024) + v_ax0) % T.int64(2), (v_ax1 * T.int64(32) + v_ax3 // T.int64(640) + v_ax2) % T.int64(1024), v_ax3 % T.int64(640)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv324[((v_ax1 * T.int64(32) + v_ax3 // T.int64(640) + v_ax2) // T.int64(1024) + v_ax0) % T.int64(2), (v_ax1 * T.int64(32) + v_ax3 // T.int64(640) + v_ax2) % T.int64(1024), v_ax3 % T.int64(640)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape45_transpose38_reshape46(lv464: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(8), T.int64(160)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(256), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(256), T.int64(8), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv464[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(256), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv464[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(256), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(256), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(256), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(256), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(256), v_ax2 % T.int64(160)]

    @T.prim_func(private=True)
    def fused_reshape45_transpose38_reshape46_transpose39(lv466: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(160), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(8), T.int64(160)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(256), T.int64(160)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(256), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(256), T.int64(8), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv466[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(256), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv466[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(256), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(256), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(256), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(256), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(256) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(256), v_ax2 % T.int64(160)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(160), T.int64(256)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape47_transpose40_reshape48(lv482: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(256), T.int64(160)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(256), T.int64(8), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(256), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv482[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(160) + v_ax2) // T.int64(256) + v_ax1) % T.int64(16), (v_ax3 // T.int64(160) + v_ax2) % T.int64(256), v_ax3 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv482[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(160) + v_ax2) // T.int64(256) + v_ax1) % T.int64(16), (v_ax3 // T.int64(160) + v_ax2) % T.int64(256), v_ax3 % T.int64(160)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(256), T.int64(8), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(256), v_ax2 % T.int64(1280) // T.int64(160), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(256), v_ax2 % T.int64(1280) // T.int64(160), v_ax2 % T.int64(160)]

    @T.prim_func(private=True)
    def fused_reshape49_transpose42_reshape50(lv496: T.Buffer((T.int64(2), T.int64(77), T.int64(1280)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(77), T.int64(160)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(77), T.int64(8), T.int64(160)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(77), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(77), T.int64(8), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv496[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(77), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv496[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(77), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(77), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(77), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(77), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(77), v_ax2 % T.int64(160)]

    @T.prim_func(private=True)
    def fused_reshape49_transpose42_reshape50_transpose43(lv494: T.Buffer((T.int64(2), T.int64(77), T.int64(1280)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(160), T.int64(77)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(77), T.int64(8), T.int64(160)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(77), T.int64(160)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(77), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(77), T.int64(8), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv494[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(77), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv494[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(77) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(77), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(77), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(77), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(77), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(77) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(77), v_ax2 % T.int64(160)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(160), T.int64(77)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape51_transpose46(lv530: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(16), T.int64(16), T.int64(1280)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(16), T.int64(16), T.int64(1280)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv530[((v_ax1 * T.int64(16) + v_ax3 // T.int64(1280) + v_ax2) // T.int64(256) + v_ax0) % T.int64(2), (v_ax1 * T.int64(16) + v_ax3 // T.int64(1280) + v_ax2) % T.int64(256), v_ax3 % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv530[((v_ax1 * T.int64(16) + v_ax3 // T.int64(1280) + v_ax2) // T.int64(256) + v_ax0) % T.int64(2), (v_ax1 * T.int64(16) + v_ax3 // T.int64(1280) + v_ax2) % T.int64(256), v_ax3 % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape53_transpose48_reshape54(lv705: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(8), T.int64(160)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(64), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(64), T.int64(8), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv705[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(64), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv705[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(64), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(64), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(64), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(64), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(64), v_ax2 % T.int64(160)]

    @T.prim_func(private=True)
    def fused_reshape53_transpose48_reshape54_transpose49(lv707: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(16), T.int64(160), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(8), T.int64(160)))
        var_T_transpose_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(64), T.int64(160)))
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(16), T.int64(64), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(64), T.int64(8), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv707[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(64), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv707[(((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), ((v_ax2 * T.int64(160) + v_ax3) // T.int64(1280) + v_ax1) % T.int64(64), (v_ax2 * T.int64(160) + v_ax3) % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(64), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(64), T.int64(160)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate_1[((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(64), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate_1[((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(16) // T.int64(8), ((v_ax2 // T.int64(160) + v_ax1) // T.int64(64) + v_ax0) % T.int64(8), (v_ax2 // T.int64(160) + v_ax1) % T.int64(64), v_ax2 % T.int64(160)]
        for ax0, ax1, ax2 in T.grid(T.int64(16), T.int64(160), T.int64(64)):
            with T.block("T_transpose_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape55_transpose50_reshape56(lv723: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(64), T.int64(160)))
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(8), T.int64(160)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(64), T.int64(160)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv723[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(160) + v_ax2) // T.int64(64) + v_ax1) % T.int64(16), (v_ax3 // T.int64(160) + v_ax2) % T.int64(64), v_ax3 % T.int64(160)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv723[(v_ax0 * T.int64(8) + (v_ax3 // T.int64(160) + v_ax2) // T.int64(64) + v_ax1) % T.int64(16), (v_ax3 // T.int64(160) + v_ax2) % T.int64(64), v_ax3 % T.int64(160)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(64), T.int64(8), T.int64(160)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate_1[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(64), v_ax2 % T.int64(1280) // T.int64(160), v_ax2 % T.int64(160)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(64), v_ax2 % T.int64(1280) // T.int64(160), v_ax2 % T.int64(160)]

    @T.prim_func(private=True)
    def fused_reshape57_transpose51(lv771: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), var_T_transpose_intermediate: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(8), T.int64(1280)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(8), T.int64(1280)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv771[((v_ax1 * T.int64(8) + v_ax3 // T.int64(1280) + v_ax2) // T.int64(64) + v_ax0) % T.int64(2), (v_ax1 * T.int64(8) + v_ax3 // T.int64(1280) + v_ax2) % T.int64(64), v_ax3 % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv771[((v_ax1 * T.int64(8) + v_ax3 // T.int64(1280) + v_ax2) // T.int64(64) + v_ax0) % T.int64(2), (v_ax1 * T.int64(8) + v_ax3 // T.int64(1280) + v_ax2) % T.int64(64), v_ax3 % T.int64(1280)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax2, v_ax3, v_ax1]

    @T.prim_func(private=True)
    def fused_reshape9_cast_reshape10(inp_0: T.Buffer((T.int64(1), T.int64(77)), "int32"), var_T_reshape_intermediate: T.Buffer((T.int64(77),), "int32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_reshape_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(77)), "int32")
        var_compute_intermediate = T.alloc_buffer((T.int64(1), T.int64(77)), "int32")
        for ax0, ax1 in T.grid(T.int64(1), T.int64(77)):
            with T.block("T_reshape"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(inp_0[T.int64(0), v_ax1 % T.int64(77)])
                T.writes(var_T_reshape_intermediate_1[v_ax0, v_ax1])
                var_T_reshape_intermediate_1[v_ax0, v_ax1] = inp_0[T.int64(0), v_ax1 % T.int64(77)]
        for i0, i1 in T.grid(T.int64(1), T.int64(77)):
            with T.block("compute"):
                v_i0, v_i1 = T.axis.remap("SS", [i0, i1])
                T.reads(var_T_reshape_intermediate_1[v_i0, v_i1])
                T.writes(var_compute_intermediate[v_i0, v_i1])
                var_compute_intermediate[v_i0, v_i1] = var_T_reshape_intermediate_1[v_i0, v_i1]
        for ax0 in range(T.int64(77)):
            with T.block("T_reshape_1"):
                v_ax0 = T.axis.spatial(T.int64(77), ax0)
                T.reads(var_compute_intermediate[T.int64(0), v_ax0 % T.int64(77)])
                T.writes(var_T_reshape_intermediate[v_ax0])
                var_T_reshape_intermediate[v_ax0] = var_compute_intermediate[T.int64(0), v_ax0 % T.int64(77)]

    @T.prim_func(private=True)
    def fused_split_subtract_multiply25_add(lv1818: T.Buffer((T.int64(2), T.int64(4), T.int64(64), T.int64(64)), "float32"), var_T_add_intermediate: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_split_sections_intermediate = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)))
        var_T_split_sections_intermediate_1 = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)))
        var_T_subtract_intermediate = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)))
        var_T_multiply_intermediate = T.alloc_buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_split_sections"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv1818[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_split_sections_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_split_sections_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv1818[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_split_sections_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv1818[v_ax0 + T.int64(1), v_ax1, v_ax2, v_ax3])
                T.writes(var_T_split_sections_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_split_sections_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv1818[v_ax0 + T.int64(1), v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_split_sections_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3], var_T_split_sections_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_subtract_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_subtract_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_split_sections_intermediate_1[v_ax0, v_ax1, v_ax2, v_ax3] - var_T_split_sections_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_subtract_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(7.5) * var_T_subtract_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_split_sections_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_split_sections_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_transpose16_reshape24(lv47: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(64), T.int64(64), T.int64(320)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(64), T.int64(64), T.int64(320)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv47[v_ax0, v_ax3, v_ax1, v_ax2])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv47[v_ax0, v_ax3, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), (v_ax2 // T.int64(320) + v_ax1) % T.int64(4096) // T.int64(64), (v_ax2 // T.int64(320) + v_ax1) % T.int64(64), v_ax2 % T.int64(320)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(320) + v_ax1) // T.int64(4096) + v_ax0) % T.int64(2), (v_ax2 // T.int64(320) + v_ax1) % T.int64(4096) // T.int64(64), (v_ax2 // T.int64(320) + v_ax1) % T.int64(64), v_ax2 % T.int64(320)]

    @T.prim_func(private=True)
    def fused_transpose1_reshape5_add3_divide3(lv50: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32"), lv18: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), var_T_divide_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(4096)))
        var_T_reshape_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        var_T_add_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(512), T.int64(4096)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(lv50[v_ax0, v_ax2, v_ax1])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2] = lv50[v_ax0, v_ax2, v_ax1]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_transpose_intermediate[T.int64(0), ((v_ax2 * T.int64(64) + v_ax3) // T.int64(4096) + v_ax1) % T.int64(512), (v_ax2 * T.int64(64) + v_ax3) % T.int64(4096)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_transpose_intermediate[T.int64(0), ((v_ax2 * T.int64(64) + v_ax3) // T.int64(4096) + v_ax1) % T.int64(512), (v_ax2 * T.int64(64) + v_ax3) % T.int64(4096)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3], lv18[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] + lv18[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(64), T.int64(64)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_divide_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_add_intermediate[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def fused_transpose26_reshape34(lv253: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(32), T.int64(640)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(32), T.int64(32), T.int64(640)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv253[v_ax0, v_ax3, v_ax1, v_ax2])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv253[v_ax0, v_ax3, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), (v_ax2 // T.int64(640) + v_ax1) % T.int64(1024) // T.int64(32), (v_ax2 // T.int64(640) + v_ax1) % T.int64(32), v_ax2 % T.int64(640)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(640) + v_ax1) // T.int64(1024) + v_ax0) % T.int64(2), (v_ax2 // T.int64(640) + v_ax1) % T.int64(1024) // T.int64(32), (v_ax2 // T.int64(640) + v_ax1) % T.int64(32), v_ax2 % T.int64(640)]

    @T.prim_func(private=True)
    def fused_transpose37_reshape44(lv459: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(16), T.int64(16), T.int64(1280)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(16), T.int64(16), T.int64(1280)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv459[v_ax0, v_ax3, v_ax1, v_ax2])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv459[v_ax0, v_ax3, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(256) // T.int64(16), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(16), v_ax2 % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(256) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(256) // T.int64(16), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(16), v_ax2 % T.int64(1280)]

    @T.prim_func(private=True)
    def fused_transpose47_reshape52(lv700: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(2), T.int64(8), T.int64(8), T.int64(1280)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(8), T.int64(8), T.int64(1280)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv700[v_ax0, v_ax3, v_ax1, v_ax2])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv700[v_ax0, v_ax3, v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(64) // T.int64(8), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(8), v_ax2 % T.int64(1280)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[((v_ax2 // T.int64(1280) + v_ax1) // T.int64(64) + v_ax0) % T.int64(2), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(64) // T.int64(8), (v_ax2 // T.int64(1280) + v_ax1) % T.int64(8), v_ax2 % T.int64(1280)]

    @T.prim_func(private=True)
    def fused_transpose5_reshape4(lv45: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(512)), "float32"), var_T_reshape_intermediate: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(1), T.int64(4096), T.int64(1), T.int64(512)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4096), T.int64(1), T.int64(512)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv45[v_ax0, v_ax2, v_ax1, v_ax3])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv45[v_ax0, v_ax2, v_ax1, v_ax3]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(4096), T.int64(512)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(var_T_transpose_intermediate[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(4096), T.int64(0), v_ax2 % T.int64(512)])
                T.writes(var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2])
                var_T_reshape_intermediate[v_ax0, v_ax1, v_ax2] = var_T_transpose_intermediate[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(4096), T.int64(0), v_ax2 % T.int64(512)]

    @T.prim_func(private=True)
    def fused_transpose6_multiply6_tir_round(lv237: T.Buffer((T.int64(1), T.int64(3), T.int64(512), T.int64(512)), "float32"), var_compute_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(512), T.int64(3)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        var_T_transpose_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(512), T.int64(3)))
        var_T_multiply_intermediate = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(512), T.int64(3)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(512), T.int64(3)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv237[v_ax0, v_ax3, v_ax1, v_ax2])
                T.writes(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = lv237[v_ax0, v_ax3, v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(512), T.int64(3)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3])
                var_T_multiply_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] = var_T_transpose_intermediate[v_ax0, v_ax1, v_ax2, v_ax3] * T.float32(255)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(512), T.int64(3)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(var_T_multiply_intermediate[v_i0, v_i1, v_i2, v_i3])
                T.writes(var_compute_intermediate[v_i0, v_i1, v_i2, v_i3])
                var_compute_intermediate[v_i0, v_i1, v_i2, v_i3] = T.round(var_T_multiply_intermediate[v_i0, v_i1, v_i2, v_i3])

    @T.prim_func(private=True)
    def group_norm1(A: T.Buffer((T.int64(1), T.int64(512), T.int64(4096)), "float32"), B: T.Buffer((T.int64(512),), "float32"), C: T.Buffer((T.int64(512),), "float32"), T_reshape: T.Buffer((T.int64(1), T.int64(512), T.int64(4096)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(4096)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(32)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_reshape_3 = T.alloc_buffer((T.int64(32), T.int64(16)))
        T_group_norm = T.alloc_buffer((T.int64(1), T.int64(32), T.int64(16), T.int64(4096)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(4096)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[T.int64(0), (v_ax1 * T.int64(16) + v_ax3 // T.int64(4096) + v_ax2) % T.int64(512), v_ax3 % T.int64(4096)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = A[T.int64(0), (v_ax1 * T.int64(16) + v_ax3 // T.int64(4096) + v_ax2) % T.int64(512), v_ax3 % T.int64(4096)]
        for ax0, ax1, k2, k3 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(4096)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3 = T.axis.remap("SSRR", [ax0, ax1, k2, k3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_k2, v_k3])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3] * T_reshape_1[v_ax0, v_ax1, v_k2, v_k3]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(B[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = B[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(16)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(C[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)])
                T.writes(T_reshape_3[v_ax0, v_ax1])
                T_reshape_3[v_ax0, v_ax1] = C[(v_ax0 * T.int64(16) + v_ax1) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(32), T.int64(16), T.int64(4096)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_2[v_ax1, v_ax2], T_reshape_3[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3] = (T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.52587890625e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(1.52587890625e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.52587890625e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(1.52587890625e-05)) + T.float32(9.9999999999999995e-07)) * T_reshape_2[v_ax1, v_ax2] + T_reshape_3[v_ax1, v_ax2]
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(512), T.int64(4096)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(T_group_norm[T.int64(0), (v_ax2 // T.int64(4096) + v_ax1) % T.int64(512) // T.int64(16), (v_ax2 // T.int64(4096) + v_ax1) % T.int64(16), v_ax2 % T.int64(4096)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2])
                T_reshape[v_ax0, v_ax1, v_ax2] = T_group_norm[T.int64(0), (v_ax2 // T.int64(4096) + v_ax1) % T.int64(512) // T.int64(16), (v_ax2 // T.int64(4096) + v_ax1) % T.int64(16), v_ax2 % T.int64(4096)]

    @T.prim_func(private=True)
    def group_norm11(A: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), B: T.Buffer((T.int64(640),), "float32"), C: T.Buffer((T.int64(640),), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape_1 = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_reshape_3 = T.alloc_buffer((T.int64(32), T.int64(20)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(A[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(640), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = A[((v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 * T.int64(20) + (v_ax4 // T.int64(32) + v_ax3) // T.int64(32) + v_ax2) % T.int64(640), (v_ax4 // T.int64(32) + v_ax3) % T.int64(32), v_ax4 % T.int64(32)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(B[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = B[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(20)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(C[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)])
                T.writes(T_reshape_3[v_ax0, v_ax1])
                T_reshape_3[v_ax0, v_ax1] = C[(v_ax0 * T.int64(20) + v_ax1) % T.int64(640)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(20), T.int64(32), T.int64(32)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_2[v_ax1, v_ax2], T_reshape_3[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(4.8828125000000003e-05)) + T.float32(9.9999999999999995e-07)) * T_reshape_2[v_ax1, v_ax2] + T_reshape_3[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(32), T.int64(32)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(20), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) // T.int64(640) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(640) // T.int64(20), ((v_ax3 // T.int64(32) + v_ax2) // T.int64(32) + v_ax1) % T.int64(20), (v_ax3 // T.int64(32) + v_ax2) % T.int64(32), v_ax3 % T.int64(32)]

    @T.prim_func(private=True)
    def group_norm14(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), B: T.Buffer((T.int64(1280),), "float32"), C: T.Buffer((T.int64(1280),), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape_1 = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_reshape_3 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(A[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = A[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(16) + v_ax3) // T.int64(16) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(16) + v_ax3) % T.int64(16), v_ax4 % T.int64(16)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(B[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = B[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(C[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_3[v_ax0, v_ax1])
                T_reshape_3[v_ax0, v_ax1] = C[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(16), T.int64(16)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_2[v_ax1, v_ax2], T_reshape_3[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(9.7656250000000005e-05)) + T.float32(9.9999999999999995e-07)) * T_reshape_2[v_ax1, v_ax2] + T_reshape_3[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(40), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(16) + v_ax2) // T.int64(16) + v_ax1) % T.int64(40), (v_ax3 // T.int64(16) + v_ax2) % T.int64(16), v_ax3 % T.int64(16)]

    @T.prim_func(private=True)
    def group_norm16(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), B: T.Buffer((T.int64(1280),), "float32"), C: T.Buffer((T.int64(1280),), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape_1 = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_reshape_3 = T.alloc_buffer((T.int64(32), T.int64(40)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(A[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(8) + v_ax3) % T.int64(8), v_ax4 % T.int64(8)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = A[((v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 * T.int64(40) + (v_ax4 // T.int64(8) + v_ax3) // T.int64(8) + v_ax2) % T.int64(1280), (v_ax4 // T.int64(8) + v_ax3) % T.int64(8), v_ax4 % T.int64(8)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(B[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = B[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(40)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(C[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)])
                T.writes(T_reshape_3[v_ax0, v_ax1])
                T_reshape_3[v_ax0, v_ax1] = C[(v_ax0 * T.int64(40) + v_ax1) % T.int64(1280)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(40), T.int64(8), T.int64(8)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_2[v_ax1, v_ax2], T_reshape_3[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00039062500000000002)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.00039062500000000002) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00039062500000000002) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00039062500000000002)) + T.float32(9.9999999999999995e-07)) * T_reshape_2[v_ax1, v_ax2] + T_reshape_3[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(8), T.int64(8)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(40), (v_ax3 // T.int64(8) + v_ax2) % T.int64(8), v_ax3 % T.int64(8)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) // T.int64(1280) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(1280) // T.int64(40), ((v_ax3 // T.int64(8) + v_ax2) // T.int64(8) + v_ax1) % T.int64(40), (v_ax3 // T.int64(8) + v_ax2) % T.int64(8), v_ax3 % T.int64(8)]

    @T.prim_func(private=True)
    def group_norm8(A: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(320),), "float32"), C: T.Buffer((T.int64(320),), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(320), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_reshape_1 = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)))
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(32)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(32)))
        T_reshape_2 = T.alloc_buffer((T.int64(32), T.int64(10)))
        T_reshape_3 = T.alloc_buffer((T.int64(32), T.int64(10)))
        T_group_norm = T.alloc_buffer((T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)))
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(A[((v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(320), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = A[((v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 * T.int64(10) + (v_ax4 // T.int64(64) + v_ax3) // T.int64(64) + v_ax2) % T.int64(320), (v_ax4 // T.int64(64) + v_ax3) % T.int64(64), v_ax4 % T.int64(64)]
        for ax0, ax1, k2, k3, k4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2, v_k3, v_k4 = T.axis.remap("SSRRR", [ax0, ax1, k2, k3, k4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4] * T_reshape_1[v_ax0, v_ax1, v_k2, v_k3, v_k4]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1 in T.grid(T.int64(32), T.int64(10)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(B[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)])
                T.writes(T_reshape_2[v_ax0, v_ax1])
                T_reshape_2[v_ax0, v_ax1] = B[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)]
        for ax0, ax1 in T.grid(T.int64(32), T.int64(10)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(C[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)])
                T.writes(T_reshape_3[v_ax0, v_ax1])
                T_reshape_3[v_ax0, v_ax1] = C[(v_ax0 * T.int64(10) + v_ax1) % T.int64(320)]
        for ax0, ax1, ax2, ax3, ax4 in T.grid(T.int64(2), T.int64(32), T.int64(10), T.int64(64), T.int64(64)):
            with T.block("T_group_norm"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_ax4 = T.axis.remap("SSSSS", [ax0, ax1, ax2, ax3, ax4])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], T_reshape_2[v_ax1, v_ax2], T_reshape_3[v_ax1, v_ax2])
                T.writes(T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4])
                T_group_norm[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] = (T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3, v_ax4] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(2.4414062500000001e-05)) + T.float32(9.9999999999999995e-07)) * T_reshape_2[v_ax1, v_ax2] + T_reshape_3[v_ax1, v_ax2]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(64), T.int64(64)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(320) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(320) // T.int64(10), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(10), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = T_group_norm[(((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) // T.int64(320) + v_ax0) % T.int64(2), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(320) // T.int64(10), ((v_ax3 // T.int64(64) + v_ax2) // T.int64(64) + v_ax1) % T.int64(10), (v_ax3 // T.int64(64) + v_ax2) % T.int64(64), v_ax3 % T.int64(64)]

    @T.prim_func(private=True)
    def layer_norm(A: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32"), B: T.Buffer((T.int64(768),), "float32"), C: T.Buffer((T.int64(768),), "float32"), T_layer_norm: T.Buffer((T.int64(1), T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        A_red_temp_v0 = T.alloc_buffer((T.int64(1), T.int64(77)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(1), T.int64(77)))
        for ax0, ax1, k2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2 = T.axis.remap("SSR", [ax0, ax1, k2])
                T.reads(A[v_ax0, v_ax1, v_k2])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2] * A[v_ax0, v_ax1, v_k2]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(77), T.int64(768)):
            with T.block("T_layer_norm"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(A[v_ax0, v_ax1, v_ax2], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], B[v_ax2], C[v_ax2])
                T.writes(T_layer_norm[v_ax0, v_ax1, v_ax2])
                T_layer_norm[v_ax0, v_ax1, v_ax2] = (A[v_ax0, v_ax1, v_ax2] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0013020833333333333)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.0013020833333333333) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0013020833333333333) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0013020833333333333)) + T.float32(1.0000000000000001e-05)) * B[v_ax2] + C[v_ax2]

    @T.prim_func(private=True)
    def layer_norm1(A: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), B: T.Buffer((T.int64(320),), "float32"), C: T.Buffer((T.int64(320),), "float32"), T_layer_norm: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(4096)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(4096)))
        for ax0, ax1, k2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2 = T.axis.remap("SSR", [ax0, ax1, k2])
                T.reads(A[v_ax0, v_ax1, v_k2])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2] * A[v_ax0, v_ax1, v_k2]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(4096), T.int64(320)):
            with T.block("T_layer_norm"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(A[v_ax0, v_ax1, v_ax2], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], B[v_ax2], C[v_ax2])
                T.writes(T_layer_norm[v_ax0, v_ax1, v_ax2])
                T_layer_norm[v_ax0, v_ax1, v_ax2] = (A[v_ax0, v_ax1, v_ax2] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0031250000000000002)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.0031250000000000002) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0031250000000000002) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0031250000000000002)) + T.float32(1.0000000000000001e-05)) * B[v_ax2] + C[v_ax2]

    @T.prim_func(private=True)
    def layer_norm2(A: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), B: T.Buffer((T.int64(640),), "float32"), C: T.Buffer((T.int64(640),), "float32"), T_layer_norm: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(1024)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(1024)))
        for ax0, ax1, k2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2 = T.axis.remap("SSR", [ax0, ax1, k2])
                T.reads(A[v_ax0, v_ax1, v_k2])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2] * A[v_ax0, v_ax1, v_k2]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(1024), T.int64(640)):
            with T.block("T_layer_norm"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(A[v_ax0, v_ax1, v_ax2], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], B[v_ax2], C[v_ax2])
                T.writes(T_layer_norm[v_ax0, v_ax1, v_ax2])
                T_layer_norm[v_ax0, v_ax1, v_ax2] = (A[v_ax0, v_ax1, v_ax2] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0015625000000000001)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.0015625000000000001) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0015625000000000001) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.0015625000000000001)) + T.float32(1.0000000000000001e-05)) * B[v_ax2] + C[v_ax2]

    @T.prim_func(private=True)
    def layer_norm3(A: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), B: T.Buffer((T.int64(1280),), "float32"), C: T.Buffer((T.int64(1280),), "float32"), T_layer_norm: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(256)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(256)))
        for ax0, ax1, k2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2 = T.axis.remap("SSR", [ax0, ax1, k2])
                T.reads(A[v_ax0, v_ax1, v_k2])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2] * A[v_ax0, v_ax1, v_k2]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(256), T.int64(1280)):
            with T.block("T_layer_norm"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(A[v_ax0, v_ax1, v_ax2], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], B[v_ax2], C[v_ax2])
                T.writes(T_layer_norm[v_ax0, v_ax1, v_ax2])
                T_layer_norm[v_ax0, v_ax1, v_ax2] = (A[v_ax0, v_ax1, v_ax2] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00078125000000000004)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.00078125000000000004) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00078125000000000004) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00078125000000000004)) + T.float32(1.0000000000000001e-05)) * B[v_ax2] + C[v_ax2]

    @T.prim_func(private=True)
    def layer_norm4(A: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), B: T.Buffer((T.int64(1280),), "float32"), C: T.Buffer((T.int64(1280),), "float32"), T_layer_norm: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        A_red_temp_v0 = T.alloc_buffer((T.int64(2), T.int64(64)))
        A_red_temp_v1 = T.alloc_buffer((T.int64(2), T.int64(64)))
        for ax0, ax1, k2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("A_red_temp"):
                v_ax0, v_ax1, v_k2 = T.axis.remap("SSR", [ax0, ax1, k2])
                T.reads(A[v_ax0, v_ax1, v_k2])
                T.writes(A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1])
                with T.init():
                    A_red_temp_v0[v_ax0, v_ax1] = T.float32(0)
                    A_red_temp_v1[v_ax0, v_ax1] = T.float32(0)
                v_A_red_temp_v0: T.float32 = A_red_temp_v0[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2]
                v_A_red_temp_v1: T.float32 = A_red_temp_v1[v_ax0, v_ax1] + A[v_ax0, v_ax1, v_k2] * A[v_ax0, v_ax1, v_k2]
                A_red_temp_v0[v_ax0, v_ax1] = v_A_red_temp_v0
                A_red_temp_v1[v_ax0, v_ax1] = v_A_red_temp_v1
        for ax0, ax1, ax2 in T.grid(T.int64(2), T.int64(64), T.int64(1280)):
            with T.block("T_layer_norm"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(A[v_ax0, v_ax1, v_ax2], A_red_temp_v0[v_ax0, v_ax1], A_red_temp_v1[v_ax0, v_ax1], B[v_ax2], C[v_ax2])
                T.writes(T_layer_norm[v_ax0, v_ax1, v_ax2])
                T_layer_norm[v_ax0, v_ax1, v_ax2] = (A[v_ax0, v_ax1, v_ax2] - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00078125000000000004)) * T.rsqrt(A_red_temp_v1[v_ax0, v_ax1] * T.float32(0.00078125000000000004) - A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00078125000000000004) * (A_red_temp_v0[v_ax0, v_ax1] * T.float32(0.00078125000000000004)) + T.float32(1.0000000000000001e-05)) * B[v_ax2] + C[v_ax2]

    @T.prim_func(private=True)
    def matmul11(A: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32"), B: T.Buffer((T.int64(320), T.int64(320)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(4096), T.int64(320)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(4096), T.int64(320), T.int64(320)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul13(A: T.Buffer((T.int64(16), T.int64(4096), T.int64(4096)), "float32"), B: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(4096), T.int64(40), T.int64(4096)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul14(A: T.Buffer((T.int64(2), T.int64(77), T.int64(768)), "float32"), B: T.Buffer((T.int64(768), T.int64(320)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(77), T.int64(320)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(77), T.int64(320), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul16(A: T.Buffer((T.int64(16), T.int64(4096), T.int64(77)), "float32"), B: T.Buffer((T.int64(16), T.int64(77), T.int64(40)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(4096), T.int64(40)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(4096), T.int64(40), T.int64(77)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul2(A: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)), "float32"), B: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(512)), "float32"), matmul: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(512)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3, k in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(512), T.int64(4096)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_i3, v_k = T.axis.remap("SSSSR", [i0, i1, i2, i3, k])
                T.reads(A[v_i0, v_i1, v_i2, v_k], B[v_i0, v_i1, v_k, v_i3])
                T.writes(matmul[v_i0, v_i1, v_i2, v_i3])
                with T.init():
                    matmul[v_i0, v_i1, v_i2, v_i3] = T.float32(0)
                matmul[v_i0, v_i1, v_i2, v_i3] = matmul[v_i0, v_i1, v_i2, v_i3] + A[v_i0, v_i1, v_i2, v_k] * B[v_i0, v_i1, v_k, v_i3]

    @T.prim_func(private=True)
    def matmul20(A: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32"), B: T.Buffer((T.int64(640), T.int64(640)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(1024), T.int64(640)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(1024), T.int64(640), T.int64(640)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul22(A: T.Buffer((T.int64(16), T.int64(1024), T.int64(1024)), "float32"), B: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(1024), T.int64(80), T.int64(1024)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul23(A: T.Buffer((T.int64(2), T.int64(77), T.int64(768)), "float32"), B: T.Buffer((T.int64(768), T.int64(640)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(77), T.int64(640)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(77), T.int64(640), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul25(A: T.Buffer((T.int64(16), T.int64(1024), T.int64(77)), "float32"), B: T.Buffer((T.int64(16), T.int64(77), T.int64(80)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(1024), T.int64(80)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(1024), T.int64(80), T.int64(77)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul28(A: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32"), B: T.Buffer((T.int64(1280), T.int64(1280)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(256), T.int64(1280)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(256), T.int64(1280), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul30(A: T.Buffer((T.int64(16), T.int64(256), T.int64(256)), "float32"), B: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(256), T.int64(160), T.int64(256)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul31(A: T.Buffer((T.int64(2), T.int64(77), T.int64(768)), "float32"), B: T.Buffer((T.int64(768), T.int64(1280)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(77), T.int64(1280)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(77), T.int64(1280), T.int64(768)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul33(A: T.Buffer((T.int64(16), T.int64(256), T.int64(77)), "float32"), B: T.Buffer((T.int64(16), T.int64(77), T.int64(160)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(256), T.int64(160)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(256), T.int64(160), T.int64(77)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul36(A: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32"), B: T.Buffer((T.int64(1280), T.int64(1280)), "float32"), matmul: T.Buffer((T.int64(2), T.int64(64), T.int64(1280)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(2), T.int64(64), T.int64(1280), T.int64(1280)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_k, v_i2]

    @T.prim_func(private=True)
    def matmul38(A: T.Buffer((T.int64(16), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(64), T.int64(160), T.int64(64)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul4(A: T.Buffer((T.int64(12), T.int64(77), T.int64(64)), "float32"), B: T.Buffer((T.int64(12), T.int64(64), T.int64(77)), "float32"), matmul: T.Buffer((T.int64(12), T.int64(77), T.int64(77)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(12), T.int64(77), T.int64(77), T.int64(64)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul40(A: T.Buffer((T.int64(16), T.int64(64), T.int64(77)), "float32"), B: T.Buffer((T.int64(16), T.int64(77), T.int64(160)), "float32"), matmul: T.Buffer((T.int64(16), T.int64(64), T.int64(160)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(16), T.int64(64), T.int64(160), T.int64(77)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def matmul5(A: T.Buffer((T.int64(12), T.int64(77), T.int64(77)), "float32"), B: T.Buffer((T.int64(12), T.int64(77), T.int64(64)), "float32"), matmul: T.Buffer((T.int64(12), T.int64(77), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, k in T.grid(T.int64(12), T.int64(77), T.int64(64), T.int64(77)):
            with T.block("matmul"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_k], B[v_i0, v_k, v_i2])
                T.writes(matmul[v_i0, v_i1, v_i2])
                with T.init():
                    matmul[v_i0, v_i1, v_i2] = T.float32(0)
                matmul[v_i0, v_i1, v_i2] = matmul[v_i0, v_i1, v_i2] + A[v_i0, v_i1, v_k] * B[v_i0, v_k, v_i2]

    @T.prim_func(private=True)
    def multiply(A: T.Buffer((), "float32"), B: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[()], B[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = A[()] * B[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply1(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(23) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply10(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(3) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply2(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(16) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply26(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(55) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply27(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(59) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply28(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(37) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply29(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(9) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply3(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(5) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply30(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(0.041666667908430099) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def multiply4(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_multiply: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(7.6775431632995605) * A[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def reshape23(A: T.Buffer((T.int64(2), T.int64(320)), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(320), T.int64(1), T.int64(1)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(320), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[((v_ax1 + v_ax2 + v_ax3) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 + v_ax2 + v_ax3) % T.int64(320)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = A[((v_ax1 + v_ax2 + v_ax3) // T.int64(320) + v_ax0) % T.int64(2), (v_ax1 + v_ax2 + v_ax3) % T.int64(320)]

    @T.prim_func(private=True)
    def reshape33(A: T.Buffer((T.int64(2), T.int64(640)), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(640), T.int64(1), T.int64(1)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(640), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[((v_ax1 + v_ax2 + v_ax3) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 + v_ax2 + v_ax3) % T.int64(640)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = A[((v_ax1 + v_ax2 + v_ax3) // T.int64(640) + v_ax0) % T.int64(2), (v_ax1 + v_ax2 + v_ax3) % T.int64(640)]

    @T.prim_func(private=True)
    def reshape43(A: T.Buffer((T.int64(2), T.int64(1280)), "float32"), T_reshape: T.Buffer((T.int64(2), T.int64(1280), T.int64(1), T.int64(1)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(2), T.int64(1280), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[((v_ax1 + v_ax2 + v_ax3) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 + v_ax2 + v_ax3) % T.int64(1280)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = A[((v_ax1 + v_ax2 + v_ax3) // T.int64(1280) + v_ax0) % T.int64(2), (v_ax1 + v_ax2 + v_ax3) % T.int64(1280)]

    @T.prim_func(private=True)
    def resize2d(A: T.Buffer((T.int64(1), T.int64(512), T.int64(64), T.int64(64)), "float32"), resize: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(128), T.int64(128)):
            with T.block("resize"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(63)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(63)), T.int64(0))])
                T.writes(resize[v_i0, v_i1, v_i2, v_i3])
                resize[v_i0, v_i1, v_i2, v_i3] = A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(63)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(63)), T.int64(0))]

    @T.prim_func(private=True)
    def resize2d1(A: T.Buffer((T.int64(1), T.int64(512), T.int64(128), T.int64(128)), "float32"), resize: T.Buffer((T.int64(1), T.int64(512), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(256), T.int64(256)):
            with T.block("resize"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(127)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(127)), T.int64(0))])
                T.writes(resize[v_i0, v_i1, v_i2, v_i3])
                resize[v_i0, v_i1, v_i2, v_i3] = A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(127)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(127)), T.int64(0))]

    @T.prim_func(private=True)
    def resize2d2(A: T.Buffer((T.int64(1), T.int64(256), T.int64(256), T.int64(256)), "float32"), resize: T.Buffer((T.int64(1), T.int64(256), T.int64(512), T.int64(512)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(512), T.int64(512)):
            with T.block("resize"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(255)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(255)), T.int64(0))])
                T.writes(resize[v_i0, v_i1, v_i2, v_i3])
                resize[v_i0, v_i1, v_i2, v_i3] = A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(255)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(255)), T.int64(0))]

    @T.prim_func(private=True)
    def resize2d3(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(8), T.int64(8)), "float32"), resize: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(16), T.int64(16)):
            with T.block("resize"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(7)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(7)), T.int64(0))])
                T.writes(resize[v_i0, v_i1, v_i2, v_i3])
                resize[v_i0, v_i1, v_i2, v_i3] = A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(7)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(7)), T.int64(0))]

    @T.prim_func(private=True)
    def resize2d4(A: T.Buffer((T.int64(2), T.int64(1280), T.int64(16), T.int64(16)), "float32"), resize: T.Buffer((T.int64(2), T.int64(1280), T.int64(32), T.int64(32)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(1280), T.int64(32), T.int64(32)):
            with T.block("resize"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(15)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(15)), T.int64(0))])
                T.writes(resize[v_i0, v_i1, v_i2, v_i3])
                resize[v_i0, v_i1, v_i2, v_i3] = A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(15)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(15)), T.int64(0))]

    @T.prim_func(private=True)
    def resize2d5(A: T.Buffer((T.int64(2), T.int64(640), T.int64(32), T.int64(32)), "float32"), resize: T.Buffer((T.int64(2), T.int64(640), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(2), T.int64(640), T.int64(64), T.int64(64)):
            with T.block("resize"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(31)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(31)), T.int64(0))])
                T.writes(resize[v_i0, v_i1, v_i2, v_i3])
                resize[v_i0, v_i1, v_i2, v_i3] = A[v_i0, v_i1, T.max(T.min(T.Div(v_i2, T.int64(2)), T.int64(31)), T.int64(0)), T.max(T.min(T.Div(v_i3, T.int64(2)), T.int64(31)), T.int64(0))]

    @T.prim_func(private=True)
    def silu6(A: T.Buffer((T.int64(2), T.int64(1280)), "float32"), T_multiply: T.Buffer((T.int64(2), T.int64(1280)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        compute = T.alloc_buffer((T.int64(2), T.int64(1280)))
        for i0, i1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("compute"):
                v_i0, v_i1 = T.axis.remap("SS", [i0, i1])
                T.reads(A[v_i0, v_i1])
                T.writes(compute[v_i0, v_i1])
                compute[v_i0, v_i1] = T.sigmoid(A[v_i0, v_i1])
        for ax0, ax1 in T.grid(T.int64(2), T.int64(1280)):
            with T.block("T_multiply"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(A[v_ax0, v_ax1], compute[v_ax0, v_ax1])
                T.writes(T_multiply[v_ax0, v_ax1])
                T_multiply[v_ax0, v_ax1] = A[v_ax0, v_ax1] * compute[v_ax0, v_ax1]

    @T.prim_func(private=True)
    def softmax(A: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)), "float32"), T_softmax_norm: T.Buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(4096)))
        T_softmax_exp = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)))
        T_softmax_expsum = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(4096)))
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(A[v_i0, v_i1, v_i2, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1, v_i2])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1, v_i2] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1, v_i2] = T.max(T_softmax_maxelem[v_i0, v_i1, v_i2], A[v_i0, v_i1, v_i2, v_k])
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(A[v_i0, v_i1, v_i2, v_i3], T_softmax_maxelem[v_i0, v_i1, v_i2])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2, v_i3])
                T_softmax_exp[v_i0, v_i1, v_i2, v_i3] = T.exp(A[v_i0, v_i1, v_i2, v_i3] - T_softmax_maxelem[v_i0, v_i1, v_i2])
        for i0, i1, i2, k in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_i2, v_k = T.axis.remap("SSSR", [i0, i1, i2, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1, v_i2])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1, v_i2] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1, v_i2] = T_softmax_expsum[v_i0, v_i1, v_i2] + T_softmax_exp[v_i0, v_i1, v_i2, v_k]
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2, v_i3], T_softmax_expsum[v_i0, v_i1, v_i2])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2, v_i3])
                T.block_attr({"axis": 3})
                T_softmax_norm[v_i0, v_i1, v_i2, v_i3] = T_softmax_exp[v_i0, v_i1, v_i2, v_i3] / T_softmax_expsum[v_i0, v_i1, v_i2]

    @T.prim_func(private=True)
    def softmax1(A: T.Buffer((T.int64(12), T.int64(77), T.int64(77)), "float32"), T_softmax_norm: T.Buffer((T.int64(12), T.int64(77), T.int64(77)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(12), T.int64(77)))
        T_softmax_exp = T.alloc_buffer((T.int64(12), T.int64(77), T.int64(77)))
        T_softmax_expsum = T.alloc_buffer((T.int64(12), T.int64(77)))
        for i0, i1, k in T.grid(T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(12), T.int64(77), T.int64(77)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax2(A: T.Buffer((T.int64(16), T.int64(4096), T.int64(4096)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(4096), T.int64(4096)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(4096)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(4096), T.int64(4096)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(4096)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(4096), T.int64(4096)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax3(A: T.Buffer((T.int64(16), T.int64(4096), T.int64(77)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(4096), T.int64(77)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(4096)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(4096), T.int64(77)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(4096)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(4096), T.int64(77)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(4096), T.int64(77)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(4096), T.int64(77)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(4096), T.int64(77)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax4(A: T.Buffer((T.int64(16), T.int64(1024), T.int64(1024)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(1024), T.int64(1024)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(1024)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(1024), T.int64(1024)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(1024)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(1024), T.int64(1024)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(1024), T.int64(1024)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(1024), T.int64(1024)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(1024), T.int64(1024)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax5(A: T.Buffer((T.int64(16), T.int64(1024), T.int64(77)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(1024), T.int64(77)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(1024)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(1024), T.int64(77)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(1024)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(1024), T.int64(77)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(1024), T.int64(77)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(1024), T.int64(77)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(1024), T.int64(77)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax6(A: T.Buffer((T.int64(16), T.int64(256), T.int64(256)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(256), T.int64(256)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(256)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(256), T.int64(256)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(256)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(256), T.int64(256)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax7(A: T.Buffer((T.int64(16), T.int64(256), T.int64(77)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(256), T.int64(77)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(256)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(256), T.int64(77)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(256)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(256), T.int64(77)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(256), T.int64(77)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(256), T.int64(77)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(256), T.int64(77)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax8(A: T.Buffer((T.int64(16), T.int64(64), T.int64(64)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(64)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(64), T.int64(64)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(64)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(64), T.int64(64)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def softmax9(A: T.Buffer((T.int64(16), T.int64(64), T.int64(77)), "float32"), T_softmax_norm: T.Buffer((T.int64(16), T.int64(64), T.int64(77)), "float32")):
        T.func_attr({"op_pattern": 4, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        T_softmax_maxelem = T.alloc_buffer((T.int64(16), T.int64(64)))
        T_softmax_exp = T.alloc_buffer((T.int64(16), T.int64(64), T.int64(77)))
        T_softmax_expsum = T.alloc_buffer((T.int64(16), T.int64(64)))
        for i0, i1, k in T.grid(T.int64(16), T.int64(64), T.int64(77)):
            with T.block("T_softmax_maxelem"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(A[v_i0, v_i1, v_k])
                T.writes(T_softmax_maxelem[v_i0, v_i1])
                with T.init():
                    T_softmax_maxelem[v_i0, v_i1] = T.float32(-3.4028234663852886e+38)
                T_softmax_maxelem[v_i0, v_i1] = T.max(T_softmax_maxelem[v_i0, v_i1], A[v_i0, v_i1, v_k])
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(64), T.int64(77)):
            with T.block("T_softmax_exp"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(A[v_i0, v_i1, v_i2], T_softmax_maxelem[v_i0, v_i1])
                T.writes(T_softmax_exp[v_i0, v_i1, v_i2])
                T_softmax_exp[v_i0, v_i1, v_i2] = T.exp(A[v_i0, v_i1, v_i2] - T_softmax_maxelem[v_i0, v_i1])
        for i0, i1, k in T.grid(T.int64(16), T.int64(64), T.int64(77)):
            with T.block("T_softmax_expsum"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(T_softmax_exp[v_i0, v_i1, v_k])
                T.writes(T_softmax_expsum[v_i0, v_i1])
                with T.init():
                    T_softmax_expsum[v_i0, v_i1] = T.float32(0)
                T_softmax_expsum[v_i0, v_i1] = T_softmax_expsum[v_i0, v_i1] + T_softmax_exp[v_i0, v_i1, v_k]
        for i0, i1, i2 in T.grid(T.int64(16), T.int64(64), T.int64(77)):
            with T.block("T_softmax_norm"):
                v_i0, v_i1, v_i2 = T.axis.remap("SSS", [i0, i1, i2])
                T.reads(T_softmax_exp[v_i0, v_i1, v_i2], T_softmax_expsum[v_i0, v_i1])
                T.writes(T_softmax_norm[v_i0, v_i1, v_i2])
                T.block_attr({"axis": 2})
                T_softmax_norm[v_i0, v_i1, v_i2] = T_softmax_exp[v_i0, v_i1, v_i2] / T_softmax_expsum[v_i0, v_i1]

    @T.prim_func(private=True)
    def subtract(A: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), B: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32"), T_subtract: T.Buffer((T.int64(1), T.int64(4), T.int64(64), T.int64(64)), "float32")):
        T.func_attr({"op_pattern": 0, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(4), T.int64(64), T.int64(64)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(A[v_ax0, v_ax1, v_ax2, v_ax3], B[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = A[v_ax0, v_ax1, v_ax2, v_ax3] - B[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def take(A: T.Buffer((T.int64(49408), T.int64(768)), "float32"), B: T.Buffer((T.int64(77),), "int32"), T_take: T.Buffer((T.int64(77), T.int64(768)), "float32")):
        T.func_attr({"op_pattern": 8, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1 in T.grid(T.int64(77), T.int64(768)):
            with T.block("T_take"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(A[B[v_ax0], v_ax1], B[v_ax0])
                T.writes(T_take[v_ax0, v_ax1])
                T_take[v_ax0, v_ax1] = A[B[v_ax0], v_ax1]

    @T.prim_func(private=True)
    def tir_image_to_rgba(A: T.Buffer((T.int64(1), T.int64(512), T.int64(512), T.int64(3)), "float32"), image_to_rgba: T.Buffer((T.int64(512), T.int64(512)), "uint32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for y, x in T.grid(T.int64(512), T.int64(512)):
            with T.block("image_to_rgba"):
                v_y, v_x = T.axis.remap("SS", [y, x])
                T.reads(A[T.int64(0), v_y, v_x, T.int64(0):T.int64(3)])
                T.writes(image_to_rgba[v_y, v_x])
                image_to_rgba[v_y, v_x] = T.bitwise_or(T.bitwise_or(T.bitwise_or(T.Cast("uint32", A[T.int64(0), v_y, v_x, T.int64(0)]), T.shift_left(T.Cast("uint32", A[T.int64(0), v_y, v_x, T.int64(1)]), T.uint32(8))), T.shift_left(T.Cast("uint32", A[T.int64(0), v_y, v_x, T.int64(2)]), T.uint32(16))), T.uint32(4278190080))

    @T.prim_func(private=True)
    def transpose(A: T.Buffer((T.int64(1), T.int64(512), T.int64(4096)), "float32"), T_transpose: T.Buffer((T.int64(1), T.int64(4096), T.int64(512)), "float32")):
        T.func_attr({"op_pattern": 2, "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(4096), T.int64(512)):
            with T.block("T_transpose"):
                v_ax0, v_ax1, v_ax2 = T.axis.remap("SSS", [ax0, ax1, ax2])
                T.reads(A[v_ax0, v_ax2, v_ax1])
                T.writes(T_transpose[v_ax0, v_ax1, v_ax2])
                T_transpose[v_ax0, v_ax1, v_ax2] = A[v_ax0, v_ax2, v_ax1]

    @R.function
    def clip(inp_0: R.Tensor((1, 77), dtype="int32"), transformed_param_0: R.Tensor((49408, 768), dtype="float32"), transformed_param_1: R.Tensor((768,), dtype="float32"), transformed_param_2: R.Tensor((768,), dtype="float32"), transformed_param_3: R.Tensor((768,), dtype="float32"), transformed_param_4: R.Tensor((768,), dtype="float32"), transformed_param_5: R.Tensor((3072,), dtype="float32"), transformed_param_6: R.Tensor((768,), dtype="float32"), transformed_param_7: R.Tensor((768,), dtype="float32"), transformed_param_8: R.Tensor((768,), dtype="float32"), transformed_param_9: R.Tensor((768,), dtype="float32"), transformed_param_10: R.Tensor((768,), dtype="float32"), transformed_param_11: R.Tensor((768,), dtype="float32"), transformed_param_12: R.Tensor((768,), dtype="float32"), transformed_param_13: R.Tensor((768,), dtype="float32"), transformed_param_14: R.Tensor((768,), dtype="float32"), transformed_param_15: R.Tensor((3072,), dtype="float32"), transformed_param_16: R.Tensor((768,), dtype="float32"), transformed_param_17: R.Tensor((768,), dtype="float32"), transformed_param_18: R.Tensor((768,), dtype="float32"), transformed_param_19: R.Tensor((768,), dtype="float32"), transformed_param_20: R.Tensor((768,), dtype="float32"), transformed_param_21: R.Tensor((768,), dtype="float32"), transformed_param_22: R.Tensor((768,), dtype="float32"), transformed_param_23: R.Tensor((768,), dtype="float32"), transformed_param_24: R.Tensor((768,), dtype="float32"), transformed_param_25: R.Tensor((3072,), dtype="float32"), transformed_param_26: R.Tensor((768,), dtype="float32"), transformed_param_27: R.Tensor((768,), dtype="float32"), transformed_param_28: R.Tensor((768,), dtype="float32"), transformed_param_29: R.Tensor((768,), dtype="float32"), transformed_param_30: R.Tensor((768,), dtype="float32"), transformed_param_31: R.Tensor((768,), dtype="float32"), transformed_param_32: R.Tensor((768,), dtype="float32"), transformed_param_33: R.Tensor((768,), dtype="float32"), transformed_param_34: R.Tensor((768,), dtype="float32"), transformed_param_35: R.Tensor((3072,), dtype="float32"), transformed_param_36: R.Tensor((768,), dtype="float32"), transformed_param_37: R.Tensor((768,), dtype="float32"), transformed_param_38: R.Tensor((768,), dtype="float32"), transformed_param_39: R.Tensor((768,), dtype="float32"), transformed_param_40: R.Tensor((768,), dtype="float32"), transformed_param_41: R.Tensor((768,), dtype="float32"), transformed_param_42: R.Tensor((768,), dtype="float32"), transformed_param_43: R.Tensor((768,), dtype="float32"), transformed_param_44: R.Tensor((768,), dtype="float32"), transformed_param_45: R.Tensor((3072,), dtype="float32"), transformed_param_46: R.Tensor((768,), dtype="float32"), transformed_param_47: R.Tensor((768,), dtype="float32"), transformed_param_48: R.Tensor((768,), dtype="float32"), transformed_param_49: R.Tensor((768,), dtype="float32"), transformed_param_50: R.Tensor((768,), dtype="float32"), transformed_param_51: R.Tensor((768,), dtype="float32"), transformed_param_52: R.Tensor((768,), dtype="float32"), transformed_param_53: R.Tensor((768,), dtype="float32"), transformed_param_54: R.Tensor((768,), dtype="float32"), transformed_param_55: R.Tensor((3072,), dtype="float32"), transformed_param_56: R.Tensor((768,), dtype="float32"), transformed_param_57: R.Tensor((768,), dtype="float32"), transformed_param_58: R.Tensor((768,), dtype="float32"), transformed_param_59: R.Tensor((768,), dtype="float32"), transformed_param_60: R.Tensor((768,), dtype="float32"), transformed_param_61: R.Tensor((768,), dtype="float32"), transformed_param_62: R.Tensor((768,), dtype="float32"), transformed_param_63: R.Tensor((768,), dtype="float32"), transformed_param_64: R.Tensor((768,), dtype="float32"), transformed_param_65: R.Tensor((3072,), dtype="float32"), transformed_param_66: R.Tensor((768,), dtype="float32"), transformed_param_67: R.Tensor((768,), dtype="float32"), transformed_param_68: R.Tensor((768,), dtype="float32"), transformed_param_69: R.Tensor((768,), dtype="float32"), transformed_param_70: R.Tensor((768,), dtype="float32"), transformed_param_71: R.Tensor((768,), dtype="float32"), transformed_param_72: R.Tensor((768,), dtype="float32"), transformed_param_73: R.Tensor((768,), dtype="float32"), transformed_param_74: R.Tensor((768,), dtype="float32"), transformed_param_75: R.Tensor((3072,), dtype="float32"), transformed_param_76: R.Tensor((768,), dtype="float32"), transformed_param_77: R.Tensor((768,), dtype="float32"), transformed_param_78: R.Tensor((768,), dtype="float32"), transformed_param_79: R.Tensor((768,), dtype="float32"), transformed_param_80: R.Tensor((768,), dtype="float32"), transformed_param_81: R.Tensor((768,), dtype="float32"), transformed_param_82: R.Tensor((768,), dtype="float32"), transformed_param_83: R.Tensor((768,), dtype="float32"), transformed_param_84: R.Tensor((768,), dtype="float32"), transformed_param_85: R.Tensor((3072,), dtype="float32"), transformed_param_86: R.Tensor((768,), dtype="float32"), transformed_param_87: R.Tensor((768,), dtype="float32"), transformed_param_88: R.Tensor((768,), dtype="float32"), transformed_param_89: R.Tensor((768,), dtype="float32"), transformed_param_90: R.Tensor((768,), dtype="float32"), transformed_param_91: R.Tensor((768,), dtype="float32"), transformed_param_92: R.Tensor((768,), dtype="float32"), transformed_param_93: R.Tensor((768,), dtype="float32"), transformed_param_94: R.Tensor((768,), dtype="float32"), transformed_param_95: R.Tensor((3072,), dtype="float32"), transformed_param_96: R.Tensor((768,), dtype="float32"), transformed_param_97: R.Tensor((768,), dtype="float32"), transformed_param_98: R.Tensor((768,), dtype="float32"), transformed_param_99: R.Tensor((768,), dtype="float32"), transformed_param_100: R.Tensor((768,), dtype="float32"), transformed_param_101: R.Tensor((768,), dtype="float32"), transformed_param_102: R.Tensor((768,), dtype="float32"), transformed_param_103: R.Tensor((768,), dtype="float32"), transformed_param_104: R.Tensor((768,), dtype="float32"), transformed_param_105: R.Tensor((3072,), dtype="float32"), transformed_param_106: R.Tensor((768,), dtype="float32"), transformed_param_107: R.Tensor((768,), dtype="float32"), transformed_param_108: R.Tensor((768,), dtype="float32"), transformed_param_109: R.Tensor((768,), dtype="float32"), transformed_param_110: R.Tensor((768,), dtype="float32"), transformed_param_111: R.Tensor((768,), dtype="float32"), transformed_param_112: R.Tensor((768,), dtype="float32"), transformed_param_113: R.Tensor((768,), dtype="float32"), transformed_param_114: R.Tensor((768,), dtype="float32"), transformed_param_115: R.Tensor((3072,), dtype="float32"), transformed_param_116: R.Tensor((768,), dtype="float32"), transformed_param_117: R.Tensor((768,), dtype="float32"), transformed_param_118: R.Tensor((768,), dtype="float32"), transformed_param_119: R.Tensor((768,), dtype="float32"), transformed_param_120: R.Tensor((768,), dtype="float32"), transformed_param_121: R.Tensor((768,), dtype="float32"), transformed_param_122: R.Tensor((768,), dtype="float32"), transformed_param_123: R.Tensor((77, 768), dtype="float32"), transformed_param_124: R.Tensor((768, 768), dtype="float32"), transformed_param_125: R.Tensor((768, 768), dtype="float32"), transformed_param_126: R.Tensor((768, 768), dtype="float32"), transformed_param_127: R.Tensor((768, 768), dtype="float32"), transformed_param_128: R.Tensor((768, 3072), dtype="float32"), transformed_param_129: R.Tensor((3072, 768), dtype="float32"), transformed_param_130: R.Tensor((768, 768), dtype="float32"), transformed_param_131: R.Tensor((768, 768), dtype="float32"), transformed_param_132: R.Tensor((768, 768), dtype="float32"), transformed_param_133: R.Tensor((768, 768), dtype="float32"), transformed_param_134: R.Tensor((768, 3072), dtype="float32"), transformed_param_135: R.Tensor((3072, 768), dtype="float32"), transformed_param_136: R.Tensor((768, 768), dtype="float32"), transformed_param_137: R.Tensor((768, 768), dtype="float32"), transformed_param_138: R.Tensor((768, 768), dtype="float32"), transformed_param_139: R.Tensor((768, 768), dtype="float32"), transformed_param_140: R.Tensor((768, 3072), dtype="float32"), transformed_param_141: R.Tensor((3072, 768), dtype="float32"), transformed_param_142: R.Tensor((768, 768), dtype="float32"), transformed_param_143: R.Tensor((768, 768), dtype="float32"), transformed_param_144: R.Tensor((768, 768), dtype="float32"), transformed_param_145: R.Tensor((768, 768), dtype="float32"), transformed_param_146: R.Tensor((768, 3072), dtype="float32"), transformed_param_147: R.Tensor((3072, 768), dtype="float32"), transformed_param_148: R.Tensor((768, 768), dtype="float32"), transformed_param_149: R.Tensor((768, 768), dtype="float32"), transformed_param_150: R.Tensor((768, 768), dtype="float32"), transformed_param_151: R.Tensor((768, 768), dtype="float32"), transformed_param_152: R.Tensor((768, 3072), dtype="float32"), transformed_param_153: R.Tensor((3072, 768), dtype="float32"), transformed_param_154: R.Tensor((768, 768), dtype="float32"), transformed_param_155: R.Tensor((768, 768), dtype="float32"), transformed_param_156: R.Tensor((768, 768), dtype="float32"), transformed_param_157: R.Tensor((768, 768), dtype="float32"), transformed_param_158: R.Tensor((768, 3072), dtype="float32"), transformed_param_159: R.Tensor((3072, 768), dtype="float32"), transformed_param_160: R.Tensor((768, 768), dtype="float32"), transformed_param_161: R.Tensor((768, 768), dtype="float32"), transformed_param_162: R.Tensor((768, 768), dtype="float32"), transformed_param_163: R.Tensor((768, 768), dtype="float32"), transformed_param_164: R.Tensor((768, 3072), dtype="float32"), transformed_param_165: R.Tensor((3072, 768), dtype="float32"), transformed_param_166: R.Tensor((768, 768), dtype="float32"), transformed_param_167: R.Tensor((768, 768), dtype="float32"), transformed_param_168: R.Tensor((768, 768), dtype="float32"), transformed_param_169: R.Tensor((768, 768), dtype="float32"), transformed_param_170: R.Tensor((768, 3072), dtype="float32"), transformed_param_171: R.Tensor((3072, 768), dtype="float32"), transformed_param_172: R.Tensor((768, 768), dtype="float32"), transformed_param_173: R.Tensor((768, 768), dtype="float32"), transformed_param_174: R.Tensor((768, 768), dtype="float32"), transformed_param_175: R.Tensor((768, 768), dtype="float32"), transformed_param_176: R.Tensor((768, 3072), dtype="float32"), transformed_param_177: R.Tensor((3072, 768), dtype="float32"), transformed_param_178: R.Tensor((768, 768), dtype="float32"), transformed_param_179: R.Tensor((768, 768), dtype="float32"), transformed_param_180: R.Tensor((768, 768), dtype="float32"), transformed_param_181: R.Tensor((768, 768), dtype="float32"), transformed_param_182: R.Tensor((768, 3072), dtype="float32"), transformed_param_183: R.Tensor((3072, 768), dtype="float32"), transformed_param_184: R.Tensor((768, 768), dtype="float32"), transformed_param_185: R.Tensor((768, 768), dtype="float32"), transformed_param_186: R.Tensor((768, 768), dtype="float32"), transformed_param_187: R.Tensor((768, 768), dtype="float32"), transformed_param_188: R.Tensor((768, 3072), dtype="float32"), transformed_param_189: R.Tensor((3072, 768), dtype="float32"), transformed_param_190: R.Tensor((768, 768), dtype="float32"), transformed_param_191: R.Tensor((768, 768), dtype="float32"), transformed_param_192: R.Tensor((768, 768), dtype="float32"), transformed_param_193: R.Tensor((768, 768), dtype="float32"), transformed_param_194: R.Tensor((768, 3072), dtype="float32"), transformed_param_195: R.Tensor((3072, 768), dtype="float32")) -> R.Tensor((1, 77, 768), dtype="float32"):
        R.func_attr({"global_symbol": "subgraph_0", "num_input": 1})
        cls = Module
        with R.dataflow():
            lv77 = R.call_tir(cls.fused_reshape9_cast_reshape10, (inp_0,), out_sinfo=R.Tensor((77,), dtype="int32"))
            lv: R.Tensor((49408, 768), dtype="float32") = transformed_param_0
            lv3 = R.call_tir(cls.take, (lv, lv77), out_sinfo=R.Tensor((77, 768), dtype="float32"))
            lv1: R.Tensor((77, 768), dtype="float32") = transformed_param_123
            lv78 = R.call_tir(cls.fused_reshape11_reshape11_add15, (lv3, lv1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv2: R.Tensor((768,), dtype="float32") = transformed_param_2
            lv3_1: R.Tensor((768,), dtype="float32") = transformed_param_1
            lv21 = R.call_tir(cls.layer_norm, (lv78, lv2, lv3_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv4: R.Tensor((768, 768), dtype="float32") = transformed_param_124
            lv5: R.Tensor((768,), dtype="float32") = transformed_param_9
            lv79 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv21, lv4, lv5), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv6: R.Tensor((768, 768), dtype="float32") = transformed_param_125
            lv7: R.Tensor((768,), dtype="float32") = transformed_param_7
            lv80 = R.call_tir(cls.fused_matmul3_add17, (lv21, lv6, lv7), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv81 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv80,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv8: R.Tensor((768, 768), dtype="float32") = transformed_param_126
            lv9: R.Tensor((768,), dtype="float32") = transformed_param_10
            lv82 = R.call_tir(cls.fused_matmul3_add17, (lv21, lv8, lv9), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv83 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv82,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv84 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv79,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv42 = R.call_tir(cls.matmul4, (lv84, lv81), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv85 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv42, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv46 = R.call_tir(cls.softmax1, (lv85,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv47 = R.call_tir(cls.matmul5, (lv46, lv83), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv86 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv47,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv10: R.Tensor((768, 768), dtype="float32") = transformed_param_127
            lv11: R.Tensor((768,), dtype="float32") = transformed_param_8
            lv87 = R.call_tir(cls.fused_matmul3_add17_add15, (lv86, lv10, lv11, lv78), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv12: R.Tensor((768,), dtype="float32") = transformed_param_4
            lv13: R.Tensor((768,), dtype="float32") = transformed_param_3
            lv55 = R.call_tir(cls.layer_norm, (lv87, lv12, lv13), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv14: R.Tensor((768, 3072), dtype="float32") = transformed_param_128
            lv15: R.Tensor((3072,), dtype="float32") = transformed_param_5
            lv88 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv55, lv14, lv15), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv16: R.Tensor((3072, 768), dtype="float32") = transformed_param_129
            lv17: R.Tensor((768,), dtype="float32") = transformed_param_6
            lv89 = R.call_tir(cls.fused_matmul7_add17_add15, (lv88, lv16, lv17, lv87), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv18: R.Tensor((768,), dtype="float32") = transformed_param_32
            lv19: R.Tensor((768,), dtype="float32") = transformed_param_31
            lv66 = R.call_tir(cls.layer_norm, (lv89, lv18, lv19), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv20: R.Tensor((768, 768), dtype="float32") = transformed_param_130
            lv21_1: R.Tensor((768,), dtype="float32") = transformed_param_39
            lv90 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv66, lv20, lv21_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv22: R.Tensor((768, 768), dtype="float32") = transformed_param_131
            lv23: R.Tensor((768,), dtype="float32") = transformed_param_37
            lv91 = R.call_tir(cls.fused_matmul3_add17, (lv66, lv22, lv23), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv92 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv91,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv24: R.Tensor((768, 768), dtype="float32") = transformed_param_132
            lv25: R.Tensor((768,), dtype="float32") = transformed_param_40
            lv93 = R.call_tir(cls.fused_matmul3_add17, (lv66, lv24, lv25), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv94 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv93,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv95 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv90,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv87_1 = R.call_tir(cls.matmul4, (lv95, lv92), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv96 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv87_1, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv91_1 = R.call_tir(cls.softmax1, (lv96,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv92_1 = R.call_tir(cls.matmul5, (lv91_1, lv94), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv97 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv92_1,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv26: R.Tensor((768, 768), dtype="float32") = transformed_param_133
            lv27: R.Tensor((768,), dtype="float32") = transformed_param_38
            lv98 = R.call_tir(cls.fused_matmul3_add17_add15, (lv97, lv26, lv27, lv89), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv28: R.Tensor((768,), dtype="float32") = transformed_param_34
            lv29: R.Tensor((768,), dtype="float32") = transformed_param_33
            lv100 = R.call_tir(cls.layer_norm, (lv98, lv28, lv29), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv30: R.Tensor((768, 3072), dtype="float32") = transformed_param_134
            lv31: R.Tensor((3072,), dtype="float32") = transformed_param_35
            lv99 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv100, lv30, lv31), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv32: R.Tensor((3072, 768), dtype="float32") = transformed_param_135
            lv33: R.Tensor((768,), dtype="float32") = transformed_param_36
            lv100_1 = R.call_tir(cls.fused_matmul7_add17_add15, (lv99, lv32, lv33, lv98), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv34: R.Tensor((768,), dtype="float32") = transformed_param_42
            lv35: R.Tensor((768,), dtype="float32") = transformed_param_41
            lv111 = R.call_tir(cls.layer_norm, (lv100_1, lv34, lv35), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv36: R.Tensor((768, 768), dtype="float32") = transformed_param_136
            lv37: R.Tensor((768,), dtype="float32") = transformed_param_49
            lv101 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv111, lv36, lv37), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv38: R.Tensor((768, 768), dtype="float32") = transformed_param_137
            lv39: R.Tensor((768,), dtype="float32") = transformed_param_47
            lv102 = R.call_tir(cls.fused_matmul3_add17, (lv111, lv38, lv39), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv103 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv102,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv40: R.Tensor((768, 768), dtype="float32") = transformed_param_138
            lv41: R.Tensor((768,), dtype="float32") = transformed_param_50
            lv104 = R.call_tir(cls.fused_matmul3_add17, (lv111, lv40, lv41), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv105 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv104,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv106 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv101,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv132 = R.call_tir(cls.matmul4, (lv106, lv103), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv107 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv132, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv136 = R.call_tir(cls.softmax1, (lv107,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv137 = R.call_tir(cls.matmul5, (lv136, lv105), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv108 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv137,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv42_1: R.Tensor((768, 768), dtype="float32") = transformed_param_139
            lv43: R.Tensor((768,), dtype="float32") = transformed_param_48
            lv109 = R.call_tir(cls.fused_matmul3_add17_add15, (lv108, lv42_1, lv43, lv100_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv44: R.Tensor((768,), dtype="float32") = transformed_param_44
            lv45: R.Tensor((768,), dtype="float32") = transformed_param_43
            lv145 = R.call_tir(cls.layer_norm, (lv109, lv44, lv45), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv46_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_140
            lv47_1: R.Tensor((3072,), dtype="float32") = transformed_param_45
            lv110 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv145, lv46_1, lv47_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv48: R.Tensor((3072, 768), dtype="float32") = transformed_param_141
            lv49: R.Tensor((768,), dtype="float32") = transformed_param_46
            lv111_1 = R.call_tir(cls.fused_matmul7_add17_add15, (lv110, lv48, lv49, lv109), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv50: R.Tensor((768,), dtype="float32") = transformed_param_52
            lv51: R.Tensor((768,), dtype="float32") = transformed_param_51
            lv156 = R.call_tir(cls.layer_norm, (lv111_1, lv50, lv51), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv52: R.Tensor((768, 768), dtype="float32") = transformed_param_142
            lv53: R.Tensor((768,), dtype="float32") = transformed_param_59
            lv112 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv156, lv52, lv53), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv54: R.Tensor((768, 768), dtype="float32") = transformed_param_143
            lv55_1: R.Tensor((768,), dtype="float32") = transformed_param_57
            lv113 = R.call_tir(cls.fused_matmul3_add17, (lv156, lv54, lv55_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv114 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv113,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv56: R.Tensor((768, 768), dtype="float32") = transformed_param_144
            lv57: R.Tensor((768,), dtype="float32") = transformed_param_60
            lv115 = R.call_tir(cls.fused_matmul3_add17, (lv156, lv56, lv57), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv116 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv115,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv117 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv112,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv177 = R.call_tir(cls.matmul4, (lv117, lv114), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv118 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv177, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv181 = R.call_tir(cls.softmax1, (lv118,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv182 = R.call_tir(cls.matmul5, (lv181, lv116), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv119 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv182,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv58: R.Tensor((768, 768), dtype="float32") = transformed_param_145
            lv59: R.Tensor((768,), dtype="float32") = transformed_param_58
            lv120 = R.call_tir(cls.fused_matmul3_add17_add15, (lv119, lv58, lv59, lv111_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv60: R.Tensor((768,), dtype="float32") = transformed_param_54
            lv61: R.Tensor((768,), dtype="float32") = transformed_param_53
            lv190 = R.call_tir(cls.layer_norm, (lv120, lv60, lv61), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv62: R.Tensor((768, 3072), dtype="float32") = transformed_param_146
            lv63: R.Tensor((3072,), dtype="float32") = transformed_param_55
            lv121 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv190, lv62, lv63), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv64: R.Tensor((3072, 768), dtype="float32") = transformed_param_147
            lv65: R.Tensor((768,), dtype="float32") = transformed_param_56
            lv122 = R.call_tir(cls.fused_matmul7_add17_add15, (lv121, lv64, lv65, lv120), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv66_1: R.Tensor((768,), dtype="float32") = transformed_param_62
            lv67: R.Tensor((768,), dtype="float32") = transformed_param_61
            lv201 = R.call_tir(cls.layer_norm, (lv122, lv66_1, lv67), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv68: R.Tensor((768, 768), dtype="float32") = transformed_param_148
            lv69: R.Tensor((768,), dtype="float32") = transformed_param_69
            lv123 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv201, lv68, lv69), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv70: R.Tensor((768, 768), dtype="float32") = transformed_param_149
            lv71: R.Tensor((768,), dtype="float32") = transformed_param_67
            lv124 = R.call_tir(cls.fused_matmul3_add17, (lv201, lv70, lv71), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv125 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv124,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv72: R.Tensor((768, 768), dtype="float32") = transformed_param_150
            lv73: R.Tensor((768,), dtype="float32") = transformed_param_70
            lv126 = R.call_tir(cls.fused_matmul3_add17, (lv201, lv72, lv73), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv127 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv126,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv128 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv123,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv222 = R.call_tir(cls.matmul4, (lv128, lv125), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv129 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv222, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv226 = R.call_tir(cls.softmax1, (lv129,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv227 = R.call_tir(cls.matmul5, (lv226, lv127), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv130 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv227,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv74: R.Tensor((768, 768), dtype="float32") = transformed_param_151
            lv75: R.Tensor((768,), dtype="float32") = transformed_param_68
            lv131 = R.call_tir(cls.fused_matmul3_add17_add15, (lv130, lv74, lv75, lv122), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv76: R.Tensor((768,), dtype="float32") = transformed_param_64
            lv77_1: R.Tensor((768,), dtype="float32") = transformed_param_63
            lv235 = R.call_tir(cls.layer_norm, (lv131, lv76, lv77_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv78_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_152
            lv79_1: R.Tensor((3072,), dtype="float32") = transformed_param_65
            lv132_1 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv235, lv78_1, lv79_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv80_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_153
            lv81_1: R.Tensor((768,), dtype="float32") = transformed_param_66
            lv133 = R.call_tir(cls.fused_matmul7_add17_add15, (lv132_1, lv80_1, lv81_1, lv131), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv82_1: R.Tensor((768,), dtype="float32") = transformed_param_72
            lv83_1: R.Tensor((768,), dtype="float32") = transformed_param_71
            lv246 = R.call_tir(cls.layer_norm, (lv133, lv82_1, lv83_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv84_1: R.Tensor((768, 768), dtype="float32") = transformed_param_154
            lv85_1: R.Tensor((768,), dtype="float32") = transformed_param_79
            lv134 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv246, lv84_1, lv85_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv86_1: R.Tensor((768, 768), dtype="float32") = transformed_param_155
            lv87_2: R.Tensor((768,), dtype="float32") = transformed_param_77
            lv135 = R.call_tir(cls.fused_matmul3_add17, (lv246, lv86_1, lv87_2), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv136_1 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv135,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv88_1: R.Tensor((768, 768), dtype="float32") = transformed_param_156
            lv89_1: R.Tensor((768,), dtype="float32") = transformed_param_80
            lv137_1 = R.call_tir(cls.fused_matmul3_add17, (lv246, lv88_1, lv89_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv138 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv137_1,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv139 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv134,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv267 = R.call_tir(cls.matmul4, (lv139, lv136_1), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv140 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv267, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv271 = R.call_tir(cls.softmax1, (lv140,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv272 = R.call_tir(cls.matmul5, (lv271, lv138), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv141 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv272,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv90_1: R.Tensor((768, 768), dtype="float32") = transformed_param_157
            lv91_2: R.Tensor((768,), dtype="float32") = transformed_param_78
            lv142 = R.call_tir(cls.fused_matmul3_add17_add15, (lv141, lv90_1, lv91_2, lv133), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv92_2: R.Tensor((768,), dtype="float32") = transformed_param_74
            lv93_1: R.Tensor((768,), dtype="float32") = transformed_param_73
            lv280 = R.call_tir(cls.layer_norm, (lv142, lv92_2, lv93_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv94_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_158
            lv95_1: R.Tensor((3072,), dtype="float32") = transformed_param_75
            lv143 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv280, lv94_1, lv95_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv96_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_159
            lv97_1: R.Tensor((768,), dtype="float32") = transformed_param_76
            lv144 = R.call_tir(cls.fused_matmul7_add17_add15, (lv143, lv96_1, lv97_1, lv142), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv98_1: R.Tensor((768,), dtype="float32") = transformed_param_82
            lv99_1: R.Tensor((768,), dtype="float32") = transformed_param_81
            lv291 = R.call_tir(cls.layer_norm, (lv144, lv98_1, lv99_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv100_2: R.Tensor((768, 768), dtype="float32") = transformed_param_160
            lv101_1: R.Tensor((768,), dtype="float32") = transformed_param_89
            lv145_1 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv291, lv100_2, lv101_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv102_1: R.Tensor((768, 768), dtype="float32") = transformed_param_161
            lv103_1: R.Tensor((768,), dtype="float32") = transformed_param_87
            lv146 = R.call_tir(cls.fused_matmul3_add17, (lv291, lv102_1, lv103_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv147 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv146,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv104_1: R.Tensor((768, 768), dtype="float32") = transformed_param_162
            lv105_1: R.Tensor((768,), dtype="float32") = transformed_param_90
            lv148 = R.call_tir(cls.fused_matmul3_add17, (lv291, lv104_1, lv105_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv149 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv148,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv150 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv145_1,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv312 = R.call_tir(cls.matmul4, (lv150, lv147), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv151 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv312, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv316 = R.call_tir(cls.softmax1, (lv151,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv317 = R.call_tir(cls.matmul5, (lv316, lv149), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv152 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv317,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv106_1: R.Tensor((768, 768), dtype="float32") = transformed_param_163
            lv107_1: R.Tensor((768,), dtype="float32") = transformed_param_88
            lv153 = R.call_tir(cls.fused_matmul3_add17_add15, (lv152, lv106_1, lv107_1, lv144), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv108_1: R.Tensor((768,), dtype="float32") = transformed_param_84
            lv109_1: R.Tensor((768,), dtype="float32") = transformed_param_83
            lv325 = R.call_tir(cls.layer_norm, (lv153, lv108_1, lv109_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv110_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_164
            lv111_2: R.Tensor((3072,), dtype="float32") = transformed_param_85
            lv154 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv325, lv110_1, lv111_2), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv112_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_165
            lv113_1: R.Tensor((768,), dtype="float32") = transformed_param_86
            lv155 = R.call_tir(cls.fused_matmul7_add17_add15, (lv154, lv112_1, lv113_1, lv153), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv114_1: R.Tensor((768,), dtype="float32") = transformed_param_92
            lv115_1: R.Tensor((768,), dtype="float32") = transformed_param_91
            lv336 = R.call_tir(cls.layer_norm, (lv155, lv114_1, lv115_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv116_1: R.Tensor((768, 768), dtype="float32") = transformed_param_166
            lv117_1: R.Tensor((768,), dtype="float32") = transformed_param_99
            lv156_1 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv336, lv116_1, lv117_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv118_1: R.Tensor((768, 768), dtype="float32") = transformed_param_167
            lv119_1: R.Tensor((768,), dtype="float32") = transformed_param_97
            lv157 = R.call_tir(cls.fused_matmul3_add17, (lv336, lv118_1, lv119_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv158 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv157,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv120_1: R.Tensor((768, 768), dtype="float32") = transformed_param_168
            lv121_1: R.Tensor((768,), dtype="float32") = transformed_param_100
            lv159 = R.call_tir(cls.fused_matmul3_add17, (lv336, lv120_1, lv121_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv160 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv159,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv161 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv156_1,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv357 = R.call_tir(cls.matmul4, (lv161, lv158), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv162 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv357, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv361 = R.call_tir(cls.softmax1, (lv162,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv362 = R.call_tir(cls.matmul5, (lv361, lv160), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv163 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv362,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv122_1: R.Tensor((768, 768), dtype="float32") = transformed_param_169
            lv123_1: R.Tensor((768,), dtype="float32") = transformed_param_98
            lv164 = R.call_tir(cls.fused_matmul3_add17_add15, (lv163, lv122_1, lv123_1, lv155), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv124_1: R.Tensor((768,), dtype="float32") = transformed_param_94
            lv125_1: R.Tensor((768,), dtype="float32") = transformed_param_93
            lv370 = R.call_tir(cls.layer_norm, (lv164, lv124_1, lv125_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv126_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_170
            lv127_1: R.Tensor((3072,), dtype="float32") = transformed_param_95
            lv165 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv370, lv126_1, lv127_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv128_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_171
            lv129_1: R.Tensor((768,), dtype="float32") = transformed_param_96
            lv166 = R.call_tir(cls.fused_matmul7_add17_add15, (lv165, lv128_1, lv129_1, lv164), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv130_1: R.Tensor((768,), dtype="float32") = transformed_param_102
            lv131_1: R.Tensor((768,), dtype="float32") = transformed_param_101
            lv381 = R.call_tir(cls.layer_norm, (lv166, lv130_1, lv131_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv132_2: R.Tensor((768, 768), dtype="float32") = transformed_param_172
            lv133_1: R.Tensor((768,), dtype="float32") = transformed_param_109
            lv167 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv381, lv132_2, lv133_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv134_1: R.Tensor((768, 768), dtype="float32") = transformed_param_173
            lv135_1: R.Tensor((768,), dtype="float32") = transformed_param_107
            lv168 = R.call_tir(cls.fused_matmul3_add17, (lv381, lv134_1, lv135_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv169 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv168,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv136_2: R.Tensor((768, 768), dtype="float32") = transformed_param_174
            lv137_2: R.Tensor((768,), dtype="float32") = transformed_param_110
            lv170 = R.call_tir(cls.fused_matmul3_add17, (lv381, lv136_2, lv137_2), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv171 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv170,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv172 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv167,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv402 = R.call_tir(cls.matmul4, (lv172, lv169), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv173 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv402, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv406 = R.call_tir(cls.softmax1, (lv173,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv407 = R.call_tir(cls.matmul5, (lv406, lv171), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv174 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv407,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv138_1: R.Tensor((768, 768), dtype="float32") = transformed_param_175
            lv139_1: R.Tensor((768,), dtype="float32") = transformed_param_108
            lv175 = R.call_tir(cls.fused_matmul3_add17_add15, (lv174, lv138_1, lv139_1, lv166), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv140_1: R.Tensor((768,), dtype="float32") = transformed_param_104
            lv141_1: R.Tensor((768,), dtype="float32") = transformed_param_103
            lv415 = R.call_tir(cls.layer_norm, (lv175, lv140_1, lv141_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv142_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_176
            lv143_1: R.Tensor((3072,), dtype="float32") = transformed_param_105
            lv176 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv415, lv142_1, lv143_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv144_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_177
            lv145_2: R.Tensor((768,), dtype="float32") = transformed_param_106
            lv177_1 = R.call_tir(cls.fused_matmul7_add17_add15, (lv176, lv144_1, lv145_2, lv175), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv146_1: R.Tensor((768,), dtype="float32") = transformed_param_112
            lv147_1: R.Tensor((768,), dtype="float32") = transformed_param_111
            lv426 = R.call_tir(cls.layer_norm, (lv177_1, lv146_1, lv147_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv148_1: R.Tensor((768, 768), dtype="float32") = transformed_param_178
            lv149_1: R.Tensor((768,), dtype="float32") = transformed_param_119
            lv178 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv426, lv148_1, lv149_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv150_1: R.Tensor((768, 768), dtype="float32") = transformed_param_179
            lv151_1: R.Tensor((768,), dtype="float32") = transformed_param_117
            lv179 = R.call_tir(cls.fused_matmul3_add17, (lv426, lv150_1, lv151_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv180 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv179,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv152_1: R.Tensor((768, 768), dtype="float32") = transformed_param_180
            lv153_1: R.Tensor((768,), dtype="float32") = transformed_param_120
            lv181_1 = R.call_tir(cls.fused_matmul3_add17, (lv426, lv152_1, lv153_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv182_1 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv181_1,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv183 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv178,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv447 = R.call_tir(cls.matmul4, (lv183, lv180), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv184 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv447, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv451 = R.call_tir(cls.softmax1, (lv184,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv452 = R.call_tir(cls.matmul5, (lv451, lv182_1), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv185 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv452,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv154_1: R.Tensor((768, 768), dtype="float32") = transformed_param_181
            lv155_1: R.Tensor((768,), dtype="float32") = transformed_param_118
            lv186 = R.call_tir(cls.fused_matmul3_add17_add15, (lv185, lv154_1, lv155_1, lv177_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv156_2: R.Tensor((768,), dtype="float32") = transformed_param_114
            lv157_1: R.Tensor((768,), dtype="float32") = transformed_param_113
            lv460 = R.call_tir(cls.layer_norm, (lv186, lv156_2, lv157_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv158_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_182
            lv159_1: R.Tensor((3072,), dtype="float32") = transformed_param_115
            lv187 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv460, lv158_1, lv159_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv160_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_183
            lv161_1: R.Tensor((768,), dtype="float32") = transformed_param_116
            lv188 = R.call_tir(cls.fused_matmul7_add17_add15, (lv187, lv160_1, lv161_1, lv186), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv162_1: R.Tensor((768,), dtype="float32") = transformed_param_12
            lv163_1: R.Tensor((768,), dtype="float32") = transformed_param_11
            lv471 = R.call_tir(cls.layer_norm, (lv188, lv162_1, lv163_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv164_1: R.Tensor((768, 768), dtype="float32") = transformed_param_184
            lv165_1: R.Tensor((768,), dtype="float32") = transformed_param_19
            lv189 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv471, lv164_1, lv165_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv166_1: R.Tensor((768, 768), dtype="float32") = transformed_param_185
            lv167_1: R.Tensor((768,), dtype="float32") = transformed_param_17
            lv190_1 = R.call_tir(cls.fused_matmul3_add17, (lv471, lv166_1, lv167_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv191 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv190_1,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv168_1: R.Tensor((768, 768), dtype="float32") = transformed_param_186
            lv169_1: R.Tensor((768,), dtype="float32") = transformed_param_20
            lv192 = R.call_tir(cls.fused_matmul3_add17, (lv471, lv168_1, lv169_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv193 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv192,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv194 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv189,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv492 = R.call_tir(cls.matmul4, (lv194, lv191), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv195 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv492, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv496 = R.call_tir(cls.softmax1, (lv195,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv497 = R.call_tir(cls.matmul5, (lv496, lv193), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv196 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv497,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv170_1: R.Tensor((768, 768), dtype="float32") = transformed_param_187
            lv171_1: R.Tensor((768,), dtype="float32") = transformed_param_18
            lv197 = R.call_tir(cls.fused_matmul3_add17_add15, (lv196, lv170_1, lv171_1, lv188), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv172_1: R.Tensor((768,), dtype="float32") = transformed_param_14
            lv173_1: R.Tensor((768,), dtype="float32") = transformed_param_13
            lv505 = R.call_tir(cls.layer_norm, (lv197, lv172_1, lv173_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv174_1: R.Tensor((768, 3072), dtype="float32") = transformed_param_188
            lv175_1: R.Tensor((3072,), dtype="float32") = transformed_param_15
            lv198 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv505, lv174_1, lv175_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv176_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_189
            lv177_2: R.Tensor((768,), dtype="float32") = transformed_param_16
            lv199 = R.call_tir(cls.fused_matmul7_add17_add15, (lv198, lv176_1, lv177_2, lv197), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv178_1: R.Tensor((768,), dtype="float32") = transformed_param_22
            lv179_1: R.Tensor((768,), dtype="float32") = transformed_param_21
            lv516 = R.call_tir(cls.layer_norm, (lv199, lv178_1, lv179_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv180_1: R.Tensor((768, 768), dtype="float32") = transformed_param_190
            lv181_2: R.Tensor((768,), dtype="float32") = transformed_param_29
            lv200 = R.call_tir(cls.fused_matmul3_add17_multiply7, (lv516, lv180_1, lv181_2), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv182_2: R.Tensor((768, 768), dtype="float32") = transformed_param_191
            lv183_1: R.Tensor((768,), dtype="float32") = transformed_param_27
            lv201_1 = R.call_tir(cls.fused_matmul3_add17, (lv516, lv182_2, lv183_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv202 = R.call_tir(cls.fused_reshape14_transpose8_reshape15_transpose9, (lv201_1,), out_sinfo=R.Tensor((12, 64, 77), dtype="float32"))
            lv184_1: R.Tensor((768, 768), dtype="float32") = transformed_param_192
            lv185_1: R.Tensor((768,), dtype="float32") = transformed_param_30
            lv203 = R.call_tir(cls.fused_matmul3_add17, (lv516, lv184_1, lv185_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv204 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv203,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv205 = R.call_tir(cls.fused_reshape14_transpose8_reshape15, (lv200,), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv537 = R.call_tir(cls.matmul4, (lv205, lv202), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv206 = R.call_tir(cls.fused_reshape16_add18_reshape17, (lv537, metadata["relax.expr.Constant"][0]), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv541 = R.call_tir(cls.softmax1, (lv206,), out_sinfo=R.Tensor((12, 77, 77), dtype="float32"))
            lv542 = R.call_tir(cls.matmul5, (lv541, lv204), out_sinfo=R.Tensor((12, 77, 64), dtype="float32"))
            lv207 = R.call_tir(cls.fused_reshape18_transpose10_reshape19, (lv542,), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv186_1: R.Tensor((768, 768), dtype="float32") = transformed_param_193
            lv187_1: R.Tensor((768,), dtype="float32") = transformed_param_28
            lv208 = R.call_tir(cls.fused_matmul3_add17_add15, (lv207, lv186_1, lv187_1, lv199), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv188_1: R.Tensor((768,), dtype="float32") = transformed_param_24
            lv189_1: R.Tensor((768,), dtype="float32") = transformed_param_23
            lv550 = R.call_tir(cls.layer_norm, (lv208, lv188_1, lv189_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv190_2: R.Tensor((768, 3072), dtype="float32") = transformed_param_194
            lv191_1: R.Tensor((3072,), dtype="float32") = transformed_param_25
            lv209 = R.call_tir(cls.fused_matmul6_add19_multiply8_tir_sigmoid_multiply9, (lv550, lv190_2, lv191_1), out_sinfo=R.Tensor((1, 77, 3072), dtype="float32"))
            lv192_1: R.Tensor((3072, 768), dtype="float32") = transformed_param_195
            lv193_1: R.Tensor((768,), dtype="float32") = transformed_param_26
            lv210 = R.call_tir(cls.fused_matmul7_add17_add15, (lv209, lv192_1, lv193_1, lv208), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            lv194_1: R.Tensor((768,), dtype="float32") = transformed_param_122
            lv195_1: R.Tensor((768,), dtype="float32") = transformed_param_121
            lv561 = R.call_tir(cls.layer_norm, (lv210, lv194_1, lv195_1), out_sinfo=R.Tensor((1, 77, 768), dtype="float32"))
            gv: R.Tensor((1, 77, 768), dtype="float32") = lv561
            R.output(gv)
        return gv

    @R.function
    def concat_embeddings(cond_embeddings: R.Tensor((1, 77, 768), dtype="float32"), uncond_embeddings: R.Tensor((1, 77, 768), dtype="float32")) -> R.Tensor((2, 77, 768), dtype="float32"):
        cls = Module
        gv = R.call_tir(cls.concatenate, (cond_embeddings, uncond_embeddings), out_sinfo=R.Tensor((2, 77, 768), dtype="float32"))
        return gv

    @R.function
    def dpm_solver_multistep_scheduler_convert_model_output(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), alpha: R.Tensor((), dtype="float32"), sigma: R.Tensor((), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv = R.call_tir(cls.multiply, (sigma, model_output), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv1 = R.call_tir(cls.subtract, (sample, gv), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        converted_model_output = R.call_tir(cls.divide, (gv1, alpha), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return converted_model_output

    @R.function
    def dpm_solver_multistep_scheduler_step(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), last_model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), c0: R.Tensor((), dtype="float32"), c1: R.Tensor((), dtype="float32"), c2: R.Tensor((), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv2 = R.call_tir(cls.multiply, (c0, sample), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv3 = R.call_tir(cls.multiply, (c1, model_output), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv4 = R.call_tir(cls.subtract, (gv2, gv3), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv5 = R.call_tir(cls.subtract, (model_output, last_model_output), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv6 = R.call_tir(cls.multiply, (c2, gv5), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        prev_sample = R.call_tir(cls.subtract, (gv4, gv6), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return prev_sample

    @R.function
    def image_to_rgba(x: R.Tensor((1, 512, 512, 3), dtype="float32")) -> R.Tensor((512, 512), dtype="uint32"):
        cls = Module
        gv = R.call_tir(cls.tir_image_to_rgba, (x,), out_sinfo=R.Tensor((512, 512), dtype="uint32"))
        return gv

    @R.function
    def pndm_scheduler_step_0(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), sample_coeff: R.Tensor((), dtype="float32"), alpha_diff: R.Tensor((), dtype="float32"), model_output_denom_coeff: R.Tensor((), dtype="float32"), ets0: R.Tensor((1, 4, 64, 64), dtype="float32"), ets1: R.Tensor((1, 4, 64, 64), dtype="float32"), ets2: R.Tensor((1, 4, 64, 64), dtype="float32"), ets3: R.Tensor((1, 4, 64, 64), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv = R.call_tir(cls.multiply, (sample_coeff, sample), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv1 = R.call_tir(cls.multiply, (alpha_diff, model_output), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv2 = R.call_tir(cls.divide, (gv1, model_output_denom_coeff), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        prev_sample = R.call_tir(cls.subtract, (gv, gv2), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return prev_sample

    @R.function
    def pndm_scheduler_step_1(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), sample_coeff: R.Tensor((), dtype="float32"), alpha_diff: R.Tensor((), dtype="float32"), model_output_denom_coeff: R.Tensor((), dtype="float32"), ets0: R.Tensor((1, 4, 64, 64), dtype="float32"), ets1: R.Tensor((1, 4, 64, 64), dtype="float32"), ets2: R.Tensor((1, 4, 64, 64), dtype="float32"), ets3: R.Tensor((1, 4, 64, 64), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv3 = R.call_tir(cls.multiply, (sample_coeff, sample), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv4 = R.call_tir(cls.add, (model_output, ets3), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv5 = R.call_tir(cls.divide2, (gv4,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv6 = R.call_tir(cls.multiply, (alpha_diff, gv5), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv7 = R.call_tir(cls.divide, (gv6, model_output_denom_coeff), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        prev_sample1 = R.call_tir(cls.subtract, (gv3, gv7), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return prev_sample1

    @R.function
    def pndm_scheduler_step_2(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), sample_coeff: R.Tensor((), dtype="float32"), alpha_diff: R.Tensor((), dtype="float32"), model_output_denom_coeff: R.Tensor((), dtype="float32"), ets0: R.Tensor((1, 4, 64, 64), dtype="float32"), ets1: R.Tensor((1, 4, 64, 64), dtype="float32"), ets2: R.Tensor((1, 4, 64, 64), dtype="float32"), ets3: R.Tensor((1, 4, 64, 64), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv8 = R.call_tir(cls.multiply, (sample_coeff, sample), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv9 = R.call_tir(cls.multiply10, (ets3,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv10 = R.call_tir(cls.subtract, (gv9, ets2), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv11 = R.call_tir(cls.divide2, (gv10,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv12 = R.call_tir(cls.multiply, (alpha_diff, gv11), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv13 = R.call_tir(cls.divide, (gv12, model_output_denom_coeff), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        prev_sample2 = R.call_tir(cls.subtract, (gv8, gv13), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return prev_sample2

    @R.function
    def pndm_scheduler_step_3(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), sample_coeff: R.Tensor((), dtype="float32"), alpha_diff: R.Tensor((), dtype="float32"), model_output_denom_coeff: R.Tensor((), dtype="float32"), ets0: R.Tensor((1, 4, 64, 64), dtype="float32"), ets1: R.Tensor((1, 4, 64, 64), dtype="float32"), ets2: R.Tensor((1, 4, 64, 64), dtype="float32"), ets3: R.Tensor((1, 4, 64, 64), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv14 = R.call_tir(cls.multiply, (sample_coeff, sample), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv15 = R.call_tir(cls.multiply1, (ets3,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv16 = R.call_tir(cls.multiply2, (ets2,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv17 = R.call_tir(cls.subtract, (gv15, gv16), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv18 = R.call_tir(cls.multiply3, (ets1,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv19 = R.call_tir(cls.add, (gv17, gv18), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv20 = R.call_tir(cls.divide1, (gv19,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv21 = R.call_tir(cls.multiply, (alpha_diff, gv20), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv22 = R.call_tir(cls.divide, (gv21, model_output_denom_coeff), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        prev_sample3 = R.call_tir(cls.subtract, (gv14, gv22), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return prev_sample3

    @R.function
    def pndm_scheduler_step_4(sample: R.Tensor((1, 4, 64, 64), dtype="float32"), model_output: R.Tensor((1, 4, 64, 64), dtype="float32"), sample_coeff: R.Tensor((), dtype="float32"), alpha_diff: R.Tensor((), dtype="float32"), model_output_denom_coeff: R.Tensor((), dtype="float32"), ets0: R.Tensor((1, 4, 64, 64), dtype="float32"), ets1: R.Tensor((1, 4, 64, 64), dtype="float32"), ets2: R.Tensor((1, 4, 64, 64), dtype="float32"), ets3: R.Tensor((1, 4, 64, 64), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        cls = Module
        gv23 = R.call_tir(cls.multiply, (sample_coeff, sample), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv24 = R.call_tir(cls.multiply26, (ets3,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv25 = R.call_tir(cls.multiply27, (ets2,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv26 = R.call_tir(cls.subtract, (gv24, gv25), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv27 = R.call_tir(cls.multiply28, (ets1,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv28 = R.call_tir(cls.add, (gv26, gv27), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv29 = R.call_tir(cls.multiply29, (ets0,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv30 = R.call_tir(cls.subtract, (gv28, gv29), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv31 = R.call_tir(cls.multiply30, (gv30,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv32 = R.call_tir(cls.multiply, (alpha_diff, gv31), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        gv33 = R.call_tir(cls.divide, (gv32, model_output_denom_coeff), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        prev_sample4 = R.call_tir(cls.subtract, (gv23, gv33), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
        return prev_sample4

    @R.function
    def unet(inp_0: R.Tensor((1, 4, 64, 64), dtype="float32"), inp_1: R.Tensor((), dtype="int32"), inp_2: R.Tensor((2, 77, 768), dtype="float32"), transformed_param_0: R.Tensor((320, 4, 3, 3), dtype="float32"), transformed_param_1: R.Tensor((320,), dtype="float32"), transformed_param_2: R.Tensor((320,), dtype="float32"), transformed_param_3: R.Tensor((4, 320, 3, 3), dtype="float32"), transformed_param_4: R.Tensor((320,), dtype="float32"), transformed_param_5: R.Tensor((320,), dtype="float32"), transformed_param_6: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_7: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_8: R.Tensor((320,), dtype="float32"), transformed_param_9: R.Tensor((320,), dtype="float32"), transformed_param_10: R.Tensor((1280,), dtype="float32"), transformed_param_11: R.Tensor((1280,), dtype="float32"), transformed_param_12: R.Tensor((320,), dtype="float32"), transformed_param_13: R.Tensor((320,), dtype="float32"), transformed_param_14: R.Tensor((320,), dtype="float32"), transformed_param_15: R.Tensor((320,), dtype="float32"), transformed_param_16: R.Tensor((320,), dtype="float32"), transformed_param_17: R.Tensor((320,), dtype="float32"), transformed_param_18: R.Tensor((320,), dtype="float32"), transformed_param_19: R.Tensor((320,), dtype="float32"), transformed_param_20: R.Tensor((320,), dtype="float32"), transformed_param_21: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_22: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_23: R.Tensor((320,), dtype="float32"), transformed_param_24: R.Tensor((320,), dtype="float32"), transformed_param_25: R.Tensor((1280,), dtype="float32"), transformed_param_26: R.Tensor((1280,), dtype="float32"), transformed_param_27: R.Tensor((320,), dtype="float32"), transformed_param_28: R.Tensor((320,), dtype="float32"), transformed_param_29: R.Tensor((320,), dtype="float32"), transformed_param_30: R.Tensor((320,), dtype="float32"), transformed_param_31: R.Tensor((320,), dtype="float32"), transformed_param_32: R.Tensor((320,), dtype="float32"), transformed_param_33: R.Tensor((320,), dtype="float32"), transformed_param_34: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_35: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_36: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_37: R.Tensor((320,), dtype="float32"), transformed_param_38: R.Tensor((320,), dtype="float32"), transformed_param_39: R.Tensor((320,), dtype="float32"), transformed_param_40: R.Tensor((320,), dtype="float32"), transformed_param_41: R.Tensor((320,), dtype="float32"), transformed_param_42: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_43: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_44: R.Tensor((320,), dtype="float32"), transformed_param_45: R.Tensor((320,), dtype="float32"), transformed_param_46: R.Tensor((320,), dtype="float32"), transformed_param_47: R.Tensor((320,), dtype="float32"), transformed_param_48: R.Tensor((320,), dtype="float32"), transformed_param_49: R.Tensor((640,), dtype="float32"), transformed_param_50: R.Tensor((640,), dtype="float32"), transformed_param_51: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_52: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_53: R.Tensor((640,), dtype="float32"), transformed_param_54: R.Tensor((640,), dtype="float32"), transformed_param_55: R.Tensor((2560,), dtype="float32"), transformed_param_56: R.Tensor((2560,), dtype="float32"), transformed_param_57: R.Tensor((640,), dtype="float32"), transformed_param_58: R.Tensor((640,), dtype="float32"), transformed_param_59: R.Tensor((640,), dtype="float32"), transformed_param_60: R.Tensor((640,), dtype="float32"), transformed_param_61: R.Tensor((640,), dtype="float32"), transformed_param_62: R.Tensor((640,), dtype="float32"), transformed_param_63: R.Tensor((640,), dtype="float32"), transformed_param_64: R.Tensor((640,), dtype="float32"), transformed_param_65: R.Tensor((640,), dtype="float32"), transformed_param_66: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_67: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_68: R.Tensor((640,), dtype="float32"), transformed_param_69: R.Tensor((640,), dtype="float32"), transformed_param_70: R.Tensor((2560,), dtype="float32"), transformed_param_71: R.Tensor((2560,), dtype="float32"), transformed_param_72: R.Tensor((640,), dtype="float32"), transformed_param_73: R.Tensor((640,), dtype="float32"), transformed_param_74: R.Tensor((640,), dtype="float32"), transformed_param_75: R.Tensor((640,), dtype="float32"), transformed_param_76: R.Tensor((640,), dtype="float32"), transformed_param_77: R.Tensor((640,), dtype="float32"), transformed_param_78: R.Tensor((640,), dtype="float32"), transformed_param_79: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_80: R.Tensor((640, 320, 3, 3), dtype="float32"), transformed_param_81: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_82: R.Tensor((640, 320, 1, 1), dtype="float32"), transformed_param_83: R.Tensor((320,), dtype="float32"), transformed_param_84: R.Tensor((320,), dtype="float32"), transformed_param_85: R.Tensor((640,), dtype="float32"), transformed_param_86: R.Tensor((640,), dtype="float32"), transformed_param_87: R.Tensor((640,), dtype="float32"), transformed_param_88: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_89: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_90: R.Tensor((640,), dtype="float32"), transformed_param_91: R.Tensor((640,), dtype="float32"), transformed_param_92: R.Tensor((640,), dtype="float32"), transformed_param_93: R.Tensor((640,), dtype="float32"), transformed_param_94: R.Tensor((640,), dtype="float32"), transformed_param_95: R.Tensor((1280,), dtype="float32"), transformed_param_96: R.Tensor((1280,), dtype="float32"), transformed_param_97: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_98: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_99: R.Tensor((1280,), dtype="float32"), transformed_param_100: R.Tensor((1280,), dtype="float32"), transformed_param_101: R.Tensor((5120,), dtype="float32"), transformed_param_102: R.Tensor((5120,), dtype="float32"), transformed_param_103: R.Tensor((1280,), dtype="float32"), transformed_param_104: R.Tensor((1280,), dtype="float32"), transformed_param_105: R.Tensor((1280,), dtype="float32"), transformed_param_106: R.Tensor((1280,), dtype="float32"), transformed_param_107: R.Tensor((1280,), dtype="float32"), transformed_param_108: R.Tensor((1280,), dtype="float32"), transformed_param_109: R.Tensor((1280,), dtype="float32"), transformed_param_110: R.Tensor((1280,), dtype="float32"), transformed_param_111: R.Tensor((1280,), dtype="float32"), transformed_param_112: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_113: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_114: R.Tensor((1280,), dtype="float32"), transformed_param_115: R.Tensor((1280,), dtype="float32"), transformed_param_116: R.Tensor((5120,), dtype="float32"), transformed_param_117: R.Tensor((5120,), dtype="float32"), transformed_param_118: R.Tensor((1280,), dtype="float32"), transformed_param_119: R.Tensor((1280,), dtype="float32"), transformed_param_120: R.Tensor((1280,), dtype="float32"), transformed_param_121: R.Tensor((1280,), dtype="float32"), transformed_param_122: R.Tensor((1280,), dtype="float32"), transformed_param_123: R.Tensor((1280,), dtype="float32"), transformed_param_124: R.Tensor((1280,), dtype="float32"), transformed_param_125: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_126: R.Tensor((1280, 640, 3, 3), dtype="float32"), transformed_param_127: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_128: R.Tensor((1280, 640, 1, 1), dtype="float32"), transformed_param_129: R.Tensor((640,), dtype="float32"), transformed_param_130: R.Tensor((640,), dtype="float32"), transformed_param_131: R.Tensor((1280,), dtype="float32"), transformed_param_132: R.Tensor((1280,), dtype="float32"), transformed_param_133: R.Tensor((1280,), dtype="float32"), transformed_param_134: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_135: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_136: R.Tensor((1280,), dtype="float32"), transformed_param_137: R.Tensor((1280,), dtype="float32"), transformed_param_138: R.Tensor((1280,), dtype="float32"), transformed_param_139: R.Tensor((1280,), dtype="float32"), transformed_param_140: R.Tensor((1280,), dtype="float32"), transformed_param_141: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_142: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_143: R.Tensor((1280,), dtype="float32"), transformed_param_144: R.Tensor((1280,), dtype="float32"), transformed_param_145: R.Tensor((1280,), dtype="float32"), transformed_param_146: R.Tensor((1280,), dtype="float32"), transformed_param_147: R.Tensor((1280,), dtype="float32"), transformed_param_148: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_149: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_150: R.Tensor((1280,), dtype="float32"), transformed_param_151: R.Tensor((1280,), dtype="float32"), transformed_param_152: R.Tensor((1280,), dtype="float32"), transformed_param_153: R.Tensor((1280,), dtype="float32"), transformed_param_154: R.Tensor((1280,), dtype="float32"), transformed_param_155: R.Tensor((1280,), dtype="float32"), transformed_param_156: R.Tensor((1280,), dtype="float32"), transformed_param_157: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_158: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_159: R.Tensor((1280,), dtype="float32"), transformed_param_160: R.Tensor((1280,), dtype="float32"), transformed_param_161: R.Tensor((5120,), dtype="float32"), transformed_param_162: R.Tensor((5120,), dtype="float32"), transformed_param_163: R.Tensor((1280,), dtype="float32"), transformed_param_164: R.Tensor((1280,), dtype="float32"), transformed_param_165: R.Tensor((1280,), dtype="float32"), transformed_param_166: R.Tensor((1280,), dtype="float32"), transformed_param_167: R.Tensor((1280,), dtype="float32"), transformed_param_168: R.Tensor((1280,), dtype="float32"), transformed_param_169: R.Tensor((1280,), dtype="float32"), transformed_param_170: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_171: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_172: R.Tensor((1280,), dtype="float32"), transformed_param_173: R.Tensor((1280,), dtype="float32"), transformed_param_174: R.Tensor((1280,), dtype="float32"), transformed_param_175: R.Tensor((1280,), dtype="float32"), transformed_param_176: R.Tensor((1280,), dtype="float32"), transformed_param_177: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_178: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_179: R.Tensor((1280,), dtype="float32"), transformed_param_180: R.Tensor((1280,), dtype="float32"), transformed_param_181: R.Tensor((1280,), dtype="float32"), transformed_param_182: R.Tensor((1280,), dtype="float32"), transformed_param_183: R.Tensor((1280,), dtype="float32"), transformed_param_184: R.Tensor((1280,), dtype="float32"), transformed_param_185: R.Tensor((1280,), dtype="float32"), transformed_param_186: R.Tensor((1280, 2560, 3, 3), dtype="float32"), transformed_param_187: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_188: R.Tensor((1280, 2560, 1, 1), dtype="float32"), transformed_param_189: R.Tensor((2560,), dtype="float32"), transformed_param_190: R.Tensor((2560,), dtype="float32"), transformed_param_191: R.Tensor((1280,), dtype="float32"), transformed_param_192: R.Tensor((1280,), dtype="float32"), transformed_param_193: R.Tensor((1280,), dtype="float32"), transformed_param_194: R.Tensor((1280, 2560, 3, 3), dtype="float32"), transformed_param_195: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_196: R.Tensor((1280, 2560, 1, 1), dtype="float32"), transformed_param_197: R.Tensor((2560,), dtype="float32"), transformed_param_198: R.Tensor((2560,), dtype="float32"), transformed_param_199: R.Tensor((1280,), dtype="float32"), transformed_param_200: R.Tensor((1280,), dtype="float32"), transformed_param_201: R.Tensor((1280,), dtype="float32"), transformed_param_202: R.Tensor((1280, 2560, 3, 3), dtype="float32"), transformed_param_203: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_204: R.Tensor((1280, 2560, 1, 1), dtype="float32"), transformed_param_205: R.Tensor((2560,), dtype="float32"), transformed_param_206: R.Tensor((2560,), dtype="float32"), transformed_param_207: R.Tensor((1280,), dtype="float32"), transformed_param_208: R.Tensor((1280,), dtype="float32"), transformed_param_209: R.Tensor((1280,), dtype="float32"), transformed_param_210: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_211: R.Tensor((1280,), dtype="float32"), transformed_param_212: R.Tensor((1280,), dtype="float32"), transformed_param_213: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_214: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_215: R.Tensor((1280,), dtype="float32"), transformed_param_216: R.Tensor((1280,), dtype="float32"), transformed_param_217: R.Tensor((5120,), dtype="float32"), transformed_param_218: R.Tensor((5120,), dtype="float32"), transformed_param_219: R.Tensor((1280,), dtype="float32"), transformed_param_220: R.Tensor((1280,), dtype="float32"), transformed_param_221: R.Tensor((1280,), dtype="float32"), transformed_param_222: R.Tensor((1280,), dtype="float32"), transformed_param_223: R.Tensor((1280,), dtype="float32"), transformed_param_224: R.Tensor((1280,), dtype="float32"), transformed_param_225: R.Tensor((1280,), dtype="float32"), transformed_param_226: R.Tensor((1280,), dtype="float32"), transformed_param_227: R.Tensor((1280,), dtype="float32"), transformed_param_228: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_229: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_230: R.Tensor((1280,), dtype="float32"), transformed_param_231: R.Tensor((1280,), dtype="float32"), transformed_param_232: R.Tensor((5120,), dtype="float32"), transformed_param_233: R.Tensor((5120,), dtype="float32"), transformed_param_234: R.Tensor((1280,), dtype="float32"), transformed_param_235: R.Tensor((1280,), dtype="float32"), transformed_param_236: R.Tensor((1280,), dtype="float32"), transformed_param_237: R.Tensor((1280,), dtype="float32"), transformed_param_238: R.Tensor((1280,), dtype="float32"), transformed_param_239: R.Tensor((1280,), dtype="float32"), transformed_param_240: R.Tensor((1280,), dtype="float32"), transformed_param_241: R.Tensor((1280,), dtype="float32"), transformed_param_242: R.Tensor((1280,), dtype="float32"), transformed_param_243: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_244: R.Tensor((1280, 1280, 1, 1), dtype="float32"), transformed_param_245: R.Tensor((1280,), dtype="float32"), transformed_param_246: R.Tensor((1280,), dtype="float32"), transformed_param_247: R.Tensor((5120,), dtype="float32"), transformed_param_248: R.Tensor((5120,), dtype="float32"), transformed_param_249: R.Tensor((1280,), dtype="float32"), transformed_param_250: R.Tensor((1280,), dtype="float32"), transformed_param_251: R.Tensor((1280,), dtype="float32"), transformed_param_252: R.Tensor((1280,), dtype="float32"), transformed_param_253: R.Tensor((1280,), dtype="float32"), transformed_param_254: R.Tensor((1280,), dtype="float32"), transformed_param_255: R.Tensor((1280,), dtype="float32"), transformed_param_256: R.Tensor((1280, 2560, 3, 3), dtype="float32"), transformed_param_257: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_258: R.Tensor((1280, 2560, 1, 1), dtype="float32"), transformed_param_259: R.Tensor((2560,), dtype="float32"), transformed_param_260: R.Tensor((2560,), dtype="float32"), transformed_param_261: R.Tensor((1280,), dtype="float32"), transformed_param_262: R.Tensor((1280,), dtype="float32"), transformed_param_263: R.Tensor((1280,), dtype="float32"), transformed_param_264: R.Tensor((1280, 2560, 3, 3), dtype="float32"), transformed_param_265: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_266: R.Tensor((1280, 2560, 1, 1), dtype="float32"), transformed_param_267: R.Tensor((2560,), dtype="float32"), transformed_param_268: R.Tensor((2560,), dtype="float32"), transformed_param_269: R.Tensor((1280,), dtype="float32"), transformed_param_270: R.Tensor((1280,), dtype="float32"), transformed_param_271: R.Tensor((1280,), dtype="float32"), transformed_param_272: R.Tensor((1280, 1920, 3, 3), dtype="float32"), transformed_param_273: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_274: R.Tensor((1280, 1920, 1, 1), dtype="float32"), transformed_param_275: R.Tensor((1920,), dtype="float32"), transformed_param_276: R.Tensor((1920,), dtype="float32"), transformed_param_277: R.Tensor((1280,), dtype="float32"), transformed_param_278: R.Tensor((1280,), dtype="float32"), transformed_param_279: R.Tensor((1280,), dtype="float32"), transformed_param_280: R.Tensor((1280, 1280, 3, 3), dtype="float32"), transformed_param_281: R.Tensor((640,), dtype="float32"), transformed_param_282: R.Tensor((640,), dtype="float32"), transformed_param_283: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_284: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_285: R.Tensor((640,), dtype="float32"), transformed_param_286: R.Tensor((640,), dtype="float32"), transformed_param_287: R.Tensor((2560,), dtype="float32"), transformed_param_288: R.Tensor((2560,), dtype="float32"), transformed_param_289: R.Tensor((640,), dtype="float32"), transformed_param_290: R.Tensor((640,), dtype="float32"), transformed_param_291: R.Tensor((640,), dtype="float32"), transformed_param_292: R.Tensor((640,), dtype="float32"), transformed_param_293: R.Tensor((640,), dtype="float32"), transformed_param_294: R.Tensor((640,), dtype="float32"), transformed_param_295: R.Tensor((640,), dtype="float32"), transformed_param_296: R.Tensor((640,), dtype="float32"), transformed_param_297: R.Tensor((640,), dtype="float32"), transformed_param_298: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_299: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_300: R.Tensor((640,), dtype="float32"), transformed_param_301: R.Tensor((640,), dtype="float32"), transformed_param_302: R.Tensor((2560,), dtype="float32"), transformed_param_303: R.Tensor((2560,), dtype="float32"), transformed_param_304: R.Tensor((640,), dtype="float32"), transformed_param_305: R.Tensor((640,), dtype="float32"), transformed_param_306: R.Tensor((640,), dtype="float32"), transformed_param_307: R.Tensor((640,), dtype="float32"), transformed_param_308: R.Tensor((640,), dtype="float32"), transformed_param_309: R.Tensor((640,), dtype="float32"), transformed_param_310: R.Tensor((640,), dtype="float32"), transformed_param_311: R.Tensor((640,), dtype="float32"), transformed_param_312: R.Tensor((640,), dtype="float32"), transformed_param_313: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_314: R.Tensor((640, 640, 1, 1), dtype="float32"), transformed_param_315: R.Tensor((640,), dtype="float32"), transformed_param_316: R.Tensor((640,), dtype="float32"), transformed_param_317: R.Tensor((2560,), dtype="float32"), transformed_param_318: R.Tensor((2560,), dtype="float32"), transformed_param_319: R.Tensor((640,), dtype="float32"), transformed_param_320: R.Tensor((640,), dtype="float32"), transformed_param_321: R.Tensor((640,), dtype="float32"), transformed_param_322: R.Tensor((640,), dtype="float32"), transformed_param_323: R.Tensor((640,), dtype="float32"), transformed_param_324: R.Tensor((640,), dtype="float32"), transformed_param_325: R.Tensor((640,), dtype="float32"), transformed_param_326: R.Tensor((640, 1920, 3, 3), dtype="float32"), transformed_param_327: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_328: R.Tensor((640, 1920, 1, 1), dtype="float32"), transformed_param_329: R.Tensor((1920,), dtype="float32"), transformed_param_330: R.Tensor((1920,), dtype="float32"), transformed_param_331: R.Tensor((640,), dtype="float32"), transformed_param_332: R.Tensor((640,), dtype="float32"), transformed_param_333: R.Tensor((640,), dtype="float32"), transformed_param_334: R.Tensor((640, 1280, 3, 3), dtype="float32"), transformed_param_335: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_336: R.Tensor((640, 1280, 1, 1), dtype="float32"), transformed_param_337: R.Tensor((1280,), dtype="float32"), transformed_param_338: R.Tensor((1280,), dtype="float32"), transformed_param_339: R.Tensor((640,), dtype="float32"), transformed_param_340: R.Tensor((640,), dtype="float32"), transformed_param_341: R.Tensor((640,), dtype="float32"), transformed_param_342: R.Tensor((640, 960, 3, 3), dtype="float32"), transformed_param_343: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_344: R.Tensor((640, 960, 1, 1), dtype="float32"), transformed_param_345: R.Tensor((960,), dtype="float32"), transformed_param_346: R.Tensor((960,), dtype="float32"), transformed_param_347: R.Tensor((640,), dtype="float32"), transformed_param_348: R.Tensor((640,), dtype="float32"), transformed_param_349: R.Tensor((640,), dtype="float32"), transformed_param_350: R.Tensor((640, 640, 3, 3), dtype="float32"), transformed_param_351: R.Tensor((320,), dtype="float32"), transformed_param_352: R.Tensor((320,), dtype="float32"), transformed_param_353: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_354: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_355: R.Tensor((320,), dtype="float32"), transformed_param_356: R.Tensor((320,), dtype="float32"), transformed_param_357: R.Tensor((1280,), dtype="float32"), transformed_param_358: R.Tensor((1280,), dtype="float32"), transformed_param_359: R.Tensor((320,), dtype="float32"), transformed_param_360: R.Tensor((320,), dtype="float32"), transformed_param_361: R.Tensor((320,), dtype="float32"), transformed_param_362: R.Tensor((320,), dtype="float32"), transformed_param_363: R.Tensor((320,), dtype="float32"), transformed_param_364: R.Tensor((320,), dtype="float32"), transformed_param_365: R.Tensor((320,), dtype="float32"), transformed_param_366: R.Tensor((320,), dtype="float32"), transformed_param_367: R.Tensor((320,), dtype="float32"), transformed_param_368: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_369: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_370: R.Tensor((320,), dtype="float32"), transformed_param_371: R.Tensor((320,), dtype="float32"), transformed_param_372: R.Tensor((1280,), dtype="float32"), transformed_param_373: R.Tensor((1280,), dtype="float32"), transformed_param_374: R.Tensor((320,), dtype="float32"), transformed_param_375: R.Tensor((320,), dtype="float32"), transformed_param_376: R.Tensor((320,), dtype="float32"), transformed_param_377: R.Tensor((320,), dtype="float32"), transformed_param_378: R.Tensor((320,), dtype="float32"), transformed_param_379: R.Tensor((320,), dtype="float32"), transformed_param_380: R.Tensor((320,), dtype="float32"), transformed_param_381: R.Tensor((320,), dtype="float32"), transformed_param_382: R.Tensor((320,), dtype="float32"), transformed_param_383: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_384: R.Tensor((320, 320, 1, 1), dtype="float32"), transformed_param_385: R.Tensor((320,), dtype="float32"), transformed_param_386: R.Tensor((320,), dtype="float32"), transformed_param_387: R.Tensor((1280,), dtype="float32"), transformed_param_388: R.Tensor((1280,), dtype="float32"), transformed_param_389: R.Tensor((320,), dtype="float32"), transformed_param_390: R.Tensor((320,), dtype="float32"), transformed_param_391: R.Tensor((320,), dtype="float32"), transformed_param_392: R.Tensor((320,), dtype="float32"), transformed_param_393: R.Tensor((320,), dtype="float32"), transformed_param_394: R.Tensor((320,), dtype="float32"), transformed_param_395: R.Tensor((320,), dtype="float32"), transformed_param_396: R.Tensor((320, 960, 3, 3), dtype="float32"), transformed_param_397: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_398: R.Tensor((320, 960, 1, 1), dtype="float32"), transformed_param_399: R.Tensor((960,), dtype="float32"), transformed_param_400: R.Tensor((960,), dtype="float32"), transformed_param_401: R.Tensor((320,), dtype="float32"), transformed_param_402: R.Tensor((320,), dtype="float32"), transformed_param_403: R.Tensor((320,), dtype="float32"), transformed_param_404: R.Tensor((320, 640, 3, 3), dtype="float32"), transformed_param_405: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_406: R.Tensor((320, 640, 1, 1), dtype="float32"), transformed_param_407: R.Tensor((640,), dtype="float32"), transformed_param_408: R.Tensor((640,), dtype="float32"), transformed_param_409: R.Tensor((320,), dtype="float32"), transformed_param_410: R.Tensor((320,), dtype="float32"), transformed_param_411: R.Tensor((320,), dtype="float32"), transformed_param_412: R.Tensor((320, 640, 3, 3), dtype="float32"), transformed_param_413: R.Tensor((320, 320, 3, 3), dtype="float32"), transformed_param_414: R.Tensor((320, 640, 1, 1), dtype="float32"), transformed_param_415: R.Tensor((640,), dtype="float32"), transformed_param_416: R.Tensor((640,), dtype="float32"), transformed_param_417: R.Tensor((320,), dtype="float32"), transformed_param_418: R.Tensor((320,), dtype="float32"), transformed_param_419: R.Tensor((320,), dtype="float32"), transformed_param_420: R.Tensor((320, 1280), dtype="float32"), transformed_param_421: R.Tensor((1280, 1280), dtype="float32"), transformed_param_422: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_423: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_424: R.Tensor((1280, 320), dtype="float32"), transformed_param_425: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_426: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_427: R.Tensor((320, 320), dtype="float32"), transformed_param_428: R.Tensor((320, 320), dtype="float32"), transformed_param_429: R.Tensor((320, 320), dtype="float32"), transformed_param_430: R.Tensor((320, 320), dtype="float32"), transformed_param_431: R.Tensor((320, 320), dtype="float32"), transformed_param_432: R.Tensor((768, 320), dtype="float32"), transformed_param_433: R.Tensor((768, 320), dtype="float32"), transformed_param_434: R.Tensor((320, 320), dtype="float32"), transformed_param_435: R.Tensor((320, 1280), dtype="float32"), transformed_param_436: R.Tensor((320, 1280), dtype="float32"), transformed_param_437: R.Tensor((1280, 320), dtype="float32"), transformed_param_438: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_439: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_440: R.Tensor((1280, 320), dtype="float32"), transformed_param_441: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_442: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_443: R.Tensor((320, 320), dtype="float32"), transformed_param_444: R.Tensor((320, 320), dtype="float32"), transformed_param_445: R.Tensor((320, 320), dtype="float32"), transformed_param_446: R.Tensor((320, 320), dtype="float32"), transformed_param_447: R.Tensor((320, 320), dtype="float32"), transformed_param_448: R.Tensor((768, 320), dtype="float32"), transformed_param_449: R.Tensor((768, 320), dtype="float32"), transformed_param_450: R.Tensor((320, 320), dtype="float32"), transformed_param_451: R.Tensor((320, 1280), dtype="float32"), transformed_param_452: R.Tensor((320, 1280), dtype="float32"), transformed_param_453: R.Tensor((1280, 320), dtype="float32"), transformed_param_454: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_455: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_456: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_457: R.Tensor((1280, 640), dtype="float32"), transformed_param_458: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_459: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_460: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_461: R.Tensor((640, 640), dtype="float32"), transformed_param_462: R.Tensor((640, 640), dtype="float32"), transformed_param_463: R.Tensor((640, 640), dtype="float32"), transformed_param_464: R.Tensor((640, 640), dtype="float32"), transformed_param_465: R.Tensor((640, 640), dtype="float32"), transformed_param_466: R.Tensor((768, 640), dtype="float32"), transformed_param_467: R.Tensor((768, 640), dtype="float32"), transformed_param_468: R.Tensor((640, 640), dtype="float32"), transformed_param_469: R.Tensor((640, 2560), dtype="float32"), transformed_param_470: R.Tensor((640, 2560), dtype="float32"), transformed_param_471: R.Tensor((2560, 640), dtype="float32"), transformed_param_472: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_473: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_474: R.Tensor((1280, 640), dtype="float32"), transformed_param_475: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_476: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_477: R.Tensor((640, 640), dtype="float32"), transformed_param_478: R.Tensor((640, 640), dtype="float32"), transformed_param_479: R.Tensor((640, 640), dtype="float32"), transformed_param_480: R.Tensor((640, 640), dtype="float32"), transformed_param_481: R.Tensor((640, 640), dtype="float32"), transformed_param_482: R.Tensor((768, 640), dtype="float32"), transformed_param_483: R.Tensor((768, 640), dtype="float32"), transformed_param_484: R.Tensor((640, 640), dtype="float32"), transformed_param_485: R.Tensor((640, 2560), dtype="float32"), transformed_param_486: R.Tensor((640, 2560), dtype="float32"), transformed_param_487: R.Tensor((2560, 640), dtype="float32"), transformed_param_488: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_489: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_490: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_491: R.Tensor((1280, 1280), dtype="float32"), transformed_param_492: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_493: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_494: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_495: R.Tensor((1280, 1280), dtype="float32"), transformed_param_496: R.Tensor((1280, 1280), dtype="float32"), transformed_param_497: R.Tensor((1280, 1280), dtype="float32"), transformed_param_498: R.Tensor((1280, 1280), dtype="float32"), transformed_param_499: R.Tensor((1280, 1280), dtype="float32"), transformed_param_500: R.Tensor((768, 1280), dtype="float32"), transformed_param_501: R.Tensor((768, 1280), dtype="float32"), transformed_param_502: R.Tensor((1280, 1280), dtype="float32"), transformed_param_503: R.Tensor((1280, 5120), dtype="float32"), transformed_param_504: R.Tensor((1280, 5120), dtype="float32"), transformed_param_505: R.Tensor((5120, 1280), dtype="float32"), transformed_param_506: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_507: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_508: R.Tensor((1280, 1280), dtype="float32"), transformed_param_509: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_510: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_511: R.Tensor((1280, 1280), dtype="float32"), transformed_param_512: R.Tensor((1280, 1280), dtype="float32"), transformed_param_513: R.Tensor((1280, 1280), dtype="float32"), transformed_param_514: R.Tensor((1280, 1280), dtype="float32"), transformed_param_515: R.Tensor((1280, 1280), dtype="float32"), transformed_param_516: R.Tensor((768, 1280), dtype="float32"), transformed_param_517: R.Tensor((768, 1280), dtype="float32"), transformed_param_518: R.Tensor((1280, 1280), dtype="float32"), transformed_param_519: R.Tensor((1280, 5120), dtype="float32"), transformed_param_520: R.Tensor((1280, 5120), dtype="float32"), transformed_param_521: R.Tensor((5120, 1280), dtype="float32"), transformed_param_522: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_523: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_524: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_525: R.Tensor((1280, 1280), dtype="float32"), transformed_param_526: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_527: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_528: R.Tensor((1280, 1280), dtype="float32"), transformed_param_529: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_530: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_531: R.Tensor((1280, 1280), dtype="float32"), transformed_param_532: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_533: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_534: R.Tensor((1280, 1280), dtype="float32"), transformed_param_535: R.Tensor((1280, 1280), dtype="float32"), transformed_param_536: R.Tensor((1280, 1280), dtype="float32"), transformed_param_537: R.Tensor((1280, 1280), dtype="float32"), transformed_param_538: R.Tensor((1280, 1280), dtype="float32"), transformed_param_539: R.Tensor((768, 1280), dtype="float32"), transformed_param_540: R.Tensor((768, 1280), dtype="float32"), transformed_param_541: R.Tensor((1280, 1280), dtype="float32"), transformed_param_542: R.Tensor((1280, 5120), dtype="float32"), transformed_param_543: R.Tensor((1280, 5120), dtype="float32"), transformed_param_544: R.Tensor((5120, 1280), dtype="float32"), transformed_param_545: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_546: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_547: R.Tensor((1280, 1280), dtype="float32"), transformed_param_548: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_549: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_550: R.Tensor((1280, 1280), dtype="float32"), transformed_param_551: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_552: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_553: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_554: R.Tensor((1280, 1280), dtype="float32"), transformed_param_555: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_556: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_557: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_558: R.Tensor((1280, 1280), dtype="float32"), transformed_param_559: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_560: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_561: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_562: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_563: R.Tensor((1280, 1280), dtype="float32"), transformed_param_564: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_565: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_566: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_567: R.Tensor((1280, 1280), dtype="float32"), transformed_param_568: R.Tensor((1280, 1280), dtype="float32"), transformed_param_569: R.Tensor((1280, 1280), dtype="float32"), transformed_param_570: R.Tensor((1280, 1280), dtype="float32"), transformed_param_571: R.Tensor((1280, 1280), dtype="float32"), transformed_param_572: R.Tensor((768, 1280), dtype="float32"), transformed_param_573: R.Tensor((768, 1280), dtype="float32"), transformed_param_574: R.Tensor((1280, 1280), dtype="float32"), transformed_param_575: R.Tensor((1280, 5120), dtype="float32"), transformed_param_576: R.Tensor((1280, 5120), dtype="float32"), transformed_param_577: R.Tensor((5120, 1280), dtype="float32"), transformed_param_578: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_579: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_580: R.Tensor((1280, 1280), dtype="float32"), transformed_param_581: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_582: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_583: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_584: R.Tensor((1280, 1280), dtype="float32"), transformed_param_585: R.Tensor((1280, 1280), dtype="float32"), transformed_param_586: R.Tensor((1280, 1280), dtype="float32"), transformed_param_587: R.Tensor((1280, 1280), dtype="float32"), transformed_param_588: R.Tensor((1280, 1280), dtype="float32"), transformed_param_589: R.Tensor((768, 1280), dtype="float32"), transformed_param_590: R.Tensor((768, 1280), dtype="float32"), transformed_param_591: R.Tensor((1280, 1280), dtype="float32"), transformed_param_592: R.Tensor((1280, 5120), dtype="float32"), transformed_param_593: R.Tensor((1280, 5120), dtype="float32"), transformed_param_594: R.Tensor((5120, 1280), dtype="float32"), transformed_param_595: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_596: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_597: R.Tensor((1280, 1280), dtype="float32"), transformed_param_598: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_599: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_600: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_601: R.Tensor((1280, 1280), dtype="float32"), transformed_param_602: R.Tensor((1280, 1280), dtype="float32"), transformed_param_603: R.Tensor((1280, 1280), dtype="float32"), transformed_param_604: R.Tensor((1280, 1280), dtype="float32"), transformed_param_605: R.Tensor((1280, 1280), dtype="float32"), transformed_param_606: R.Tensor((768, 1280), dtype="float32"), transformed_param_607: R.Tensor((768, 1280), dtype="float32"), transformed_param_608: R.Tensor((1280, 1280), dtype="float32"), transformed_param_609: R.Tensor((1280, 5120), dtype="float32"), transformed_param_610: R.Tensor((1280, 5120), dtype="float32"), transformed_param_611: R.Tensor((5120, 1280), dtype="float32"), transformed_param_612: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_613: R.Tensor((1, 1280, 1, 1), dtype="float32"), transformed_param_614: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_615: R.Tensor((1280, 640), dtype="float32"), transformed_param_616: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_617: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_618: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_619: R.Tensor((640, 640), dtype="float32"), transformed_param_620: R.Tensor((640, 640), dtype="float32"), transformed_param_621: R.Tensor((640, 640), dtype="float32"), transformed_param_622: R.Tensor((640, 640), dtype="float32"), transformed_param_623: R.Tensor((640, 640), dtype="float32"), transformed_param_624: R.Tensor((768, 640), dtype="float32"), transformed_param_625: R.Tensor((768, 640), dtype="float32"), transformed_param_626: R.Tensor((640, 640), dtype="float32"), transformed_param_627: R.Tensor((640, 2560), dtype="float32"), transformed_param_628: R.Tensor((640, 2560), dtype="float32"), transformed_param_629: R.Tensor((2560, 640), dtype="float32"), transformed_param_630: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_631: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_632: R.Tensor((1280, 640), dtype="float32"), transformed_param_633: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_634: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_635: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_636: R.Tensor((640, 640), dtype="float32"), transformed_param_637: R.Tensor((640, 640), dtype="float32"), transformed_param_638: R.Tensor((640, 640), dtype="float32"), transformed_param_639: R.Tensor((640, 640), dtype="float32"), transformed_param_640: R.Tensor((640, 640), dtype="float32"), transformed_param_641: R.Tensor((768, 640), dtype="float32"), transformed_param_642: R.Tensor((768, 640), dtype="float32"), transformed_param_643: R.Tensor((640, 640), dtype="float32"), transformed_param_644: R.Tensor((640, 2560), dtype="float32"), transformed_param_645: R.Tensor((640, 2560), dtype="float32"), transformed_param_646: R.Tensor((2560, 640), dtype="float32"), transformed_param_647: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_648: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_649: R.Tensor((1280, 640), dtype="float32"), transformed_param_650: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_651: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_652: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_653: R.Tensor((640, 640), dtype="float32"), transformed_param_654: R.Tensor((640, 640), dtype="float32"), transformed_param_655: R.Tensor((640, 640), dtype="float32"), transformed_param_656: R.Tensor((640, 640), dtype="float32"), transformed_param_657: R.Tensor((640, 640), dtype="float32"), transformed_param_658: R.Tensor((768, 640), dtype="float32"), transformed_param_659: R.Tensor((768, 640), dtype="float32"), transformed_param_660: R.Tensor((640, 640), dtype="float32"), transformed_param_661: R.Tensor((640, 2560), dtype="float32"), transformed_param_662: R.Tensor((640, 2560), dtype="float32"), transformed_param_663: R.Tensor((2560, 640), dtype="float32"), transformed_param_664: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_665: R.Tensor((1, 640, 1, 1), dtype="float32"), transformed_param_666: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_667: R.Tensor((1280, 320), dtype="float32"), transformed_param_668: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_669: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_670: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_671: R.Tensor((320, 320), dtype="float32"), transformed_param_672: R.Tensor((320, 320), dtype="float32"), transformed_param_673: R.Tensor((320, 320), dtype="float32"), transformed_param_674: R.Tensor((320, 320), dtype="float32"), transformed_param_675: R.Tensor((320, 320), dtype="float32"), transformed_param_676: R.Tensor((768, 320), dtype="float32"), transformed_param_677: R.Tensor((768, 320), dtype="float32"), transformed_param_678: R.Tensor((320, 320), dtype="float32"), transformed_param_679: R.Tensor((320, 1280), dtype="float32"), transformed_param_680: R.Tensor((320, 1280), dtype="float32"), transformed_param_681: R.Tensor((1280, 320), dtype="float32"), transformed_param_682: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_683: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_684: R.Tensor((1280, 320), dtype="float32"), transformed_param_685: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_686: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_687: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_688: R.Tensor((320, 320), dtype="float32"), transformed_param_689: R.Tensor((320, 320), dtype="float32"), transformed_param_690: R.Tensor((320, 320), dtype="float32"), transformed_param_691: R.Tensor((320, 320), dtype="float32"), transformed_param_692: R.Tensor((320, 320), dtype="float32"), transformed_param_693: R.Tensor((768, 320), dtype="float32"), transformed_param_694: R.Tensor((768, 320), dtype="float32"), transformed_param_695: R.Tensor((320, 320), dtype="float32"), transformed_param_696: R.Tensor((320, 1280), dtype="float32"), transformed_param_697: R.Tensor((320, 1280), dtype="float32"), transformed_param_698: R.Tensor((1280, 320), dtype="float32"), transformed_param_699: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_700: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_701: R.Tensor((1280, 320), dtype="float32"), transformed_param_702: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_703: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_704: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_705: R.Tensor((320, 320), dtype="float32"), transformed_param_706: R.Tensor((320, 320), dtype="float32"), transformed_param_707: R.Tensor((320, 320), dtype="float32"), transformed_param_708: R.Tensor((320, 320), dtype="float32"), transformed_param_709: R.Tensor((320, 320), dtype="float32"), transformed_param_710: R.Tensor((768, 320), dtype="float32"), transformed_param_711: R.Tensor((768, 320), dtype="float32"), transformed_param_712: R.Tensor((320, 320), dtype="float32"), transformed_param_713: R.Tensor((320, 1280), dtype="float32"), transformed_param_714: R.Tensor((320, 1280), dtype="float32"), transformed_param_715: R.Tensor((1280, 320), dtype="float32"), transformed_param_716: R.Tensor((1, 320, 1, 1), dtype="float32"), transformed_param_717: R.Tensor((1, 4, 1, 1), dtype="float32")) -> R.Tensor((1, 4, 64, 64), dtype="float32"):
        R.func_attr({"global_symbol": "main", "num_input": 3})
        cls = Module
        with R.dataflow():
            lv = R.call_tir(cls.concatenate1, (inp_0, inp_0), out_sinfo=R.Tensor((2, 4, 64, 64), dtype="float32"))
            lv211 = R.call_tir(cls.fused_broadcast_to1_strided_slice_reshape20_cast3_multiply11_multiply12_tir_sin_tir_cos_concatenate2_strided_slice1_reshape21_strided_slice2_reshape21_concatenate2, (inp_1, metadata["relax.expr.Constant"][1]), out_sinfo=R.Tensor((2, 320), dtype="float32"))
            lv336: R.Tensor((320, 1280), dtype="float32") = transformed_param_420
            lv337: R.Tensor((1280,), dtype="float32") = transformed_param_184
            lv212 = R.call_tir(cls.fused_matmul8_add20_silu6, (lv211, lv336, lv337), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv338: R.Tensor((1280, 1280), dtype="float32") = transformed_param_421
            lv339: R.Tensor((1280,), dtype="float32") = transformed_param_185
            lv213 = R.call_tir(cls.fused_matmul9_add20, (lv212, lv338, lv339), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv340: R.Tensor((320, 4, 3, 3), dtype="float32") = transformed_param_0
            lv341: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_422
            lv214 = R.call_tir(cls.fused_conv2d13_add21, (lv, lv340, lv341), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv342: R.Tensor((320,), dtype="float32") = transformed_param_38
            lv343: R.Tensor((320,), dtype="float32") = transformed_param_37
            lv215 = R.call_tir(cls.fused_group_norm7_silu7, (lv214, lv342, lv343), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv30 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv344: R.Tensor((1280, 320), dtype="float32") = transformed_param_424
            lv345: R.Tensor((320,), dtype="float32") = transformed_param_41
            lv216 = R.call_tir(cls.fused_matmul10_add22_strided_slice3, (lv30, lv344, lv345), out_sinfo=R.Tensor((2, 320), dtype="float32"))
            lv35 = R.call_tir(cls.reshape23, (lv216,), out_sinfo=R.Tensor((2, 320, 1, 1), dtype="float32"))
            lv346: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_35
            lv347: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_423
            lv217 = R.call_tir(cls.fused_conv2d14_add21_add23, (lv215, lv346, lv347, lv35), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv348: R.Tensor((320,), dtype="float32") = transformed_param_40
            lv349: R.Tensor((320,), dtype="float32") = transformed_param_39
            lv218 = R.call_tir(cls.fused_group_norm7_silu7, (lv217, lv348, lv349), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv350: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_36
            lv351: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_425
            lv219 = R.call_tir(cls.fused_conv2d14_add21_add24_divide9, (lv218, lv350, lv351, lv214), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv352: R.Tensor((320,), dtype="float32") = transformed_param_5
            lv353: R.Tensor((320,), dtype="float32") = transformed_param_4
            lv44 = R.call_tir(cls.group_norm8, (lv219, lv352, lv353), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv354: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_6
            lv355: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_426
            lv220 = R.call_tir(cls.fused_conv2d15_add21, (lv44, lv354, lv355), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv221 = R.call_tir(cls.fused_transpose16_reshape24, (lv220,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv356: R.Tensor((320,), dtype="float32") = transformed_param_14
            lv357: R.Tensor((320,), dtype="float32") = transformed_param_13
            lv50 = R.call_tir(cls.layer_norm1, (lv221, lv356, lv357), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv358: R.Tensor((320, 320), dtype="float32") = transformed_param_427
            lv52 = R.call_tir(cls.matmul11, (lv50, lv358), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv359: R.Tensor((320, 320), dtype="float32") = transformed_param_428
            lv54 = R.call_tir(cls.matmul11, (lv50, lv359), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv360: R.Tensor((320, 320), dtype="float32") = transformed_param_429
            lv56 = R.call_tir(cls.matmul11, (lv50, lv360), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv222 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv52,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv223 = R.call_tir(cls.fused_reshape25_transpose18_reshape26_transpose19, (lv54,), out_sinfo=R.Tensor((16, 40, 4096), dtype="float32"))
            lv224 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv56,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv225 = R.call_tir(cls.fused_matmul12_multiply13, (lv222, lv223), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv69 = R.call_tir(cls.softmax2, (lv225,), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv70 = R.call_tir(cls.matmul13, (lv69, lv224), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv226 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv70,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv361: R.Tensor((320, 320), dtype="float32") = transformed_param_430
            lv362: R.Tensor((320,), dtype="float32") = transformed_param_8
            lv227 = R.call_tir(cls.fused_matmul11_add25_add26, (lv226, lv361, lv362, lv221), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv363: R.Tensor((320,), dtype="float32") = transformed_param_16
            lv364: R.Tensor((320,), dtype="float32") = transformed_param_15
            lv78 = R.call_tir(cls.layer_norm1, (lv227, lv363, lv364), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv365: R.Tensor((320, 320), dtype="float32") = transformed_param_431
            lv80 = R.call_tir(cls.matmul11, (lv78, lv365), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv366: R.Tensor((768, 320), dtype="float32") = transformed_param_432
            lv82 = R.call_tir(cls.matmul14, (inp_2, lv366), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv367: R.Tensor((768, 320), dtype="float32") = transformed_param_433
            lv84 = R.call_tir(cls.matmul14, (inp_2, lv367), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv228 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv80,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv229 = R.call_tir(cls.fused_reshape29_transpose22_reshape30_transpose23, (lv82,), out_sinfo=R.Tensor((16, 40, 77), dtype="float32"))
            lv230 = R.call_tir(cls.fused_reshape29_transpose22_reshape30, (lv84,), out_sinfo=R.Tensor((16, 77, 40), dtype="float32"))
            lv231 = R.call_tir(cls.fused_matmul15_multiply14, (lv228, lv229), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv97 = R.call_tir(cls.softmax3, (lv231,), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv98 = R.call_tir(cls.matmul16, (lv97, lv230), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv232 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv98,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv368: R.Tensor((320, 320), dtype="float32") = transformed_param_434
            lv369: R.Tensor((320,), dtype="float32") = transformed_param_9
            lv233 = R.call_tir(cls.fused_matmul11_add25_add26, (lv232, lv368, lv369, lv227), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv370: R.Tensor((320,), dtype="float32") = transformed_param_18
            lv371: R.Tensor((320,), dtype="float32") = transformed_param_17
            lv106 = R.call_tir(cls.layer_norm1, (lv233, lv370, lv371), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv372: R.Tensor((320, 1280), dtype="float32") = transformed_param_436
            lv373: R.Tensor((1280,), dtype="float32") = transformed_param_11
            lv234 = R.call_tir(cls.fused_matmul17_add27_gelu, (lv106, lv372, lv373), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv374: R.Tensor((320, 1280), dtype="float32") = transformed_param_435
            lv375: R.Tensor((1280,), dtype="float32") = transformed_param_10
            lv235 = R.call_tir(cls.fused_matmul17_add27_multiply15, (lv106, lv374, lv375, lv234), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv376: R.Tensor((1280, 320), dtype="float32") = transformed_param_437
            lv377: R.Tensor((320,), dtype="float32") = transformed_param_12
            lv236 = R.call_tir(cls.fused_matmul18_add25_add26, (lv235, lv376, lv377, lv233), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv237 = R.call_tir(cls.fused_reshape31_transpose24, (lv236,), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv378: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_7
            lv379: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_438
            lv238 = R.call_tir(cls.fused_conv2d15_add21_add24, (lv237, lv378, lv379, lv219), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv380: R.Tensor((320,), dtype="float32") = transformed_param_45
            lv381: R.Tensor((320,), dtype="float32") = transformed_param_44
            lv239 = R.call_tir(cls.fused_group_norm7_silu7, (lv238, lv380, lv381), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv130 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv382: R.Tensor((1280, 320), dtype="float32") = transformed_param_440
            lv383: R.Tensor((320,), dtype="float32") = transformed_param_48
            lv240 = R.call_tir(cls.fused_matmul10_add22_strided_slice3, (lv130, lv382, lv383), out_sinfo=R.Tensor((2, 320), dtype="float32"))
            lv135 = R.call_tir(cls.reshape23, (lv240,), out_sinfo=R.Tensor((2, 320, 1, 1), dtype="float32"))
            lv384: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_42
            lv385: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_439
            lv241 = R.call_tir(cls.fused_conv2d14_add21_add23, (lv239, lv384, lv385, lv135), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv386: R.Tensor((320,), dtype="float32") = transformed_param_47
            lv387: R.Tensor((320,), dtype="float32") = transformed_param_46
            lv242 = R.call_tir(cls.fused_group_norm7_silu7, (lv241, lv386, lv387), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv388: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_43
            lv389: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_441
            lv243 = R.call_tir(cls.fused_conv2d14_add21_add24_divide9, (lv242, lv388, lv389, lv238), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv390: R.Tensor((320,), dtype="float32") = transformed_param_20
            lv391: R.Tensor((320,), dtype="float32") = transformed_param_19
            lv144 = R.call_tir(cls.group_norm8, (lv243, lv390, lv391), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv392: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_21
            lv393: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_442
            lv244 = R.call_tir(cls.fused_conv2d15_add21, (lv144, lv392, lv393), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv245 = R.call_tir(cls.fused_transpose16_reshape24, (lv244,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv394: R.Tensor((320,), dtype="float32") = transformed_param_29
            lv395: R.Tensor((320,), dtype="float32") = transformed_param_28
            lv150 = R.call_tir(cls.layer_norm1, (lv245, lv394, lv395), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv396: R.Tensor((320, 320), dtype="float32") = transformed_param_443
            lv152 = R.call_tir(cls.matmul11, (lv150, lv396), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv397: R.Tensor((320, 320), dtype="float32") = transformed_param_444
            lv154 = R.call_tir(cls.matmul11, (lv150, lv397), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv398: R.Tensor((320, 320), dtype="float32") = transformed_param_445
            lv156 = R.call_tir(cls.matmul11, (lv150, lv398), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv246 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv152,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv247 = R.call_tir(cls.fused_reshape25_transpose18_reshape26_transpose19, (lv154,), out_sinfo=R.Tensor((16, 40, 4096), dtype="float32"))
            lv248 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv156,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv249 = R.call_tir(cls.fused_matmul12_multiply13, (lv246, lv247), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv169 = R.call_tir(cls.softmax2, (lv249,), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv170 = R.call_tir(cls.matmul13, (lv169, lv248), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv250 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv170,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv399: R.Tensor((320, 320), dtype="float32") = transformed_param_446
            lv400: R.Tensor((320,), dtype="float32") = transformed_param_23
            lv251 = R.call_tir(cls.fused_matmul11_add25_add26, (lv250, lv399, lv400, lv245), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv401: R.Tensor((320,), dtype="float32") = transformed_param_31
            lv402: R.Tensor((320,), dtype="float32") = transformed_param_30
            lv178 = R.call_tir(cls.layer_norm1, (lv251, lv401, lv402), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv403: R.Tensor((320, 320), dtype="float32") = transformed_param_447
            lv180 = R.call_tir(cls.matmul11, (lv178, lv403), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv404: R.Tensor((768, 320), dtype="float32") = transformed_param_448
            lv182 = R.call_tir(cls.matmul14, (inp_2, lv404), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv405: R.Tensor((768, 320), dtype="float32") = transformed_param_449
            lv184 = R.call_tir(cls.matmul14, (inp_2, lv405), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv252 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv180,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv253 = R.call_tir(cls.fused_reshape29_transpose22_reshape30_transpose23, (lv182,), out_sinfo=R.Tensor((16, 40, 77), dtype="float32"))
            lv254 = R.call_tir(cls.fused_reshape29_transpose22_reshape30, (lv184,), out_sinfo=R.Tensor((16, 77, 40), dtype="float32"))
            lv255 = R.call_tir(cls.fused_matmul15_multiply14, (lv252, lv253), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv197 = R.call_tir(cls.softmax3, (lv255,), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv198 = R.call_tir(cls.matmul16, (lv197, lv254), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv256 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv198,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv406: R.Tensor((320, 320), dtype="float32") = transformed_param_450
            lv407: R.Tensor((320,), dtype="float32") = transformed_param_24
            lv257 = R.call_tir(cls.fused_matmul11_add25_add26, (lv256, lv406, lv407, lv251), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv408: R.Tensor((320,), dtype="float32") = transformed_param_33
            lv409: R.Tensor((320,), dtype="float32") = transformed_param_32
            lv206 = R.call_tir(cls.layer_norm1, (lv257, lv408, lv409), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv410: R.Tensor((320, 1280), dtype="float32") = transformed_param_452
            lv411: R.Tensor((1280,), dtype="float32") = transformed_param_26
            lv258 = R.call_tir(cls.fused_matmul17_add27_gelu, (lv206, lv410, lv411), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv412: R.Tensor((320, 1280), dtype="float32") = transformed_param_451
            lv413: R.Tensor((1280,), dtype="float32") = transformed_param_25
            lv259 = R.call_tir(cls.fused_matmul17_add27_multiply15, (lv206, lv412, lv413, lv258), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv414: R.Tensor((1280, 320), dtype="float32") = transformed_param_453
            lv415: R.Tensor((320,), dtype="float32") = transformed_param_27
            lv260 = R.call_tir(cls.fused_matmul18_add25_add26, (lv259, lv414, lv415, lv257), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv261 = R.call_tir(cls.fused_reshape31_transpose24, (lv260,), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv416: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_22
            lv417: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_454
            lv262 = R.call_tir(cls.fused_conv2d15_add21_add24, (lv261, lv416, lv417, lv243), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv418: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_34
            lv419: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_455
            lv263 = R.call_tir(cls.fused_conv2d16_add28, (lv262, lv418, lv419), out_sinfo=R.Tensor((2, 320, 32, 32), dtype="float32"))
            lv420: R.Tensor((320,), dtype="float32") = transformed_param_84
            lv421: R.Tensor((320,), dtype="float32") = transformed_param_83
            lv264 = R.call_tir(cls.fused_group_norm9_silu8, (lv263, lv420, lv421), out_sinfo=R.Tensor((2, 320, 32, 32), dtype="float32"))
            lv233_1 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv422: R.Tensor((1280, 640), dtype="float32") = transformed_param_457
            lv423: R.Tensor((640,), dtype="float32") = transformed_param_87
            lv265 = R.call_tir(cls.fused_matmul19_add30_strided_slice4, (lv233_1, lv422, lv423), out_sinfo=R.Tensor((2, 640), dtype="float32"))
            lv238_1 = R.call_tir(cls.reshape33, (lv265,), out_sinfo=R.Tensor((2, 640, 1, 1), dtype="float32"))
            lv424: R.Tensor((640, 320, 3, 3), dtype="float32") = transformed_param_80
            lv425: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_456
            lv266 = R.call_tir(cls.fused_conv2d17_add29_add31, (lv264, lv424, lv425, lv238_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv426: R.Tensor((640,), dtype="float32") = transformed_param_86
            lv427: R.Tensor((640,), dtype="float32") = transformed_param_85
            lv267 = R.call_tir(cls.fused_group_norm10_silu9, (lv266, lv426, lv427), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv428: R.Tensor((640, 320, 1, 1), dtype="float32") = transformed_param_82
            lv429: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_459
            lv268 = R.call_tir(cls.fused_conv2d19_add29, (lv263, lv428, lv429), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv430: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_81
            lv431: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_458
            lv269 = R.call_tir(cls.fused_conv2d18_add29_add32_divide10, (lv267, lv430, lv431, lv268), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv432: R.Tensor((640,), dtype="float32") = transformed_param_50
            lv433: R.Tensor((640,), dtype="float32") = transformed_param_49
            lv250_1 = R.call_tir(cls.group_norm11, (lv269, lv432, lv433), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv434: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_51
            lv435: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_460
            lv270 = R.call_tir(cls.fused_conv2d20_add29, (lv250_1, lv434, lv435), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv271 = R.call_tir(cls.fused_transpose26_reshape34, (lv270,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv436: R.Tensor((640,), dtype="float32") = transformed_param_59
            lv437: R.Tensor((640,), dtype="float32") = transformed_param_58
            lv256_1 = R.call_tir(cls.layer_norm2, (lv271, lv436, lv437), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv438: R.Tensor((640, 640), dtype="float32") = transformed_param_461
            lv258_1 = R.call_tir(cls.matmul20, (lv256_1, lv438), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv439: R.Tensor((640, 640), dtype="float32") = transformed_param_462
            lv260_1 = R.call_tir(cls.matmul20, (lv256_1, lv439), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv440: R.Tensor((640, 640), dtype="float32") = transformed_param_463
            lv262_1 = R.call_tir(cls.matmul20, (lv256_1, lv440), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv272 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv258_1,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv273 = R.call_tir(cls.fused_reshape35_transpose28_reshape36_transpose29, (lv260_1,), out_sinfo=R.Tensor((16, 80, 1024), dtype="float32"))
            lv274 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv262_1,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv275 = R.call_tir(cls.fused_matmul21_multiply16, (lv272, lv273), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv275_1 = R.call_tir(cls.softmax4, (lv275,), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv276 = R.call_tir(cls.matmul22, (lv275_1, lv274), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv276_1 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv276,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv441: R.Tensor((640, 640), dtype="float32") = transformed_param_464
            lv442: R.Tensor((640,), dtype="float32") = transformed_param_53
            lv277 = R.call_tir(cls.fused_matmul20_add33_add34, (lv276_1, lv441, lv442, lv271), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv443: R.Tensor((640,), dtype="float32") = transformed_param_61
            lv444: R.Tensor((640,), dtype="float32") = transformed_param_60
            lv284 = R.call_tir(cls.layer_norm2, (lv277, lv443, lv444), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv445: R.Tensor((640, 640), dtype="float32") = transformed_param_465
            lv286 = R.call_tir(cls.matmul20, (lv284, lv445), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv446: R.Tensor((768, 640), dtype="float32") = transformed_param_466
            lv288 = R.call_tir(cls.matmul23, (inp_2, lv446), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv447: R.Tensor((768, 640), dtype="float32") = transformed_param_467
            lv290 = R.call_tir(cls.matmul23, (inp_2, lv447), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv278 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv286,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv279 = R.call_tir(cls.fused_reshape39_transpose32_reshape40_transpose33, (lv288,), out_sinfo=R.Tensor((16, 80, 77), dtype="float32"))
            lv280 = R.call_tir(cls.fused_reshape39_transpose32_reshape40, (lv290,), out_sinfo=R.Tensor((16, 77, 80), dtype="float32"))
            lv281 = R.call_tir(cls.fused_matmul24_multiply17, (lv278, lv279), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv303 = R.call_tir(cls.softmax5, (lv281,), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv304 = R.call_tir(cls.matmul25, (lv303, lv280), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv282 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv304,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv448: R.Tensor((640, 640), dtype="float32") = transformed_param_468
            lv449: R.Tensor((640,), dtype="float32") = transformed_param_54
            lv283 = R.call_tir(cls.fused_matmul20_add33_add34, (lv282, lv448, lv449, lv277), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv450: R.Tensor((640,), dtype="float32") = transformed_param_63
            lv451: R.Tensor((640,), dtype="float32") = transformed_param_62
            lv312 = R.call_tir(cls.layer_norm2, (lv283, lv450, lv451), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv452: R.Tensor((640, 2560), dtype="float32") = transformed_param_470
            lv453: R.Tensor((2560,), dtype="float32") = transformed_param_56
            lv284_1 = R.call_tir(cls.fused_matmul26_add35_gelu1, (lv312, lv452, lv453), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv454: R.Tensor((640, 2560), dtype="float32") = transformed_param_469
            lv455: R.Tensor((2560,), dtype="float32") = transformed_param_55
            lv285 = R.call_tir(cls.fused_matmul26_add35_multiply18, (lv312, lv454, lv455, lv284_1), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv456: R.Tensor((2560, 640), dtype="float32") = transformed_param_471
            lv457: R.Tensor((640,), dtype="float32") = transformed_param_57
            lv286_1 = R.call_tir(cls.fused_matmul27_add33_add34, (lv285, lv456, lv457, lv283), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv287 = R.call_tir(cls.fused_reshape41_transpose36, (lv286_1,), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv458: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_52
            lv459: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_472
            lv288_1 = R.call_tir(cls.fused_conv2d20_add29_add32, (lv287, lv458, lv459, lv269), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv460: R.Tensor((640,), dtype="float32") = transformed_param_91
            lv461: R.Tensor((640,), dtype="float32") = transformed_param_90
            lv289 = R.call_tir(cls.fused_group_norm10_silu9, (lv288_1, lv460, lv461), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv336_1 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv462: R.Tensor((1280, 640), dtype="float32") = transformed_param_474
            lv463: R.Tensor((640,), dtype="float32") = transformed_param_94
            lv290_1 = R.call_tir(cls.fused_matmul19_add30_strided_slice4, (lv336_1, lv462, lv463), out_sinfo=R.Tensor((2, 640), dtype="float32"))
            lv341_1 = R.call_tir(cls.reshape33, (lv290_1,), out_sinfo=R.Tensor((2, 640, 1, 1), dtype="float32"))
            lv464: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_88
            lv465: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_473
            lv291 = R.call_tir(cls.fused_conv2d18_add29_add31, (lv289, lv464, lv465, lv341_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv466: R.Tensor((640,), dtype="float32") = transformed_param_93
            lv467: R.Tensor((640,), dtype="float32") = transformed_param_92
            lv292 = R.call_tir(cls.fused_group_norm10_silu9, (lv291, lv466, lv467), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv468: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_89
            lv469: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_475
            lv293 = R.call_tir(cls.fused_conv2d18_add29_add32_divide10, (lv292, lv468, lv469, lv288_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv470: R.Tensor((640,), dtype="float32") = transformed_param_65
            lv471: R.Tensor((640,), dtype="float32") = transformed_param_64
            lv350_1 = R.call_tir(cls.group_norm11, (lv293, lv470, lv471), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv472: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_66
            lv473: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_476
            lv294 = R.call_tir(cls.fused_conv2d20_add29, (lv350_1, lv472, lv473), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv295 = R.call_tir(cls.fused_transpose26_reshape34, (lv294,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv474: R.Tensor((640,), dtype="float32") = transformed_param_74
            lv475: R.Tensor((640,), dtype="float32") = transformed_param_73
            lv356_1 = R.call_tir(cls.layer_norm2, (lv295, lv474, lv475), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv476: R.Tensor((640, 640), dtype="float32") = transformed_param_477
            lv358_1 = R.call_tir(cls.matmul20, (lv356_1, lv476), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv477: R.Tensor((640, 640), dtype="float32") = transformed_param_478
            lv360_1 = R.call_tir(cls.matmul20, (lv356_1, lv477), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv478: R.Tensor((640, 640), dtype="float32") = transformed_param_479
            lv362_1 = R.call_tir(cls.matmul20, (lv356_1, lv478), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv296 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv358_1,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv297 = R.call_tir(cls.fused_reshape35_transpose28_reshape36_transpose29, (lv360_1,), out_sinfo=R.Tensor((16, 80, 1024), dtype="float32"))
            lv298 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv362_1,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv299 = R.call_tir(cls.fused_matmul21_multiply16, (lv296, lv297), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv375_1 = R.call_tir(cls.softmax4, (lv299,), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv376_1 = R.call_tir(cls.matmul22, (lv375_1, lv298), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv300 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv376_1,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv479: R.Tensor((640, 640), dtype="float32") = transformed_param_480
            lv480: R.Tensor((640,), dtype="float32") = transformed_param_68
            lv301 = R.call_tir(cls.fused_matmul20_add33_add34, (lv300, lv479, lv480, lv295), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv481: R.Tensor((640,), dtype="float32") = transformed_param_76
            lv482: R.Tensor((640,), dtype="float32") = transformed_param_75
            lv384_1 = R.call_tir(cls.layer_norm2, (lv301, lv481, lv482), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv483: R.Tensor((640, 640), dtype="float32") = transformed_param_481
            lv386_1 = R.call_tir(cls.matmul20, (lv384_1, lv483), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv484: R.Tensor((768, 640), dtype="float32") = transformed_param_482
            lv388_1 = R.call_tir(cls.matmul23, (inp_2, lv484), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv485: R.Tensor((768, 640), dtype="float32") = transformed_param_483
            lv390_1 = R.call_tir(cls.matmul23, (inp_2, lv485), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv302 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv386_1,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv303_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40_transpose33, (lv388_1,), out_sinfo=R.Tensor((16, 80, 77), dtype="float32"))
            lv304_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40, (lv390_1,), out_sinfo=R.Tensor((16, 77, 80), dtype="float32"))
            lv305 = R.call_tir(cls.fused_matmul24_multiply17, (lv302, lv303_1), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv403_1 = R.call_tir(cls.softmax5, (lv305,), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv404_1 = R.call_tir(cls.matmul25, (lv403_1, lv304_1), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv306 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv404_1,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv486: R.Tensor((640, 640), dtype="float32") = transformed_param_484
            lv487: R.Tensor((640,), dtype="float32") = transformed_param_69
            lv307 = R.call_tir(cls.fused_matmul20_add33_add34, (lv306, lv486, lv487, lv301), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv488: R.Tensor((640,), dtype="float32") = transformed_param_78
            lv489: R.Tensor((640,), dtype="float32") = transformed_param_77
            lv412_1 = R.call_tir(cls.layer_norm2, (lv307, lv488, lv489), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv490: R.Tensor((640, 2560), dtype="float32") = transformed_param_486
            lv491: R.Tensor((2560,), dtype="float32") = transformed_param_71
            lv308 = R.call_tir(cls.fused_matmul26_add35_gelu1, (lv412_1, lv490, lv491), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv492: R.Tensor((640, 2560), dtype="float32") = transformed_param_485
            lv493: R.Tensor((2560,), dtype="float32") = transformed_param_70
            lv309 = R.call_tir(cls.fused_matmul26_add35_multiply18, (lv412_1, lv492, lv493, lv308), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv494: R.Tensor((2560, 640), dtype="float32") = transformed_param_487
            lv495: R.Tensor((640,), dtype="float32") = transformed_param_72
            lv310 = R.call_tir(cls.fused_matmul27_add33_add34, (lv309, lv494, lv495, lv307), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv311 = R.call_tir(cls.fused_reshape41_transpose36, (lv310,), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv496: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_67
            lv497: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_488
            lv312_1 = R.call_tir(cls.fused_conv2d20_add29_add32, (lv311, lv496, lv497, lv293), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv498: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_79
            lv499: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_489
            lv313 = R.call_tir(cls.fused_conv2d21_add36, (lv312_1, lv498, lv499), out_sinfo=R.Tensor((2, 640, 16, 16), dtype="float32"))
            lv500: R.Tensor((640,), dtype="float32") = transformed_param_130
            lv501: R.Tensor((640,), dtype="float32") = transformed_param_129
            lv314 = R.call_tir(cls.fused_group_norm12_silu10, (lv313, lv500, lv501), out_sinfo=R.Tensor((2, 640, 16, 16), dtype="float32"))
            lv439_1 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv502: R.Tensor((1280, 1280), dtype="float32") = transformed_param_491
            lv503: R.Tensor((1280,), dtype="float32") = transformed_param_133
            lv315 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv439_1, lv502, lv503), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv444_1 = R.call_tir(cls.reshape43, (lv315,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv504: R.Tensor((1280, 640, 3, 3), dtype="float32") = transformed_param_126
            lv505: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_490
            lv316 = R.call_tir(cls.fused_conv2d22_add37_add38, (lv314, lv504, lv505, lv444_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv506: R.Tensor((1280,), dtype="float32") = transformed_param_132
            lv507: R.Tensor((1280,), dtype="float32") = transformed_param_131
            lv317 = R.call_tir(cls.fused_group_norm13_silu11, (lv316, lv506, lv507), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv508: R.Tensor((1280, 640, 1, 1), dtype="float32") = transformed_param_128
            lv509: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_493
            lv318 = R.call_tir(cls.fused_conv2d24_add37, (lv313, lv508, lv509), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv510: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_127
            lv511: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_492
            lv319 = R.call_tir(cls.fused_conv2d23_add37_add39_divide11, (lv317, lv510, lv511, lv318), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv512: R.Tensor((1280,), dtype="float32") = transformed_param_96
            lv513: R.Tensor((1280,), dtype="float32") = transformed_param_95
            lv456_1 = R.call_tir(cls.group_norm14, (lv319, lv512, lv513), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv514: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_97
            lv515: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_494
            lv320 = R.call_tir(cls.fused_conv2d25_add37, (lv456_1, lv514, lv515), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv321 = R.call_tir(cls.fused_transpose37_reshape44, (lv320,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv516: R.Tensor((1280,), dtype="float32") = transformed_param_105
            lv517: R.Tensor((1280,), dtype="float32") = transformed_param_104
            lv462_1 = R.call_tir(cls.layer_norm3, (lv321, lv516, lv517), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv518: R.Tensor((1280, 1280), dtype="float32") = transformed_param_495
            lv464_1 = R.call_tir(cls.matmul28, (lv462_1, lv518), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv519: R.Tensor((1280, 1280), dtype="float32") = transformed_param_496
            lv466_1 = R.call_tir(cls.matmul28, (lv462_1, lv519), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv520: R.Tensor((1280, 1280), dtype="float32") = transformed_param_497
            lv468_1 = R.call_tir(cls.matmul28, (lv462_1, lv520), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv322 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv464_1,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv323 = R.call_tir(cls.fused_reshape45_transpose38_reshape46_transpose39, (lv466_1,), out_sinfo=R.Tensor((16, 160, 256), dtype="float32"))
            lv324 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv468_1,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv325 = R.call_tir(cls.fused_matmul29_multiply19, (lv322, lv323), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv481_1 = R.call_tir(cls.softmax6, (lv325,), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv482_1 = R.call_tir(cls.matmul30, (lv481_1, lv324), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv326 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv482_1,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv521: R.Tensor((1280, 1280), dtype="float32") = transformed_param_498
            lv522: R.Tensor((1280,), dtype="float32") = transformed_param_99
            lv327 = R.call_tir(cls.fused_matmul28_add40_add41, (lv326, lv521, lv522, lv321), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv523: R.Tensor((1280,), dtype="float32") = transformed_param_107
            lv524: R.Tensor((1280,), dtype="float32") = transformed_param_106
            lv490_1 = R.call_tir(cls.layer_norm3, (lv327, lv523, lv524), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv525: R.Tensor((1280, 1280), dtype="float32") = transformed_param_499
            lv492_1 = R.call_tir(cls.matmul28, (lv490_1, lv525), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv526: R.Tensor((768, 1280), dtype="float32") = transformed_param_500
            lv494_1 = R.call_tir(cls.matmul31, (inp_2, lv526), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv527: R.Tensor((768, 1280), dtype="float32") = transformed_param_501
            lv496_1 = R.call_tir(cls.matmul31, (inp_2, lv527), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv328 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv492_1,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv329 = R.call_tir(cls.fused_reshape49_transpose42_reshape50_transpose43, (lv494_1,), out_sinfo=R.Tensor((16, 160, 77), dtype="float32"))
            lv330 = R.call_tir(cls.fused_reshape49_transpose42_reshape50, (lv496_1,), out_sinfo=R.Tensor((16, 77, 160), dtype="float32"))
            lv331 = R.call_tir(cls.fused_matmul32_multiply20, (lv328, lv329), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv509_1 = R.call_tir(cls.softmax7, (lv331,), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv510_1 = R.call_tir(cls.matmul33, (lv509_1, lv330), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv332 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv510_1,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv528: R.Tensor((1280, 1280), dtype="float32") = transformed_param_502
            lv529: R.Tensor((1280,), dtype="float32") = transformed_param_100
            lv333 = R.call_tir(cls.fused_matmul28_add40_add41, (lv332, lv528, lv529, lv327), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv530: R.Tensor((1280,), dtype="float32") = transformed_param_109
            lv531: R.Tensor((1280,), dtype="float32") = transformed_param_108
            lv518_1 = R.call_tir(cls.layer_norm3, (lv333, lv530, lv531), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv532: R.Tensor((1280, 5120), dtype="float32") = transformed_param_504
            lv533: R.Tensor((5120,), dtype="float32") = transformed_param_102
            lv334 = R.call_tir(cls.fused_matmul34_add42_gelu2, (lv518_1, lv532, lv533), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv534: R.Tensor((1280, 5120), dtype="float32") = transformed_param_503
            lv535: R.Tensor((5120,), dtype="float32") = transformed_param_101
            lv335 = R.call_tir(cls.fused_matmul34_add42_multiply21, (lv518_1, lv534, lv535, lv334), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv536: R.Tensor((5120, 1280), dtype="float32") = transformed_param_505
            lv537: R.Tensor((1280,), dtype="float32") = transformed_param_103
            lv336_2 = R.call_tir(cls.fused_matmul35_add40_add41, (lv335, lv536, lv537, lv333), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv337_1 = R.call_tir(cls.fused_reshape51_transpose46, (lv336_2,), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv538: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_98
            lv539: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_506
            lv338_1 = R.call_tir(cls.fused_conv2d25_add37_add39, (lv337_1, lv538, lv539, lv319), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv540: R.Tensor((1280,), dtype="float32") = transformed_param_137
            lv541: R.Tensor((1280,), dtype="float32") = transformed_param_136
            lv339_1 = R.call_tir(cls.fused_group_norm13_silu11, (lv338_1, lv540, lv541), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv542 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv542_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_508
            lv543: R.Tensor((1280,), dtype="float32") = transformed_param_140
            lv340_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv542, lv542_1, lv543), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv547 = R.call_tir(cls.reshape43, (lv340_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv544: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_134
            lv545: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_507
            lv341_2 = R.call_tir(cls.fused_conv2d23_add37_add38, (lv339_1, lv544, lv545, lv547), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv546: R.Tensor((1280,), dtype="float32") = transformed_param_139
            lv547_1: R.Tensor((1280,), dtype="float32") = transformed_param_138
            lv342_1 = R.call_tir(cls.fused_group_norm13_silu11, (lv341_2, lv546, lv547_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv548: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_135
            lv549: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_509
            lv343_1 = R.call_tir(cls.fused_conv2d23_add37_add39_divide11, (lv342_1, lv548, lv549, lv338_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv550: R.Tensor((1280,), dtype="float32") = transformed_param_111
            lv551: R.Tensor((1280,), dtype="float32") = transformed_param_110
            lv556 = R.call_tir(cls.group_norm14, (lv343_1, lv550, lv551), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv552: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_112
            lv553: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_510
            lv344_1 = R.call_tir(cls.fused_conv2d25_add37, (lv556, lv552, lv553), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv345_1 = R.call_tir(cls.fused_transpose37_reshape44, (lv344_1,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv554: R.Tensor((1280,), dtype="float32") = transformed_param_120
            lv555: R.Tensor((1280,), dtype="float32") = transformed_param_119
            lv562 = R.call_tir(cls.layer_norm3, (lv345_1, lv554, lv555), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv556_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_511
            lv564 = R.call_tir(cls.matmul28, (lv562, lv556_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv557: R.Tensor((1280, 1280), dtype="float32") = transformed_param_512
            lv566 = R.call_tir(cls.matmul28, (lv562, lv557), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv558: R.Tensor((1280, 1280), dtype="float32") = transformed_param_513
            lv568 = R.call_tir(cls.matmul28, (lv562, lv558), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv346_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv564,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv347_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46_transpose39, (lv566,), out_sinfo=R.Tensor((16, 160, 256), dtype="float32"))
            lv348_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv568,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv349_1 = R.call_tir(cls.fused_matmul29_multiply19, (lv346_1, lv347_1), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv581 = R.call_tir(cls.softmax6, (lv349_1,), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv582 = R.call_tir(cls.matmul30, (lv581, lv348_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv350_2 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv582,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv559: R.Tensor((1280, 1280), dtype="float32") = transformed_param_514
            lv560: R.Tensor((1280,), dtype="float32") = transformed_param_114
            lv351_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv350_2, lv559, lv560, lv345_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv561: R.Tensor((1280,), dtype="float32") = transformed_param_122
            lv562_1: R.Tensor((1280,), dtype="float32") = transformed_param_121
            lv590 = R.call_tir(cls.layer_norm3, (lv351_1, lv561, lv562_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv563: R.Tensor((1280, 1280), dtype="float32") = transformed_param_515
            lv592 = R.call_tir(cls.matmul28, (lv590, lv563), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv564_1: R.Tensor((768, 1280), dtype="float32") = transformed_param_516
            lv594 = R.call_tir(cls.matmul31, (inp_2, lv564_1), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv565: R.Tensor((768, 1280), dtype="float32") = transformed_param_517
            lv596 = R.call_tir(cls.matmul31, (inp_2, lv565), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv352_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv592,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv353_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50_transpose43, (lv594,), out_sinfo=R.Tensor((16, 160, 77), dtype="float32"))
            lv354_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50, (lv596,), out_sinfo=R.Tensor((16, 77, 160), dtype="float32"))
            lv355_1 = R.call_tir(cls.fused_matmul32_multiply20, (lv352_1, lv353_1), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv609 = R.call_tir(cls.softmax7, (lv355_1,), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv610 = R.call_tir(cls.matmul33, (lv609, lv354_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv356_2 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv610,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv566_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_518
            lv567: R.Tensor((1280,), dtype="float32") = transformed_param_115
            lv357_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv356_2, lv566_1, lv567, lv351_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv568_1: R.Tensor((1280,), dtype="float32") = transformed_param_124
            lv569: R.Tensor((1280,), dtype="float32") = transformed_param_123
            lv618 = R.call_tir(cls.layer_norm3, (lv357_1, lv568_1, lv569), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv570: R.Tensor((1280, 5120), dtype="float32") = transformed_param_520
            lv571: R.Tensor((5120,), dtype="float32") = transformed_param_117
            lv358_2 = R.call_tir(cls.fused_matmul34_add42_gelu2, (lv618, lv570, lv571), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv572: R.Tensor((1280, 5120), dtype="float32") = transformed_param_519
            lv573: R.Tensor((5120,), dtype="float32") = transformed_param_116
            lv359_1 = R.call_tir(cls.fused_matmul34_add42_multiply21, (lv618, lv572, lv573, lv358_2), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv574: R.Tensor((5120, 1280), dtype="float32") = transformed_param_521
            lv575: R.Tensor((1280,), dtype="float32") = transformed_param_118
            lv360_2 = R.call_tir(cls.fused_matmul35_add40_add41, (lv359_1, lv574, lv575, lv357_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv361_1 = R.call_tir(cls.fused_reshape51_transpose46, (lv360_2,), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv576: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_113
            lv577: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_522
            lv362_2 = R.call_tir(cls.fused_conv2d25_add37_add39, (lv361_1, lv576, lv577, lv343_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv578: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_125
            lv579: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_523
            lv363_1 = R.call_tir(cls.fused_conv2d26_add43, (lv362_2, lv578, lv579), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv580: R.Tensor((1280,), dtype="float32") = transformed_param_144
            lv581_1: R.Tensor((1280,), dtype="float32") = transformed_param_143
            lv364_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv363_1, lv580, lv581_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv645 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv582_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_525
            lv583: R.Tensor((1280,), dtype="float32") = transformed_param_147
            lv365_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv645, lv582_1, lv583), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv650 = R.call_tir(cls.reshape43, (lv365_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv584: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_141
            lv585: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_524
            lv366_1 = R.call_tir(cls.fused_conv2d27_add43_add44, (lv364_1, lv584, lv585, lv650), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv586: R.Tensor((1280,), dtype="float32") = transformed_param_146
            lv587: R.Tensor((1280,), dtype="float32") = transformed_param_145
            lv367_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv366_1, lv586, lv587), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv588: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_142
            lv589: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_526
            lv368_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv367_1, lv588, lv589, lv363_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv590_1: R.Tensor((1280,), dtype="float32") = transformed_param_151
            lv591: R.Tensor((1280,), dtype="float32") = transformed_param_150
            lv369_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv368_1, lv590_1, lv591), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv664 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv592_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_528
            lv593: R.Tensor((1280,), dtype="float32") = transformed_param_154
            lv370_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv664, lv592_1, lv593), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv669 = R.call_tir(cls.reshape43, (lv370_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv594_1: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_148
            lv595: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_527
            lv371_1 = R.call_tir(cls.fused_conv2d27_add43_add44, (lv369_1, lv594_1, lv595, lv669), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv596_1: R.Tensor((1280,), dtype="float32") = transformed_param_153
            lv597: R.Tensor((1280,), dtype="float32") = transformed_param_152
            lv372_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv371_1, lv596_1, lv597), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv598: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_149
            lv599: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_529
            lv373_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv372_1, lv598, lv599, lv368_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv600: R.Tensor((1280,), dtype="float32") = transformed_param_173
            lv601: R.Tensor((1280,), dtype="float32") = transformed_param_172
            lv374_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv373_1, lv600, lv601), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv683 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv602: R.Tensor((1280, 1280), dtype="float32") = transformed_param_531
            lv603: R.Tensor((1280,), dtype="float32") = transformed_param_176
            lv375_2 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv683, lv602, lv603), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv688 = R.call_tir(cls.reshape43, (lv375_2,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv604: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_170
            lv605: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_530
            lv376_2 = R.call_tir(cls.fused_conv2d27_add43_add44, (lv374_1, lv604, lv605, lv688), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv606: R.Tensor((1280,), dtype="float32") = transformed_param_175
            lv607: R.Tensor((1280,), dtype="float32") = transformed_param_174
            lv377_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv376_2, lv606, lv607), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv608: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_171
            lv609_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_532
            lv378_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv377_1, lv608, lv609_1, lv373_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv610_1: R.Tensor((1280,), dtype="float32") = transformed_param_156
            lv611: R.Tensor((1280,), dtype="float32") = transformed_param_155
            lv697 = R.call_tir(cls.group_norm16, (lv378_1, lv610_1, lv611), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv612: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_157
            lv613: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_533
            lv379_1 = R.call_tir(cls.fused_conv2d28_add43, (lv697, lv612, lv613), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv380_1 = R.call_tir(cls.fused_transpose47_reshape52, (lv379_1,), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv614: R.Tensor((1280,), dtype="float32") = transformed_param_165
            lv615: R.Tensor((1280,), dtype="float32") = transformed_param_164
            lv703 = R.call_tir(cls.layer_norm4, (lv380_1, lv614, lv615), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv616: R.Tensor((1280, 1280), dtype="float32") = transformed_param_534
            lv705 = R.call_tir(cls.matmul36, (lv703, lv616), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv617: R.Tensor((1280, 1280), dtype="float32") = transformed_param_535
            lv707 = R.call_tir(cls.matmul36, (lv703, lv617), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv618_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_536
            lv709 = R.call_tir(cls.matmul36, (lv703, lv618_1), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv381_1 = R.call_tir(cls.fused_reshape53_transpose48_reshape54, (lv705,), out_sinfo=R.Tensor((16, 64, 160), dtype="float32"))
            lv382_1 = R.call_tir(cls.fused_reshape53_transpose48_reshape54_transpose49, (lv707,), out_sinfo=R.Tensor((16, 160, 64), dtype="float32"))
            lv383_1 = R.call_tir(cls.fused_reshape53_transpose48_reshape54, (lv709,), out_sinfo=R.Tensor((16, 64, 160), dtype="float32"))
            lv384_2 = R.call_tir(cls.fused_matmul37_multiply22, (lv381_1, lv382_1), out_sinfo=R.Tensor((16, 64, 64), dtype="float32"))
            lv722 = R.call_tir(cls.softmax8, (lv384_2,), out_sinfo=R.Tensor((16, 64, 64), dtype="float32"))
            lv723 = R.call_tir(cls.matmul38, (lv722, lv383_1), out_sinfo=R.Tensor((16, 64, 160), dtype="float32"))
            lv385_1 = R.call_tir(cls.fused_reshape55_transpose50_reshape56, (lv723,), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv619: R.Tensor((1280, 1280), dtype="float32") = transformed_param_537
            lv620: R.Tensor((1280,), dtype="float32") = transformed_param_159
            lv386_2 = R.call_tir(cls.fused_matmul36_add46_add47, (lv385_1, lv619, lv620, lv380_1), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv621: R.Tensor((1280,), dtype="float32") = transformed_param_167
            lv622: R.Tensor((1280,), dtype="float32") = transformed_param_166
            lv731 = R.call_tir(cls.layer_norm4, (lv386_2, lv621, lv622), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv623: R.Tensor((1280, 1280), dtype="float32") = transformed_param_538
            lv733 = R.call_tir(cls.matmul36, (lv731, lv623), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv624: R.Tensor((768, 1280), dtype="float32") = transformed_param_539
            lv735 = R.call_tir(cls.matmul31, (inp_2, lv624), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv625: R.Tensor((768, 1280), dtype="float32") = transformed_param_540
            lv737 = R.call_tir(cls.matmul31, (inp_2, lv625), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv387_1 = R.call_tir(cls.fused_reshape53_transpose48_reshape54, (lv733,), out_sinfo=R.Tensor((16, 64, 160), dtype="float32"))
            lv388_2 = R.call_tir(cls.fused_reshape49_transpose42_reshape50_transpose43, (lv735,), out_sinfo=R.Tensor((16, 160, 77), dtype="float32"))
            lv389_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50, (lv737,), out_sinfo=R.Tensor((16, 77, 160), dtype="float32"))
            lv390_2 = R.call_tir(cls.fused_matmul39_multiply23, (lv387_1, lv388_2), out_sinfo=R.Tensor((16, 64, 77), dtype="float32"))
            lv750 = R.call_tir(cls.softmax9, (lv390_2,), out_sinfo=R.Tensor((16, 64, 77), dtype="float32"))
            lv751 = R.call_tir(cls.matmul40, (lv750, lv389_1), out_sinfo=R.Tensor((16, 64, 160), dtype="float32"))
            lv391_1 = R.call_tir(cls.fused_reshape55_transpose50_reshape56, (lv751,), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv626: R.Tensor((1280, 1280), dtype="float32") = transformed_param_541
            lv627: R.Tensor((1280,), dtype="float32") = transformed_param_160
            lv392_1 = R.call_tir(cls.fused_matmul36_add46_add47, (lv391_1, lv626, lv627, lv386_2), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv628: R.Tensor((1280,), dtype="float32") = transformed_param_169
            lv629: R.Tensor((1280,), dtype="float32") = transformed_param_168
            lv759 = R.call_tir(cls.layer_norm4, (lv392_1, lv628, lv629), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv630: R.Tensor((1280, 5120), dtype="float32") = transformed_param_543
            lv631: R.Tensor((5120,), dtype="float32") = transformed_param_162
            lv393_1 = R.call_tir(cls.fused_matmul41_add48_gelu3, (lv759, lv630, lv631), out_sinfo=R.Tensor((2, 64, 5120), dtype="float32"))
            lv632: R.Tensor((1280, 5120), dtype="float32") = transformed_param_542
            lv633: R.Tensor((5120,), dtype="float32") = transformed_param_161
            lv394_1 = R.call_tir(cls.fused_matmul41_add48_multiply24, (lv759, lv632, lv633, lv393_1), out_sinfo=R.Tensor((2, 64, 5120), dtype="float32"))
            lv634: R.Tensor((5120, 1280), dtype="float32") = transformed_param_544
            lv635: R.Tensor((1280,), dtype="float32") = transformed_param_163
            lv395_1 = R.call_tir(cls.fused_matmul42_add46_add47, (lv394_1, lv634, lv635, lv392_1), out_sinfo=R.Tensor((2, 64, 1280), dtype="float32"))
            lv396_1 = R.call_tir(cls.fused_reshape57_transpose51, (lv395_1,), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv636: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_158
            lv637: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_545
            lv397_1 = R.call_tir(cls.fused_conv2d28_add43_add45, (lv396_1, lv636, lv637, lv378_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv638: R.Tensor((1280,), dtype="float32") = transformed_param_180
            lv639: R.Tensor((1280,), dtype="float32") = transformed_param_179
            lv398_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv397_1, lv638, lv639), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv783 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv640: R.Tensor((1280, 1280), dtype="float32") = transformed_param_547
            lv641: R.Tensor((1280,), dtype="float32") = transformed_param_183
            lv399_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv783, lv640, lv641), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv788 = R.call_tir(cls.reshape43, (lv399_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv642: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_177
            lv643: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_546
            lv400_1 = R.call_tir(cls.fused_conv2d27_add43_add44, (lv398_1, lv642, lv643, lv788), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv644: R.Tensor((1280,), dtype="float32") = transformed_param_182
            lv645_1: R.Tensor((1280,), dtype="float32") = transformed_param_181
            lv401_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv400_1, lv644, lv645_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv646: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_178
            lv647: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_548
            lv402_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv401_1, lv646, lv647, lv397_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv797 = R.call_tir(cls.concatenate3, (lv402_1, lv373_1), out_sinfo=R.Tensor((2, 2560, 8, 8), dtype="float32"))
            lv648: R.Tensor((2560,), dtype="float32") = transformed_param_190
            lv649: R.Tensor((2560,), dtype="float32") = transformed_param_189
            lv403_2 = R.call_tir(cls.fused_group_norm17_silu13, (lv797, lv648, lv649), out_sinfo=R.Tensor((2, 2560, 8, 8), dtype="float32"))
            lv803 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv650_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_550
            lv651: R.Tensor((1280,), dtype="float32") = transformed_param_193
            lv404_2 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv803, lv650_1, lv651), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv808 = R.call_tir(cls.reshape43, (lv404_2,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv652: R.Tensor((1280, 2560, 3, 3), dtype="float32") = transformed_param_186
            lv653: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_549
            lv405_1 = R.call_tir(cls.fused_conv2d29_add43_add44, (lv403_2, lv652, lv653, lv808), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv654: R.Tensor((1280,), dtype="float32") = transformed_param_192
            lv655: R.Tensor((1280,), dtype="float32") = transformed_param_191
            lv406_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv405_1, lv654, lv655), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv656: R.Tensor((1280, 2560, 1, 1), dtype="float32") = transformed_param_188
            lv657: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_552
            lv407_1 = R.call_tir(cls.fused_conv2d30_add43, (lv797, lv656, lv657), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv658: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_187
            lv659: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_551
            lv408_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv406_1, lv658, lv659, lv407_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv820 = R.call_tir(cls.concatenate3, (lv408_1, lv368_1), out_sinfo=R.Tensor((2, 2560, 8, 8), dtype="float32"))
            lv660: R.Tensor((2560,), dtype="float32") = transformed_param_198
            lv661: R.Tensor((2560,), dtype="float32") = transformed_param_197
            lv409_1 = R.call_tir(cls.fused_group_norm17_silu13, (lv820, lv660, lv661), out_sinfo=R.Tensor((2, 2560, 8, 8), dtype="float32"))
            lv826 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv662: R.Tensor((1280, 1280), dtype="float32") = transformed_param_554
            lv663: R.Tensor((1280,), dtype="float32") = transformed_param_201
            lv410_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv826, lv662, lv663), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv831 = R.call_tir(cls.reshape43, (lv410_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv664_1: R.Tensor((1280, 2560, 3, 3), dtype="float32") = transformed_param_194
            lv665: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_553
            lv411_1 = R.call_tir(cls.fused_conv2d29_add43_add44, (lv409_1, lv664_1, lv665, lv831), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv666: R.Tensor((1280,), dtype="float32") = transformed_param_200
            lv667: R.Tensor((1280,), dtype="float32") = transformed_param_199
            lv412_2 = R.call_tir(cls.fused_group_norm15_silu12, (lv411_1, lv666, lv667), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv668: R.Tensor((1280, 2560, 1, 1), dtype="float32") = transformed_param_196
            lv669_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_556
            lv413_1 = R.call_tir(cls.fused_conv2d30_add43, (lv820, lv668, lv669_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv670: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_195
            lv671: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_555
            lv414_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv412_2, lv670, lv671, lv413_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv843 = R.call_tir(cls.concatenate3, (lv414_1, lv363_1), out_sinfo=R.Tensor((2, 2560, 8, 8), dtype="float32"))
            lv672: R.Tensor((2560,), dtype="float32") = transformed_param_206
            lv673: R.Tensor((2560,), dtype="float32") = transformed_param_205
            lv415_1 = R.call_tir(cls.fused_group_norm17_silu13, (lv843, lv672, lv673), out_sinfo=R.Tensor((2, 2560, 8, 8), dtype="float32"))
            lv849 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv674: R.Tensor((1280, 1280), dtype="float32") = transformed_param_558
            lv675: R.Tensor((1280,), dtype="float32") = transformed_param_209
            lv416_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv849, lv674, lv675), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv854 = R.call_tir(cls.reshape43, (lv416_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv676: R.Tensor((1280, 2560, 3, 3), dtype="float32") = transformed_param_202
            lv677: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_557
            lv417_1 = R.call_tir(cls.fused_conv2d29_add43_add44, (lv415_1, lv676, lv677, lv854), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv678: R.Tensor((1280,), dtype="float32") = transformed_param_208
            lv679: R.Tensor((1280,), dtype="float32") = transformed_param_207
            lv418_1 = R.call_tir(cls.fused_group_norm15_silu12, (lv417_1, lv678, lv679), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv680: R.Tensor((1280, 2560, 1, 1), dtype="float32") = transformed_param_204
            lv681: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_560
            lv419_1 = R.call_tir(cls.fused_conv2d30_add43, (lv843, lv680, lv681), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv682: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_203
            lv683_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_559
            lv420_1 = R.call_tir(cls.fused_conv2d27_add43_add45_divide12, (lv418_1, lv682, lv683_1, lv419_1), out_sinfo=R.Tensor((2, 1280, 8, 8), dtype="float32"))
            lv866 = R.call_tir(cls.resize2d3, (lv420_1,), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv684: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_210
            lv685: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_561
            lv421_1 = R.call_tir(cls.fused_conv2d23_add37, (lv866, lv684, lv685), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv870 = R.call_tir(cls.concatenate4, (lv421_1, lv362_2), out_sinfo=R.Tensor((2, 2560, 16, 16), dtype="float32"))
            lv686: R.Tensor((2560,), dtype="float32") = transformed_param_260
            lv687: R.Tensor((2560,), dtype="float32") = transformed_param_259
            lv422_1 = R.call_tir(cls.fused_group_norm18_silu14, (lv870, lv686, lv687), out_sinfo=R.Tensor((2, 2560, 16, 16), dtype="float32"))
            lv876 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv688_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_563
            lv689: R.Tensor((1280,), dtype="float32") = transformed_param_263
            lv423_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv876, lv688_1, lv689), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv881 = R.call_tir(cls.reshape43, (lv423_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv690: R.Tensor((1280, 2560, 3, 3), dtype="float32") = transformed_param_256
            lv691: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_562
            lv424_1 = R.call_tir(cls.fused_conv2d31_add37_add38, (lv422_1, lv690, lv691, lv881), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv692: R.Tensor((1280,), dtype="float32") = transformed_param_262
            lv693: R.Tensor((1280,), dtype="float32") = transformed_param_261
            lv425_1 = R.call_tir(cls.fused_group_norm13_silu11, (lv424_1, lv692, lv693), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv694: R.Tensor((1280, 2560, 1, 1), dtype="float32") = transformed_param_258
            lv695: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_565
            lv426_1 = R.call_tir(cls.fused_conv2d32_add37, (lv870, lv694, lv695), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv696: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_257
            lv697_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_564
            lv427_1 = R.call_tir(cls.fused_conv2d23_add37_add39_divide11, (lv425_1, lv696, lv697_1, lv426_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv698: R.Tensor((1280,), dtype="float32") = transformed_param_212
            lv699: R.Tensor((1280,), dtype="float32") = transformed_param_211
            lv893 = R.call_tir(cls.group_norm14, (lv427_1, lv698, lv699), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv700: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_213
            lv701: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_566
            lv428_1 = R.call_tir(cls.fused_conv2d25_add37, (lv893, lv700, lv701), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv429_1 = R.call_tir(cls.fused_transpose37_reshape44, (lv428_1,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv702: R.Tensor((1280,), dtype="float32") = transformed_param_221
            lv703_1: R.Tensor((1280,), dtype="float32") = transformed_param_220
            lv899 = R.call_tir(cls.layer_norm3, (lv429_1, lv702, lv703_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv704: R.Tensor((1280, 1280), dtype="float32") = transformed_param_567
            lv901 = R.call_tir(cls.matmul28, (lv899, lv704), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv705_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_568
            lv903 = R.call_tir(cls.matmul28, (lv899, lv705_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv706: R.Tensor((1280, 1280), dtype="float32") = transformed_param_569
            lv905 = R.call_tir(cls.matmul28, (lv899, lv706), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv430_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv901,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv431_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46_transpose39, (lv903,), out_sinfo=R.Tensor((16, 160, 256), dtype="float32"))
            lv432_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv905,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv433_1 = R.call_tir(cls.fused_matmul29_multiply19, (lv430_1, lv431_1), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv918 = R.call_tir(cls.softmax6, (lv433_1,), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv919 = R.call_tir(cls.matmul30, (lv918, lv432_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv434_1 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv919,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv707_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_570
            lv708: R.Tensor((1280,), dtype="float32") = transformed_param_215
            lv435_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv434_1, lv707_1, lv708, lv429_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv709_1: R.Tensor((1280,), dtype="float32") = transformed_param_223
            lv710: R.Tensor((1280,), dtype="float32") = transformed_param_222
            lv927 = R.call_tir(cls.layer_norm3, (lv435_1, lv709_1, lv710), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv711: R.Tensor((1280, 1280), dtype="float32") = transformed_param_571
            lv929 = R.call_tir(cls.matmul28, (lv927, lv711), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv712: R.Tensor((768, 1280), dtype="float32") = transformed_param_572
            lv931 = R.call_tir(cls.matmul31, (inp_2, lv712), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv713: R.Tensor((768, 1280), dtype="float32") = transformed_param_573
            lv933 = R.call_tir(cls.matmul31, (inp_2, lv713), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv436_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv929,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv437_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50_transpose43, (lv931,), out_sinfo=R.Tensor((16, 160, 77), dtype="float32"))
            lv438_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50, (lv933,), out_sinfo=R.Tensor((16, 77, 160), dtype="float32"))
            lv439_2 = R.call_tir(cls.fused_matmul32_multiply20, (lv436_1, lv437_1), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv946 = R.call_tir(cls.softmax7, (lv439_2,), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv947 = R.call_tir(cls.matmul33, (lv946, lv438_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv440_1 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv947,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv714: R.Tensor((1280, 1280), dtype="float32") = transformed_param_574
            lv715: R.Tensor((1280,), dtype="float32") = transformed_param_216
            lv441_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv440_1, lv714, lv715, lv435_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv716: R.Tensor((1280,), dtype="float32") = transformed_param_225
            lv717: R.Tensor((1280,), dtype="float32") = transformed_param_224
            lv955 = R.call_tir(cls.layer_norm3, (lv441_1, lv716, lv717), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv718: R.Tensor((1280, 5120), dtype="float32") = transformed_param_576
            lv719: R.Tensor((5120,), dtype="float32") = transformed_param_218
            lv442_1 = R.call_tir(cls.fused_matmul34_add42_gelu2, (lv955, lv718, lv719), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv720: R.Tensor((1280, 5120), dtype="float32") = transformed_param_575
            lv721: R.Tensor((5120,), dtype="float32") = transformed_param_217
            lv443_1 = R.call_tir(cls.fused_matmul34_add42_multiply21, (lv955, lv720, lv721, lv442_1), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv722_1: R.Tensor((5120, 1280), dtype="float32") = transformed_param_577
            lv723_1: R.Tensor((1280,), dtype="float32") = transformed_param_219
            lv444_2 = R.call_tir(cls.fused_matmul35_add40_add41, (lv443_1, lv722_1, lv723_1, lv441_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv445_1 = R.call_tir(cls.fused_reshape51_transpose46, (lv444_2,), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv724: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_214
            lv725: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_578
            lv446_1 = R.call_tir(cls.fused_conv2d25_add37_add39, (lv445_1, lv724, lv725, lv427_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv974 = R.call_tir(cls.concatenate4, (lv446_1, lv338_1), out_sinfo=R.Tensor((2, 2560, 16, 16), dtype="float32"))
            lv726: R.Tensor((2560,), dtype="float32") = transformed_param_268
            lv727: R.Tensor((2560,), dtype="float32") = transformed_param_267
            lv447_1 = R.call_tir(cls.fused_group_norm18_silu14, (lv974, lv726, lv727), out_sinfo=R.Tensor((2, 2560, 16, 16), dtype="float32"))
            lv980 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv728: R.Tensor((1280, 1280), dtype="float32") = transformed_param_580
            lv729: R.Tensor((1280,), dtype="float32") = transformed_param_271
            lv448_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv980, lv728, lv729), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv985 = R.call_tir(cls.reshape43, (lv448_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv730: R.Tensor((1280, 2560, 3, 3), dtype="float32") = transformed_param_264
            lv731_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_579
            lv449_1 = R.call_tir(cls.fused_conv2d31_add37_add38, (lv447_1, lv730, lv731_1, lv985), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv732: R.Tensor((1280,), dtype="float32") = transformed_param_270
            lv733_1: R.Tensor((1280,), dtype="float32") = transformed_param_269
            lv450_1 = R.call_tir(cls.fused_group_norm13_silu11, (lv449_1, lv732, lv733_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv734: R.Tensor((1280, 2560, 1, 1), dtype="float32") = transformed_param_266
            lv735_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_582
            lv451_1 = R.call_tir(cls.fused_conv2d32_add37, (lv974, lv734, lv735_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv736: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_265
            lv737_1: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_581
            lv452_1 = R.call_tir(cls.fused_conv2d23_add37_add39_divide11, (lv450_1, lv736, lv737_1, lv451_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv738: R.Tensor((1280,), dtype="float32") = transformed_param_227
            lv739: R.Tensor((1280,), dtype="float32") = transformed_param_226
            lv997 = R.call_tir(cls.group_norm14, (lv452_1, lv738, lv739), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv740: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_228
            lv741: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_583
            lv453_1 = R.call_tir(cls.fused_conv2d25_add37, (lv997, lv740, lv741), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv454_1 = R.call_tir(cls.fused_transpose37_reshape44, (lv453_1,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv742: R.Tensor((1280,), dtype="float32") = transformed_param_236
            lv743: R.Tensor((1280,), dtype="float32") = transformed_param_235
            lv1003 = R.call_tir(cls.layer_norm3, (lv454_1, lv742, lv743), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv744: R.Tensor((1280, 1280), dtype="float32") = transformed_param_584
            lv1005 = R.call_tir(cls.matmul28, (lv1003, lv744), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv745: R.Tensor((1280, 1280), dtype="float32") = transformed_param_585
            lv1007 = R.call_tir(cls.matmul28, (lv1003, lv745), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv746: R.Tensor((1280, 1280), dtype="float32") = transformed_param_586
            lv1009 = R.call_tir(cls.matmul28, (lv1003, lv746), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv455_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv1005,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv456_2 = R.call_tir(cls.fused_reshape45_transpose38_reshape46_transpose39, (lv1007,), out_sinfo=R.Tensor((16, 160, 256), dtype="float32"))
            lv457_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv1009,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv458_1 = R.call_tir(cls.fused_matmul29_multiply19, (lv455_1, lv456_2), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv1022 = R.call_tir(cls.softmax6, (lv458_1,), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv1023 = R.call_tir(cls.matmul30, (lv1022, lv457_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv459_1 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv1023,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv747: R.Tensor((1280, 1280), dtype="float32") = transformed_param_587
            lv748: R.Tensor((1280,), dtype="float32") = transformed_param_230
            lv460_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv459_1, lv747, lv748, lv454_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv749: R.Tensor((1280,), dtype="float32") = transformed_param_238
            lv750_1: R.Tensor((1280,), dtype="float32") = transformed_param_237
            lv1031 = R.call_tir(cls.layer_norm3, (lv460_1, lv749, lv750_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv751_1: R.Tensor((1280, 1280), dtype="float32") = transformed_param_588
            lv1033 = R.call_tir(cls.matmul28, (lv1031, lv751_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv752: R.Tensor((768, 1280), dtype="float32") = transformed_param_589
            lv1035 = R.call_tir(cls.matmul31, (inp_2, lv752), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv753: R.Tensor((768, 1280), dtype="float32") = transformed_param_590
            lv1037 = R.call_tir(cls.matmul31, (inp_2, lv753), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv461_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv1033,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv462_2 = R.call_tir(cls.fused_reshape49_transpose42_reshape50_transpose43, (lv1035,), out_sinfo=R.Tensor((16, 160, 77), dtype="float32"))
            lv463_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50, (lv1037,), out_sinfo=R.Tensor((16, 77, 160), dtype="float32"))
            lv464_2 = R.call_tir(cls.fused_matmul32_multiply20, (lv461_1, lv462_2), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv1050 = R.call_tir(cls.softmax7, (lv464_2,), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv1051 = R.call_tir(cls.matmul33, (lv1050, lv463_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv465_1 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv1051,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv754: R.Tensor((1280, 1280), dtype="float32") = transformed_param_591
            lv755: R.Tensor((1280,), dtype="float32") = transformed_param_231
            lv466_2 = R.call_tir(cls.fused_matmul28_add40_add41, (lv465_1, lv754, lv755, lv460_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv756: R.Tensor((1280,), dtype="float32") = transformed_param_240
            lv757: R.Tensor((1280,), dtype="float32") = transformed_param_239
            lv1059 = R.call_tir(cls.layer_norm3, (lv466_2, lv756, lv757), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv758: R.Tensor((1280, 5120), dtype="float32") = transformed_param_593
            lv759_1: R.Tensor((5120,), dtype="float32") = transformed_param_233
            lv467_1 = R.call_tir(cls.fused_matmul34_add42_gelu2, (lv1059, lv758, lv759_1), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv760: R.Tensor((1280, 5120), dtype="float32") = transformed_param_592
            lv761: R.Tensor((5120,), dtype="float32") = transformed_param_232
            lv468_2 = R.call_tir(cls.fused_matmul34_add42_multiply21, (lv1059, lv760, lv761, lv467_1), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv762: R.Tensor((5120, 1280), dtype="float32") = transformed_param_594
            lv763: R.Tensor((1280,), dtype="float32") = transformed_param_234
            lv469_1 = R.call_tir(cls.fused_matmul35_add40_add41, (lv468_2, lv762, lv763, lv466_2), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv470_1 = R.call_tir(cls.fused_reshape51_transpose46, (lv469_1,), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv764: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_229
            lv765: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_595
            lv471_1 = R.call_tir(cls.fused_conv2d25_add37_add39, (lv470_1, lv764, lv765, lv452_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv1078 = R.call_tir(cls.concatenate5, (lv471_1, lv313), out_sinfo=R.Tensor((2, 1920, 16, 16), dtype="float32"))
            lv766: R.Tensor((1920,), dtype="float32") = transformed_param_276
            lv767: R.Tensor((1920,), dtype="float32") = transformed_param_275
            lv472_1 = R.call_tir(cls.fused_group_norm19_silu15, (lv1078, lv766, lv767), out_sinfo=R.Tensor((2, 1920, 16, 16), dtype="float32"))
            lv1084 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv768: R.Tensor((1280, 1280), dtype="float32") = transformed_param_597
            lv769: R.Tensor((1280,), dtype="float32") = transformed_param_279
            lv473_1 = R.call_tir(cls.fused_matmul9_add20_strided_slice5, (lv1084, lv768, lv769), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv1089 = R.call_tir(cls.reshape43, (lv473_1,), out_sinfo=R.Tensor((2, 1280, 1, 1), dtype="float32"))
            lv770: R.Tensor((1280, 1920, 3, 3), dtype="float32") = transformed_param_272
            lv771: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_596
            lv474_1 = R.call_tir(cls.fused_conv2d33_add37_add38, (lv472_1, lv770, lv771, lv1089), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv772: R.Tensor((1280,), dtype="float32") = transformed_param_278
            lv773: R.Tensor((1280,), dtype="float32") = transformed_param_277
            lv475_1 = R.call_tir(cls.fused_group_norm13_silu11, (lv474_1, lv772, lv773), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv774: R.Tensor((1280, 1920, 1, 1), dtype="float32") = transformed_param_274
            lv775: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_599
            lv476_1 = R.call_tir(cls.fused_conv2d34_add37, (lv1078, lv774, lv775), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv776: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_273
            lv777: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_598
            lv477_1 = R.call_tir(cls.fused_conv2d23_add37_add39_divide11, (lv475_1, lv776, lv777, lv476_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv778: R.Tensor((1280,), dtype="float32") = transformed_param_242
            lv779: R.Tensor((1280,), dtype="float32") = transformed_param_241
            lv1101 = R.call_tir(cls.group_norm14, (lv477_1, lv778, lv779), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv780: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_243
            lv781: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_600
            lv478_1 = R.call_tir(cls.fused_conv2d25_add37, (lv1101, lv780, lv781), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv479_1 = R.call_tir(cls.fused_transpose37_reshape44, (lv478_1,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv782: R.Tensor((1280,), dtype="float32") = transformed_param_251
            lv783_1: R.Tensor((1280,), dtype="float32") = transformed_param_250
            lv1107 = R.call_tir(cls.layer_norm3, (lv479_1, lv782, lv783_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv784: R.Tensor((1280, 1280), dtype="float32") = transformed_param_601
            lv1109 = R.call_tir(cls.matmul28, (lv1107, lv784), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv785: R.Tensor((1280, 1280), dtype="float32") = transformed_param_602
            lv1111 = R.call_tir(cls.matmul28, (lv1107, lv785), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv786: R.Tensor((1280, 1280), dtype="float32") = transformed_param_603
            lv1113 = R.call_tir(cls.matmul28, (lv1107, lv786), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv480_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv1109,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv481_2 = R.call_tir(cls.fused_reshape45_transpose38_reshape46_transpose39, (lv1111,), out_sinfo=R.Tensor((16, 160, 256), dtype="float32"))
            lv482_2 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv1113,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv483_1 = R.call_tir(cls.fused_matmul29_multiply19, (lv480_1, lv481_2), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv1126 = R.call_tir(cls.softmax6, (lv483_1,), out_sinfo=R.Tensor((16, 256, 256), dtype="float32"))
            lv1127 = R.call_tir(cls.matmul30, (lv1126, lv482_2), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv484_1 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv1127,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv787: R.Tensor((1280, 1280), dtype="float32") = transformed_param_604
            lv788_1: R.Tensor((1280,), dtype="float32") = transformed_param_245
            lv485_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv484_1, lv787, lv788_1, lv479_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv789: R.Tensor((1280,), dtype="float32") = transformed_param_253
            lv790: R.Tensor((1280,), dtype="float32") = transformed_param_252
            lv1135 = R.call_tir(cls.layer_norm3, (lv485_1, lv789, lv790), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv791: R.Tensor((1280, 1280), dtype="float32") = transformed_param_605
            lv1137 = R.call_tir(cls.matmul28, (lv1135, lv791), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv792: R.Tensor((768, 1280), dtype="float32") = transformed_param_606
            lv1139 = R.call_tir(cls.matmul31, (inp_2, lv792), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv793: R.Tensor((768, 1280), dtype="float32") = transformed_param_607
            lv1141 = R.call_tir(cls.matmul31, (inp_2, lv793), out_sinfo=R.Tensor((2, 77, 1280), dtype="float32"))
            lv486_1 = R.call_tir(cls.fused_reshape45_transpose38_reshape46, (lv1137,), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv487_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50_transpose43, (lv1139,), out_sinfo=R.Tensor((16, 160, 77), dtype="float32"))
            lv488_1 = R.call_tir(cls.fused_reshape49_transpose42_reshape50, (lv1141,), out_sinfo=R.Tensor((16, 77, 160), dtype="float32"))
            lv489_1 = R.call_tir(cls.fused_matmul32_multiply20, (lv486_1, lv487_1), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv1154 = R.call_tir(cls.softmax7, (lv489_1,), out_sinfo=R.Tensor((16, 256, 77), dtype="float32"))
            lv1155 = R.call_tir(cls.matmul33, (lv1154, lv488_1), out_sinfo=R.Tensor((16, 256, 160), dtype="float32"))
            lv490_2 = R.call_tir(cls.fused_reshape47_transpose40_reshape48, (lv1155,), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv794: R.Tensor((1280, 1280), dtype="float32") = transformed_param_608
            lv795: R.Tensor((1280,), dtype="float32") = transformed_param_246
            lv491_1 = R.call_tir(cls.fused_matmul28_add40_add41, (lv490_2, lv794, lv795, lv485_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv796: R.Tensor((1280,), dtype="float32") = transformed_param_255
            lv797_1: R.Tensor((1280,), dtype="float32") = transformed_param_254
            lv1163 = R.call_tir(cls.layer_norm3, (lv491_1, lv796, lv797_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv798: R.Tensor((1280, 5120), dtype="float32") = transformed_param_610
            lv799: R.Tensor((5120,), dtype="float32") = transformed_param_248
            lv492_2 = R.call_tir(cls.fused_matmul34_add42_gelu2, (lv1163, lv798, lv799), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv800: R.Tensor((1280, 5120), dtype="float32") = transformed_param_609
            lv801: R.Tensor((5120,), dtype="float32") = transformed_param_247
            lv493_1 = R.call_tir(cls.fused_matmul34_add42_multiply21, (lv1163, lv800, lv801, lv492_2), out_sinfo=R.Tensor((2, 256, 5120), dtype="float32"))
            lv802: R.Tensor((5120, 1280), dtype="float32") = transformed_param_611
            lv803_1: R.Tensor((1280,), dtype="float32") = transformed_param_249
            lv494_2 = R.call_tir(cls.fused_matmul35_add40_add41, (lv493_1, lv802, lv803_1, lv491_1), out_sinfo=R.Tensor((2, 256, 1280), dtype="float32"))
            lv495_1 = R.call_tir(cls.fused_reshape51_transpose46, (lv494_2,), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv804: R.Tensor((1280, 1280, 1, 1), dtype="float32") = transformed_param_244
            lv805: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_612
            lv496_2 = R.call_tir(cls.fused_conv2d25_add37_add39, (lv495_1, lv804, lv805, lv477_1), out_sinfo=R.Tensor((2, 1280, 16, 16), dtype="float32"))
            lv1182 = R.call_tir(cls.resize2d4, (lv496_2,), out_sinfo=R.Tensor((2, 1280, 32, 32), dtype="float32"))
            lv806: R.Tensor((1280, 1280, 3, 3), dtype="float32") = transformed_param_280
            lv807: R.Tensor((1, 1280, 1, 1), dtype="float32") = transformed_param_613
            lv497_1 = R.call_tir(cls.fused_conv2d35_add49, (lv1182, lv806, lv807), out_sinfo=R.Tensor((2, 1280, 32, 32), dtype="float32"))
            lv1186 = R.call_tir(cls.concatenate6, (lv497_1, lv312_1), out_sinfo=R.Tensor((2, 1920, 32, 32), dtype="float32"))
            lv808_1: R.Tensor((1920,), dtype="float32") = transformed_param_330
            lv809: R.Tensor((1920,), dtype="float32") = transformed_param_329
            lv498_1 = R.call_tir(cls.fused_group_norm20_silu16, (lv1186, lv808_1, lv809), out_sinfo=R.Tensor((2, 1920, 32, 32), dtype="float32"))
            lv1192 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv810: R.Tensor((1280, 640), dtype="float32") = transformed_param_615
            lv811: R.Tensor((640,), dtype="float32") = transformed_param_333
            lv499_1 = R.call_tir(cls.fused_matmul19_add30_strided_slice4, (lv1192, lv810, lv811), out_sinfo=R.Tensor((2, 640), dtype="float32"))
            lv1197 = R.call_tir(cls.reshape33, (lv499_1,), out_sinfo=R.Tensor((2, 640, 1, 1), dtype="float32"))
            lv812: R.Tensor((640, 1920, 3, 3), dtype="float32") = transformed_param_326
            lv813: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_614
            lv500_1 = R.call_tir(cls.fused_conv2d36_add29_add31, (lv498_1, lv812, lv813, lv1197), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv814: R.Tensor((640,), dtype="float32") = transformed_param_332
            lv815: R.Tensor((640,), dtype="float32") = transformed_param_331
            lv501_1 = R.call_tir(cls.fused_group_norm10_silu9, (lv500_1, lv814, lv815), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv816: R.Tensor((640, 1920, 1, 1), dtype="float32") = transformed_param_328
            lv817: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_617
            lv502_1 = R.call_tir(cls.fused_conv2d37_add29, (lv1186, lv816, lv817), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv818: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_327
            lv819: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_616
            lv503_1 = R.call_tir(cls.fused_conv2d18_add29_add32_divide10, (lv501_1, lv818, lv819, lv502_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv820_1: R.Tensor((640,), dtype="float32") = transformed_param_282
            lv821: R.Tensor((640,), dtype="float32") = transformed_param_281
            lv1209 = R.call_tir(cls.group_norm11, (lv503_1, lv820_1, lv821), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv822: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_283
            lv823: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_618
            lv504_1 = R.call_tir(cls.fused_conv2d20_add29, (lv1209, lv822, lv823), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv505_1 = R.call_tir(cls.fused_transpose26_reshape34, (lv504_1,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv824: R.Tensor((640,), dtype="float32") = transformed_param_291
            lv825: R.Tensor((640,), dtype="float32") = transformed_param_290
            lv1215 = R.call_tir(cls.layer_norm2, (lv505_1, lv824, lv825), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv826_1: R.Tensor((640, 640), dtype="float32") = transformed_param_619
            lv1217 = R.call_tir(cls.matmul20, (lv1215, lv826_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv827: R.Tensor((640, 640), dtype="float32") = transformed_param_620
            lv1219 = R.call_tir(cls.matmul20, (lv1215, lv827), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv828: R.Tensor((640, 640), dtype="float32") = transformed_param_621
            lv1221 = R.call_tir(cls.matmul20, (lv1215, lv828), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv506_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1217,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv507_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36_transpose29, (lv1219,), out_sinfo=R.Tensor((16, 80, 1024), dtype="float32"))
            lv508_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1221,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv509_2 = R.call_tir(cls.fused_matmul21_multiply16, (lv506_1, lv507_1), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv1234 = R.call_tir(cls.softmax4, (lv509_2,), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv1235 = R.call_tir(cls.matmul22, (lv1234, lv508_1), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv510_2 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv1235,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv829: R.Tensor((640, 640), dtype="float32") = transformed_param_622
            lv830: R.Tensor((640,), dtype="float32") = transformed_param_285
            lv511_1 = R.call_tir(cls.fused_matmul20_add33_add34, (lv510_2, lv829, lv830, lv505_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv831_1: R.Tensor((640,), dtype="float32") = transformed_param_293
            lv832: R.Tensor((640,), dtype="float32") = transformed_param_292
            lv1243 = R.call_tir(cls.layer_norm2, (lv511_1, lv831_1, lv832), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv833: R.Tensor((640, 640), dtype="float32") = transformed_param_623
            lv1245 = R.call_tir(cls.matmul20, (lv1243, lv833), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv834: R.Tensor((768, 640), dtype="float32") = transformed_param_624
            lv1247 = R.call_tir(cls.matmul23, (inp_2, lv834), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv835: R.Tensor((768, 640), dtype="float32") = transformed_param_625
            lv1249 = R.call_tir(cls.matmul23, (inp_2, lv835), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv512_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1245,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv513_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40_transpose33, (lv1247,), out_sinfo=R.Tensor((16, 80, 77), dtype="float32"))
            lv514_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40, (lv1249,), out_sinfo=R.Tensor((16, 77, 80), dtype="float32"))
            lv515_1 = R.call_tir(cls.fused_matmul24_multiply17, (lv512_1, lv513_1), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv1262 = R.call_tir(cls.softmax5, (lv515_1,), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv1263 = R.call_tir(cls.matmul25, (lv1262, lv514_1), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv516_1 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv1263,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv836: R.Tensor((640, 640), dtype="float32") = transformed_param_626
            lv837: R.Tensor((640,), dtype="float32") = transformed_param_286
            lv517_1 = R.call_tir(cls.fused_matmul20_add33_add34, (lv516_1, lv836, lv837, lv511_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv838: R.Tensor((640,), dtype="float32") = transformed_param_295
            lv839: R.Tensor((640,), dtype="float32") = transformed_param_294
            lv1271 = R.call_tir(cls.layer_norm2, (lv517_1, lv838, lv839), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv840: R.Tensor((640, 2560), dtype="float32") = transformed_param_628
            lv841: R.Tensor((2560,), dtype="float32") = transformed_param_288
            lv518_2 = R.call_tir(cls.fused_matmul26_add35_gelu1, (lv1271, lv840, lv841), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv842: R.Tensor((640, 2560), dtype="float32") = transformed_param_627
            lv843_1: R.Tensor((2560,), dtype="float32") = transformed_param_287
            lv519_1 = R.call_tir(cls.fused_matmul26_add35_multiply18, (lv1271, lv842, lv843_1, lv518_2), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv844: R.Tensor((2560, 640), dtype="float32") = transformed_param_629
            lv845: R.Tensor((640,), dtype="float32") = transformed_param_289
            lv520_1 = R.call_tir(cls.fused_matmul27_add33_add34, (lv519_1, lv844, lv845, lv517_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv521_1 = R.call_tir(cls.fused_reshape41_transpose36, (lv520_1,), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv846: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_284
            lv847: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_630
            lv522_1 = R.call_tir(cls.fused_conv2d20_add29_add32, (lv521_1, lv846, lv847, lv503_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv1290 = R.call_tir(cls.concatenate7, (lv522_1, lv288_1), out_sinfo=R.Tensor((2, 1280, 32, 32), dtype="float32"))
            lv848: R.Tensor((1280,), dtype="float32") = transformed_param_338
            lv849_1: R.Tensor((1280,), dtype="float32") = transformed_param_337
            lv523_1 = R.call_tir(cls.fused_group_norm21_silu17, (lv1290, lv848, lv849_1), out_sinfo=R.Tensor((2, 1280, 32, 32), dtype="float32"))
            lv1296 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv850: R.Tensor((1280, 640), dtype="float32") = transformed_param_632
            lv851: R.Tensor((640,), dtype="float32") = transformed_param_341
            lv524_1 = R.call_tir(cls.fused_matmul19_add30_strided_slice4, (lv1296, lv850, lv851), out_sinfo=R.Tensor((2, 640), dtype="float32"))
            lv1301 = R.call_tir(cls.reshape33, (lv524_1,), out_sinfo=R.Tensor((2, 640, 1, 1), dtype="float32"))
            lv852: R.Tensor((640, 1280, 3, 3), dtype="float32") = transformed_param_334
            lv853: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_631
            lv525_1 = R.call_tir(cls.fused_conv2d38_add29_add31, (lv523_1, lv852, lv853, lv1301), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv854_1: R.Tensor((640,), dtype="float32") = transformed_param_340
            lv855: R.Tensor((640,), dtype="float32") = transformed_param_339
            lv526_1 = R.call_tir(cls.fused_group_norm10_silu9, (lv525_1, lv854_1, lv855), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv856: R.Tensor((640, 1280, 1, 1), dtype="float32") = transformed_param_336
            lv857: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_634
            lv527_1 = R.call_tir(cls.fused_conv2d39_add29, (lv1290, lv856, lv857), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv858: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_335
            lv859: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_633
            lv528_1 = R.call_tir(cls.fused_conv2d18_add29_add32_divide10, (lv526_1, lv858, lv859, lv527_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv860: R.Tensor((640,), dtype="float32") = transformed_param_297
            lv861: R.Tensor((640,), dtype="float32") = transformed_param_296
            lv1313 = R.call_tir(cls.group_norm11, (lv528_1, lv860, lv861), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv862: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_298
            lv863: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_635
            lv529_1 = R.call_tir(cls.fused_conv2d20_add29, (lv1313, lv862, lv863), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv530_1 = R.call_tir(cls.fused_transpose26_reshape34, (lv529_1,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv864: R.Tensor((640,), dtype="float32") = transformed_param_306
            lv865: R.Tensor((640,), dtype="float32") = transformed_param_305
            lv1319 = R.call_tir(cls.layer_norm2, (lv530_1, lv864, lv865), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv866_1: R.Tensor((640, 640), dtype="float32") = transformed_param_636
            lv1321 = R.call_tir(cls.matmul20, (lv1319, lv866_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv867: R.Tensor((640, 640), dtype="float32") = transformed_param_637
            lv1323 = R.call_tir(cls.matmul20, (lv1319, lv867), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv868: R.Tensor((640, 640), dtype="float32") = transformed_param_638
            lv1325 = R.call_tir(cls.matmul20, (lv1319, lv868), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv531_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1321,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv532_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36_transpose29, (lv1323,), out_sinfo=R.Tensor((16, 80, 1024), dtype="float32"))
            lv533_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1325,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv534_1 = R.call_tir(cls.fused_matmul21_multiply16, (lv531_1, lv532_1), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv1338 = R.call_tir(cls.softmax4, (lv534_1,), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv1339 = R.call_tir(cls.matmul22, (lv1338, lv533_1), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv535_1 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv1339,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv869: R.Tensor((640, 640), dtype="float32") = transformed_param_639
            lv870_1: R.Tensor((640,), dtype="float32") = transformed_param_300
            lv536_1 = R.call_tir(cls.fused_matmul20_add33_add34, (lv535_1, lv869, lv870_1, lv530_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv871: R.Tensor((640,), dtype="float32") = transformed_param_308
            lv872: R.Tensor((640,), dtype="float32") = transformed_param_307
            lv1347 = R.call_tir(cls.layer_norm2, (lv536_1, lv871, lv872), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv873: R.Tensor((640, 640), dtype="float32") = transformed_param_640
            lv1349 = R.call_tir(cls.matmul20, (lv1347, lv873), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv874: R.Tensor((768, 640), dtype="float32") = transformed_param_641
            lv1351 = R.call_tir(cls.matmul23, (inp_2, lv874), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv875: R.Tensor((768, 640), dtype="float32") = transformed_param_642
            lv1353 = R.call_tir(cls.matmul23, (inp_2, lv875), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv537_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1349,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv538_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40_transpose33, (lv1351,), out_sinfo=R.Tensor((16, 80, 77), dtype="float32"))
            lv539_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40, (lv1353,), out_sinfo=R.Tensor((16, 77, 80), dtype="float32"))
            lv540_1 = R.call_tir(cls.fused_matmul24_multiply17, (lv537_1, lv538_1), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv1366 = R.call_tir(cls.softmax5, (lv540_1,), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv1367 = R.call_tir(cls.matmul25, (lv1366, lv539_1), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv541_1 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv1367,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv876_1: R.Tensor((640, 640), dtype="float32") = transformed_param_643
            lv877: R.Tensor((640,), dtype="float32") = transformed_param_301
            lv542_2 = R.call_tir(cls.fused_matmul20_add33_add34, (lv541_1, lv876_1, lv877, lv536_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv878: R.Tensor((640,), dtype="float32") = transformed_param_310
            lv879: R.Tensor((640,), dtype="float32") = transformed_param_309
            lv1375 = R.call_tir(cls.layer_norm2, (lv542_2, lv878, lv879), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv880: R.Tensor((640, 2560), dtype="float32") = transformed_param_645
            lv881_1: R.Tensor((2560,), dtype="float32") = transformed_param_303
            lv543_1 = R.call_tir(cls.fused_matmul26_add35_gelu1, (lv1375, lv880, lv881_1), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv882: R.Tensor((640, 2560), dtype="float32") = transformed_param_644
            lv883: R.Tensor((2560,), dtype="float32") = transformed_param_302
            lv544_1 = R.call_tir(cls.fused_matmul26_add35_multiply18, (lv1375, lv882, lv883, lv543_1), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv884: R.Tensor((2560, 640), dtype="float32") = transformed_param_646
            lv885: R.Tensor((640,), dtype="float32") = transformed_param_304
            lv545_1 = R.call_tir(cls.fused_matmul27_add33_add34, (lv544_1, lv884, lv885, lv542_2), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv546_1 = R.call_tir(cls.fused_reshape41_transpose36, (lv545_1,), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv886: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_299
            lv887: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_647
            lv547_2 = R.call_tir(cls.fused_conv2d20_add29_add32, (lv546_1, lv886, lv887, lv528_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv1394 = R.call_tir(cls.concatenate8, (lv547_2, lv263), out_sinfo=R.Tensor((2, 960, 32, 32), dtype="float32"))
            lv888: R.Tensor((960,), dtype="float32") = transformed_param_346
            lv889: R.Tensor((960,), dtype="float32") = transformed_param_345
            lv548_1 = R.call_tir(cls.fused_group_norm22_silu18, (lv1394, lv888, lv889), out_sinfo=R.Tensor((2, 960, 32, 32), dtype="float32"))
            lv1400 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv890: R.Tensor((1280, 640), dtype="float32") = transformed_param_649
            lv891: R.Tensor((640,), dtype="float32") = transformed_param_349
            lv549_1 = R.call_tir(cls.fused_matmul19_add30_strided_slice4, (lv1400, lv890, lv891), out_sinfo=R.Tensor((2, 640), dtype="float32"))
            lv1405 = R.call_tir(cls.reshape33, (lv549_1,), out_sinfo=R.Tensor((2, 640, 1, 1), dtype="float32"))
            lv892: R.Tensor((640, 960, 3, 3), dtype="float32") = transformed_param_342
            lv893_1: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_648
            lv550_1 = R.call_tir(cls.fused_conv2d40_add29_add31, (lv548_1, lv892, lv893_1, lv1405), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv894: R.Tensor((640,), dtype="float32") = transformed_param_348
            lv895: R.Tensor((640,), dtype="float32") = transformed_param_347
            lv551_1 = R.call_tir(cls.fused_group_norm10_silu9, (lv550_1, lv894, lv895), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv896: R.Tensor((640, 960, 1, 1), dtype="float32") = transformed_param_344
            lv897: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_651
            lv552_1 = R.call_tir(cls.fused_conv2d41_add29, (lv1394, lv896, lv897), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv898: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_343
            lv899_1: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_650
            lv553_1 = R.call_tir(cls.fused_conv2d18_add29_add32_divide10, (lv551_1, lv898, lv899_1, lv552_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv900: R.Tensor((640,), dtype="float32") = transformed_param_312
            lv901_1: R.Tensor((640,), dtype="float32") = transformed_param_311
            lv1417 = R.call_tir(cls.group_norm11, (lv553_1, lv900, lv901_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv902: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_313
            lv903_1: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_652
            lv554_1 = R.call_tir(cls.fused_conv2d20_add29, (lv1417, lv902, lv903_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv555_1 = R.call_tir(cls.fused_transpose26_reshape34, (lv554_1,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv904: R.Tensor((640,), dtype="float32") = transformed_param_321
            lv905_1: R.Tensor((640,), dtype="float32") = transformed_param_320
            lv1423 = R.call_tir(cls.layer_norm2, (lv555_1, lv904, lv905_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv906: R.Tensor((640, 640), dtype="float32") = transformed_param_653
            lv1425 = R.call_tir(cls.matmul20, (lv1423, lv906), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv907: R.Tensor((640, 640), dtype="float32") = transformed_param_654
            lv1427 = R.call_tir(cls.matmul20, (lv1423, lv907), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv908: R.Tensor((640, 640), dtype="float32") = transformed_param_655
            lv1429 = R.call_tir(cls.matmul20, (lv1423, lv908), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv556_2 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1425,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv557_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36_transpose29, (lv1427,), out_sinfo=R.Tensor((16, 80, 1024), dtype="float32"))
            lv558_1 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1429,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv559_1 = R.call_tir(cls.fused_matmul21_multiply16, (lv556_2, lv557_1), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv1442 = R.call_tir(cls.softmax4, (lv559_1,), out_sinfo=R.Tensor((16, 1024, 1024), dtype="float32"))
            lv1443 = R.call_tir(cls.matmul22, (lv1442, lv558_1), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv560_1 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv1443,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv909: R.Tensor((640, 640), dtype="float32") = transformed_param_656
            lv910: R.Tensor((640,), dtype="float32") = transformed_param_315
            lv561_1 = R.call_tir(cls.fused_matmul20_add33_add34, (lv560_1, lv909, lv910, lv555_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv911: R.Tensor((640,), dtype="float32") = transformed_param_323
            lv912: R.Tensor((640,), dtype="float32") = transformed_param_322
            lv1451 = R.call_tir(cls.layer_norm2, (lv561_1, lv911, lv912), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv913: R.Tensor((640, 640), dtype="float32") = transformed_param_657
            lv1453 = R.call_tir(cls.matmul20, (lv1451, lv913), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv914: R.Tensor((768, 640), dtype="float32") = transformed_param_658
            lv1455 = R.call_tir(cls.matmul23, (inp_2, lv914), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv915: R.Tensor((768, 640), dtype="float32") = transformed_param_659
            lv1457 = R.call_tir(cls.matmul23, (inp_2, lv915), out_sinfo=R.Tensor((2, 77, 640), dtype="float32"))
            lv562_2 = R.call_tir(cls.fused_reshape35_transpose28_reshape36, (lv1453,), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv563_1 = R.call_tir(cls.fused_reshape39_transpose32_reshape40_transpose33, (lv1455,), out_sinfo=R.Tensor((16, 80, 77), dtype="float32"))
            lv564_2 = R.call_tir(cls.fused_reshape39_transpose32_reshape40, (lv1457,), out_sinfo=R.Tensor((16, 77, 80), dtype="float32"))
            lv565_1 = R.call_tir(cls.fused_matmul24_multiply17, (lv562_2, lv563_1), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv1470 = R.call_tir(cls.softmax5, (lv565_1,), out_sinfo=R.Tensor((16, 1024, 77), dtype="float32"))
            lv1471 = R.call_tir(cls.matmul25, (lv1470, lv564_2), out_sinfo=R.Tensor((16, 1024, 80), dtype="float32"))
            lv566_2 = R.call_tir(cls.fused_reshape37_transpose30_reshape38, (lv1471,), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv916: R.Tensor((640, 640), dtype="float32") = transformed_param_660
            lv917: R.Tensor((640,), dtype="float32") = transformed_param_316
            lv567_1 = R.call_tir(cls.fused_matmul20_add33_add34, (lv566_2, lv916, lv917, lv561_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv918_1: R.Tensor((640,), dtype="float32") = transformed_param_325
            lv919_1: R.Tensor((640,), dtype="float32") = transformed_param_324
            lv1479 = R.call_tir(cls.layer_norm2, (lv567_1, lv918_1, lv919_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv920: R.Tensor((640, 2560), dtype="float32") = transformed_param_662
            lv921: R.Tensor((2560,), dtype="float32") = transformed_param_318
            lv568_2 = R.call_tir(cls.fused_matmul26_add35_gelu1, (lv1479, lv920, lv921), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv922: R.Tensor((640, 2560), dtype="float32") = transformed_param_661
            lv923: R.Tensor((2560,), dtype="float32") = transformed_param_317
            lv569_1 = R.call_tir(cls.fused_matmul26_add35_multiply18, (lv1479, lv922, lv923, lv568_2), out_sinfo=R.Tensor((2, 1024, 2560), dtype="float32"))
            lv924: R.Tensor((2560, 640), dtype="float32") = transformed_param_663
            lv925: R.Tensor((640,), dtype="float32") = transformed_param_319
            lv570_1 = R.call_tir(cls.fused_matmul27_add33_add34, (lv569_1, lv924, lv925, lv567_1), out_sinfo=R.Tensor((2, 1024, 640), dtype="float32"))
            lv571_1 = R.call_tir(cls.fused_reshape41_transpose36, (lv570_1,), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv926: R.Tensor((640, 640, 1, 1), dtype="float32") = transformed_param_314
            lv927_1: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_664
            lv572_1 = R.call_tir(cls.fused_conv2d20_add29_add32, (lv571_1, lv926, lv927_1, lv553_1), out_sinfo=R.Tensor((2, 640, 32, 32), dtype="float32"))
            lv1498 = R.call_tir(cls.resize2d5, (lv572_1,), out_sinfo=R.Tensor((2, 640, 64, 64), dtype="float32"))
            lv928: R.Tensor((640, 640, 3, 3), dtype="float32") = transformed_param_350
            lv929_1: R.Tensor((1, 640, 1, 1), dtype="float32") = transformed_param_665
            lv573_1 = R.call_tir(cls.fused_conv2d42_add50, (lv1498, lv928, lv929_1), out_sinfo=R.Tensor((2, 640, 64, 64), dtype="float32"))
            lv1502 = R.call_tir(cls.concatenate9, (lv573_1, lv262), out_sinfo=R.Tensor((2, 960, 64, 64), dtype="float32"))
            lv930: R.Tensor((960,), dtype="float32") = transformed_param_400
            lv931_1: R.Tensor((960,), dtype="float32") = transformed_param_399
            lv574_1 = R.call_tir(cls.fused_group_norm23_silu19, (lv1502, lv930, lv931_1), out_sinfo=R.Tensor((2, 960, 64, 64), dtype="float32"))
            lv1508 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv932: R.Tensor((1280, 320), dtype="float32") = transformed_param_667
            lv933_1: R.Tensor((320,), dtype="float32") = transformed_param_403
            lv575_1 = R.call_tir(cls.fused_matmul10_add22_strided_slice3, (lv1508, lv932, lv933_1), out_sinfo=R.Tensor((2, 320), dtype="float32"))
            lv1513 = R.call_tir(cls.reshape23, (lv575_1,), out_sinfo=R.Tensor((2, 320, 1, 1), dtype="float32"))
            lv934: R.Tensor((320, 960, 3, 3), dtype="float32") = transformed_param_396
            lv935: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_666
            lv576_1 = R.call_tir(cls.fused_conv2d43_add21_add23, (lv574_1, lv934, lv935, lv1513), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv936: R.Tensor((320,), dtype="float32") = transformed_param_402
            lv937: R.Tensor((320,), dtype="float32") = transformed_param_401
            lv577_1 = R.call_tir(cls.fused_group_norm7_silu7, (lv576_1, lv936, lv937), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv938: R.Tensor((320, 960, 1, 1), dtype="float32") = transformed_param_398
            lv939: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_669
            lv578_1 = R.call_tir(cls.fused_conv2d44_add21, (lv1502, lv938, lv939), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv940: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_397
            lv941: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_668
            lv579_1 = R.call_tir(cls.fused_conv2d14_add21_add24_divide9, (lv577_1, lv940, lv941, lv578_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv942: R.Tensor((320,), dtype="float32") = transformed_param_352
            lv943: R.Tensor((320,), dtype="float32") = transformed_param_351
            lv1525 = R.call_tir(cls.group_norm8, (lv579_1, lv942, lv943), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv944: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_353
            lv945: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_670
            lv580_1 = R.call_tir(cls.fused_conv2d15_add21, (lv1525, lv944, lv945), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv581_2 = R.call_tir(cls.fused_transpose16_reshape24, (lv580_1,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv946_1: R.Tensor((320,), dtype="float32") = transformed_param_361
            lv947_1: R.Tensor((320,), dtype="float32") = transformed_param_360
            lv1531 = R.call_tir(cls.layer_norm1, (lv581_2, lv946_1, lv947_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv948: R.Tensor((320, 320), dtype="float32") = transformed_param_671
            lv1533 = R.call_tir(cls.matmul11, (lv1531, lv948), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv949: R.Tensor((320, 320), dtype="float32") = transformed_param_672
            lv1535 = R.call_tir(cls.matmul11, (lv1531, lv949), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv950: R.Tensor((320, 320), dtype="float32") = transformed_param_673
            lv1537 = R.call_tir(cls.matmul11, (lv1531, lv950), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv582_2 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1533,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv583_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26_transpose19, (lv1535,), out_sinfo=R.Tensor((16, 40, 4096), dtype="float32"))
            lv584_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1537,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv585_1 = R.call_tir(cls.fused_matmul12_multiply13, (lv582_2, lv583_1), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv1550 = R.call_tir(cls.softmax2, (lv585_1,), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv1551 = R.call_tir(cls.matmul13, (lv1550, lv584_1), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv586_1 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv1551,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv951: R.Tensor((320, 320), dtype="float32") = transformed_param_674
            lv952: R.Tensor((320,), dtype="float32") = transformed_param_355
            lv587_1 = R.call_tir(cls.fused_matmul11_add25_add26, (lv586_1, lv951, lv952, lv581_2), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv953: R.Tensor((320,), dtype="float32") = transformed_param_363
            lv954: R.Tensor((320,), dtype="float32") = transformed_param_362
            lv1559 = R.call_tir(cls.layer_norm1, (lv587_1, lv953, lv954), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv955_1: R.Tensor((320, 320), dtype="float32") = transformed_param_675
            lv1561 = R.call_tir(cls.matmul11, (lv1559, lv955_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv956: R.Tensor((768, 320), dtype="float32") = transformed_param_676
            lv1563 = R.call_tir(cls.matmul14, (inp_2, lv956), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv957: R.Tensor((768, 320), dtype="float32") = transformed_param_677
            lv1565 = R.call_tir(cls.matmul14, (inp_2, lv957), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv588_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1561,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv589_1 = R.call_tir(cls.fused_reshape29_transpose22_reshape30_transpose23, (lv1563,), out_sinfo=R.Tensor((16, 40, 77), dtype="float32"))
            lv590_2 = R.call_tir(cls.fused_reshape29_transpose22_reshape30, (lv1565,), out_sinfo=R.Tensor((16, 77, 40), dtype="float32"))
            lv591_1 = R.call_tir(cls.fused_matmul15_multiply14, (lv588_1, lv589_1), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv1578 = R.call_tir(cls.softmax3, (lv591_1,), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv1579 = R.call_tir(cls.matmul16, (lv1578, lv590_2), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv592_2 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv1579,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv958: R.Tensor((320, 320), dtype="float32") = transformed_param_678
            lv959: R.Tensor((320,), dtype="float32") = transformed_param_356
            lv593_1 = R.call_tir(cls.fused_matmul11_add25_add26, (lv592_2, lv958, lv959, lv587_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv960: R.Tensor((320,), dtype="float32") = transformed_param_365
            lv961: R.Tensor((320,), dtype="float32") = transformed_param_364
            lv1587 = R.call_tir(cls.layer_norm1, (lv593_1, lv960, lv961), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv962: R.Tensor((320, 1280), dtype="float32") = transformed_param_680
            lv963: R.Tensor((1280,), dtype="float32") = transformed_param_358
            lv594_2 = R.call_tir(cls.fused_matmul17_add27_gelu, (lv1587, lv962, lv963), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv964: R.Tensor((320, 1280), dtype="float32") = transformed_param_679
            lv965: R.Tensor((1280,), dtype="float32") = transformed_param_357
            lv595_1 = R.call_tir(cls.fused_matmul17_add27_multiply15, (lv1587, lv964, lv965, lv594_2), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv966: R.Tensor((1280, 320), dtype="float32") = transformed_param_681
            lv967: R.Tensor((320,), dtype="float32") = transformed_param_359
            lv596_2 = R.call_tir(cls.fused_matmul18_add25_add26, (lv595_1, lv966, lv967, lv593_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv597_1 = R.call_tir(cls.fused_reshape31_transpose24, (lv596_2,), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv968: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_354
            lv969: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_682
            lv598_1 = R.call_tir(cls.fused_conv2d15_add21_add24, (lv597_1, lv968, lv969, lv579_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1606 = R.call_tir(cls.concatenate10, (lv598_1, lv238), out_sinfo=R.Tensor((2, 640, 64, 64), dtype="float32"))
            lv970: R.Tensor((640,), dtype="float32") = transformed_param_408
            lv971: R.Tensor((640,), dtype="float32") = transformed_param_407
            lv599_1 = R.call_tir(cls.fused_group_norm24_silu20, (lv1606, lv970, lv971), out_sinfo=R.Tensor((2, 640, 64, 64), dtype="float32"))
            lv1612 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv972: R.Tensor((1280, 320), dtype="float32") = transformed_param_684
            lv973: R.Tensor((320,), dtype="float32") = transformed_param_411
            lv600_1 = R.call_tir(cls.fused_matmul10_add22_strided_slice3, (lv1612, lv972, lv973), out_sinfo=R.Tensor((2, 320), dtype="float32"))
            lv1617 = R.call_tir(cls.reshape23, (lv600_1,), out_sinfo=R.Tensor((2, 320, 1, 1), dtype="float32"))
            lv974_1: R.Tensor((320, 640, 3, 3), dtype="float32") = transformed_param_404
            lv975: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_683
            lv601_1 = R.call_tir(cls.fused_conv2d45_add21_add23, (lv599_1, lv974_1, lv975, lv1617), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv976: R.Tensor((320,), dtype="float32") = transformed_param_410
            lv977: R.Tensor((320,), dtype="float32") = transformed_param_409
            lv602_1 = R.call_tir(cls.fused_group_norm7_silu7, (lv601_1, lv976, lv977), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv978: R.Tensor((320, 640, 1, 1), dtype="float32") = transformed_param_406
            lv979: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_686
            lv603_1 = R.call_tir(cls.fused_conv2d46_add21, (lv1606, lv978, lv979), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv980_1: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_405
            lv981: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_685
            lv604_1 = R.call_tir(cls.fused_conv2d14_add21_add24_divide9, (lv602_1, lv980_1, lv981, lv603_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv982: R.Tensor((320,), dtype="float32") = transformed_param_367
            lv983: R.Tensor((320,), dtype="float32") = transformed_param_366
            lv1629 = R.call_tir(cls.group_norm8, (lv604_1, lv982, lv983), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv984: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_368
            lv985_1: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_687
            lv605_1 = R.call_tir(cls.fused_conv2d15_add21, (lv1629, lv984, lv985_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv606_1 = R.call_tir(cls.fused_transpose16_reshape24, (lv605_1,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv986: R.Tensor((320,), dtype="float32") = transformed_param_376
            lv987: R.Tensor((320,), dtype="float32") = transformed_param_375
            lv1635 = R.call_tir(cls.layer_norm1, (lv606_1, lv986, lv987), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv988: R.Tensor((320, 320), dtype="float32") = transformed_param_688
            lv1637 = R.call_tir(cls.matmul11, (lv1635, lv988), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv989: R.Tensor((320, 320), dtype="float32") = transformed_param_689
            lv1639 = R.call_tir(cls.matmul11, (lv1635, lv989), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv990: R.Tensor((320, 320), dtype="float32") = transformed_param_690
            lv1641 = R.call_tir(cls.matmul11, (lv1635, lv990), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv607_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1637,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv608_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26_transpose19, (lv1639,), out_sinfo=R.Tensor((16, 40, 4096), dtype="float32"))
            lv609_2 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1641,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv610_2 = R.call_tir(cls.fused_matmul12_multiply13, (lv607_1, lv608_1), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv1654 = R.call_tir(cls.softmax2, (lv610_2,), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv1655 = R.call_tir(cls.matmul13, (lv1654, lv609_2), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv611_1 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv1655,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv991: R.Tensor((320, 320), dtype="float32") = transformed_param_691
            lv992: R.Tensor((320,), dtype="float32") = transformed_param_370
            lv612_1 = R.call_tir(cls.fused_matmul11_add25_add26, (lv611_1, lv991, lv992, lv606_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv993: R.Tensor((320,), dtype="float32") = transformed_param_378
            lv994: R.Tensor((320,), dtype="float32") = transformed_param_377
            lv1663 = R.call_tir(cls.layer_norm1, (lv612_1, lv993, lv994), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv995: R.Tensor((320, 320), dtype="float32") = transformed_param_692
            lv1665 = R.call_tir(cls.matmul11, (lv1663, lv995), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv996: R.Tensor((768, 320), dtype="float32") = transformed_param_693
            lv1667 = R.call_tir(cls.matmul14, (inp_2, lv996), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv997_1: R.Tensor((768, 320), dtype="float32") = transformed_param_694
            lv1669 = R.call_tir(cls.matmul14, (inp_2, lv997_1), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv613_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1665,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv614_1 = R.call_tir(cls.fused_reshape29_transpose22_reshape30_transpose23, (lv1667,), out_sinfo=R.Tensor((16, 40, 77), dtype="float32"))
            lv615_1 = R.call_tir(cls.fused_reshape29_transpose22_reshape30, (lv1669,), out_sinfo=R.Tensor((16, 77, 40), dtype="float32"))
            lv616_1 = R.call_tir(cls.fused_matmul15_multiply14, (lv613_1, lv614_1), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv1682 = R.call_tir(cls.softmax3, (lv616_1,), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv1683 = R.call_tir(cls.matmul16, (lv1682, lv615_1), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv617_1 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv1683,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv998: R.Tensor((320, 320), dtype="float32") = transformed_param_695
            lv999: R.Tensor((320,), dtype="float32") = transformed_param_371
            lv618_2 = R.call_tir(cls.fused_matmul11_add25_add26, (lv617_1, lv998, lv999, lv612_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1000: R.Tensor((320,), dtype="float32") = transformed_param_380
            lv1001: R.Tensor((320,), dtype="float32") = transformed_param_379
            lv1691 = R.call_tir(cls.layer_norm1, (lv618_2, lv1000, lv1001), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1002: R.Tensor((320, 1280), dtype="float32") = transformed_param_697
            lv1003_1: R.Tensor((1280,), dtype="float32") = transformed_param_373
            lv619_1 = R.call_tir(cls.fused_matmul17_add27_gelu, (lv1691, lv1002, lv1003_1), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv1004: R.Tensor((320, 1280), dtype="float32") = transformed_param_696
            lv1005_1: R.Tensor((1280,), dtype="float32") = transformed_param_372
            lv620_1 = R.call_tir(cls.fused_matmul17_add27_multiply15, (lv1691, lv1004, lv1005_1, lv619_1), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv1006: R.Tensor((1280, 320), dtype="float32") = transformed_param_698
            lv1007_1: R.Tensor((320,), dtype="float32") = transformed_param_374
            lv621_1 = R.call_tir(cls.fused_matmul18_add25_add26, (lv620_1, lv1006, lv1007_1, lv618_2), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv622_1 = R.call_tir(cls.fused_reshape31_transpose24, (lv621_1,), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1008: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_369
            lv1009_1: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_699
            lv623_1 = R.call_tir(cls.fused_conv2d15_add21_add24, (lv622_1, lv1008, lv1009_1, lv604_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1710 = R.call_tir(cls.concatenate10, (lv623_1, lv214), out_sinfo=R.Tensor((2, 640, 64, 64), dtype="float32"))
            lv1010: R.Tensor((640,), dtype="float32") = transformed_param_416
            lv1011: R.Tensor((640,), dtype="float32") = transformed_param_415
            lv624_1 = R.call_tir(cls.fused_group_norm24_silu20, (lv1710, lv1010, lv1011), out_sinfo=R.Tensor((2, 640, 64, 64), dtype="float32"))
            lv1716 = R.call_tir(cls.silu6, (lv213,), out_sinfo=R.Tensor((2, 1280), dtype="float32"))
            lv1012: R.Tensor((1280, 320), dtype="float32") = transformed_param_701
            lv1013: R.Tensor((320,), dtype="float32") = transformed_param_419
            lv625_1 = R.call_tir(cls.fused_matmul10_add22_strided_slice3, (lv1716, lv1012, lv1013), out_sinfo=R.Tensor((2, 320), dtype="float32"))
            lv1721 = R.call_tir(cls.reshape23, (lv625_1,), out_sinfo=R.Tensor((2, 320, 1, 1), dtype="float32"))
            lv1014: R.Tensor((320, 640, 3, 3), dtype="float32") = transformed_param_412
            lv1015: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_700
            lv626_1 = R.call_tir(cls.fused_conv2d45_add21_add23, (lv624_1, lv1014, lv1015, lv1721), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1016: R.Tensor((320,), dtype="float32") = transformed_param_418
            lv1017: R.Tensor((320,), dtype="float32") = transformed_param_417
            lv627_1 = R.call_tir(cls.fused_group_norm7_silu7, (lv626_1, lv1016, lv1017), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1018: R.Tensor((320, 640, 1, 1), dtype="float32") = transformed_param_414
            lv1019: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_703
            lv628_1 = R.call_tir(cls.fused_conv2d46_add21, (lv1710, lv1018, lv1019), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1020: R.Tensor((320, 320, 3, 3), dtype="float32") = transformed_param_413
            lv1021: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_702
            lv629_1 = R.call_tir(cls.fused_conv2d14_add21_add24_divide9, (lv627_1, lv1020, lv1021, lv628_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1022_1: R.Tensor((320,), dtype="float32") = transformed_param_382
            lv1023_1: R.Tensor((320,), dtype="float32") = transformed_param_381
            lv1733 = R.call_tir(cls.group_norm8, (lv629_1, lv1022_1, lv1023_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1024: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_383
            lv1025: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_704
            lv630_1 = R.call_tir(cls.fused_conv2d15_add21, (lv1733, lv1024, lv1025), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv631_1 = R.call_tir(cls.fused_transpose16_reshape24, (lv630_1,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1026: R.Tensor((320,), dtype="float32") = transformed_param_391
            lv1027: R.Tensor((320,), dtype="float32") = transformed_param_390
            lv1739 = R.call_tir(cls.layer_norm1, (lv631_1, lv1026, lv1027), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1028: R.Tensor((320, 320), dtype="float32") = transformed_param_705
            lv1741 = R.call_tir(cls.matmul11, (lv1739, lv1028), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1029: R.Tensor((320, 320), dtype="float32") = transformed_param_706
            lv1743 = R.call_tir(cls.matmul11, (lv1739, lv1029), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1030: R.Tensor((320, 320), dtype="float32") = transformed_param_707
            lv1745 = R.call_tir(cls.matmul11, (lv1739, lv1030), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv632_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1741,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv633_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26_transpose19, (lv1743,), out_sinfo=R.Tensor((16, 40, 4096), dtype="float32"))
            lv634_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1745,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv635_1 = R.call_tir(cls.fused_matmul12_multiply13, (lv632_1, lv633_1), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv1758 = R.call_tir(cls.softmax2, (lv635_1,), out_sinfo=R.Tensor((16, 4096, 4096), dtype="float32"))
            lv1759 = R.call_tir(cls.matmul13, (lv1758, lv634_1), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv636_1 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv1759,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1031_1: R.Tensor((320, 320), dtype="float32") = transformed_param_708
            lv1032: R.Tensor((320,), dtype="float32") = transformed_param_385
            lv637_1 = R.call_tir(cls.fused_matmul11_add25_add26, (lv636_1, lv1031_1, lv1032, lv631_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1033_1: R.Tensor((320,), dtype="float32") = transformed_param_393
            lv1034: R.Tensor((320,), dtype="float32") = transformed_param_392
            lv1767 = R.call_tir(cls.layer_norm1, (lv637_1, lv1033_1, lv1034), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1035_1: R.Tensor((320, 320), dtype="float32") = transformed_param_709
            lv1769 = R.call_tir(cls.matmul11, (lv1767, lv1035_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1036: R.Tensor((768, 320), dtype="float32") = transformed_param_710
            lv1771 = R.call_tir(cls.matmul14, (inp_2, lv1036), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv1037_1: R.Tensor((768, 320), dtype="float32") = transformed_param_711
            lv1773 = R.call_tir(cls.matmul14, (inp_2, lv1037_1), out_sinfo=R.Tensor((2, 77, 320), dtype="float32"))
            lv638_1 = R.call_tir(cls.fused_reshape25_transpose18_reshape26, (lv1769,), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv639_1 = R.call_tir(cls.fused_reshape29_transpose22_reshape30_transpose23, (lv1771,), out_sinfo=R.Tensor((16, 40, 77), dtype="float32"))
            lv640_1 = R.call_tir(cls.fused_reshape29_transpose22_reshape30, (lv1773,), out_sinfo=R.Tensor((16, 77, 40), dtype="float32"))
            lv641_1 = R.call_tir(cls.fused_matmul15_multiply14, (lv638_1, lv639_1), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv1786 = R.call_tir(cls.softmax3, (lv641_1,), out_sinfo=R.Tensor((16, 4096, 77), dtype="float32"))
            lv1787 = R.call_tir(cls.matmul16, (lv1786, lv640_1), out_sinfo=R.Tensor((16, 4096, 40), dtype="float32"))
            lv642_1 = R.call_tir(cls.fused_reshape27_transpose20_reshape28, (lv1787,), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1038: R.Tensor((320, 320), dtype="float32") = transformed_param_712
            lv1039: R.Tensor((320,), dtype="float32") = transformed_param_386
            lv643_1 = R.call_tir(cls.fused_matmul11_add25_add26, (lv642_1, lv1038, lv1039, lv637_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1040: R.Tensor((320,), dtype="float32") = transformed_param_395
            lv1041: R.Tensor((320,), dtype="float32") = transformed_param_394
            lv1795 = R.call_tir(cls.layer_norm1, (lv643_1, lv1040, lv1041), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv1042: R.Tensor((320, 1280), dtype="float32") = transformed_param_714
            lv1043: R.Tensor((1280,), dtype="float32") = transformed_param_388
            lv644_1 = R.call_tir(cls.fused_matmul17_add27_gelu, (lv1795, lv1042, lv1043), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv1044: R.Tensor((320, 1280), dtype="float32") = transformed_param_713
            lv1045: R.Tensor((1280,), dtype="float32") = transformed_param_387
            lv645_2 = R.call_tir(cls.fused_matmul17_add27_multiply15, (lv1795, lv1044, lv1045, lv644_1), out_sinfo=R.Tensor((2, 4096, 1280), dtype="float32"))
            lv1046: R.Tensor((1280, 320), dtype="float32") = transformed_param_715
            lv1047: R.Tensor((320,), dtype="float32") = transformed_param_389
            lv646_1 = R.call_tir(cls.fused_matmul18_add25_add26, (lv645_2, lv1046, lv1047, lv643_1), out_sinfo=R.Tensor((2, 4096, 320), dtype="float32"))
            lv647_1 = R.call_tir(cls.fused_reshape31_transpose24, (lv646_1,), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1048: R.Tensor((320, 320, 1, 1), dtype="float32") = transformed_param_384
            lv1049: R.Tensor((1, 320, 1, 1), dtype="float32") = transformed_param_716
            lv648_1 = R.call_tir(cls.fused_conv2d15_add21_add24, (lv647_1, lv1048, lv1049, lv629_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1050_1: R.Tensor((320,), dtype="float32") = transformed_param_2
            lv1051_1: R.Tensor((320,), dtype="float32") = transformed_param_1
            lv649_1 = R.call_tir(cls.fused_group_norm7_silu7, (lv648_1, lv1050_1, lv1051_1), out_sinfo=R.Tensor((2, 320, 64, 64), dtype="float32"))
            lv1052: R.Tensor((4, 320, 3, 3), dtype="float32") = transformed_param_3
            lv1053: R.Tensor((1, 4, 1, 1), dtype="float32") = transformed_param_717
            lv650_2 = R.call_tir(cls.fused_conv2d47_add51, (lv649_1, lv1052, lv1053), out_sinfo=R.Tensor((2, 4, 64, 64), dtype="float32"))
            lv651_1 = R.call_tir(cls.fused_split_subtract_multiply25_add, (lv650_2,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
            gv: R.Tensor((1, 4, 64, 64), dtype="float32") = lv651_1
            R.output(gv)
        return gv

    @R.function
    def vae(inp_0: R.Tensor((1, 4, 64, 64), dtype="float32"), transformed_param_0: R.Tensor((512, 4, 3, 3), dtype="float32"), transformed_param_1: R.Tensor((128,), dtype="float32"), transformed_param_2: R.Tensor((128,), dtype="float32"), transformed_param_3: R.Tensor((3, 128, 3, 3), dtype="float32"), transformed_param_4: R.Tensor((512,), dtype="float32"), transformed_param_5: R.Tensor((512,), dtype="float32"), transformed_param_6: R.Tensor((512,), dtype="float32"), transformed_param_7: R.Tensor((512,), dtype="float32"), transformed_param_8: R.Tensor((512,), dtype="float32"), transformed_param_9: R.Tensor((512,), dtype="float32"), transformed_param_10: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_11: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_12: R.Tensor((512,), dtype="float32"), transformed_param_13: R.Tensor((512,), dtype="float32"), transformed_param_14: R.Tensor((512,), dtype="float32"), transformed_param_15: R.Tensor((512,), dtype="float32"), transformed_param_16: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_17: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_18: R.Tensor((512,), dtype="float32"), transformed_param_19: R.Tensor((512,), dtype="float32"), transformed_param_20: R.Tensor((512,), dtype="float32"), transformed_param_21: R.Tensor((512,), dtype="float32"), transformed_param_22: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_23: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_24: R.Tensor((512,), dtype="float32"), transformed_param_25: R.Tensor((512,), dtype="float32"), transformed_param_26: R.Tensor((512,), dtype="float32"), transformed_param_27: R.Tensor((512,), dtype="float32"), transformed_param_28: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_29: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_30: R.Tensor((512,), dtype="float32"), transformed_param_31: R.Tensor((512,), dtype="float32"), transformed_param_32: R.Tensor((512,), dtype="float32"), transformed_param_33: R.Tensor((512,), dtype="float32"), transformed_param_34: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_35: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_36: R.Tensor((512,), dtype="float32"), transformed_param_37: R.Tensor((512,), dtype="float32"), transformed_param_38: R.Tensor((512,), dtype="float32"), transformed_param_39: R.Tensor((512,), dtype="float32"), transformed_param_40: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_41: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_42: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_43: R.Tensor((512,), dtype="float32"), transformed_param_44: R.Tensor((512,), dtype="float32"), transformed_param_45: R.Tensor((512,), dtype="float32"), transformed_param_46: R.Tensor((512,), dtype="float32"), transformed_param_47: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_48: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_49: R.Tensor((512,), dtype="float32"), transformed_param_50: R.Tensor((512,), dtype="float32"), transformed_param_51: R.Tensor((512,), dtype="float32"), transformed_param_52: R.Tensor((512,), dtype="float32"), transformed_param_53: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_54: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_55: R.Tensor((512,), dtype="float32"), transformed_param_56: R.Tensor((512,), dtype="float32"), transformed_param_57: R.Tensor((512,), dtype="float32"), transformed_param_58: R.Tensor((512,), dtype="float32"), transformed_param_59: R.Tensor((512, 512, 3, 3), dtype="float32"), transformed_param_60: R.Tensor((256, 512, 3, 3), dtype="float32"), transformed_param_61: R.Tensor((256, 256, 3, 3), dtype="float32"), transformed_param_62: R.Tensor((256, 512, 1, 1), dtype="float32"), transformed_param_63: R.Tensor((512,), dtype="float32"), transformed_param_64: R.Tensor((512,), dtype="float32"), transformed_param_65: R.Tensor((256,), dtype="float32"), transformed_param_66: R.Tensor((256,), dtype="float32"), transformed_param_67: R.Tensor((256, 256, 3, 3), dtype="float32"), transformed_param_68: R.Tensor((256, 256, 3, 3), dtype="float32"), transformed_param_69: R.Tensor((256,), dtype="float32"), transformed_param_70: R.Tensor((256,), dtype="float32"), transformed_param_71: R.Tensor((256,), dtype="float32"), transformed_param_72: R.Tensor((256,), dtype="float32"), transformed_param_73: R.Tensor((256, 256, 3, 3), dtype="float32"), transformed_param_74: R.Tensor((256, 256, 3, 3), dtype="float32"), transformed_param_75: R.Tensor((256,), dtype="float32"), transformed_param_76: R.Tensor((256,), dtype="float32"), transformed_param_77: R.Tensor((256,), dtype="float32"), transformed_param_78: R.Tensor((256,), dtype="float32"), transformed_param_79: R.Tensor((256, 256, 3, 3), dtype="float32"), transformed_param_80: R.Tensor((128, 256, 3, 3), dtype="float32"), transformed_param_81: R.Tensor((128, 128, 3, 3), dtype="float32"), transformed_param_82: R.Tensor((128, 256, 1, 1), dtype="float32"), transformed_param_83: R.Tensor((256,), dtype="float32"), transformed_param_84: R.Tensor((256,), dtype="float32"), transformed_param_85: R.Tensor((128,), dtype="float32"), transformed_param_86: R.Tensor((128,), dtype="float32"), transformed_param_87: R.Tensor((128, 128, 3, 3), dtype="float32"), transformed_param_88: R.Tensor((128, 128, 3, 3), dtype="float32"), transformed_param_89: R.Tensor((128,), dtype="float32"), transformed_param_90: R.Tensor((128,), dtype="float32"), transformed_param_91: R.Tensor((128,), dtype="float32"), transformed_param_92: R.Tensor((128,), dtype="float32"), transformed_param_93: R.Tensor((128, 128, 3, 3), dtype="float32"), transformed_param_94: R.Tensor((128, 128, 3, 3), dtype="float32"), transformed_param_95: R.Tensor((128,), dtype="float32"), transformed_param_96: R.Tensor((128,), dtype="float32"), transformed_param_97: R.Tensor((128,), dtype="float32"), transformed_param_98: R.Tensor((128,), dtype="float32"), transformed_param_99: R.Tensor((4, 4, 1, 1), dtype="float32"), transformed_param_100: R.Tensor((1, 4, 1, 1), dtype="float32"), transformed_param_101: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_102: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_103: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_104: R.Tensor((512, 512), dtype="float32"), transformed_param_105: R.Tensor((512, 512), dtype="float32"), transformed_param_106: R.Tensor((512, 512), dtype="float32"), transformed_param_107: R.Tensor((512, 512), dtype="float32"), transformed_param_108: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_109: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_110: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_111: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_112: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_113: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_114: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_115: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_116: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_117: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_118: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_119: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_120: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_121: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_122: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_123: R.Tensor((1, 512, 1, 1), dtype="float32"), transformed_param_124: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_125: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_126: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_127: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_128: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_129: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_130: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_131: R.Tensor((1, 256, 1, 1), dtype="float32"), transformed_param_132: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_133: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_134: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_135: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_136: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_137: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_138: R.Tensor((1, 128, 1, 1), dtype="float32"), transformed_param_139: R.Tensor((1, 3, 1, 1), dtype="float32")) -> R.Tensor((1, 512, 512, 3), dtype="float32"):
        R.func_attr({"global_symbol": "main", "num_input": 1})
        cls = Module
        with R.dataflow():
            lv = R.call_tir(cls.multiply4, (inp_0,), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
            lv196: R.Tensor((4, 4, 1, 1), dtype="float32") = transformed_param_99
            lv197: R.Tensor((1, 4, 1, 1), dtype="float32") = transformed_param_100
            lv_1 = R.call_tir(cls.fused_conv2d_add1, (lv, lv196, lv197), out_sinfo=R.Tensor((1, 4, 64, 64), dtype="float32"))
            lv198: R.Tensor((512, 4, 3, 3), dtype="float32") = transformed_param_0
            lv199: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_101
            lv1 = R.call_tir(cls.fused_conv2d1_add2, (lv_1, lv198, lv199), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv200: R.Tensor((512,), dtype="float32") = transformed_param_13
            lv201: R.Tensor((512,), dtype="float32") = transformed_param_12
            lv2 = R.call_tir(cls.fused_group_norm_silu, (lv1, lv200, lv201), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv202: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_10
            lv203: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_102
            lv3 = R.call_tir(cls.fused_conv2d2_add2, (lv2, lv202, lv203), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv204: R.Tensor((512,), dtype="float32") = transformed_param_15
            lv205: R.Tensor((512,), dtype="float32") = transformed_param_14
            lv4 = R.call_tir(cls.fused_group_norm_silu, (lv3, lv204, lv205), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv206: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_11
            lv207: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_103
            lv5 = R.call_tir(cls.fused_conv2d2_add2_add3_divide3, (lv4, lv206, lv207, lv1), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv6 = R.call_tir(cls.fused_reshape2_transpose_transpose1, (lv5,), out_sinfo=R.Tensor((1, 512, 4096), dtype="float32"))
            lv208: R.Tensor((512,), dtype="float32") = transformed_param_5
            lv209: R.Tensor((512,), dtype="float32") = transformed_param_4
            lv22 = R.call_tir(cls.group_norm1, (lv6, lv208, lv209), out_sinfo=R.Tensor((1, 512, 4096), dtype="float32"))
            lv23 = R.call_tir(cls.transpose, (lv22,), out_sinfo=R.Tensor((1, 4096, 512), dtype="float32"))
            lv210: R.Tensor((512, 512), dtype="float32") = transformed_param_104
            lv211: R.Tensor((512,), dtype="float32") = transformed_param_8
            lv7 = R.call_tir(cls.fused_matmul_add4, (lv23, lv210, lv211), out_sinfo=R.Tensor((1, 4096, 512), dtype="float32"))
            lv212: R.Tensor((512, 512), dtype="float32") = transformed_param_105
            lv213: R.Tensor((512,), dtype="float32") = transformed_param_6
            lv8 = R.call_tir(cls.fused_matmul_add4, (lv23, lv212, lv213), out_sinfo=R.Tensor((1, 4096, 512), dtype="float32"))
            lv214: R.Tensor((512, 512), dtype="float32") = transformed_param_106
            lv215: R.Tensor((512,), dtype="float32") = transformed_param_9
            lv9 = R.call_tir(cls.fused_matmul_add4, (lv23, lv214, lv215), out_sinfo=R.Tensor((1, 4096, 512), dtype="float32"))
            lv10 = R.call_tir(cls.fused_reshape3_transpose3, (lv7,), out_sinfo=R.Tensor((1, 1, 4096, 512), dtype="float32"))
            lv11 = R.call_tir(cls.fused_reshape3_transpose3_transpose4, (lv8,), out_sinfo=R.Tensor((1, 1, 512, 4096), dtype="float32"))
            lv12 = R.call_tir(cls.fused_reshape3_transpose3, (lv9,), out_sinfo=R.Tensor((1, 1, 4096, 512), dtype="float32"))
            lv13 = R.call_tir(cls.fused_matmul1_multiply5, (lv10, lv11, R.const(0.044194173067808151, "float32")), out_sinfo=R.Tensor((1, 1, 4096, 4096), dtype="float32"))
            lv44 = R.call_tir(cls.softmax, (lv13,), out_sinfo=R.Tensor((1, 1, 4096, 4096), dtype="float32"))
            lv45 = R.call_tir(cls.matmul2, (lv44, lv12), out_sinfo=R.Tensor((1, 1, 4096, 512), dtype="float32"))
            lv14 = R.call_tir(cls.fused_transpose5_reshape4, (lv45,), out_sinfo=R.Tensor((1, 4096, 512), dtype="float32"))
            lv216: R.Tensor((512, 512), dtype="float32") = transformed_param_107
            lv217: R.Tensor((512,), dtype="float32") = transformed_param_7
            lv15 = R.call_tir(cls.fused_matmul_add4, (lv14, lv216, lv217), out_sinfo=R.Tensor((1, 4096, 512), dtype="float32"))
            lv16 = R.call_tir(cls.fused_transpose1_reshape5_add3_divide3, (lv15, lv5), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv218: R.Tensor((512,), dtype="float32") = transformed_param_19
            lv219: R.Tensor((512,), dtype="float32") = transformed_param_18
            lv17 = R.call_tir(cls.fused_group_norm_silu, (lv16, lv218, lv219), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv220: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_16
            lv221: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_108
            lv18 = R.call_tir(cls.fused_conv2d2_add2, (lv17, lv220, lv221), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv222: R.Tensor((512,), dtype="float32") = transformed_param_21
            lv223: R.Tensor((512,), dtype="float32") = transformed_param_20
            lv19 = R.call_tir(cls.fused_group_norm_silu, (lv18, lv222, lv223), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv224: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_17
            lv225: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_109
            lv20 = R.call_tir(cls.fused_conv2d2_add2_add3_divide3_divide3, (lv19, lv224, lv225, lv16), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv226: R.Tensor((512,), dtype="float32") = transformed_param_25
            lv227: R.Tensor((512,), dtype="float32") = transformed_param_24
            lv21 = R.call_tir(cls.fused_group_norm_silu, (lv20, lv226, lv227), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv228: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_22
            lv229: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_110
            lv22_1 = R.call_tir(cls.fused_conv2d2_add2, (lv21, lv228, lv229), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv230: R.Tensor((512,), dtype="float32") = transformed_param_27
            lv231: R.Tensor((512,), dtype="float32") = transformed_param_26
            lv23_1 = R.call_tir(cls.fused_group_norm_silu, (lv22_1, lv230, lv231), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv232: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_23
            lv233: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_111
            lv24 = R.call_tir(cls.fused_conv2d2_add2_add3_divide3, (lv23_1, lv232, lv233, lv20), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv234: R.Tensor((512,), dtype="float32") = transformed_param_31
            lv235: R.Tensor((512,), dtype="float32") = transformed_param_30
            lv25 = R.call_tir(cls.fused_group_norm_silu, (lv24, lv234, lv235), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv236: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_28
            lv237: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_112
            lv26 = R.call_tir(cls.fused_conv2d2_add2, (lv25, lv236, lv237), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv238: R.Tensor((512,), dtype="float32") = transformed_param_33
            lv239: R.Tensor((512,), dtype="float32") = transformed_param_32
            lv27 = R.call_tir(cls.fused_group_norm_silu, (lv26, lv238, lv239), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv240: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_29
            lv241: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_113
            lv28 = R.call_tir(cls.fused_conv2d2_add2_add3_divide3, (lv27, lv240, lv241, lv24), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv242: R.Tensor((512,), dtype="float32") = transformed_param_37
            lv243: R.Tensor((512,), dtype="float32") = transformed_param_36
            lv29 = R.call_tir(cls.fused_group_norm_silu, (lv28, lv242, lv243), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv244: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_34
            lv245: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_114
            lv30 = R.call_tir(cls.fused_conv2d2_add2, (lv29, lv244, lv245), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv246: R.Tensor((512,), dtype="float32") = transformed_param_39
            lv247: R.Tensor((512,), dtype="float32") = transformed_param_38
            lv31 = R.call_tir(cls.fused_group_norm_silu, (lv30, lv246, lv247), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv248: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_35
            lv249: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_115
            lv32 = R.call_tir(cls.fused_conv2d2_add2_add3_divide3, (lv31, lv248, lv249, lv28), out_sinfo=R.Tensor((1, 512, 64, 64), dtype="float32"))
            lv104 = R.call_tir(cls.resize2d, (lv32,), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv250: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_40
            lv251: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_116
            lv33 = R.call_tir(cls.fused_conv2d3_add5, (lv104, lv250, lv251), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv252: R.Tensor((512,), dtype="float32") = transformed_param_44
            lv253: R.Tensor((512,), dtype="float32") = transformed_param_43
            lv34 = R.call_tir(cls.fused_group_norm2_silu1, (lv33, lv252, lv253), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv254: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_41
            lv255: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_117
            lv35 = R.call_tir(cls.fused_conv2d3_add5, (lv34, lv254, lv255), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv256: R.Tensor((512,), dtype="float32") = transformed_param_46
            lv257: R.Tensor((512,), dtype="float32") = transformed_param_45
            lv36 = R.call_tir(cls.fused_group_norm2_silu1, (lv35, lv256, lv257), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv258: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_42
            lv259: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_118
            lv37 = R.call_tir(cls.fused_conv2d3_add5_add6_divide5, (lv36, lv258, lv259, lv33), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv260: R.Tensor((512,), dtype="float32") = transformed_param_50
            lv261: R.Tensor((512,), dtype="float32") = transformed_param_49
            lv38 = R.call_tir(cls.fused_group_norm2_silu1, (lv37, lv260, lv261), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv262: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_47
            lv263: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_119
            lv39 = R.call_tir(cls.fused_conv2d3_add5, (lv38, lv262, lv263), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv264: R.Tensor((512,), dtype="float32") = transformed_param_52
            lv265: R.Tensor((512,), dtype="float32") = transformed_param_51
            lv40 = R.call_tir(cls.fused_group_norm2_silu1, (lv39, lv264, lv265), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv266: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_48
            lv267: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_120
            lv41 = R.call_tir(cls.fused_conv2d3_add5_add6_divide5, (lv40, lv266, lv267, lv37), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv268: R.Tensor((512,), dtype="float32") = transformed_param_56
            lv269: R.Tensor((512,), dtype="float32") = transformed_param_55
            lv42 = R.call_tir(cls.fused_group_norm2_silu1, (lv41, lv268, lv269), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv270: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_53
            lv271: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_121
            lv43 = R.call_tir(cls.fused_conv2d3_add5, (lv42, lv270, lv271), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv272: R.Tensor((512,), dtype="float32") = transformed_param_58
            lv273: R.Tensor((512,), dtype="float32") = transformed_param_57
            lv44_1 = R.call_tir(cls.fused_group_norm2_silu1, (lv43, lv272, lv273), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv274: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_54
            lv275: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_122
            lv45_1 = R.call_tir(cls.fused_conv2d3_add5_add6_divide5, (lv44_1, lv274, lv275, lv41), out_sinfo=R.Tensor((1, 512, 128, 128), dtype="float32"))
            lv144 = R.call_tir(cls.resize2d1, (lv45_1,), out_sinfo=R.Tensor((1, 512, 256, 256), dtype="float32"))
            lv276: R.Tensor((512, 512, 3, 3), dtype="float32") = transformed_param_59
            lv277: R.Tensor((1, 512, 1, 1), dtype="float32") = transformed_param_123
            lv46 = R.call_tir(cls.fused_conv2d4_add7, (lv144, lv276, lv277), out_sinfo=R.Tensor((1, 512, 256, 256), dtype="float32"))
            lv278: R.Tensor((512,), dtype="float32") = transformed_param_64
            lv279: R.Tensor((512,), dtype="float32") = transformed_param_63
            lv47 = R.call_tir(cls.fused_group_norm3_silu2, (lv46, lv278, lv279), out_sinfo=R.Tensor((1, 512, 256, 256), dtype="float32"))
            lv280: R.Tensor((256, 512, 3, 3), dtype="float32") = transformed_param_60
            lv281: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_124
            lv48 = R.call_tir(cls.fused_conv2d5_add8, (lv47, lv280, lv281), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv282: R.Tensor((256,), dtype="float32") = transformed_param_66
            lv283: R.Tensor((256,), dtype="float32") = transformed_param_65
            lv49 = R.call_tir(cls.fused_group_norm4_silu3, (lv48, lv282, lv283), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv284: R.Tensor((256, 512, 1, 1), dtype="float32") = transformed_param_62
            lv285: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_126
            lv50 = R.call_tir(cls.fused_conv2d7_add8, (lv46, lv284, lv285), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv286: R.Tensor((256, 256, 3, 3), dtype="float32") = transformed_param_61
            lv287: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_125
            lv51 = R.call_tir(cls.fused_conv2d6_add8_add9_divide6, (lv49, lv286, lv287, lv50), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv288: R.Tensor((256,), dtype="float32") = transformed_param_70
            lv289: R.Tensor((256,), dtype="float32") = transformed_param_69
            lv52 = R.call_tir(cls.fused_group_norm4_silu3, (lv51, lv288, lv289), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv290: R.Tensor((256, 256, 3, 3), dtype="float32") = transformed_param_67
            lv291: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_127
            lv53 = R.call_tir(cls.fused_conv2d6_add8, (lv52, lv290, lv291), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv292: R.Tensor((256,), dtype="float32") = transformed_param_72
            lv293: R.Tensor((256,), dtype="float32") = transformed_param_71
            lv54 = R.call_tir(cls.fused_group_norm4_silu3, (lv53, lv292, lv293), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv294: R.Tensor((256, 256, 3, 3), dtype="float32") = transformed_param_68
            lv295: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_128
            lv55 = R.call_tir(cls.fused_conv2d6_add8_add9_divide6, (lv54, lv294, lv295, lv51), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv296: R.Tensor((256,), dtype="float32") = transformed_param_76
            lv297: R.Tensor((256,), dtype="float32") = transformed_param_75
            lv56 = R.call_tir(cls.fused_group_norm4_silu3, (lv55, lv296, lv297), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv298: R.Tensor((256, 256, 3, 3), dtype="float32") = transformed_param_73
            lv299: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_129
            lv57 = R.call_tir(cls.fused_conv2d6_add8, (lv56, lv298, lv299), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv300: R.Tensor((256,), dtype="float32") = transformed_param_78
            lv301: R.Tensor((256,), dtype="float32") = transformed_param_77
            lv58 = R.call_tir(cls.fused_group_norm4_silu3, (lv57, lv300, lv301), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv302: R.Tensor((256, 256, 3, 3), dtype="float32") = transformed_param_74
            lv303: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_130
            lv59 = R.call_tir(cls.fused_conv2d6_add8_add9_divide6, (lv58, lv302, lv303, lv55), out_sinfo=R.Tensor((1, 256, 256, 256), dtype="float32"))
            lv187 = R.call_tir(cls.resize2d2, (lv59,), out_sinfo=R.Tensor((1, 256, 512, 512), dtype="float32"))
            lv304: R.Tensor((256, 256, 3, 3), dtype="float32") = transformed_param_79
            lv305: R.Tensor((1, 256, 1, 1), dtype="float32") = transformed_param_131
            lv60 = R.call_tir(cls.fused_conv2d8_add10, (lv187, lv304, lv305), out_sinfo=R.Tensor((1, 256, 512, 512), dtype="float32"))
            lv306: R.Tensor((256,), dtype="float32") = transformed_param_84
            lv307: R.Tensor((256,), dtype="float32") = transformed_param_83
            lv61 = R.call_tir(cls.fused_group_norm5_silu4, (lv60, lv306, lv307), out_sinfo=R.Tensor((1, 256, 512, 512), dtype="float32"))
            lv308: R.Tensor((128, 256, 3, 3), dtype="float32") = transformed_param_80
            lv309: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_132
            lv62 = R.call_tir(cls.fused_conv2d9_add11, (lv61, lv308, lv309), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv310: R.Tensor((128,), dtype="float32") = transformed_param_86
            lv311: R.Tensor((128,), dtype="float32") = transformed_param_85
            lv63 = R.call_tir(cls.fused_group_norm6_silu5, (lv62, lv310, lv311), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv312: R.Tensor((128, 256, 1, 1), dtype="float32") = transformed_param_82
            lv313: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_134
            lv64 = R.call_tir(cls.fused_conv2d11_add11, (lv60, lv312, lv313), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv314: R.Tensor((128, 128, 3, 3), dtype="float32") = transformed_param_81
            lv315: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_133
            lv65 = R.call_tir(cls.fused_conv2d10_add11_add12_divide7, (lv63, lv314, lv315, lv64), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv316: R.Tensor((128,), dtype="float32") = transformed_param_90
            lv317: R.Tensor((128,), dtype="float32") = transformed_param_89
            lv66 = R.call_tir(cls.fused_group_norm6_silu5, (lv65, lv316, lv317), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv318: R.Tensor((128, 128, 3, 3), dtype="float32") = transformed_param_87
            lv319: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_135
            lv67 = R.call_tir(cls.fused_conv2d10_add11, (lv66, lv318, lv319), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv320: R.Tensor((128,), dtype="float32") = transformed_param_92
            lv321: R.Tensor((128,), dtype="float32") = transformed_param_91
            lv68 = R.call_tir(cls.fused_group_norm6_silu5, (lv67, lv320, lv321), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv322: R.Tensor((128, 128, 3, 3), dtype="float32") = transformed_param_88
            lv323: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_136
            lv69 = R.call_tir(cls.fused_conv2d10_add11_add12_divide7, (lv68, lv322, lv323, lv65), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv324: R.Tensor((128,), dtype="float32") = transformed_param_96
            lv325: R.Tensor((128,), dtype="float32") = transformed_param_95
            lv70 = R.call_tir(cls.fused_group_norm6_silu5, (lv69, lv324, lv325), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv326: R.Tensor((128, 128, 3, 3), dtype="float32") = transformed_param_93
            lv327: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_137
            lv71 = R.call_tir(cls.fused_conv2d10_add11, (lv70, lv326, lv327), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv328: R.Tensor((128,), dtype="float32") = transformed_param_98
            lv329: R.Tensor((128,), dtype="float32") = transformed_param_97
            lv72 = R.call_tir(cls.fused_group_norm6_silu5, (lv71, lv328, lv329), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv330: R.Tensor((128, 128, 3, 3), dtype="float32") = transformed_param_94
            lv331: R.Tensor((1, 128, 1, 1), dtype="float32") = transformed_param_138
            lv73 = R.call_tir(cls.fused_conv2d10_add11_add12_divide7, (lv72, lv330, lv331, lv69), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv332: R.Tensor((128,), dtype="float32") = transformed_param_2
            lv333: R.Tensor((128,), dtype="float32") = transformed_param_1
            lv74 = R.call_tir(cls.fused_group_norm6_silu5, (lv73, lv332, lv333), out_sinfo=R.Tensor((1, 128, 512, 512), dtype="float32"))
            lv334: R.Tensor((3, 128, 3, 3), dtype="float32") = transformed_param_3
            lv335: R.Tensor((1, 3, 1, 1), dtype="float32") = transformed_param_139
            lv75 = R.call_tir(cls.fused_conv2d12_add13_divide8_add14_tir_clip, (lv74, lv334, lv335), out_sinfo=R.Tensor((1, 3, 512, 512), dtype="float32"))
            lv76 = R.call_tir(cls.fused_transpose6_multiply6_tir_round, (lv75,), out_sinfo=R.Tensor((1, 512, 512, 3), dtype="float32"))
            gv: R.Tensor((1, 512, 512, 3), dtype="float32") = lv76
            R.output(gv)
        return gv
