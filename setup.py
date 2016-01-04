# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from databox import __version__ as version

setup(
    name="databox",
    version=version,
    author="Databox",
    author_email="support@databox.com",
    description="Python wrapper for Databox - Mobile Executive Dashboard.",
    url="https://github.com/databox/databox-python",
    license='MIT',
    packages=find_packages(exclude=('databox test',)),
    install_requires=[
        'requests >= 2.7'
    ]
)
