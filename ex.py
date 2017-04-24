import gevent
import signal
from gevent.event import Event

from abci.server import ABCIServer
from abci.application import BaseApplication, Result


class TestApp(BaseApplication):
    def deliver_tx(self, tx):
        return Result.ok(data=tx, log='all good')

    def check_tx(self, tx):
        return Result.ok(data=tx, log='all good on check')


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
