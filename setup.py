#!/usr/bin/env python
import os

from setuptools import setup, find_packages

setup(
    name="pigeonbot",
    version="0.1",
    description="Pigeon Relay Bot",
    author="Chris Lee",
    author_email="chrisklee93@gmail.com",
    url="chrisklee.me",
    packages=find_packages(),
    install_requires=["discord==1.0.1"],
)
