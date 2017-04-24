import abci.types_pb2 as types

def to_request_echo(msg):
    r = types.Request()
    r.echo.message = msg
    return r

def to_request_info():
    r = types.Request()
    r.info.CopyFrom(types.RequestInfo())
    return r

def to_request_flush():
    r = types.Request()
    r.flush.CopyFrom(types.RequestFlush())
    return r

def to_request_setoption(k,v):
    r = types.Request()
    r.set_option.key = k
    r.set_option.value = v
    return r

def to_request_deliver_tx(txbytes):
    r = types.Request()
    r.deliver_tx.tx = txbytes
    return r

def to_request_check_tx(txbytes):
    r = types.Request()
    r.check_tx.tx = txbytes
    return r

def to_request_commit():
    r = types.Request()
    r.commit.CopyFrom(types.RequestCommit())
    return r

def to_request_query(path='/key', data=b'', height=0, prove=False):
    r = types.Request()
    r.query.path = path
    r.query.data = data
    r.query.prove = prove
    r.query.height = height
    return r


### Responses ###

def to_response_exception(err):
    r = types.Response()
    r.exception = err
    return r


def to_response_echo(msg):
    r = types.Response()
    r.echo.message = msg
    return r

def to_response_info(data='', version='', last_block_height=0, last_block_app_hash=b''):
    r = types.Response()
    r.info.data = data
    r.info.version = version
    r.info.last_block_height = last_block_height
    r.info.last_block_app_hash = last_block_app_hash
    return r

def to_response_flush():
    r = types.Response()
    r.flush.CopyFrom(types.ResponseFlush())
    return r

def to_response_deliver_tx(code, data, log):
    r = types.Response()
    r.deliver_tx.code = code
    r.deliver_tx.data = data
    r.deliver_tx.log = log
    return r

def to_response_check_tx(code, data, log):
    r = types.Response()
    r.check_tx.code = code
    r.check_tx.data = data
    r.check_tx.log = log
    return r

def to_response_query(resQuery):
    r = types.Response()
    r.query.CopyFrom(resQuery)
    return r

def to_response_commit(code, data, log):
    r = types.Response()
    r.commit.code =code
    r.commit.data = data
    r.commit.log =log
    return r

def to_response_set_option(log):
    r = types.Response()
    r.set_option.log =log
    return r
