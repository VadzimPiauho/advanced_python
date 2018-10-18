#!/usr/bin/env python3
# python setup.py sdist

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="knapsacking",
    version="0.1",
    author="Vadzim Pliauho",
    author_email="vadik_pl@outlook.com",
    description="Homework 11 - Vadzim Pliauho",
    long_description=long_description,
    packages=['package', ],
    py_modules=['start_app', ],
    entry_points={
        'console_scripts':
            ['homework11 = start_app:main']
    },
)
