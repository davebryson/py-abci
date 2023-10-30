from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Proof(_message.Message):
    __slots__ = ["total", "index", "leaf_hash", "aunts"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LEAF_HASH_FIELD_NUMBER: _ClassVar[int]
    AUNTS_FIELD_NUMBER: _ClassVar[int]
    total: int
    index: int
    leaf_hash: bytes
    aunts: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, total: _Optional[int] = ..., index: _Optional[int] = ..., leaf_hash: _Optional[bytes] = ..., aunts: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ValueOp(_message.Message):
    __slots__ = ["key", "proof"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    proof: Proof
    def __init__(self, key: _Optional[bytes] = ..., proof: _Optional[_Union[Proof, _Mapping]] = ...) -> None: ...

class DominoOp(_message.Message):
    __slots__ = ["key", "input", "output"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    key: str
    input: str
    output: str
    def __init__(self, key: _Optional[str] = ..., input: _Optional[str] = ..., output: _Optional[str] = ...) -> None: ...

class ProofOp(_message.Message):
    __slots__ = ["type", "key", "data"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: str
    key: bytes
    data: bytes
    def __init__(self, type: _Optional[str] = ..., key: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...

class ProofOps(_message.Message):
    __slots__ = ["ops"]
    OPS_FIELD_NUMBER: _ClassVar[int]
    ops: _containers.RepeatedCompositeFieldContainer[ProofOp]
    def __init__(self, ops: _Optional[_Iterable[_Union[ProofOp, _Mapping]]] = ...) -> None: ...
