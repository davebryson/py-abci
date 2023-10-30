from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PublicKey(_message.Message):
    __slots__ = ["ed25519", "secp256k1"]
    ED25519_FIELD_NUMBER: _ClassVar[int]
    SECP256K1_FIELD_NUMBER: _ClassVar[int]
    ed25519: bytes
    secp256k1: bytes
    def __init__(self, ed25519: _Optional[bytes] = ..., secp256k1: _Optional[bytes] = ...) -> None: ...
