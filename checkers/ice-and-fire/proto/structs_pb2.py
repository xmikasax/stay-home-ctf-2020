# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='structs.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rstructs.proto\"\x17\n\x07\x43ontact\x12\x0c\n\x04text\x18\x01 \x01(\t\"*\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n\x0fRegisterRequest\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\x12\x13\n\x0b\x63oordinates\x18\x02 \x03(\x01\x12\x19\n\x07\x63ontact\x18\x03 \x01(\x0b\x32\x08.Contact\"#\n\x0cLoginRequest\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"\x1d\n\x06MyData\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"?\n\x05Match\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\x12\x18\n\x06secret\x18\x03 \x01(\x0b\x32\x08.Contact\"$\n\x08Response\x12\n\n\x02ok\x18\x02 \x01(\x08\x12\x0c\n\x04text\x18\x01 \x01(\tb\x06proto3'
)




_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Contact.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=17,
  serialized_end=40,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='User.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=42,
  serialized_end=84,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='RegisterRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='RegisterRequest.coordinates', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contact', full_name='RegisterRequest.contact', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=86,
  serialized_end=172,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='LoginRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=174,
  serialized_end=209,
)


_MYDATA = _descriptor.Descriptor(
  name='MyData',
  full_name='MyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='MyData.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=211,
  serialized_end=240,
)


_MATCH = _descriptor.Descriptor(
  name='Match',
  full_name='Match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Match.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='Match.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret', full_name='Match.secret', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=242,
  serialized_end=305,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Response.ok', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='Response.text', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=307,
  serialized_end=343,
)

_REGISTERREQUEST.fields_by_name['user'].message_type = _USER
_REGISTERREQUEST.fields_by_name['contact'].message_type = _CONTACT
_LOGINREQUEST.fields_by_name['user'].message_type = _USER
_MYDATA.fields_by_name['user'].message_type = _USER
_MATCH.fields_by_name['secret'].message_type = _CONTACT
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['MyData'] = _MYDATA
DESCRIPTOR.message_types_by_name['Match'] = _MATCH
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), {
  'DESCRIPTOR' : _CONTACT,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:Contact)
  })
_sym_db.RegisterMessage(Contact)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

MyData = _reflection.GeneratedProtocolMessageType('MyData', (_message.Message,), {
  'DESCRIPTOR' : _MYDATA,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:MyData)
  })
_sym_db.RegisterMessage(MyData)

Match = _reflection.GeneratedProtocolMessageType('Match', (_message.Message,), {
  'DESCRIPTOR' : _MATCH,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:Match)
  })
_sym_db.RegisterMessage(Match)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'structs_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)