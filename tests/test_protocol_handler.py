from abci.encoding import *
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
    message = next(read_messages(BytesIO(data), types.Response))
    assert 'echo' == message.WhichOneof("value")
    assert message.echo.message == 'hello'

    data = p.process('flush', None)
    message = next(read_messages(BytesIO(data), types.Response))
    assert 'flush' == message.WhichOneof("value")

    data = p.process('info', None)
    message = next(read_messages(BytesIO(data), types.Response))
    assert 'info' == message.WhichOneof("value")
    assert message.info.data == 'hellothere'

    r = to_request_deliver_tx(b'0x1234')
    data = p.process('deliver_tx', r)
    message = next(read_messages(BytesIO(data), types.Response))
    assert 'deliver_tx' == message.WhichOneof("value")
    assert message.deliver_tx.code == 0
    assert message.deliver_tx.data == b'0x1234'

    r = to_request_check_tx(b'0x1234')
    data = p.process('check_tx', r)
    message = next(read_messages(BytesIO(data), types.Response))
    assert 'check_tx' == message.WhichOneof("value")
    assert message.check_tx.code == 0
    assert message.check_tx.data == b'0x1234'

    r = to_request_query(data=b'name')
    data = p.process('query', r)
    message = next(read_messages(BytesIO(data), types.Response))
    assert 'query' == message.WhichOneof("value")
    assert message.query.key == b'name'
    assert message.query.value == b'dave'
    assert message.query.code == 0
    assert message.query.proof == b'0x12'
