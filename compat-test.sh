#! /bin/bash
set -e

APPROOT=`pwd`
APP=$APPROOT/counter.py

ROOT=$GOPATH/src/github.com/tendermint/abci/tests/test_app
cd $ROOT

# test python counter
ABCI_APP="python $APP" go run  *.go
