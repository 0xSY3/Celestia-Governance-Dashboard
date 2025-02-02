# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/app/runtime/v2/module.proto
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
    'cosmos/app/runtime/v2/module.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/app/runtime/v2/module.proto\x12\x15\x63osmos.app.runtime.v2\x1a cosmos/app/v1alpha1/module.proto\"\x88\x03\n\x06Module\x12\x10\n\x08\x61pp_name\x18\x01 \x01(\t\x12\x14\n\x0cpre_blockers\x18\x02 \x03(\t\x12\x16\n\x0e\x62\x65gin_blockers\x18\x03 \x03(\t\x12\x14\n\x0c\x65nd_blockers\x18\x04 \x03(\t\x12\x15\n\rtx_validators\x18\x05 \x03(\t\x12\x14\n\x0cinit_genesis\x18\x06 \x03(\t\x12\x16\n\x0e\x65xport_genesis\x18\x07 \x03(\t\x12\x18\n\x10order_migrations\x18\x08 \x03(\t\x12\x34\n\ngas_config\x18\t \x01(\x0b\x32 .cosmos.app.runtime.v2.GasConfig\x12\x42\n\x13override_store_keys\x18\n \x03(\x0b\x32%.cosmos.app.runtime.v2.StoreKeyConfig\x12\x17\n\x0fskip_store_keys\x18\x0b \x03(\t:6\xba\xc0\x96\xda\x01\x30\n\x17\x63osmossdk.io/runtime/v2\x12\x15\n\x13\x63osmos.app.v1alpha1\"a\n\tGasConfig\x12\x1d\n\x15validate_tx_gas_limit\x18\x01 \x01(\x04\x12\x17\n\x0fquery_gas_limit\x18\x02 \x01(\x04\x12\x1c\n\x14simulation_gas_limit\x18\x03 \x01(\x04\";\n\x0eStoreKeyConfig\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x14\n\x0ckv_store_key\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.runtime.v2.module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MODULE']._loaded_options = None
  _globals['_MODULE']._serialized_options = b'\272\300\226\332\0010\n\027cosmossdk.io/runtime/v2\022\025\n\023cosmos.app.v1alpha1'
  _globals['_MODULE']._serialized_start=96
  _globals['_MODULE']._serialized_end=488
  _globals['_GASCONFIG']._serialized_start=490
  _globals['_GASCONFIG']._serialized_end=587
  _globals['_STOREKEYCONFIG']._serialized_start=589
  _globals['_STOREKEYCONFIG']._serialized_end=648
# @@protoc_insertion_point(module_scope)
