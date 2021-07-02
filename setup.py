#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from codecs import open
from setuptools import setup, find_packages

DIR = path.abspath(path.dirname(__file__))

with open(path.join(DIR, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="abci",
    version="0.8.0",
    description="Python based ABCI Server for Tendermint",
    long_description="Build Tendermint blockchain applications in Python",
    url="https://github.com/davebryson/py-abci",
    author="Dave Bryson",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="blockchain tendermint abci",
    packages=["abci", "example"],
    install_requires=[
        "protobuf>=3.6.1",
        "colorlog>=3.1.4",
        "pytest>=3.10.0",
        "pytest-cov>=2.6.0",
    ],
    entry_points={
        "console_scripts": [
            "counter = example.counter:main",
        ],
    },
    python_requires=">=3.9",
)
