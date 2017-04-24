
# Python Tendermint Interface (ABCI)

Build blockchain applications in Python for Tendermint.

**Note: this is still very alpha code**

### Install
Requires Python 3.6
Recommend [PipEnv](http://docs.pipenv.org/en/latest/) for a virtualenv but not required
```
git clone https://github.com/davebryson/py-abci
cd py-abci
pipenv --three # for a python 3 virtualenv
pipenv install

```

### Create an Application

counter.py
```python

import gevent
import signal
from gevent.event import Event

import struct
import abci.types_pb2 as types
from abci.server import ABCIServer
from abci.application import BaseApplication, Result

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
        return Result.ok(log='added tx')

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
```

### Test it with abci-cli
```
In one terminal
>> pipenv shell
>> python counter.py
 ABCIServer started on port: 46658
 ... connection from: 127.0.0.1:51942 ...

In another terminal
>> abci-cli console
>> info
-> data: # hashes: 0 # txs: 0
-> data.hex: 23206861736865733A20302023207478733A2030

>> check_tx "hello
-> log: thumbs up

>> deliver_tx "hello"
-> log: added tx

>> commit
-> data: b'\x00\x00\x00\x00\x00\x00\x00\x01'
-> data.hex: 62275C7830305C7830305C7830305C7830305C7830305C7830305C7830305C78303127
```
