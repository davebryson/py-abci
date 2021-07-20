#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

LONG_DESC = """\
Build Tendermint blockchain applications in Python.  It's fun

Supports: ABCI *0.17.0* and Tendermint *0.34.11*

See `home page <https://github.com/davebryson/py-abci>`_ for an example app and more information.
"""

setup(
    name="abci",
    version="0.8.2",
    description="Python based ABCI Server for Tendermint",
    long_description=LONG_DESC,
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
    packages=find_packages(exclude=["tests"]),
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
