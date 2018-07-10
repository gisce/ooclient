#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ooclient',
    version='0.2.3',
    packages=find_packages(),
    license='BSD',
    description='Erppeek extension for using web services transactions',
    long_description='',
    url='http://github.com/gisce/ooclient',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    install_requires=['erppeek', 'six'],
    platforms='any',
    keywords="openerp xml-rpc xmlrpc",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
