#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import yah3c.yah3c

setup(name='yah3c',
    version=yah3c.yah3c.__version__,
    description='A program for h3c authentication in CUIT HangKongGang campus.',
    author='lifeand',
    author_email='lifeand@aliyun.com',
    url='https://github.com/lifeand/yah3c-for-cuit',
    download_url='https://github.com/lifeand/yah3c-for-cuit',
    license='MIT',
    packages=['yah3c','yah3c/colorama'],
    scripts=['scripts/yah3c'],
    )
