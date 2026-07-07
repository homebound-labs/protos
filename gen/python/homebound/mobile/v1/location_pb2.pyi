from google.protobuf import timestamp_pb2 as _timestamp_pb2
from homebound.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCATION_SOURCE_UNSPECIFIED: _ClassVar[LocationSource]
    LOCATION_SOURCE_PHONE: _ClassVar[LocationSource]
    LOCATION_SOURCE_DEVICE: _ClassVar[LocationSource]
LOCATION_SOURCE_UNSPECIFIED: LocationSource
LOCATION_SOURCE_PHONE: LocationSource
LOCATION_SOURCE_DEVICE: LocationSource

class PhoneLocationUpdate(_message.Message):
    __slots__ = ("location", "altitude_meters", "speed_meters_per_second", "heading_degrees", "battery", "captured_at")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    SPEED_METERS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    location: _common_pb2.GeoPoint
    altitude_meters: float
    speed_meters_per_second: float
    heading_degrees: float
    battery: _common_pb2.BatteryStatus
    captured_at: _timestamp_pb2.Timestamp
    def __init__(self, location: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., altitude_meters: _Optional[float] = ..., speed_meters_per_second: _Optional[float] = ..., heading_degrees: _Optional[float] = ..., battery: _Optional[_Union[_common_pb2.BatteryStatus, _Mapping]] = ..., captured_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LocationPoint(_message.Message):
    __slots__ = ("id", "user_id", "device_id", "source", "location", "altitude_meters", "speed_meters_per_second", "heading_degrees", "battery", "captured_at", "received_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    SPEED_METERS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    device_id: str
    source: LocationSource
    location: _common_pb2.GeoPoint
    altitude_meters: float
    speed_meters_per_second: float
    heading_degrees: float
    battery: _common_pb2.BatteryStatus
    captured_at: _timestamp_pb2.Timestamp
    received_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., source: _Optional[_Union[LocationSource, str]] = ..., location: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., altitude_meters: _Optional[float] = ..., speed_meters_per_second: _Optional[float] = ..., heading_degrees: _Optional[float] = ..., battery: _Optional[_Union[_common_pb2.BatteryStatus, _Mapping]] = ..., captured_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LatestLocationsResponse(_message.Message):
    __slots__ = ("phone", "device")
    PHONE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    phone: LocationPoint
    device: LocationPoint
    def __init__(self, phone: _Optional[_Union[LocationPoint, _Mapping]] = ..., device: _Optional[_Union[LocationPoint, _Mapping]] = ...) -> None: ...

class DeviceLatestLocationResponse(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: LocationPoint
    def __init__(self, location: _Optional[_Union[LocationPoint, _Mapping]] = ...) -> None: ...
