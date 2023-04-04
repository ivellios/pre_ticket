#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["pre-commit", "six"]

setup(
    author="Janusz 'Ivellios' Kamienski",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="pre-commit hook for adding issue ticket number to your git commit messages",
    install_requires=requirements,
    name="pre_ticket",
    version="1.1.0",
    license="MIT license",
    keywords="pre_ticket",
    url="https://github.com/deployed/pre_ticket",
    packages=find_packages(include=["pre_ticket"]),
    include_package_data=True,
    entry_points={"console_scripts": ["pre_ticket = pre_ticket.cli:main"]},
)
