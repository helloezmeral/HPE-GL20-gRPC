# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GL20.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GL20.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nGL20.proto\"2\n\x04GPIO\x12\x0c\n\x04PINx\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x08\x32\xe0\x01\n\x0bserviceGL20\x12$\n\x12\x64igitalWriteToggle\x12\x05.GPIO\x1a\x05.GPIO\"\x00\x12\'\n\x15\x64igitalWriteToggleAll\x12\x05.GPIO\x1a\x05.GPIO\"\x00\x12 \n\x0e\x64igitalReadAll\x12\x05.GPIO\x1a\x05.GPIO\"\x00\x12\x1d\n\x0b\x64igitalRead\x12\x05.GPIO\x1a\x05.GPIO\"\x00\x12\x1e\n\x0c\x64igitalWrite\x12\x05.GPIO\x1a\x05.GPIO\"\x00\x12!\n\x0f\x64igitalWriteAll\x12\x05.GPIO\x1a\x05.GPIO\"\x00\x62\x06proto3'
)




_GPIO = _descriptor.Descriptor(
  name='GPIO',
  full_name='GPIO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PINx', full_name='GPIO.PINx', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='GPIO.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='GPIO.level', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=14,
  serialized_end=64,
)

DESCRIPTOR.message_types_by_name['GPIO'] = _GPIO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GPIO = _reflection.GeneratedProtocolMessageType('GPIO', (_message.Message,), {
  'DESCRIPTOR' : _GPIO,
  '__module__' : 'GL20_pb2'
  # @@protoc_insertion_point(class_scope:GPIO)
  })
_sym_db.RegisterMessage(GPIO)



_SERVICEGL20 = _descriptor.ServiceDescriptor(
  name='serviceGL20',
  full_name='serviceGL20',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=67,
  serialized_end=291,
  methods=[
  _descriptor.MethodDescriptor(
    name='digitalWriteToggle',
    full_name='serviceGL20.digitalWriteToggle',
    index=0,
    containing_service=None,
    input_type=_GPIO,
    output_type=_GPIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='digitalWriteToggleAll',
    full_name='serviceGL20.digitalWriteToggleAll',
    index=1,
    containing_service=None,
    input_type=_GPIO,
    output_type=_GPIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='digitalReadAll',
    full_name='serviceGL20.digitalReadAll',
    index=2,
    containing_service=None,
    input_type=_GPIO,
    output_type=_GPIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='digitalRead',
    full_name='serviceGL20.digitalRead',
    index=3,
    containing_service=None,
    input_type=_GPIO,
    output_type=_GPIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='digitalWrite',
    full_name='serviceGL20.digitalWrite',
    index=4,
    containing_service=None,
    input_type=_GPIO,
    output_type=_GPIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='digitalWriteAll',
    full_name='serviceGL20.digitalWriteAll',
    index=5,
    containing_service=None,
    input_type=_GPIO,
    output_type=_GPIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEGL20)

DESCRIPTOR.services_by_name['serviceGL20'] = _SERVICEGL20

# @@protoc_insertion_point(module_scope)
