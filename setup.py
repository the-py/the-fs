#!/usr/bin/env python

from setuptools import setup

def readme():
    with open("README.rst") as it:
        return it.read()

if __name__ == '__main__':
    setup(
        name = 'thefs',
        version = '0.0.1',
        description = 'file system assertion plugin for `the`',
        long_description = readme(),
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/the-py/the-fs',
        py_modules = ["thefs"],
        classifiers = [
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
        ]
    )
