# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftelemetry.proto\"i\n\rDeviceMetrics\x12\x15\n\rbattery_level\x18\x01 \x01(\r\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x1b\n\x13\x63hannel_utilization\x18\x03 \x01(\x02\x12\x13\n\x0b\x61ir_util_tx\x18\x04 \x01(\x02\"\x9b\x01\n\x12\x45nvironmentMetrics\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x19\n\x11relative_humidity\x18\x02 \x01(\x02\x12\x1b\n\x13\x62\x61rometric_pressure\x18\x03 \x01(\x02\x12\x16\n\x0egas_resistance\x18\x04 \x01(\x02\x12\x0f\n\x07voltage\x18\x05 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x06 \x01(\x02\"\x82\x01\n\tTelemetry\x12\x0c\n\x04time\x18\x01 \x01(\x07\x12(\n\x0e\x64\x65vice_metrics\x18\x02 \x01(\x0b\x32\x0e.DeviceMetricsH\x00\x12\x32\n\x13\x65nvironment_metrics\x18\x03 \x01(\x0b\x32\x13.EnvironmentMetricsH\x00\x42\t\n\x07variant*\x86\x01\n\x13TelemetrySensorType\x12\x10\n\x0cSENSOR_UNSET\x10\x00\x12\n\n\x06\x42ME280\x10\x01\x12\n\n\x06\x42ME680\x10\x02\x12\x0b\n\x07MCP9808\x10\x03\x12\n\n\x06INA260\x10\x04\x12\n\n\x06INA219\x10\x05\x12\n\n\x06\x42MP280\x10\x06\x12\t\n\x05SHTC3\x10\x07\x12\t\n\x05LPS22\x10\x08\x42K\n\x13\x63om.geeksville.meshB\x0fTelemetryProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3')

_TELEMETRYSENSORTYPE = DESCRIPTOR.enum_types_by_name['TelemetrySensorType']
TelemetrySensorType = enum_type_wrapper.EnumTypeWrapper(_TELEMETRYSENSORTYPE)
SENSOR_UNSET = 0
BME280 = 1
BME680 = 2
MCP9808 = 3
INA260 = 4
INA219 = 5
BMP280 = 6
SHTC3 = 7
LPS22 = 8


_DEVICEMETRICS = DESCRIPTOR.message_types_by_name['DeviceMetrics']
_ENVIRONMENTMETRICS = DESCRIPTOR.message_types_by_name['EnvironmentMetrics']
_TELEMETRY = DESCRIPTOR.message_types_by_name['Telemetry']
DeviceMetrics = _reflection.GeneratedProtocolMessageType('DeviceMetrics', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEMETRICS,
  '__module__' : 'telemetry_pb2'
  # @@protoc_insertion_point(class_scope:DeviceMetrics)
  })
_sym_db.RegisterMessage(DeviceMetrics)

EnvironmentMetrics = _reflection.GeneratedProtocolMessageType('EnvironmentMetrics', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENTMETRICS,
  '__module__' : 'telemetry_pb2'
  # @@protoc_insertion_point(class_scope:EnvironmentMetrics)
  })
_sym_db.RegisterMessage(EnvironmentMetrics)

Telemetry = _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRY,
  '__module__' : 'telemetry_pb2'
  # @@protoc_insertion_point(class_scope:Telemetry)
  })
_sym_db.RegisterMessage(Telemetry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\017TelemetryProtosH\003Z!github.com/meshtastic/gomeshproto'
  _TELEMETRYSENSORTYPE._serialized_start=418
  _TELEMETRYSENSORTYPE._serialized_end=552
  _DEVICEMETRICS._serialized_start=19
  _DEVICEMETRICS._serialized_end=124
  _ENVIRONMENTMETRICS._serialized_start=127
  _ENVIRONMENTMETRICS._serialized_end=282
  _TELEMETRY._serialized_start=285
  _TELEMETRY._serialized_end=415
# @@protoc_insertion_point(module_scope)
