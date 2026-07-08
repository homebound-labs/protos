from google.protobuf import timestamp_pb2 as _timestamp_pb2
from homebound.common.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeartbeatRequest(_message.Message):
    __slots__ = ("status", "sent_at", "source")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    status: str
    sent_at: _timestamp_pb2.Timestamp
    source: _common_pb2.Source
    def __init__(self, status: _Optional[str] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[_Union[_common_pb2.Source, _Mapping]] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ("status", "device_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    device_id: str
    def __init__(self, status: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class SosAck(_message.Message):
    __slots__ = ("status", "device_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    device_id: str
    def __init__(self, status: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...
