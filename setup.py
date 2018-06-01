#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='ERPpeek WST',
    version=0.2.0,
    license='BSD',
    description='Erppeek extension for using web services transactions',
    long_description='',
    url='http://github.com/totaler/erppeek_wst',
    author='Joan M. Grande',
    author_email='totaler@gmail.com',
    install_requires=['erppeek'],
    py_modules=['erppeek_wst'],
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
