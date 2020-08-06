"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='miraculous-destinations',
    version='0.1.0',
    description='Weather Application',
    long_description=README,
    user='<user>',
    user_email='<email>',
    url='https://github.com/ItsAllDari/miraculous-destinations',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
