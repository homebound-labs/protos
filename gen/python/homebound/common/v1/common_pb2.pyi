from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GeoPoint(_message.Message):
    __slots__ = ("latitude", "longitude", "accuracy_meters")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_METERS_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    accuracy_meters: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., accuracy_meters: _Optional[float] = ...) -> None: ...

class BatteryStatus(_message.Message):
    __slots__ = ("percent",)
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    percent: int
    def __init__(self, percent: _Optional[int] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("firmware_version", "hardware_profile")
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    firmware_version: str
    hardware_profile: str
    def __init__(self, firmware_version: _Optional[str] = ..., hardware_profile: _Optional[str] = ...) -> None: ...
