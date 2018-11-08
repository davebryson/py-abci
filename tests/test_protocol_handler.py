from io import BytesIO

from abci.server import ProtocolHandler
from abci.application import BaseApplication, CodeTypeOk
from abci.encoding import read_messages, write_message

from github.com.tendermint.tendermint.abci.types.types_pb2 import (
    Request, Response, ResponseException,
    RequestEcho, ResponseEcho,
    RequestFlush, ResponseFlush,
    RequestInitChain, ResponseInitChain,
    RequestInfo, ResponseInfo,
    RequestSetOption, ResponseSetOption,
    RequestDeliverTx, ResponseDeliverTx,
    RequestCheckTx, ResponseCheckTx,
    RequestQuery, ResponseQuery,
    RequestBeginBlock, ResponseBeginBlock,
    RequestEndBlock, ResponseEndBlock,
    RequestCommit, ResponseCommit,
    Validator, ValidatorUpdate, PubKey
)

from abci.utils import str_to_bytes


class ExampleApp(BaseApplication):

    def __init__(self):
        self.validators = []

    def info(self, req):
        v = req.version
        r = ResponseInfo(version=v, data="hello",
                         last_block_height=0, last_block_app_hash=b'0x12')
        return r

    def init_chain(self, req):
        self.validators = req.validators
        return ResponseInitChain()

    def check_tx(self, tx):
        return ResponseCheckTx(code=CodeTypeOk, data=tx, log="bueno")

    def deliver_tx(self, tx):
        return ResponseDeliverTx(code=CodeTypeOk, data=tx, log="bueno")

    def query(self, req):
        d = req.data
        return ResponseQuery(code=CodeTypeOk, value=d)

    def begin_block(self, req):
        return ResponseBeginBlock()

    def end_block(self, req):
        return ResponseEndBlock(validator_updates=self.validators)

    def commit(self):
        return ResponseCommit(data=b'0x1234')

    def set_option(self, req):
        k = req.key
        v = req.value
        return ResponseSetOption(code=CodeTypeOk, log=f'{k}={v}')


def __deserialze(raw: bytes) -> Request:
    resp = next(read_messages(BytesIO(raw), Response))
    return resp


def test_handler():
    app = ExampleApp()
    p = ProtocolHandler(app)

    # Echo
    req = Request(echo=RequestEcho(message='hello'))
    raw = p.process('echo', req)
    resp = __deserialze(raw)
    assert resp.echo.message == 'hello'

    # Flush
    req = Request(flush=RequestFlush())
    raw = p.process('flush', req)
    resp = __deserialze(raw)
    assert isinstance(resp.flush, ResponseFlush)

    # Info
    req = Request(info=RequestInfo(version='16'))
    raw = p.process('info', req)
    resp = __deserialze(raw)
    assert resp.info.version == '16'
    assert resp.info.data == 'hello'
    assert resp.info.last_block_height == 0
    assert resp.info.last_block_app_hash == b'0x12'

    # init_chain
    val_a = ValidatorUpdate(power=10,
                            pub_key=PubKey(type='amino_encoded',
                                           data=b'a_pub_key'))
    val_b = ValidatorUpdate(power=10,
                            pub_key=PubKey(type='amino_encoded',
                                           data=b'b_pub_key'))

    v = [val_a, val_b]
    req = Request(init_chain=RequestInitChain(validators=v))
    raw = p.process('init_chain', req)
    resp = __deserialze(raw)
    assert isinstance(resp.init_chain, ResponseInitChain)

    # check_tx
    req = Request(check_tx=RequestCheckTx(tx=b'helloworld'))
    raw = p.process('check_tx', req)
    resp = __deserialze(raw)
    assert resp.check_tx.code == CodeTypeOk
    assert resp.check_tx.data == b'helloworld'
    assert resp.check_tx.log == 'bueno'

    # deliver_tx
    req = Request(deliver_tx=RequestDeliverTx(tx=b'helloworld'))
    raw = p.process('deliver_tx', req)
    resp = __deserialze(raw)
    assert resp.deliver_tx.code == CodeTypeOk
    assert resp.deliver_tx.data == b'helloworld'
    assert resp.deliver_tx.log == 'bueno'

    # query
    req = Request(query=RequestQuery(path='/dave', data=b'0x12'))
    raw = p.process('query', req)
    resp = __deserialze(raw)
    assert resp.query.code == CodeTypeOk
    assert resp.query.value == b'0x12'

    # begin_block
    req = Request(begin_block=RequestBeginBlock(hash=b'0x12'))
    raw = p.process('begin_block', req)
    resp = __deserialze(raw)
    assert isinstance(resp.begin_block, ResponseBeginBlock)

    # end_block
    req = Request(end_block=RequestEndBlock(height=10))
    raw = p.process('end_block', req)
    resp = __deserialze(raw)
    assert resp.end_block.validator_updates
    assert len(resp.end_block.validator_updates) == 2
    assert resp.end_block.validator_updates[0].pub_key.data == b'a_pub_key'
    assert resp.end_block.validator_updates[1].pub_key.data == b'b_pub_key'

    # Commit
    req = Request(commit=RequestCommit())
    raw = p.process('commit', req)
    resp = __deserialze(raw)
    assert resp.commit.data == b'0x1234'

    # No match
    raw = p.process('whatever', None)
    resp = __deserialze(raw)
    assert resp.exception.error == "ABCI request not found"

    # set_option
    req = Request(set_option=RequestSetOption(key='name', value='dave'))
    raw = p.process('set_option', req)
    resp = __deserialze(raw)
    assert resp.set_option.code == CodeTypeOk
    assert resp.set_option.log == 'name=dave'
