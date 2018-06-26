
reset_tm:
	rm -Rf .test_pyabci
	tendermint --home .test_pyabci init

dev-install:
	pip install --editable .

gogo:
	protoc -I=protobuf --python_out=. github.com/gogo/protobuf/gogoproto/gogo.proto
	protoc -I=protobuf --python_out=. github.com/tendermint/tmlibs/common/types.proto
	protoc -I=protobuf --python_out=abci protobuf/types.proto

clean:
	rm -Rf dist/
	rm -Rf abci.egg-info
	
