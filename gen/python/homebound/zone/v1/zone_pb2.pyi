from google.protobuf import timestamp_pb2 as _timestamp_pb2
from homebound.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_KIND_UNSPECIFIED: _ClassVar[ZoneKind]
    ZONE_KIND_SAFE: _ClassVar[ZoneKind]
    ZONE_KIND_DANGER: _ClassVar[ZoneKind]

class ZoneShapeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_SHAPE_TYPE_UNSPECIFIED: _ClassVar[ZoneShapeType]
    ZONE_SHAPE_TYPE_CIRCLE: _ClassVar[ZoneShapeType]
    ZONE_SHAPE_TYPE_POLYGON: _ClassVar[ZoneShapeType]

class ZoneSuggestionSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_SUGGESTION_SOURCE_UNSPECIFIED: _ClassVar[ZoneSuggestionSource]
    ZONE_SUGGESTION_SOURCE_FREQUENT_DWELL: _ClassVar[ZoneSuggestionSource]
    ZONE_SUGGESTION_SOURCE_REPEATED_ROUTE: _ClassVar[ZoneSuggestionSource]
    ZONE_SUGGESTION_SOURCE_OPERATOR_REVIEW: _ClassVar[ZoneSuggestionSource]

class ZoneSuggestionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_SUGGESTION_STATUS_UNSPECIFIED: _ClassVar[ZoneSuggestionStatus]
    ZONE_SUGGESTION_STATUS_PENDING_REVIEW: _ClassVar[ZoneSuggestionStatus]
    ZONE_SUGGESTION_STATUS_ACCEPTED: _ClassVar[ZoneSuggestionStatus]
    ZONE_SUGGESTION_STATUS_REJECTED: _ClassVar[ZoneSuggestionStatus]
    ZONE_SUGGESTION_STATUS_EXPIRED: _ClassVar[ZoneSuggestionStatus]
ZONE_KIND_UNSPECIFIED: ZoneKind
ZONE_KIND_SAFE: ZoneKind
ZONE_KIND_DANGER: ZoneKind
ZONE_SHAPE_TYPE_UNSPECIFIED: ZoneShapeType
ZONE_SHAPE_TYPE_CIRCLE: ZoneShapeType
ZONE_SHAPE_TYPE_POLYGON: ZoneShapeType
ZONE_SUGGESTION_SOURCE_UNSPECIFIED: ZoneSuggestionSource
ZONE_SUGGESTION_SOURCE_FREQUENT_DWELL: ZoneSuggestionSource
ZONE_SUGGESTION_SOURCE_REPEATED_ROUTE: ZoneSuggestionSource
ZONE_SUGGESTION_SOURCE_OPERATOR_REVIEW: ZoneSuggestionSource
ZONE_SUGGESTION_STATUS_UNSPECIFIED: ZoneSuggestionStatus
ZONE_SUGGESTION_STATUS_PENDING_REVIEW: ZoneSuggestionStatus
ZONE_SUGGESTION_STATUS_ACCEPTED: ZoneSuggestionStatus
ZONE_SUGGESTION_STATUS_REJECTED: ZoneSuggestionStatus
ZONE_SUGGESTION_STATUS_EXPIRED: ZoneSuggestionStatus

class ZoneShape(_message.Message):
    __slots__ = ("shape_type", "center", "radius_meters", "vertices")
    SHAPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_METERS_FIELD_NUMBER: _ClassVar[int]
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    shape_type: ZoneShapeType
    center: _common_pb2.GeoPoint
    radius_meters: float
    vertices: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoPoint]
    def __init__(self, shape_type: _Optional[_Union[ZoneShapeType, str]] = ..., center: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., radius_meters: _Optional[float] = ..., vertices: _Optional[_Iterable[_Union[_common_pb2.GeoPoint, _Mapping]]] = ...) -> None: ...

class ZoneSuggestion(_message.Message):
    __slots__ = ("id", "user_id", "device_id", "suggested_kind", "shape", "suggested_name", "source", "confidence", "status", "quality_summary", "created_at", "reviewed_at", "reviewed_by_user_id", "rejection_reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_KIND_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    device_id: str
    suggested_kind: ZoneKind
    shape: ZoneShape
    suggested_name: str
    source: ZoneSuggestionSource
    confidence: float
    status: ZoneSuggestionStatus
    quality_summary: ZoneQualitySummary
    created_at: _timestamp_pb2.Timestamp
    reviewed_at: _timestamp_pb2.Timestamp
    reviewed_by_user_id: str
    rejection_reason: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., suggested_kind: _Optional[_Union[ZoneKind, str]] = ..., shape: _Optional[_Union[ZoneShape, _Mapping]] = ..., suggested_name: _Optional[str] = ..., source: _Optional[_Union[ZoneSuggestionSource, str]] = ..., confidence: _Optional[float] = ..., status: _Optional[_Union[ZoneSuggestionStatus, str]] = ..., quality_summary: _Optional[_Union[ZoneQualitySummary, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reviewed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reviewed_by_user_id: _Optional[str] = ..., rejection_reason: _Optional[str] = ...) -> None: ...

class ZoneQualitySummary(_message.Message):
    __slots__ = ("id", "user_id", "device_id", "zone_id", "suggestion_id", "observation_count", "distinct_day_count", "first_observed_at", "last_observed_at", "median_dwell_seconds", "signal_quality")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_DAY_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_DWELL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_QUALITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    device_id: str
    zone_id: str
    suggestion_id: str
    observation_count: int
    distinct_day_count: int
    first_observed_at: _timestamp_pb2.Timestamp
    last_observed_at: _timestamp_pb2.Timestamp
    median_dwell_seconds: float
    signal_quality: float
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., zone_id: _Optional[str] = ..., suggestion_id: _Optional[str] = ..., observation_count: _Optional[int] = ..., distinct_day_count: _Optional[int] = ..., first_observed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_observed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., median_dwell_seconds: _Optional[float] = ..., signal_quality: _Optional[float] = ...) -> None: ...
