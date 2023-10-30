from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tendermint.crypto import proof_pb2 as _proof_pb2
from tendermint.version import types_pb2 as _types_pb2
from tendermint.types import validator_pb2 as _validator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockIDFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BLOCK_ID_FLAG_UNKNOWN: _ClassVar[BlockIDFlag]
    BLOCK_ID_FLAG_ABSENT: _ClassVar[BlockIDFlag]
    BLOCK_ID_FLAG_COMMIT: _ClassVar[BlockIDFlag]
    BLOCK_ID_FLAG_NIL: _ClassVar[BlockIDFlag]

class SignedMsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIGNED_MSG_TYPE_UNKNOWN: _ClassVar[SignedMsgType]
    SIGNED_MSG_TYPE_PREVOTE: _ClassVar[SignedMsgType]
    SIGNED_MSG_TYPE_PRECOMMIT: _ClassVar[SignedMsgType]
    SIGNED_MSG_TYPE_PROPOSAL: _ClassVar[SignedMsgType]
BLOCK_ID_FLAG_UNKNOWN: BlockIDFlag
BLOCK_ID_FLAG_ABSENT: BlockIDFlag
BLOCK_ID_FLAG_COMMIT: BlockIDFlag
BLOCK_ID_FLAG_NIL: BlockIDFlag
SIGNED_MSG_TYPE_UNKNOWN: SignedMsgType
SIGNED_MSG_TYPE_PREVOTE: SignedMsgType
SIGNED_MSG_TYPE_PRECOMMIT: SignedMsgType
SIGNED_MSG_TYPE_PROPOSAL: SignedMsgType

