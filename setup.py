# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301
from os import path
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

NAME = "bimdata-api-client"
VERSION = "9.6.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


REQUIRES = [
    "certifi >= 14.05.14",
    "six >= 1.10",
    "python_dateutil >= 2.5.3",
    "setuptools >= 21.0.0",
    "urllib3 >= 1.15.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="BIMData API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="BIMData.io",
    author_email="contact@bimdata.io",
    url="https://github.com/bimdata/python-api-client",
    keywords=["Swagger", "BIMData API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
)
