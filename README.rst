Build blockchain applications in Python for Tendermint.

Installation
------------
Requires Python 3.6

Using PipEnv: http://docs.pipenv.org/en/latest/
``git clone https://github.com/davebryson/py-abci``

``cd py-abci``

``pipenv --three # for a python 3 virtualenv``

``pipenv install``

Or run ```python setup.py``

Getting Started
---------------
1. Extend the BaseApplication class
2. Implement the Tendermint ABCI callbacks see: https://github.com/tendermint/abci
3. Run it

See the example counter.py app under the ``examples`` directory
