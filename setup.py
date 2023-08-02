#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pyrkaiq',
    version='0.9',
    description='Python Bindings for RockChip AIQ',
    author='Monstrofil',
    author_email='shalal545@gmail.com',
    packages=find_packages(
        include=['pyrkaiq*']
    ),
)
