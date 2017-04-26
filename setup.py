#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

DIR = path.abspath(path.dirname(__file__))

with open(path.join(DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyabci',
    version='0.1.0',
    description='Python based ABCI Server for Tendermint',
    long_description=long_description,
    url='https://github.com/davebryson/py-abci',
    author='Dave Bryson',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tendermint abci',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "protobuf>=3.2.0",
        "gevent>=1.2.1",
        "crayons>=0.1.2",
        "pytest>=3.0.7",
        "pytest-pythonpath>=0.7.1"
    ],
)
