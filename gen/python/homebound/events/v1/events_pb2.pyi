from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DistanceAlertEvent(_message.Message):
    __slots__ = ("alert_id", "user_id", "device_id", "severity", "distance_miles", "created_at")
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_MILES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    alert_id: str
    user_id: str
    device_id: str
    severity: str
    distance_miles: float
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, alert_id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., severity: _Optional[str] = ..., distance_miles: _Optional[float] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
