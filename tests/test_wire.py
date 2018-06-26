from abci.encoding import *
from abci.messages import *
from abci.server import ProtocolHandler
import abci.types_pb2 as types


def test_encoding_decoding():
    echo = to_request_echo('hello')
    raw = write_message(echo)
    buffer = BytesIO(raw)
    message = next(read_messages(buffer, types.Request))
    assert 'echo' == message.WhichOneof("value")

    info = to_request_info()
    raw1 = write_message(info)
    buffer1 = BytesIO(raw1)
    message = next(read_messages(buffer1, types.Request))
    assert 'info' == message.WhichOneof("value")

def test_flow():
    from io import BytesIO
    # info + flush
    inbound = b'\x14"\x08\n\x060.16.0\x04\x1a\x00'
    data = BytesIO(inbound)

    message = next(read_messages(data, types.Request))
    assert 'info' == message.WhichOneof("value")

    message = next(read_messages(data, types.Request))
    assert 'flush' == message.WhichOneof("value")

    assert data.read() == b''
