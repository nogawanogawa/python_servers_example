# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosine_similarity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63osine_similarity.proto\x12\ncosine_sim\"*\n\x10\x43osineSimRequest\x12\n\n\x02v1\x18\x01 \x01(\t\x12\n\n\x02v2\x18\x02 \x01(\t\"&\n\x11\x43osineSimResponse\x12\x11\n\tcosinesim\x18\x01 \x01(\x02\x32\x62\n\x10\x43osineSimService\x12N\n\x0f\x63\x61lc_cosine_sim\x12\x1c.cosine_sim.CosineSimRequest\x1a\x1d.cosine_sim.CosineSimResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosine_similarity_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COSINESIMREQUEST']._serialized_start=39
  _globals['_COSINESIMREQUEST']._serialized_end=81
  _globals['_COSINESIMRESPONSE']._serialized_start=83
  _globals['_COSINESIMRESPONSE']._serialized_end=121
  _globals['_COSINESIMSERVICE']._serialized_start=123
  _globals['_COSINESIMSERVICE']._serialized_end=221
# @@protoc_insertion_point(module_scope)