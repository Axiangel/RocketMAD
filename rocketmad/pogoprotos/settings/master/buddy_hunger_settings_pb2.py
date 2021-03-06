# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/buddy_hunger_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/buddy_hunger_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/settings/master/buddy_hunger_settings.proto\x12\x1apogoprotos.settings.master\"\xc8\x01\n\x13\x42uddyHungerSettings\x12+\n#num_hunger_points_required_for_full\x18\x01 \x01(\x05\x12\x1f\n\x17\x64\x65\x63\x61y_points_per_bucket\x18\x02 \x01(\x05\x12\x1f\n\x17milliseconds_per_bucket\x18\x03 \x01(\x03\x12\x1c\n\x14\x63ooldown_duration_ms\x18\x04 \x01(\x03\x12$\n\x1c\x64\x65\x63\x61y_duration_after_full_ms\x18\x05 \x01(\x03\x62\x06proto3')
)




_BUDDYHUNGERSETTINGS = _descriptor.Descriptor(
  name='BuddyHungerSettings',
  full_name='pogoprotos.settings.master.BuddyHungerSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_hunger_points_required_for_full', full_name='pogoprotos.settings.master.BuddyHungerSettings.num_hunger_points_required_for_full', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decay_points_per_bucket', full_name='pogoprotos.settings.master.BuddyHungerSettings.decay_points_per_bucket', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milliseconds_per_bucket', full_name='pogoprotos.settings.master.BuddyHungerSettings.milliseconds_per_bucket', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cooldown_duration_ms', full_name='pogoprotos.settings.master.BuddyHungerSettings.cooldown_duration_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decay_duration_after_full_ms', full_name='pogoprotos.settings.master.BuddyHungerSettings.decay_duration_after_full_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=87,
  serialized_end=287,
)

DESCRIPTOR.message_types_by_name['BuddyHungerSettings'] = _BUDDYHUNGERSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyHungerSettings = _reflection.GeneratedProtocolMessageType('BuddyHungerSettings', (_message.Message,), dict(
  DESCRIPTOR = _BUDDYHUNGERSETTINGS,
  __module__ = 'pogoprotos.settings.master.buddy_hunger_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BuddyHungerSettings)
  ))
_sym_db.RegisterMessage(BuddyHungerSettings)


# @@protoc_insertion_point(module_scope)
