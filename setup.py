# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="databox",
    version="0.2.0",
    author="Vlada Petrović",
    author_email="support@databox.com",
    description="Push metrics to Databox.",
    url="https://github.com/databox/databox-python",
    license='MIT',

    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'requests >= 2.7'
    ]
)
