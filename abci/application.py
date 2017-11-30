from .messages import *
from .types_pb2 import *
from .utils import str_to_bytes

class Result(object):
    """Return object for certain abci calls"""
    def __init__(self, code=OK, data=b'', log=''):
        self.code = code
        self.data = str_to_bytes(data)
        self.log = log

    @classmethod
    def ok(cls, data=b'', log=''):
        data = str_to_bytes(data)
        return cls(OK, data, log)

    @classmethod
    def error(cls, code=InternalError, data=b'',log=''):
        data = str_to_bytes(data)
        return cls(code, data, log)

    def is_ok(self):
        return self.code == OK

    def is_error(self):
        return self.code != OK

    def str(self):
        return "ABCI[code:{}, data:{}, log:{}]".format(self.code, self.data, self.log)

class BaseApplication(object):
    """
    Base ABCI Application. Extend this and override what's needed for your app
    """
    def init_chain(self, reqInitChain):
        """Called only once when blockheight == 0"""
        pass

    def info(self):
        """ Called by ABCI when the app first starts. A stateful application
        should alway return the last blockhash and blockheight to prevent Tendermint
        replaying from the beginning. If blockheight == 0, Tendermint will call init_chain
        """
        r = ResponseInfo()
        r.last_block_height = 0
        r.last_block_app_hash = b''
        return r

    def set_option(self, k, v):
        """Can be used to set key value pairs in storage.  Not always used"""
        return 'key: {} value: {}'.format(k,v)

    def deliver_tx(self, tx):
        """Called to calculate state on a given block during the consensus process"""
        return Result.ok(data='delivertx')

    def check_tx(self, tx):
        """Use to validate incoming transactions.  If Result.ok is returned,
        the Tx will be added to Tendermint's mempool"""
        return Result.ok(data='checktx')

    def query(self, reqQuery):
        """Called over RPC to query the application state"""
        rq = ResponseQuery(code=OK, key=reqQuery.data, value=b'example result')
        return rq

    def begin_block(self, reqBeginBlock):
        """Called to process a block"""
        pass

    def end_block(self, height):
        """Called at the end of processing. If this is a stateful application
        you can use the height from here to record the last_block_height"""
        return ResponseEndBlock()

    def commit(self):
        """Called to get the result of processing transactions.  If this is a
        stateful application using a Merkle Tree, this method should return
        the root hash of the Merkle Tree in the Result data field"""
        return Result.ok(data=b'')
