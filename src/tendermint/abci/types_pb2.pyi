from tendermint.crypto import proof_pb2 as _proof_pb2
from tendermint.types import types_pb2 as _types_pb2
from tendermint.crypto import keys_pb2 as _keys_pb2
from tendermint.types import params_pb2 as _params_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckTxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NEW: _ClassVar[CheckTxType]
    RECHECK: _ClassVar[CheckTxType]

class EvidenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[EvidenceType]
    DUPLICATE_VOTE: _ClassVar[EvidenceType]
    LIGHT_CLIENT_ATTACK: _ClassVar[EvidenceType]
NEW: CheckTxType
RECHECK: CheckTxType
UNKNOWN: EvidenceType
DUPLICATE_VOTE: EvidenceType
LIGHT_CLIENT_ATTACK: EvidenceType

class Request(_message.Message):
    __slots__ = ["echo", "flush", "info", "set_option", "init_chain", "query", "begin_block", "check_tx", "deliver_tx", "end_block", "commit", "list_snapshots", "offer_snapshot", "load_snapshot_chunk", "apply_snapshot_chunk"]
    ECHO_FIELD_NUMBER: _ClassVar[int]
    FLUSH_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SET_OPTION_FIELD_NUMBER: _ClassVar[int]
    INIT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    BEGIN_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CHECK_TX_FIELD_NUMBER: _ClassVar[int]
    DELIVER_TX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    LIST_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    OFFER_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    LOAD_SNAPSHOT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    APPLY_SNAPSHOT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    echo: RequestEcho
    flush: RequestFlush
    info: RequestInfo
    set_option: RequestSetOption
    init_chain: RequestInitChain
    query: RequestQuery
    begin_block: RequestBeginBlock
    check_tx: RequestCheckTx
    deliver_tx: RequestDeliverTx
    end_block: RequestEndBlock
    commit: RequestCommit
    list_snapshots: RequestListSnapshots
    offer_snapshot: RequestOfferSnapshot
    load_snapshot_chunk: RequestLoadSnapshotChunk
    apply_snapshot_chunk: RequestApplySnapshotChunk
    def __init__(self, echo: _Optional[_Union[RequestEcho, _Mapping]] = ..., flush: _Optional[_Union[RequestFlush, _Mapping]] = ..., info: _Optional[_Union[RequestInfo, _Mapping]] = ..., set_option: _Optional[_Union[RequestSetOption, _Mapping]] = ..., init_chain: _Optional[_Union[RequestInitChain, _Mapping]] = ..., query: _Optional[_Union[RequestQuery, _Mapping]] = ..., begin_block: _Optional[_Union[RequestBeginBlock, _Mapping]] = ..., check_tx: _Optional[_Union[RequestCheckTx, _Mapping]] = ..., deliver_tx: _Optional[_Union[RequestDeliverTx, _Mapping]] = ..., end_block: _Optional[_Union[RequestEndBlock, _Mapping]] = ..., commit: _Optional[_Union[RequestCommit, _Mapping]] = ..., list_snapshots: _Optional[_Union[RequestListSnapshots, _Mapping]] = ..., offer_snapshot: _Optional[_Union[RequestOfferSnapshot, _Mapping]] = ..., load_snapshot_chunk: _Optional[_Union[RequestLoadSnapshotChunk, _Mapping]] = ..., apply_snapshot_chunk: _Optional[_Union[RequestApplySnapshotChunk, _Mapping]] = ...) -> None: ...

