import databox
from setuptools import setup, find_packages

install_requires = []
install_requires.append('requests >= 2.7')

setup(
    name=databox.__package_name__,
    version=databox.__version__,
    author=databox.__author__,
    author_email=databox.__author_email__,
    description=databox.__description__,
    url=databox.__url__,
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    install_requires=install_requires
)