class PartSetHeader(_message.Message):
    __slots__ = ["total", "hash"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    total: int
    hash: bytes
    def __init__(self, total: _Optional[int] = ..., hash: _Optional[bytes] = ...) -> None: ...

class Part(_message.Message):
    __slots__ = ["index", "bytes", "proof"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    index: int
    bytes: bytes
    proof: _proof_pb2.Proof
    def __init__(self, index: _Optional[int] = ..., bytes: _Optional[bytes] = ..., proof: _Optional[_Union[_proof_pb2.Proof, _Mapping]] = ...) -> None: ...

class BlockID(_message.Message):
    __slots__ = ["hash", "part_set_header"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PART_SET_HEADER_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    part_set_header: PartSetHeader
    def __init__(self, hash: _Optional[bytes] = ..., part_set_header: _Optional[_Union[PartSetHeader, _Mapping]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ["version", "chain_id", "height", "time", "last_block_id", "last_commit_hash", "data_hash", "validators_hash", "next_validators_hash", "consensus_hash", "app_hash", "last_results_hash", "evidence_hash", "proposer_address"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMIT_HASH_FIELD_NUMBER: _ClassVar[int]
    DATA_HASH_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_HASH_FIELD_NUMBER: _ClassVar[int]
    NEXT_VALIDATORS_HASH_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_HASH_FIELD_NUMBER: _ClassVar[int]
    APP_HASH_FIELD_NUMBER: _ClassVar[int]
    LAST_RESULTS_HASH_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_HASH_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2.Consensus
    chain_id: str
    height: int
    time: _timestamp_pb2.Timestamp
    last_block_id: BlockID
    last_commit_hash: bytes
    data_hash: bytes
    validators_hash: bytes
    next_validators_hash: bytes
    consensus_hash: bytes
    app_hash: bytes
    last_results_hash: bytes
    evidence_hash: bytes
    proposer_address: bytes
    def __init__(self, version: _Optional[_Union[_types_pb2.Consensus, _Mapping]] = ..., chain_id: _Optional[str] = ..., height: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_block_id: _Optional[_Union[BlockID, _Mapping]] = ..., last_commit_hash: _Optional[bytes] = ..., data_hash: _Optional[bytes] = ..., validators_hash: _Optional[bytes] = ..., next_validators_hash: _Optional[bytes] = ..., consensus_hash: _Optional[bytes] = ..., app_hash: _Optional[bytes] = ..., last_results_hash: _Optional[bytes] = ..., evidence_hash: _Optional[bytes] = ..., proposer_address: _Optional[bytes] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ["txs"]
    TXS_FIELD_NUMBER: _ClassVar[int]
    txs: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, txs: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Vote(_message.Message):
    __slots__ = ["type", "height", "round", "block_id", "timestamp", "validator_address", "validator_index", "signature"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    type: SignedMsgType
    height: int
    round: int
    block_id: BlockID
    timestamp: _timestamp_pb2.Timestamp
    validator_address: bytes
    validator_index: int
    signature: bytes
    def __init__(self, type: _Optional[_Union[SignedMsgType, str]] = ..., height: _Optional[int] = ..., round: _Optional[int] = ..., block_id: _Optional[_Union[BlockID, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., validator_address: _Optional[bytes] = ..., validator_index: _Optional[int] = ..., signature: _Optional[bytes] = ...) -> None: ...

class Commit(_message.Message):
    __slots__ = ["height", "round", "block_id", "signatures"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    height: int
    round: int
    block_id: BlockID
    signatures: _containers.RepeatedCompositeFieldContainer[CommitSig]
    def __init__(self, height: _Optional[int] = ..., round: _Optional[int] = ..., block_id: _Optional[_Union[BlockID, _Mapping]] = ..., signatures: _Optional[_Iterable[_Union[CommitSig, _Mapping]]] = ...) -> None: ...

class CommitSig(_message.Message):
    __slots__ = ["block_id_flag", "validator_address", "timestamp", "signature"]
    BLOCK_ID_FLAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    block_id_flag: BlockIDFlag
    validator_address: bytes
    timestamp: _timestamp_pb2.Timestamp
    signature: bytes
    def __init__(self, block_id_flag: _Optional[_Union[BlockIDFlag, str]] = ..., validator_address: _Optional[bytes] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class Proposal(_message.Message):
    __slots__ = ["type", "height", "round", "pol_round", "block_id", "timestamp", "signature"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    POL_ROUND_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    type: SignedMsgType
    height: int
    round: int
    pol_round: int
    block_id: BlockID
    timestamp: _timestamp_pb2.Timestamp
    signature: bytes
    def __init__(self, type: _Optional[_Union[SignedMsgType, str]] = ..., height: _Optional[int] = ..., round: _Optional[int] = ..., pol_round: _Optional[int] = ..., block_id: _Optional[_Union[BlockID, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class SignedHeader(_message.Message):
    __slots__ = ["header", "commit"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    header: Header
    commit: Commit
    def __init__(self, header: _Optional[_Union[Header, _Mapping]] = ..., commit: _Optional[_Union[Commit, _Mapping]] = ...) -> None: ...

class LightBlock(_message.Message):
    __slots__ = ["signed_header", "validator_set"]
    SIGNED_HEADER_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SET_FIELD_NUMBER: _ClassVar[int]
    signed_header: SignedHeader
    validator_set: _validator_pb2.ValidatorSet
    def __init__(self, signed_header: _Optional[_Union[SignedHeader, _Mapping]] = ..., validator_set: _Optional[_Union[_validator_pb2.ValidatorSet, _Mapping]] = ...) -> None: ...

class BlockMeta(_message.Message):
    __slots__ = ["block_id", "block_size", "header", "num_txs"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NUM_TXS_FIELD_NUMBER: _ClassVar[int]
    block_id: BlockID
    block_size: int
    header: Header
    num_txs: int
    def __init__(self, block_id: _Optional[_Union[BlockID, _Mapping]] = ..., block_size: _Optional[int] = ..., header: _Optional[_Union[Header, _Mapping]] = ..., num_txs: _Optional[int] = ...) -> None: ...

class TxProof(_message.Message):
    __slots__ = ["root_hash", "data", "proof"]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    root_hash: bytes
    data: bytes
    proof: _proof_pb2.Proof
    def __init__(self, root_hash: _Optional[bytes] = ..., data: _Optional[bytes] = ..., proof: _Optional[_Union[_proof_pb2.Proof, _Mapping]] = ...) -> None: ...
