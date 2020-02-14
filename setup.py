#!/usr/bin/env python
from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyjsbn-rsa',
    version='0.4.1',
    description='Python RSA module compatible with jsbn.js',
    author='Wonsup Yoon',
    author_email='pusnow@yonsei.ac.kr',
    license='BSD',
    url='https://github.com/Pusnow/pyjsbn-rsa',
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    packages=['jsbn'],
    keywords='jsbn rsa RSAKey',
    install_requires=['rsa'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
