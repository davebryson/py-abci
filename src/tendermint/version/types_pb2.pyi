from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class App(_message.Message):
    __slots__ = ["protocol", "software"]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_FIELD_NUMBER: _ClassVar[int]
    protocol: int
    software: str
    def __init__(self, protocol: _Optional[int] = ..., software: _Optional[str] = ...) -> None: ...

class Consensus(_message.Message):
    __slots__ = ["block", "app"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    block: int
    app: int
    def __init__(self, block: _Optional[int] = ..., app: _Optional[int] = ...) -> None: ...
