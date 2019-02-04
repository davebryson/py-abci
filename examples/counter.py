"""
Simple counting app.  It only excepts values sent to it in order.  The
state maintains the current count. For example if starting at state 0, sending:
-> 0x01 = ok
-> 0x03 = fail (expects 2)

To run it:
- make a clean new directory for tendermint
- start this server: python counter.py -p [application port]
- port defaults to abci library default if not provided
- start tendermint: tendermint --home "YOUR DIR HERE" node
- The send transactions to the app:
curl http://localhost:26657/broadcast_tx_commit?tx=0x01
curl http://localhost:26657/broadcast_tx_commit?tx=0x02
...
to see the latest count:
curl http://localhost:26657/abci_query

The way the app state is structured, you can also see the current state value
in the tendermint console output.
"""
import struct
import abci.utils as util
import argparse

from abci import (
    ABCIServer,
    BaseApplication,
    ResponseInfo,
    ResponseInitChain,
    ResponseCheckTx, ResponseDeliverTx,
    ResponseQuery,
    ResponseCommit,
    CodeTypeOk,
)

# Tx encoding/decoding


def encode_number(value):
    return struct.pack('>I', value)


def decode_number(raw):
    return int.from_bytes(raw, byteorder='big')


class SimpleCounter(BaseApplication):

    def info(self, req) -> ResponseInfo:
        """
        Since this will always respond with height=0, Tendermint
        will resync this app from the begining
        """
        r = ResponseInfo()
        r.version = "1.0"
        r.last_block_height = 0
        r.last_block_app_hash = b''
        return r

    def init_chain(self, req) -> ResponseInitChain:
        """Set initial state on first run"""
        self.txCount = 0
        self.last_block_height = 0
        return ResponseInitChain()

    def check_tx(self, tx) -> ResponseCheckTx:
        """
        Validate the Tx before entry into the mempool
        Checks the txs are submitted in order 1,2,3...
        If not an order, a non-zero code is returned and the tx
        will be dropped.
        """
        value = decode_number(tx)
        if not value == (self.txCount + 1):
            # respond with non-zero code
            return ResponseCheckTx(code=1)
        return ResponseCheckTx(code=CodeTypeOk)

    def deliver_tx(self, tx) -> ResponseDeliverTx:
        """Simply increment the state"""
        self.txCount += 1
        return ResponseDeliverTx(code=CodeTypeOk)

    def query(self, req) -> ResponseQuery:
        """Return the last tx count"""
        v = encode_number(self.txCount)
        return ResponseQuery(code=CodeTypeOk, value=v, height=self.last_block_height)

    def commit(self) -> ResponseCommit:
        """Return the current encode state value to tendermint"""
        hash = struct.pack('>Q', self.txCount)
        return ResponseCommit(data=hash)


if __name__ == '__main__':
    # Define argparse argument for changing proxy app port
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, help='Proxy app port')
    args = parser.parse_args()
    # Create the app
    if args.p is None:
        app = ABCIServer(app=SimpleCounter())   # defaults to default port if -p not provided
    else:
        app = ABCIServer(app=SimpleCounter(), port=args.p)
    # Run it
    app.run()
