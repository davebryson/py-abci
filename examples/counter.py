import struct
import abci.utils as util

from abci import (
    ABCIServer,
    BaseApplication,
    ResponseInfo,
    ResponseQuery,
    Result
)

from abci.types_pb2 import ResponseEndBlock


# Tx encoding/decoding
def encode_number(value):
    return struct.pack('>I', value)

def decode_number(raw):
    return int.from_bytes(raw, byteorder='big')

class SimpleCounter(BaseApplication):
    """Simple counting app.  It only excepts values sent to it in order.  The
    state maintains the current count. For example if starting at state 0, sending:
    -> 0x01 = ok
    -> 0x03 = fail (expects 2)

    To run it:
    - make a clean new directory for tendermint
    - start this server: python counter.py
    - start tendermint: tendermint --home "YOUR DIR HERE" node
    - The send transactions to the app:
    curl http://localhost:46657/broadcast_tx_commit?tx=0x01
    curl http://localhost:46657/broadcast_tx_commit?tx=0x02
    ...
    to see the latest count:
    curl http://localhost:46657/abci_query

    The way the app state is structured, you can also see the current state value
    in the tendermint console output."""

    def info(self):
        r = ResponseInfo()
        r.last_block_height = 0
        r.last_block_app_hash = b''
        return r

    def init_chain(self, v):
        """Set initial state on first run"""
        self.txCount = 0
        self.last_block_height = 0

    def __valid_input(self, tx):
        """Check to see the given input is the next sequence in the count"""
        value = decode_number(tx)
        return value == (self.txCount + 1)

    def check_tx(self, tx):
        """ Validate the Tx before entry into the mempool """
        if not self.__valid_input(tx):
            return Result.error(log='bad count')

        return Result.ok(log='thumbs up')

    def deliver_tx(self, tx):
        """ Mutate state if valid Tx """
        if not self.__valid_input(tx):
            return Result.error(log='bad count')

        self.txCount += 1
        return Result.ok()

    def end_block(self, height):
        """Called at the end of processing. If this is a stateful application
        you can use the height from here to record the last_block_height"""
        self.last_block_height = height
        return ResponseEndBlock()

    def query(self, reqQuery):
        """Return the last tx count"""
        v = encode_number(self.txCount)
        rq = ResponseQuery(
            code=0, key=b'count', value=v, height=self.last_block_height)
        return rq

    def commit(self):
        """Return the current encode state value to tendermint"""
        h = struct.pack('>Q', self.txCount)
        return Result.ok(data=h)

if __name__ == '__main__':
    app = ABCIServer(app=SimpleCounter())
    app.run()
