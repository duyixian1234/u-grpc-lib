# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: u_grpc_lib/demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='u_grpc_lib/demo.proto',
  package='demo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15u_grpc_lib/demo.proto\x12\x04\x64\x65mo\"\x18\n\x0bPlusRequest\x12\t\n\x01x\x18\x01 \x03(\x05\"?\n\x0cPlusResponse\x12\x10\n\x08msg_code\x18\x01 \x01(\x05\x12\x10\n\x08msg_info\x18\x02 \x01(\t\x12\x0b\n\x03sum\x18\x03 \x01(\x05\x32\x37\n\x04\x44\x65mo\x12/\n\x04Plus\x12\x11.demo.PlusRequest\x1a\x12.demo.PlusResponse\"\x00\x62\x06proto3'
)




_PLUSREQUEST = _descriptor.Descriptor(
  name='PlusRequest',
  full_name='demo.PlusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='demo.PlusRequest.x', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=55,
)


_PLUSRESPONSE = _descriptor.Descriptor(
  name='PlusResponse',
  full_name='demo.PlusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_code', full_name='demo.PlusResponse.msg_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_info', full_name='demo.PlusResponse.msg_info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sum', full_name='demo.PlusResponse.sum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['PlusRequest'] = _PLUSREQUEST
DESCRIPTOR.message_types_by_name['PlusResponse'] = _PLUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlusRequest = _reflection.GeneratedProtocolMessageType('PlusRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUSREQUEST,
  '__module__' : 'u_grpc_lib.demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.PlusRequest)
  })
_sym_db.RegisterMessage(PlusRequest)

PlusResponse = _reflection.GeneratedProtocolMessageType('PlusResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUSRESPONSE,
  '__module__' : 'u_grpc_lib.demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.PlusResponse)
  })
_sym_db.RegisterMessage(PlusResponse)



_DEMO = _descriptor.ServiceDescriptor(
  name='Demo',
  full_name='demo.Demo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=122,
  serialized_end=177,
  methods=[
  _descriptor.MethodDescriptor(
    name='Plus',
    full_name='demo.Demo.Plus',
    index=0,
    containing_service=None,
    input_type=_PLUSREQUEST,
    output_type=_PLUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEMO)

DESCRIPTOR.services_by_name['Demo'] = _DEMO

# @@protoc_insertion_point(module_scope)
