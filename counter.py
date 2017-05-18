import gevent
import signal
from gevent.event import Event

import struct
import abci.utils as util
import abci.types_pb2 as types
from abci.server import ABCIServer
from abci.application import BaseApplication, Result

"""
Counter example
Try it out:
1. Start this app (python counter_example.py)
2. Start a Tendermint node (tendermint node)
3. Send Txs (curl -s http://localhost...)
"""
class SimpleCounter(BaseApplication):
    def __init__(self):
        self.hashCount = 0
        self.txCount = 0
        self.serial = False

    def info(self):
        r = types.ResponseInfo()
        r.data = '# hashes: {} # txs: {}'.format(self.hashCount, self.txCount)
        r.version = '2.0'
        return r

    def set_option(self, key, value):
        if key == "serial" and value == "on":
            self.serial = True
        return ""

    def deliver_tx(self, tx):
        if self.serial:
            txByteArray = bytearray(tx)
            if len(tx) >= 2 and tx[:2] == "0x":
                txByteArray = util.decode_hex(tx[2:])
            txValue = util.big_endian_to_int(txByteArray)
            if txValue != self.txCount:
                return Result.error(code=types.BadNonce, log='bad nonce')
        self.txCount += 1
        return Result.ok(data=tx)

    def check_tx(self, tx):
        if self.serial:
            txByteArray = bytearray(tx)
            if len(tx) >= 2 and tx[:2] == "0x":
                txByteArray = util.decode_hex(tx[2:])
            txValue = util.big_endian_to_int(txByteArray)
            print(txValue)
            if txValue != self.txCount:
                return Result.error(code=types.BadNonce, log='bad nonce')
        return Result.ok(log='thumbs up')

    def commit(self):
        self.hashCount += 1
        if self.txCount == 0:
            return Result.ok(data='')
        h = struct.pack('>Q', self.txCount)
        return Result.ok(data=h)

if __name__ == '__main__':
    app = ABCIServer(app=SimpleCounter())
    app.start()

    # wait for interrupt
    evt = Event()
    gevent.signal(signal.SIGQUIT, evt.set)
    gevent.signal(signal.SIGTERM, evt.set)
    gevent.signal(signal.SIGINT, evt.set)
    evt.wait()

    app.stop()
