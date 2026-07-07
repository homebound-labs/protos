from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceAuthTokenRequest(_message.Message):
    __slots__ = ("device_id", "device_secret")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SECRET_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    device_secret: str
    def __init__(self, device_id: _Optional[str] = ..., device_secret: _Optional[str] = ...) -> None: ...

class DeviceAuthTokenResponse(_message.Message):
    __slots__ = ("access_token", "token_type", "expires_in")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    token_type: str
    expires_in: int
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...
