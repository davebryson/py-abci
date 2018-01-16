from abci.wire import *
from abci.messages import *
from io import BytesIO
import abci.types_pb2 as types
from abci.server import ProtocolHandler
from abci.application import BaseApplication, Result, OK

class SApp(BaseApplication):
    def info(self):
        r = types.ResponseInfo()
        r.data = "hellothere"
        return r

    def deliver_tx(self, tx):
        return Result(OK, data=tx, log='all good')

    def check_tx(self, tx):
        return Result(OK, data=tx, log='all good again')

    def query(self, reqQuery):
        return types.ResponseQuery(key=reqQuery.data, value=b'dave', proof=b'0x12')

def test_handler():
    p = ProtocolHandler(SApp())

    r = to_response_echo('hello')
    data = p.process('echo', r)
    res, err  = read_message(BytesIO(data), types.Response)
    assert res
    assert 'echo' == res.WhichOneof("value")
    assert res.echo.message == 'hello'

    data = p.process('flush', None)
    res, err  = read_message(BytesIO(data), types.Response)
    assert res
    assert 'flush' == res.WhichOneof("value")

    data = p.process('info', None)
    res, err  = read_message(BytesIO(data), types.Response)
    assert res
    assert 'info' == res.WhichOneof("value")
    assert res.info.data == 'hellothere'

    r = to_request_deliver_tx(b'0x1234')
    data = p.process('deliver_tx', r)
    res, err  = read_message(BytesIO(data), types.Response)
    assert res
    assert 'deliver_tx' == res.WhichOneof("value")
    assert res.deliver_tx.code == 0
    assert res.deliver_tx.data == b'0x1234'

    r = to_request_check_tx(b'0x1234')
    data = p.process('check_tx', r)
    res, err  = read_message(BytesIO(data), types.Response)
    assert res
    assert 'check_tx' == res.WhichOneof("value")
    assert res.check_tx.code == 0
    assert res.check_tx.data == b'0x1234'

    r = to_request_query(data=b'name')
    data = p.process('query', r)
    res, err  = read_message(BytesIO(data), types.Response)
    assert res
    assert 'query' == res.WhichOneof("value")
    assert res.query.key == b'name'
    assert res.query.value == b'dave'
    assert res.query.code == 0
    assert res.query.proof == b'0x12'
