# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/koala_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/koala_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/settings/koala_settings.proto\x12\x13pogoprotos.settings\"G\n\rKoalaSettings\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x13\n\x0buse_sandbox\x18\x02 \x01(\x08\x12\x11\n\tuse_koala\x18\x03 \x01(\x08\x62\x06proto3')
)




_KOALASETTINGS = _descriptor.Descriptor(
  name='KoalaSettings',
  full_name='pogoprotos.settings.KoalaSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='pogoprotos.settings.KoalaSettings.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_sandbox', full_name='pogoprotos.settings.KoalaSettings.use_sandbox', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_koala', full_name='pogoprotos.settings.KoalaSettings.use_koala', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=65,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['KoalaSettings'] = _KOALASETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KoalaSettings = _reflection.GeneratedProtocolMessageType('KoalaSettings', (_message.Message,), dict(
  DESCRIPTOR = _KOALASETTINGS,
  __module__ = 'pogoprotos.settings.koala_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.KoalaSettings)
  ))
_sym_db.RegisterMessage(KoalaSettings)


# @@protoc_insertion_point(module_scope)
