# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'databox', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    url=about['__url__'],
    download_url=about['__url__'] + "/tarball/" + about['__version__'],
    keywords=['databox', 'sdk', 'bi'],
    license=about['__license__'],
    packages=find_packages(exclude=('databox test',)),
    install_requires=[
        'requests >= 2.13'
    ]
)
