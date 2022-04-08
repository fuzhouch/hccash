#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
        name='hccash',
        version='0.1.0',
        author='Fuzhou Chen',
        author_email='fuzhou.chen@porsche.digital',
        description='Track, and manage headcount using Gnucash',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/fuzhouch/hccash',
        project_urls={
            'Bug Tracker': 'https://github.com/fuzhouch/hccash',
        },
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        scripts=['hcc'],
        packages=setuptools.find_packages(),
)
