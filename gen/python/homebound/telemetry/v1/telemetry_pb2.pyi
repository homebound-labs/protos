import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from homebound.common.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TelemetryEvent(_message.Message):
    __slots__ = ("event_id", "recorded_at", "sequence", "location", "battery", "source", "signal_strength")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    recorded_at: _timestamp_pb2.Timestamp
    sequence: int
    location: _common_pb2.GeoPoint
    battery: _common_pb2.BatteryStatus
    source: _common_pb2.Source
    signal_strength: int
    def __init__(self, event_id: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sequence: _Optional[int] = ..., location: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., battery: _Optional[_Union[_common_pb2.BatteryStatus, _Mapping]] = ..., source: _Optional[_Union[_common_pb2.Source, _Mapping]] = ..., signal_strength: _Optional[int] = ...) -> None: ...

class TelemetryAck(_message.Message):
    __slots__ = ("accepted", "event_id", "server_received_at")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    event_id: str
    server_received_at: _timestamp_pb2.Timestamp
    def __init__(self, accepted: _Optional[bool] = ..., event_id: _Optional[str] = ..., server_received_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
