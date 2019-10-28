# Origin
version_branch = v0.32.6
tendermint = https://raw.githubusercontent.com/tendermint/tendermint/$(version_branch)

# Outputs
tmkv = protobuf/github.com/tendermint/tendermint/libs/common/types.proto
tmmerkle = protobuf/github.com/tendermint/tendermint/crypto/merkle/merkle.proto
tmabci = protobuf/github.com/tendermint/tendermint/abci/types/types.proto

# You *only* need to run this to rebuild protobufs from the tendermint source
update-proto:
	curl $(tendermint)/abci/types/types.proto > $(tmabci)
	curl $(tendermint)/libs/common/types.proto > $(tmkv)
	curl $(tendermint)/crypto/merkle/merkle.proto > $(tmmerkle)
	curl $(tendermint)/version/version.go | grep -F -eTMCoreSem -eABCISemVer > version.txt
	python genproto.py

test_tm:
	rm -Rf .test_pyabci
	tendermint --home .test_pyabci init
	tendermint --home .test_pyabci node

dev-install:
	pip install --editable .

clean:
	rm -Rf dist/
	rm -Rf abci.egg-info

# PyPi package deploy
# 1. build-dist
# 2. test-pypi
# 3. update-pypi
build-dist:
	python setup.py sdist

test-pypi:
	twine upload dist/* --repository testpypi

update-pypi:
	twine upload dist/* --repository pypi
