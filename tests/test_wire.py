from abci.encoding import *
from abci.messages import *
from abci.server import ProtocolHandler
import abci.types_pb2 as types


def test_encoding_decoding():
    echo = to_request_echo('hello')
    raw = write_message(echo)
    buffer = BytesIO(raw)
    req, _ = read_message(buffer, types.Request)
    assert 'echo' == req.WhichOneof("value")

    info = to_request_info()
    raw1 = write_message(info)
    buffer1 = BytesIO(raw1)
    req1, _ = read_message(buffer1, types.Request)
    assert 'info' == req1.WhichOneof("value")

def test_flow():
    from io import BytesIO
    # info + flush
    inbound = b'\x14"\x08\n\x060.16.0\x04\x1a\x00'
    data = BytesIO(inbound)

    req_type,_  = read_message(data, types.Request)
    assert 'info' == req_type.WhichOneof("value")

    req_type2, _  = read_message(data, types.Request)
    assert 'flush' == req_type2.WhichOneof("value")

    assert data.read() == b''
