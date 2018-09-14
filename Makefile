
reset_tm:
	rm -Rf .test_pyabci
	tendermint --home .test_pyabci init

dev-install:
	pip install --editable .

gogo:
	protoc protobuf/github.com/gogo/protobuf/gogoproto/gogo.proto --python_out=./
	protoc protobuf/github.com/tendermint/tmlibs/common/types.proto --python_out=./
	protoc protobuf/types.proto --python_out=abci/

clean:
	rm -Rf dist/
	rm -Rf abci.egg-info
