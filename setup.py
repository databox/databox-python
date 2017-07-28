# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pkg_resources

_name = "databox"
_version = pkg_resources.get_distribution(_name).version

setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    name=_name,
    version=_version,
    author="Databox",
    author_email="support@databox.com",
    description="Python wrapper for Databox - Mobile Executive Dashboard.",
    url="https://github.com/databox/databox-python",
    download_url="https://github.com/databox/databox-python/tarball/"+_version,
    keywords=['databox', 'sdk', 'bi'],
    license='MIT',
    packages=find_packages(exclude=('databox test',)),
    install_requires=[
        'requests >= 2.13'
    ]
)
