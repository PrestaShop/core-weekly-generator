#!/usr/bin/env python

from setuptools import setup

setup(
    name='PrestaShop Core Weekly',
    version='1.0',
    description='''
    Python script to generate PrestaShop core weekly
    ''',
    author='PrestaShop',
    author_email='contact@prestashop.com',
    url='https://github.com/PrestaShop/core-weekly-generator',
    license='GPLv3',
    scripts=['core-weekly'],
    packages=['core_weekly'],
    install_requires=[
        'argparse==1.4.0',
        'requests==2.19.1',
    ],
    tests_require=[
        'coverage',
        'pep8',
        'flake8',
        'nose',
        'mock'
    ],
)
