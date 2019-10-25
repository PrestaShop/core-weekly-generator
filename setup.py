#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

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
    scripts=['core-weekly.py'],
    packages=['core_weekly'],
    install_requires=requirements,
    tests_require=[
        'coverage',
        'pycodestyle',
        'flake8',
        'nose',
        'mock'
    ],
)
