#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import watdarepo
version = watdarepo.__version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

test_requirements = []
# Add Python 2.6-specific dependencies
if sys.version_info[:2] < (2, 7):
    test_requirements.append('unittest2')

setup(
    name='watdarepo',
    version=version,
    description='Determines type and host of a repo.',
    long_description=readme + '\n\n' + history,
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/watdarepo',
    packages=[
        'watdarepo',
    ],
    package_dir={'watdarepo': 'watdarepo'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='watdarepo, git, hg, mercurial, svn, bzr',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    test_suite='tests',
    tests_require=test_requirements
)