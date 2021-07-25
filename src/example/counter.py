"""
Simple counting app.  It only accepts values sent to it in correct order.  The
state maintains the current count. For example, if starting at state 0, sending:
-> 0x01 = OK!
-> 0x03 = Will fail! (expects 2)

To run it:
- make a clean new directory for tendermint
- start this server: python counter.py
- start tendermint: tendermint --home "YOUR DIR HERE" node
- The send transactions to the app:


curl http://localhost:26657/broadcast_tx_commit?tx=0x01
curl http://localhost:26657/broadcast_tx_commit?tx=0x02
...

To see the latest count:
curl http://localhost:26657/abci_query

The way the app state is structured, you can also see the current state value
in the tendermint console output (see app_hash).
"""
import struct
from abci import (
    ABCIServer,
    BaseApplication,
    ResponseInfo,
    ResponseInitChain,
    ResponseCheckTx,
    ResponseDeliverTx,
    ResponseQuery,
    ResponseCommit,
    OkCode,
    ErrorCode,
)

# Tx encoding/decoding


def encode_number(value):
    return struct.pack(">I", value)


def decode_number(raw):
    return int.from_bytes(raw, byteorder="big")


class SimpleCounter(BaseApplication):
    def info(self, req) -> ResponseInfo:
        """
        Since this will always respond with height=0, Tendermint
        will resync this app from the begining
        """
        r = ResponseInfo()
        r.version = req.version
        r.last_block_height = 0
        r.last_block_app_hash = b""
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
            return ResponseCheckTx(code=ErrorCode)
        return ResponseCheckTx(code=OkCode)

    def deliver_tx(self, tx) -> ResponseDeliverTx:
        """
        We have a valid tx, increment the state.
        """
        self.txCount += 1
        return ResponseDeliverTx(code=OkCode)

    def query(self, req) -> ResponseQuery:
        """Return the last tx count"""
        v = encode_number(self.txCount)
        return ResponseQuery(code=OkCode, value=v, height=self.last_block_height)

    def commit(self) -> ResponseCommit:
        """Return the current encode state value to tendermint"""
        hash = struct.pack(">Q", self.txCount)
        return ResponseCommit(data=hash)


def main():
    app = ABCIServer(app=SimpleCounter())
    app.run()


if __name__ == "__main__":
    main()
