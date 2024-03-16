from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CosineSimRequest(_message.Message):
    __slots__ = ("v1", "v2")
    V1_FIELD_NUMBER: _ClassVar[int]
    V2_FIELD_NUMBER: _ClassVar[int]
    v1: str
    v2: str
    def __init__(self, v1: _Optional[str] = ..., v2: _Optional[str] = ...) -> None: ...

class CosineSimResponse(_message.Message):
    __slots__ = ("cosinesim",)
    COSINESIM_FIELD_NUMBER: _ClassVar[int]
    cosinesim: float
    def __init__(self, cosinesim: _Optional[float] = ...) -> None: ...
