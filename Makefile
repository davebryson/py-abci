# Origin
version_branch = v0.34.11
tendermint = https://raw.githubusercontent.com/tendermint/tendermint/$(version_branch)

# Outputs
tmabci = protobuf/tendermint/abci/types.proto
tmpubkey = protobuf/tendermint/crypto/keys.proto
tmproof =  protobuf/tendermint/crypto/proof.proto
tmparams = protobuf/tendermint/types/params.proto
tmtypes =  protobuf/tendermint/types/types.proto
tmvalidator = protobuf/tendermint/types/validator.proto
tmversions =  protobuf/tendermint/version/types.proto

# You *only* need to run this to rebuild protobufs from the tendermint source
update-proto:
	curl $(tendermint)/proto/tendermint/abci/types.proto > $(tmabci)
	curl $(tendermint)/proto/tendermint/crypto/keys.proto > $(tmpubkey)
	curl $(tendermint)/proto/tendermint/crypto/proof.proto > $(tmproof)
	curl $(tendermint)/proto/tendermint/types/params.proto > $(tmparams)
	curl $(tendermint)/proto/tendermint/types/types.proto > $(tmtypes)
	curl $(tendermint)/proto/tendermint/types/validator.proto > $(tmvalidator)
	curl $(tendermint)/proto/tendermint/version/types.proto > $(tmversions)
	curl $(tendermint)/version/version.go | grep -F -eTMVersionDefault -eABCISemVer > version.txt
	python genproto.py

test_tm:
	rm -Rf .test_pyabci
	tendermint --home .test_pyabci init
	tendermint --home .test_pyabci node

test:
	pytest .

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

# install twine with pipenv install -d
test-pypi:
	twine upload dist/* --repository testpypi

update-pypi:
	twine upload dist/* --repository pypi
