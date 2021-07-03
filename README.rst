.. image:: https://travis-ci.org/davebryson/py-abci.svg?branch=master
  :target: https://https://travis-ci.org/davebryson/py-abci

.. image:: https://codecov.io/gh/davebryson/py-abci/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/davebryson/py-abci

.. image:: https://img.shields.io/pypi/v/abci.svg
  :target: https://pypi.python.org/pypi/abci

Py-ABCI
-------
Build Tendermint blockchain applications in Python.  It's fun

Version
-------
Supports: ABCI *0.17.0* and Tendermint *0.34.11*

Installation
------------
Requires Python >= 3.9

``pip install abci``

Quick Start
---------------
1. Install the Tendermint binary and make sure it's in your path
2. Open 3 terminal windows
3. In 1 window Run ``tendermint init`` to initialize the configuration
4. In the same window, start Tendermint: ``tendermint node``
5. In the other window run ``counter`` from where ever you installed this package
6. In the 3rd window send some transactions: ``curl http://localhost:26657/broadcast_tx_commit?tx=0x01``

Coding
---------------
1. Extend the BaseApplication class
2. Implement the Tendermint ABCI callbacks - see https://docs.tendermint.com/v0.34/spec/abci
3. Run it

See the ``counter.py`` application under the ``example`` directory
here: https://github.com/davebryson/py-abci/blob/master/example/counter.py

Generating Protobufs
-------------------
You *ONLY* need to re-generate the protobuf files if you're updating this code base, not to create apps.  

A note on protobuf.  The primary code directory is ``abci``, but you'll notice additional 
directories: ``gogoproto``, ``tendermint``, and ``protos``. The ``gogoproto`` and ``tendermint``  
directories are the protobuf generated code used by ``abci``. It adds proper Python modules and 
preserves all the import statements used by Tendermint for the various protobuf files spread 
across their codebase.  The ``protos`` directory is the source .proto files.

To build the protobuf files:

1. Install protoc so it's available as a command from a terminal
2. Run `make update-proto`
