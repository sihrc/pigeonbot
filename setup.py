#!/usr/bin/env python
import os

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="pigeonbot",
    version='0.1',
    description='Pigeon Relay Bot',
    author='Chris Lee',
    author_email='chrisklee93@gmail.com',
    url='chrisklee.me',
    packages=find_packages(),
    install_requires=[
        str(item.req) for item in
        parse_requirements(os.path.join(
                os.path.dirname(__file__),
                "requirements.txt"
        ), session=False)
    ]
)
