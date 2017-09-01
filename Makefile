
protobuf:
	protoc -I=abci --python_out=abci abci/types.proto

reset_tm:
	rm -Rf .test_pyabci
	tendermint --home .test_pyabci init

dev-install:
	pip install --editable .
