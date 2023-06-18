from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
INDEX: CpiType
MOM_RATE: CpiType
YOY_RATE: CpiType

class GetCpiTimeRequest(_message.Message):
    __slots__ = ["cpiType"]
    CPITYPE_FIELD_NUMBER: _ClassVar[int]
    cpiType: CpiType
    def __init__(self, cpiType: _Optional[_Union[CpiType, str]] = ...) -> None: ...

class GetCpiTimeResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[Result]
    def __init__(self, results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ["month", "value"]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    month: _timestamp_pb2.Timestamp
    value: float
    def __init__(self, month: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class CpiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
