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
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['jsbn'],
    keywords='jsbn rsa RSAKey',
    install_requires=['rsa'])
