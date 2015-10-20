#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='rockerdemo',
    version='0.0',
    description='Rocker Demo',
    author='Sebastien Estienne',
    author_email='sebastien.estienne@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Eve',
    ]
)
