
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
