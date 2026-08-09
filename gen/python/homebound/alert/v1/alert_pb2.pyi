import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertSignalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_SIGNAL_TYPE_UNSPECIFIED: _ClassVar[AlertSignalType]
    ALERT_SIGNAL_TYPE_DISTANCE_THRESHOLD: _ClassVar[AlertSignalType]
    ALERT_SIGNAL_TYPE_DANGER_ZONE_DWELL: _ClassVar[AlertSignalType]
    ALERT_SIGNAL_TYPE_STALE_LOCATION: _ClassVar[AlertSignalType]
    ALERT_SIGNAL_TYPE_LOW_GPS_ACCURACY: _ClassVar[AlertSignalType]

class AlertConfidenceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_CONFIDENCE_LEVEL_UNSPECIFIED: _ClassVar[AlertConfidenceLevel]
    ALERT_CONFIDENCE_LEVEL_LOW: _ClassVar[AlertConfidenceLevel]
    ALERT_CONFIDENCE_LEVEL_MEDIUM: _ClassVar[AlertConfidenceLevel]
    ALERT_CONFIDENCE_LEVEL_HIGH: _ClassVar[AlertConfidenceLevel]

class NotificationChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CHANNEL_UNSPECIFIED: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_PUSH: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_EMAIL: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_SMS: _ClassVar[NotificationChannel]

class NotificationDeliveryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_DELIVERY_STATUS_UNSPECIFIED: _ClassVar[NotificationDeliveryStatus]
    NOTIFICATION_DELIVERY_STATUS_SENT: _ClassVar[NotificationDeliveryStatus]
    NOTIFICATION_DELIVERY_STATUS_DELIVERED: _ClassVar[NotificationDeliveryStatus]
    NOTIFICATION_DELIVERY_STATUS_FAILED: _ClassVar[NotificationDeliveryStatus]
    NOTIFICATION_DELIVERY_STATUS_SKIPPED: _ClassVar[NotificationDeliveryStatus]

class NotificationRecipientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_RECIPIENT_TYPE_UNSPECIFIED: _ClassVar[NotificationRecipientType]
    NOTIFICATION_RECIPIENT_TYPE_OWNER: _ClassVar[NotificationRecipientType]
    NOTIFICATION_RECIPIENT_TYPE_NOTIFICATION_RECIPIENT: _ClassVar[NotificationRecipientType]
ALERT_SIGNAL_TYPE_UNSPECIFIED: AlertSignalType
ALERT_SIGNAL_TYPE_DISTANCE_THRESHOLD: AlertSignalType
ALERT_SIGNAL_TYPE_DANGER_ZONE_DWELL: AlertSignalType
ALERT_SIGNAL_TYPE_STALE_LOCATION: AlertSignalType
ALERT_SIGNAL_TYPE_LOW_GPS_ACCURACY: AlertSignalType
ALERT_CONFIDENCE_LEVEL_UNSPECIFIED: AlertConfidenceLevel
ALERT_CONFIDENCE_LEVEL_LOW: AlertConfidenceLevel
ALERT_CONFIDENCE_LEVEL_MEDIUM: AlertConfidenceLevel
ALERT_CONFIDENCE_LEVEL_HIGH: AlertConfidenceLevel
NOTIFICATION_CHANNEL_UNSPECIFIED: NotificationChannel
NOTIFICATION_CHANNEL_PUSH: NotificationChannel
NOTIFICATION_CHANNEL_EMAIL: NotificationChannel
NOTIFICATION_CHANNEL_SMS: NotificationChannel
NOTIFICATION_DELIVERY_STATUS_UNSPECIFIED: NotificationDeliveryStatus
NOTIFICATION_DELIVERY_STATUS_SENT: NotificationDeliveryStatus
NOTIFICATION_DELIVERY_STATUS_DELIVERED: NotificationDeliveryStatus
NOTIFICATION_DELIVERY_STATUS_FAILED: NotificationDeliveryStatus
NOTIFICATION_DELIVERY_STATUS_SKIPPED: NotificationDeliveryStatus
NOTIFICATION_RECIPIENT_TYPE_UNSPECIFIED: NotificationRecipientType
NOTIFICATION_RECIPIENT_TYPE_OWNER: NotificationRecipientType
NOTIFICATION_RECIPIENT_TYPE_NOTIFICATION_RECIPIENT: NotificationRecipientType

class AlertSignal(_message.Message):
    __slots__ = ("signal_type", "weight", "detail")
    SIGNAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    signal_type: AlertSignalType
    weight: float
    detail: str
    def __init__(self, signal_type: _Optional[_Union[AlertSignalType, str]] = ..., weight: _Optional[float] = ..., detail: _Optional[str] = ...) -> None: ...

class AlertConfidence(_message.Message):
    __slots__ = ("id", "alert_id", "user_id", "device_id", "score", "level", "contributing_signals", "duplicate_suppressed", "suppressed_alert_id", "evaluation_latency_ms", "evaluated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTING_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_SUPPRESSED_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSED_ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    alert_id: str
    user_id: str
    device_id: str
    score: float
    level: AlertConfidenceLevel
    contributing_signals: _containers.RepeatedCompositeFieldContainer[AlertSignal]
    duplicate_suppressed: bool
    suppressed_alert_id: str
    evaluation_latency_ms: int
    evaluated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., alert_id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., score: _Optional[float] = ..., level: _Optional[_Union[AlertConfidenceLevel, str]] = ..., contributing_signals: _Optional[_Iterable[_Union[AlertSignal, _Mapping]]] = ..., duplicate_suppressed: _Optional[bool] = ..., suppressed_alert_id: _Optional[str] = ..., evaluation_latency_ms: _Optional[int] = ..., evaluated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NotificationOutcome(_message.Message):
    __slots__ = ("id", "alert_id", "recipient_user_id", "channel", "status", "provider", "failure_reason", "delivery_latency_ms", "escalated", "escalation_reason", "attempted_at", "recipient_type", "notification_recipient_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    ESCALATED_FIELD_NUMBER: _ClassVar[int]
    ESCALATION_REASON_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTED_AT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    alert_id: str
    recipient_user_id: str
    channel: NotificationChannel
    status: NotificationDeliveryStatus
    provider: str
    failure_reason: str
    delivery_latency_ms: int
    escalated: bool
    escalation_reason: str
    attempted_at: _timestamp_pb2.Timestamp
    recipient_type: NotificationRecipientType
    notification_recipient_id: str
    def __init__(self, id: _Optional[str] = ..., alert_id: _Optional[str] = ..., recipient_user_id: _Optional[str] = ..., channel: _Optional[_Union[NotificationChannel, str]] = ..., status: _Optional[_Union[NotificationDeliveryStatus, str]] = ..., provider: _Optional[str] = ..., failure_reason: _Optional[str] = ..., delivery_latency_ms: _Optional[int] = ..., escalated: _Optional[bool] = ..., escalation_reason: _Optional[str] = ..., attempted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., recipient_type: _Optional[_Union[NotificationRecipientType, str]] = ..., notification_recipient_id: _Optional[str] = ...) -> None: ...
