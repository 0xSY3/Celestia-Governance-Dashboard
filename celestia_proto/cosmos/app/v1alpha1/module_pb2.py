# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/app/v1alpha1/module.proto
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
    'cosmos/app/v1alpha1/module.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/app/v1alpha1/module.proto\x12\x13\x63osmos.app.v1alpha1\x1a google/protobuf/descriptor.proto\"\xa1\x01\n\x10ModuleDescriptor\x12\x11\n\tgo_import\x18\x01 \x01(\t\x12:\n\x0buse_package\x18\x02 \x03(\x0b\x32%.cosmos.app.v1alpha1.PackageReference\x12>\n\x10\x63\x61n_migrate_from\x18\x03 \x03(\x0b\x32$.cosmos.app.v1alpha1.MigrateFromInfo\"2\n\x10PackageReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\r\"!\n\x0fMigrateFromInfo\x12\x0e\n\x06module\x18\x01 \x01(\t:Y\n\x06module\x12\x1f.google.protobuf.MessageOptions\x18\x87\xe8\xa2\x1b \x01(\x0b\x32%.cosmos.app.v1alpha1.ModuleDescriptorB+Z)cosmossdk.io/depinject/appconfig/v1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.v1alpha1.module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)cosmossdk.io/depinject/appconfig/v1alpha1'
  _globals['_MODULEDESCRIPTOR']._serialized_start=92
  _globals['_MODULEDESCRIPTOR']._serialized_end=253
  _globals['_PACKAGEREFERENCE']._serialized_start=255
  _globals['_PACKAGEREFERENCE']._serialized_end=305
  _globals['_MIGRATEFROMINFO']._serialized_start=307
  _globals['_MIGRATEFROMINFO']._serialized_end=340
# @@protoc_insertion_point(module_scope)
