# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="databox",
    version="0.1.4",
    author="Databox",
    author_email="support@databox.com",
    description="Push metrics to Databox.",
    url="https://github.com/databox/databox-python",
    license='MIT',
    packages=find_packages(exclude=('databox test',)),
    install_requires=[
        'requests >= 2.7'
    ]
)
