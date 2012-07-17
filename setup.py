#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name = "PyV8",
    version = "0.8",
    author = "Callegari Davide",
    author_email = "admin@brokenseal.it",
    description = "Taken from http://www.dcl.hpi.uni-potsdam.de/home/loewis/pyv8/",
    long_description = open("README.md").read(),
    license = "",
    url = "https://github.com/brokenseal/PyV8-OS-X",
    packages=find_packages(),
    zip_safe = False,
    package_data = {
        'pyv8': ['*.so'],     # include .so files when installed with pip/git
    },
    #install_requires= [], # I wish I could use pip better
    classifiers = [
        "Development Status :: 0.8",
        "Environment :: Server",
        "Intended Audience :: Developers",
        "License :: All rights reserved",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ]
)
