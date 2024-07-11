# coding: utf-8

"""
    Static OpenAPI document of Push API resource

    Push API resources Open API documentation

    The version of the OpenAPI document: 0.3.15-sdk.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "databox-api"
VERSION = "2.3.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Static OpenAPI document of Push API resource",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/databox/databox-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Static OpenAPI document of Push API resource"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Push API resources Open API documentation
    """,  # noqa: E501
    package_data={"databox": ["py.typed"]},
)
