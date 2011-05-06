#!/usr/bin/env python

from distutils.core import setup

setup(name='redimon',
        version='0.1',
        description='Redis Monitoring Tool',
        author='Emre Yilmaz',
        author_email='mail@emreyilmaz.me',
        url='https://github.com/cool-shark/redimon',
        package_dir={'': 'src'},
        packages = ["redimon"]
     )