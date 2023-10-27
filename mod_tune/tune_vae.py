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

mod = Module

def tune(mod: tvm.IRModule) -> None:
    from tvm import meta_schedule as ms

    ms.relax_integration.tune_relax(
        mod=mod,
        target=tvm.target.Target("apple/m1-gpu-restricted"),
        params={},
        builder=ms.builder.LocalBuilder(
            max_workers=5,
        ),
        runner=ms.runner.LocalRunner(),
        work_dir="log_db_tuning_vae",
        max_trials_global=19500,
        max_trials_per_task=500,
        strategy=ms.search_strategy.EvolutionarySearch(init_min_unmeasured=10, max_fail_count=20),
    )

tune(mod)