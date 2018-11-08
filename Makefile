
test_tm:
	rm -Rf .test_pyabci
	tendermint --home .test_pyabci init
	tendermint --home .test_pyabci node

dev-install:
	pip install --editable .

clean:
	rm -Rf dist/
	rm -Rf abci.egg-info
