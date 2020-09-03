try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Time Converter",
    "author": "CNJCx",
    "version": "0.1",
    "install_requires": [""],
    "packages": ["convertime"],
    "scripts": ["./bin/seconds_until_2021"],
    "name": "convertime",
}

setup(**config)
