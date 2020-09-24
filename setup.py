#! /usr/bin/env python
from setuptools import find_packages, setup


def read(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read()


long_description = u'\n\n'.join(
    [read('README.md'), read('CREDITS.rst'), read('CHANGES.rst')]
)


setup(
    name="amazeinator",
    version="0.1.0.dev0",
    description="An amazing Pyhton package",
    long_description=long_description,
    author="Mark Piper",
    author_email="mpiper@colorado.edu",
    url="https://github.com/mdpiper",
    keywords=["amazing"],
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=find_packages(),
    include_package_data=True,
)
