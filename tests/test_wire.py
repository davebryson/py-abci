from io import BytesIO

from abci.encoding import (
    write_message,
    read_message,
)

from abci.types_pb2 import (
    Request,
    RequestEcho,
    RequestInfo,
)

def test_raw_decoding():
    from io import BytesIO
    # info + flush request
    inbound = b'\x14"\x08\n\x060.16.0\x04\x1a\x00'
    data = BytesIO(inbound)

    req_type,_  = read_message(data, Request)
    assert 'info' == req_type.WhichOneof("value")

    req_type2, _  = read_message(data, Request)
    assert 'flush' == req_type2.WhichOneof("value")

    assert data.read() == b''

def test_encoding_decoding():
    echo = Request(echo=RequestEcho(message="hello"))
    #echo = to_request_echo('hello')
    raw = write_message(echo)
    buffer = BytesIO(raw)
    req, _ = read_message(buffer, Request)
    assert 'echo' == req.WhichOneof("value")

    info = Request(info=RequestInfo(version="18.0"))
    raw1 = write_message(info)
    buffer1 = BytesIO(raw1)
    req, _ = read_message(buffer1, Request)
    assert 'info' == req.WhichOneof("value")
