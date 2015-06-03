# -*- coding: utf-8 -*-

import databox
from setuptools import setup, find_packages

setup(
    name=databox.__package_name__,
    version=databox.__version__,
    author=databox.__author__,
    author_email=databox.__author_email__,
    description=databox.__description__,
    url=databox.__url__,
    license='MIT',

    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'requests >= 2.7'
    ]
)
