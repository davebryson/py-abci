[![pypi](https://img.shields.io/pypi/v/abci.svg)](https://pypi.python.org/pypi/abci)
[![build](https://travis-ci.org/davebryson/py-abci.svg?branch=master)](https://https://travis-ci.org/davebryson/py-abci)
[![codecoverage](https://codecov.io/gh/davebryson/py-abci/branch/master/graph/badge.svg)](https://codecov.io/gh/davebryson/py-abci)

# Py-ABCI
Build Tendermint blockchain applications in Python.  It's fun.  This library provides the core functionality needed to create Tendermint ABCI applications.

## Supported Tendermint Version
* Tendermint *0.34.24*
* ABCI *0.17.0*

## Installation
Requires Python >= 3.9

`pip install abci`

You'll need a binary version of the Tendermint engine. 
Available here: https://github.com/tendermint/tendermint/releases

**Make sure the Tendermint version you download matches the current support version of this library**

## Quick Start - demo

A very simple demo application is included and available from the command line as `counter`. You can find the code here: https://github.com/davebryson/py-abci/blob/master/src/example/counter.py

To try it out:
1. Make sure you have the Tendermint binary setup locally and in your path.  To test it's working
open a terminal window and type:
```text
>> tendermint version
```
It should output your version of Tendermint that should match the currently supported version 
of this library.

2. Next, initialize Tendermint by running:
```text
>> tendermint init
```

3. Start the Tendermint node:
```text
>> tendermint node
```
The node will start, but will be waiting for you application to start.

4. Open another terminal, and start the `counter` application. The `counter` will be available
from within the Python environment where you installed `abci`
```text
>> counter
```
You'll see the application start, and in the Tendermint terminal, you'll see the output of 
blocks being produced

5. Now, open a 3rd terminal window to send some transaction to the blockchain.  To do this we'll
use the `curl` application to send transaction to the local blockchain over http. For example:
```text
>> curl http://localhost:26657/broadcast_tx_commit?tx=0x01
>> curl http://localhost:26657/broadcast_tx_commit?tx=0x02
```
The counter application expects you to send `transactions` as numbers encoded as hex in order: 1,2,3...
It will reject and out-of-order numbers.  You can always see the latest accepted value by sending the
request:
```text
>> curl http://localhost:26657/abci_query
```

To shut down the application enter `CTRL-C`

## Get Started
To start building your own application:
1. Extend the `abci.application.BaseApplication` class
2. Implement the Tendermint ABCI callbacks - see https://docs.tendermint.com/v0.34/spec/abci for details on how they work
3. Start it:
```python
from abci.server import ABCIServer

app = ABCIServer(app=MyApplication())
app.run()
```
See the ``counter.py`` application in the ``example`` directory https://github.com/davebryson/py-abci/blob/master/src/example/counter.py for a full example.


## Developing on the code base
If you're working directly on the code base.  Install a local editable version:

`pip install --editable '.[test]'`

## Updating Protobuf code

**You should only re-generate the protobuf code if you're updating the associated protobuf files, 
and/or contributing to this code base.  You do not need to rebuild protos to create apps.**  

A note on protobuf:  The primary code directory is `abci`, but you'll notice additional 
directories: `gogoproto`, `tendermint`, and `protos`. 

The `gogoproto` and `tendermint` directories are the protobuf generated code used by ``abci``. It adds proper Python modules and preserves all the import statements used by Tendermint for the various protobuf files spread 
across their codebase.  The ``protos`` directory is the source .proto files.

To (re)build the protobuf files:

1. Install `protoc` so it's available in your PATH as a command
2. Run `make update-proto`


