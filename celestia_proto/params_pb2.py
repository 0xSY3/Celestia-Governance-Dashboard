# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: params.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cparams.proto\x12\x15\x63osmos.params.v1beta1\"3\n\x12QueryParamsRequest\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"H\n\x13QueryParamsResponse\x12\x31\n\x05param\x18\x01 \x01(\x0b\x32\".cosmos.params.v1beta1.ParamChange\";\n\x0bParamChange\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t2j\n\x05Query\x12\x61\n\x06Params\x12).cosmos.params.v1beta1.QueryParamsRequest\x1a*.cosmos.params.v1beta1.QueryParamsResponse\"\x00\x42-Z+github.com/cosmos/cosmos-sdk/x/params/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/params/types'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=39
  _globals['_QUERYPARAMSREQUEST']._serialized_end=90
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=92
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=164
  _globals['_PARAMCHANGE']._serialized_start=166
  _globals['_PARAMCHANGE']._serialized_end=225
  _globals['_QUERY']._serialized_start=227
  _globals['_QUERY']._serialized_end=333
# @@protoc_insertion_point(module_scope)
