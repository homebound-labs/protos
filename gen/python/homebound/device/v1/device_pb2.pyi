from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

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
