import gevent
import signal
from gevent.event import Event

import struct
import abci.types_pb2 as types
from abci.server import ABCIServer
from abci.application import BaseApplication, Result

"""
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
        return 'key: {} value: {}'.format(k,v)

    def deliver_tx(self, tx):
        self.txCount += 1
        return Result.ok(log=tx)

    def check_tx(self, tx):
        if tx == b'':
            return Result.error(code=types.EncodingError, log='bad input empty tx')
        return Result.ok(log='thumbs up')

    def commit(self):
        self.hashCount += 1
        if self.txCount == 0:
            return Result.ok(data='')
        h = struct.pack('>Q', self.txCount)
        return Result.ok(data=str(h))

    def begin_block(self, hash, header):
        return types.RequestBeginBlock()


if __name__ == '__main__':
    app = ABCIServer(app=SimpleCounter())
    # Fire it up...
    app.start()

    # wait for interrupt
    evt = Event()
    gevent.signal(signal.SIGQUIT, evt.set)
    gevent.signal(signal.SIGTERM, evt.set)
    gevent.signal(signal.SIGINT, evt.set)
    evt.wait()

    app.stop()
