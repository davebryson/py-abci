
protobuf:
	protoc -I=abci --python_out=abci abci/types.proto

test:
	sh ./compat-test.sh
