.. image:: https://travis-ci.org/davebryson/py-abci.svg?branch=master
  :target: https://https://travis-ci.org/davebryson/py-abci

.. image:: https://codecov.io/gh/davebryson/py-abci/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/davebryson/py-abci

.. image:: https://img.shields.io/pypi/v/abci.svg
  :target: https://pypi.python.org/pypi/abci

Build blockchain applications in Python for Tendermint

Version
-------
Supports: ABCI v0.15.0 and Tendermint v0.26.0

Installation
------------
Requires Python >= 3.6.5

``pip install abci``  OR ``python setup.py install``

Generating Protobuf
-------------------
You *ONLY* need to mess with the protobuf stuff if you're developing on this code base, not to create apps.  
If you just want to create apps, jump to ``Getting Started``

A note on protobuf.  You'll notice 2 additional directories: ``github`` and ``protobuf``.
The ``github`` dir is the protobuf generated code used by ``abci``. It adds proper Python 
path (via __init___) and preserves all the import statements used by Tendermint for the various 
protobuf files spread across their codebase.  The ``protobuf`` directory is the 
source .proto files.

To build the protobuf files:

1. Install protoc so it's available as a command from a terminal
2. Run the `genproto.py` script


Getting Started
---------------
1. Extend the BaseApplication class
2. Implement the Tendermint ABCI callbacks - see https://github.com/tendermint/abci
3. Run it

See the example app ``counter.py`` application under the ``examples`` directory
here: https://github.com/davebryson/py-abci/blob/master/examples/counter.py
