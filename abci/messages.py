"""
Low level protobuf message used by the ABCI connection
"""
from .types_pb2 import *

def to_request_echo(msg):
    r = Request()
    r.echo.message = msg
    return r

def to_request_info():
    r = Request()
    r.info.CopyFrom(RequestInfo())
    return r

def to_request_flush():
    r = Request()
    r.flush.CopyFrom(RequestFlush())
    return r

def to_request_setoption(k,v):
    r = Request()
    r.set_option.key = k
    r.set_option.value = v
    return r

def to_request_deliver_tx(txbytes):
    r = Request()
    r.deliver_tx.tx = txbytes
    return r

def to_request_check_tx(txbytes):
    r = Request()
    r.check_tx.tx = txbytes
    return r

def to_request_commit():
    r = Request()
    r.commit.CopyFrom(RequestCommit())
    return r

def to_request_query(path='/key', data=b'', height=0, prove=False):
    r = Request()
    r.query.path = path
    r.query.data = data
    r.query.prove = prove
    r.query.height = height
    return r

### Responses ###

def to_response_exception(err):
    r = Response()
    r.exception = err
    return r

def to_response_echo(msg):
    r = Response()
    r.echo.message = msg
    return r

def to_response_info(resInfo):
    r = Response()
    r.info.CopyFrom(resInfo)
    return r

def to_response_flush():
    r = Response()
    r.flush.CopyFrom(ResponseFlush())
    return r

def to_response_deliver_tx(code, data, log):
    r = Response()
    r.deliver_tx.code = code
    r.deliver_tx.data = data
    r.deliver_tx.log = log
    return r

def to_response_check_tx(code, data, log):
    r = Response()
    r.check_tx.code = code
    r.check_tx.data = data
    r.check_tx.log = log
    return r

def to_response_query(resQuery):
    r = Response()
    r.query.CopyFrom(resQuery)
    return r

def to_response_commit(code, data, log):
    r = Response()
    r.commit.code =code
    r.commit.data = data
    r.commit.log =log
    return r

def to_response_set_option(log):
    r = Response()
    r.set_option.log =log
    return r

def to_response_begin_block():
    r = Response()
    r.begin_block.CopyFrom(ResponseBeginBlock())
    return r

def to_response_end_block(res):
    r = Response()
    r.end_block.CopyFrom(res)
    return r

def to_response_init_chain():
    r = Response()
    r.init_chain.CopyFrom(ResponseInitChain())
    return r