class RequestEcho(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RequestFlush(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RequestInfo(_message.Message):
    __slots__ = ["version", "block_version", "p2p_version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BLOCK_VERSION_FIELD_NUMBER: _ClassVar[int]
    P2P_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    block_version: int
    p2p_version: int
    def __init__(self, version: _Optional[str] = ..., block_version: _Optional[int] = ..., p2p_version: _Optional[int] = ...) -> None: ...

class RequestSetOption(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class RequestInitChain(_message.Message):
    __slots__ = ["time", "chain_id", "consensus_params", "validators", "app_state_bytes", "initial_height"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    APP_STATE_BYTES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    chain_id: str
    consensus_params: ConsensusParams
    validators: _containers.RepeatedCompositeFieldContainer[ValidatorUpdate]
    app_state_bytes: bytes
    initial_height: int
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., chain_id: _Optional[str] = ..., consensus_params: _Optional[_Union[ConsensusParams, _Mapping]] = ..., validators: _Optional[_Iterable[_Union[ValidatorUpdate, _Mapping]]] = ..., app_state_bytes: _Optional[bytes] = ..., initial_height: _Optional[int] = ...) -> None: ...

class RequestQuery(_message.Message):
    __slots__ = ["data", "path", "height", "prove"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PROVE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    path: str
    height: int
    prove: bool
    def __init__(self, data: _Optional[bytes] = ..., path: _Optional[str] = ..., height: _Optional[int] = ..., prove: bool = ...) -> None: ...

class RequestBeginBlock(_message.Message):
    __slots__ = ["hash", "header", "last_commit_info", "byzantine_validators"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMIT_INFO_FIELD_NUMBER: _ClassVar[int]
    BYZANTINE_VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    header: _types_pb2.Header
    last_commit_info: LastCommitInfo
    byzantine_validators: _containers.RepeatedCompositeFieldContainer[Evidence]
    def __init__(self, hash: _Optional[bytes] = ..., header: _Optional[_Union[_types_pb2.Header, _Mapping]] = ..., last_commit_info: _Optional[_Union[LastCommitInfo, _Mapping]] = ..., byzantine_validators: _Optional[_Iterable[_Union[Evidence, _Mapping]]] = ...) -> None: ...

class RequestCheckTx(_message.Message):
    __slots__ = ["tx", "type"]
    TX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    tx: bytes
    type: CheckTxType
    def __init__(self, tx: _Optional[bytes] = ..., type: _Optional[_Union[CheckTxType, str]] = ...) -> None: ...

class RequestDeliverTx(_message.Message):
    __slots__ = ["tx"]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: bytes
    def __init__(self, tx: _Optional[bytes] = ...) -> None: ...

class RequestEndBlock(_message.Message):
    __slots__ = ["height"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class RequestCommit(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RequestListSnapshots(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RequestOfferSnapshot(_message.Message):
    __slots__ = ["snapshot", "app_hash"]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    APP_HASH_FIELD_NUMBER: _ClassVar[int]
    snapshot: Snapshot
    app_hash: bytes
    def __init__(self, snapshot: _Optional[_Union[Snapshot, _Mapping]] = ..., app_hash: _Optional[bytes] = ...) -> None: ...

class RequestLoadSnapshotChunk(_message.Message):
    __slots__ = ["height", "format", "chunk"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    height: int
    format: int
    chunk: int
    def __init__(self, height: _Optional[int] = ..., format: _Optional[int] = ..., chunk: _Optional[int] = ...) -> None: ...

class RequestApplySnapshotChunk(_message.Message):
    __slots__ = ["index", "chunk", "sender"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    index: int
    chunk: bytes
    sender: str
    def __init__(self, index: _Optional[int] = ..., chunk: _Optional[bytes] = ..., sender: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["exception", "echo", "flush", "info", "set_option", "init_chain", "query", "begin_block", "check_tx", "deliver_tx", "end_block", "commit", "list_snapshots", "offer_snapshot", "load_snapshot_chunk", "apply_snapshot_chunk"]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    ECHO_FIELD_NUMBER: _ClassVar[int]
    FLUSH_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SET_OPTION_FIELD_NUMBER: _ClassVar[int]
    INIT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    BEGIN_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CHECK_TX_FIELD_NUMBER: _ClassVar[int]
    DELIVER_TX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    LIST_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    OFFER_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    LOAD_SNAPSHOT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    APPLY_SNAPSHOT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    exception: ResponseException
    echo: ResponseEcho
    flush: ResponseFlush
    info: ResponseInfo
    set_option: ResponseSetOption
    init_chain: ResponseInitChain
    query: ResponseQuery
    begin_block: ResponseBeginBlock
    check_tx: ResponseCheckTx
    deliver_tx: ResponseDeliverTx
    end_block: ResponseEndBlock
    commit: ResponseCommit
    list_snapshots: ResponseListSnapshots
    offer_snapshot: ResponseOfferSnapshot
    load_snapshot_chunk: ResponseLoadSnapshotChunk
    apply_snapshot_chunk: ResponseApplySnapshotChunk
    def __init__(self, exception: _Optional[_Union[ResponseException, _Mapping]] = ..., echo: _Optional[_Union[ResponseEcho, _Mapping]] = ..., flush: _Optional[_Union[ResponseFlush, _Mapping]] = ..., info: _Optional[_Union[ResponseInfo, _Mapping]] = ..., set_option: _Optional[_Union[ResponseSetOption, _Mapping]] = ..., init_chain: _Optional[_Union[ResponseInitChain, _Mapping]] = ..., query: _Optional[_Union[ResponseQuery, _Mapping]] = ..., begin_block: _Optional[_Union[ResponseBeginBlock, _Mapping]] = ..., check_tx: _Optional[_Union[ResponseCheckTx, _Mapping]] = ..., deliver_tx: _Optional[_Union[ResponseDeliverTx, _Mapping]] = ..., end_block: _Optional[_Union[ResponseEndBlock, _Mapping]] = ..., commit: _Optional[_Union[ResponseCommit, _Mapping]] = ..., list_snapshots: _Optional[_Union[ResponseListSnapshots, _Mapping]] = ..., offer_snapshot: _Optional[_Union[ResponseOfferSnapshot, _Mapping]] = ..., load_snapshot_chunk: _Optional[_Union[ResponseLoadSnapshotChunk, _Mapping]] = ..., apply_snapshot_chunk: _Optional[_Union[ResponseApplySnapshotChunk, _Mapping]] = ...) -> None: ...

class ResponseException(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ResponseEcho(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ResponseFlush(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResponseInfo(_message.Message):
    __slots__ = ["data", "version", "app_version", "last_block_height", "last_block_app_hash"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LAST_BLOCK_APP_HASH_FIELD_NUMBER: _ClassVar[int]
    data: str
    version: str
    app_version: int
    last_block_height: int
    last_block_app_hash: bytes
    def __init__(self, data: _Optional[str] = ..., version: _Optional[str] = ..., app_version: _Optional[int] = ..., last_block_height: _Optional[int] = ..., last_block_app_hash: _Optional[bytes] = ...) -> None: ...

class ResponseSetOption(_message.Message):
    __slots__ = ["code", "log", "info"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    code: int
    log: str
    info: str
    def __init__(self, code: _Optional[int] = ..., log: _Optional[str] = ..., info: _Optional[str] = ...) -> None: ...

class ResponseInitChain(_message.Message):
    __slots__ = ["consensus_params", "validators", "app_hash"]
    CONSENSUS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    APP_HASH_FIELD_NUMBER: _ClassVar[int]
    consensus_params: ConsensusParams
    validators: _containers.RepeatedCompositeFieldContainer[ValidatorUpdate]
    app_hash: bytes
    def __init__(self, consensus_params: _Optional[_Union[ConsensusParams, _Mapping]] = ..., validators: _Optional[_Iterable[_Union[ValidatorUpdate, _Mapping]]] = ..., app_hash: _Optional[bytes] = ...) -> None: ...

class ResponseQuery(_message.Message):
    __slots__ = ["code", "log", "info", "index", "key", "value", "proof_ops", "height", "codespace"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PROOF_OPS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    CODESPACE_FIELD_NUMBER: _ClassVar[int]
    code: int
    log: str
    info: str
    index: int
    key: bytes
    value: bytes
    proof_ops: _proof_pb2.ProofOps
    height: int
    codespace: str
    def __init__(self, code: _Optional[int] = ..., log: _Optional[str] = ..., info: _Optional[str] = ..., index: _Optional[int] = ..., key: _Optional[bytes] = ..., value: _Optional[bytes] = ..., proof_ops: _Optional[_Union[_proof_pb2.ProofOps, _Mapping]] = ..., height: _Optional[int] = ..., codespace: _Optional[str] = ...) -> None: ...

class ResponseBeginBlock(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class ResponseCheckTx(_message.Message):
    __slots__ = ["code", "data", "log", "info", "gas_wanted", "gas_used", "events", "codespace", "sender", "priority", "mempool_error"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    GAS_WANTED_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CODESPACE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MEMPOOL_ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    data: bytes
    log: str
    info: str
    gas_wanted: int
    gas_used: int
    events: _containers.RepeatedCompositeFieldContainer[Event]
    codespace: str
    sender: str
    priority: int
    mempool_error: str
    def __init__(self, code: _Optional[int] = ..., data: _Optional[bytes] = ..., log: _Optional[str] = ..., info: _Optional[str] = ..., gas_wanted: _Optional[int] = ..., gas_used: _Optional[int] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., codespace: _Optional[str] = ..., sender: _Optional[str] = ..., priority: _Optional[int] = ..., mempool_error: _Optional[str] = ...) -> None: ...

class ResponseDeliverTx(_message.Message):
    __slots__ = ["code", "data", "log", "info", "gas_wanted", "gas_used", "events", "codespace"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    GAS_WANTED_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CODESPACE_FIELD_NUMBER: _ClassVar[int]
    code: int
    data: bytes
    log: str
    info: str
    gas_wanted: int
    gas_used: int
    events: _containers.RepeatedCompositeFieldContainer[Event]
    codespace: str
    def __init__(self, code: _Optional[int] = ..., data: _Optional[bytes] = ..., log: _Optional[str] = ..., info: _Optional[str] = ..., gas_wanted: _Optional[int] = ..., gas_used: _Optional[int] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., codespace: _Optional[str] = ...) -> None: ...

class ResponseEndBlock(_message.Message):
    __slots__ = ["validator_updates", "consensus_param_updates", "events"]
    VALIDATOR_UPDATES_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_PARAM_UPDATES_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    validator_updates: _containers.RepeatedCompositeFieldContainer[ValidatorUpdate]
    consensus_param_updates: ConsensusParams
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, validator_updates: _Optional[_Iterable[_Union[ValidatorUpdate, _Mapping]]] = ..., consensus_param_updates: _Optional[_Union[ConsensusParams, _Mapping]] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class ResponseCommit(_message.Message):
    __slots__ = ["data", "retain_height"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RETAIN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    retain_height: int
    def __init__(self, data: _Optional[bytes] = ..., retain_height: _Optional[int] = ...) -> None: ...

class ResponseListSnapshots(_message.Message):
    __slots__ = ["snapshots"]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[Snapshot]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[Snapshot, _Mapping]]] = ...) -> None: ...

class ResponseOfferSnapshot(_message.Message):
    __slots__ = ["result"]
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ResponseOfferSnapshot.Result]
        ACCEPT: _ClassVar[ResponseOfferSnapshot.Result]
        ABORT: _ClassVar[ResponseOfferSnapshot.Result]
        REJECT: _ClassVar[ResponseOfferSnapshot.Result]
        REJECT_FORMAT: _ClassVar[ResponseOfferSnapshot.Result]
        REJECT_SENDER: _ClassVar[ResponseOfferSnapshot.Result]
    UNKNOWN: ResponseOfferSnapshot.Result
    ACCEPT: ResponseOfferSnapshot.Result
    ABORT: ResponseOfferSnapshot.Result
    REJECT: ResponseOfferSnapshot.Result
    REJECT_FORMAT: ResponseOfferSnapshot.Result
    REJECT_SENDER: ResponseOfferSnapshot.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResponseOfferSnapshot.Result
    def __init__(self, result: _Optional[_Union[ResponseOfferSnapshot.Result, str]] = ...) -> None: ...

class ResponseLoadSnapshotChunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ResponseApplySnapshotChunk(_message.Message):
    __slots__ = ["result", "refetch_chunks", "reject_senders"]
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ResponseApplySnapshotChunk.Result]
        ACCEPT: _ClassVar[ResponseApplySnapshotChunk.Result]
        ABORT: _ClassVar[ResponseApplySnapshotChunk.Result]
        RETRY: _ClassVar[ResponseApplySnapshotChunk.Result]
        RETRY_SNAPSHOT: _ClassVar[ResponseApplySnapshotChunk.Result]
        REJECT_SNAPSHOT: _ClassVar[ResponseApplySnapshotChunk.Result]
    UNKNOWN: ResponseApplySnapshotChunk.Result
    ACCEPT: ResponseApplySnapshotChunk.Result
    ABORT: ResponseApplySnapshotChunk.Result
    RETRY: ResponseApplySnapshotChunk.Result
    RETRY_SNAPSHOT: ResponseApplySnapshotChunk.Result
    REJECT_SNAPSHOT: ResponseApplySnapshotChunk.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    REFETCH_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    REJECT_SENDERS_FIELD_NUMBER: _ClassVar[int]
    result: ResponseApplySnapshotChunk.Result
    refetch_chunks: _containers.RepeatedScalarFieldContainer[int]
    reject_senders: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Union[ResponseApplySnapshotChunk.Result, str]] = ..., refetch_chunks: _Optional[_Iterable[int]] = ..., reject_senders: _Optional[_Iterable[str]] = ...) -> None: ...

class ConsensusParams(_message.Message):
    __slots__ = ["block", "evidence", "validator", "version"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    block: BlockParams
    evidence: _params_pb2.EvidenceParams
    validator: _params_pb2.ValidatorParams
    version: _params_pb2.VersionParams
    def __init__(self, block: _Optional[_Union[BlockParams, _Mapping]] = ..., evidence: _Optional[_Union[_params_pb2.EvidenceParams, _Mapping]] = ..., validator: _Optional[_Union[_params_pb2.ValidatorParams, _Mapping]] = ..., version: _Optional[_Union[_params_pb2.VersionParams, _Mapping]] = ...) -> None: ...

class BlockParams(_message.Message):
    __slots__ = ["max_bytes", "max_gas"]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_GAS_FIELD_NUMBER: _ClassVar[int]
    max_bytes: int
    max_gas: int
    def __init__(self, max_bytes: _Optional[int] = ..., max_gas: _Optional[int] = ...) -> None: ...

class LastCommitInfo(_message.Message):
    __slots__ = ["round", "votes"]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    round: int
    votes: _containers.RepeatedCompositeFieldContainer[VoteInfo]
    def __init__(self, round: _Optional[int] = ..., votes: _Optional[_Iterable[_Union[VoteInfo, _Mapping]]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["type", "attributes"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    type: str
    attributes: _containers.RepeatedCompositeFieldContainer[EventAttribute]
    def __init__(self, type: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[EventAttribute, _Mapping]]] = ...) -> None: ...

class EventAttribute(_message.Message):
    __slots__ = ["key", "value", "index"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    index: bool
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ..., index: bool = ...) -> None: ...

class TxResult(_message.Message):
    __slots__ = ["height", "index", "tx", "result"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    height: int
    index: int
    tx: bytes
    result: ResponseDeliverTx
    def __init__(self, height: _Optional[int] = ..., index: _Optional[int] = ..., tx: _Optional[bytes] = ..., result: _Optional[_Union[ResponseDeliverTx, _Mapping]] = ...) -> None: ...

class Validator(_message.Message):
    __slots__ = ["address", "power"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    power: int
    def __init__(self, address: _Optional[bytes] = ..., power: _Optional[int] = ...) -> None: ...

class ValidatorUpdate(_message.Message):
    __slots__ = ["pub_key", "power"]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    pub_key: _keys_pb2.PublicKey
    power: int
    def __init__(self, pub_key: _Optional[_Union[_keys_pb2.PublicKey, _Mapping]] = ..., power: _Optional[int] = ...) -> None: ...

class VoteInfo(_message.Message):
    __slots__ = ["validator", "signed_last_block"]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LAST_BLOCK_FIELD_NUMBER: _ClassVar[int]
    validator: Validator
    signed_last_block: bool
    def __init__(self, validator: _Optional[_Union[Validator, _Mapping]] = ..., signed_last_block: bool = ...) -> None: ...

class Evidence(_message.Message):
    __slots__ = ["type", "validator", "height", "time", "total_voting_power"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOTING_POWER_FIELD_NUMBER: _ClassVar[int]
    type: EvidenceType
    validator: Validator
    height: int
    time: _timestamp_pb2.Timestamp
    total_voting_power: int
    def __init__(self, type: _Optional[_Union[EvidenceType, str]] = ..., validator: _Optional[_Union[Validator, _Mapping]] = ..., height: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total_voting_power: _Optional[int] = ...) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ["height", "format", "chunks", "hash", "metadata"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    height: int
    format: int
    chunks: int
    hash: bytes
    metadata: bytes
    def __init__(self, height: _Optional[int] = ..., format: _Optional[int] = ..., chunks: _Optional[int] = ..., hash: _Optional[bytes] = ..., metadata: _Optional[bytes] = ...) -> None: ...
