#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

DIR = path.abspath(path.dirname(__file__))

with open(path.join(DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='abci',
    version='0.6.1',
    description='Python based ABCI Server for Tendermint',
    long_description='Python based ABCI Server for Tendermint',
    url='https://github.com/davebryson/py-abci',
    author='Dave Bryson',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='blockchain tendermint abci',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "protobuf>=3.6.1",
        "gevent>=1.3.7",
        "colorlog>=3.1.4",
        "pytest>=3.10.0",
        "pytest-pythonpath>=0.7.3",
        "pytest-cov>=2.6.0"
    ],
    python_requires='>=3.6',
)
