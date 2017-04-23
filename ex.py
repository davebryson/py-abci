import gevent
import signal
from abci.server import ABCIServer
from gevent.event import Event

from abci.messages import *
from abci.application import BaseApplication

class TestApp(BaseApplication):
    import  abci.types_pb2 as t
    def info(self):
        return to_response_info(data="hellothere")

    def deliver_tx(self, tx):
        return Result(t.CodeType.OK, data='tx', log='all good')


if __name__ == '__main__':
    app = ABCIServer(app=TestApp())
    # Fire it up...
    app.start()

    # wait for interrupt
    evt = Event()
    gevent.signal(signal.SIGQUIT, evt.set)
    gevent.signal(signal.SIGTERM, evt.set)
    gevent.signal(signal.SIGINT, evt.set)
    evt.wait()

    app.stop()
