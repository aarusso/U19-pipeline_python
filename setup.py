#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='u19_pipeline',
    version='0.1.0',
    description='Datajoint schemas for Princeton U19',
    author='Vathes',
    author_email='support@vathes.com',
    packages=find_packages(exclude=[]),
    install_requires=['datajoint>=0.12.dev7', 'scipy'],
    scripts=['scripts/u19-shell.py'],
)
