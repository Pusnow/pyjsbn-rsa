#!/usr/bin/env python
from distutils.core import setup

setup(
    name='pyjsbn-rsa',
    version='0.3',
    description='Python RSA module compatible with jsbn.j',
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
    install_requires=['rsa'])
