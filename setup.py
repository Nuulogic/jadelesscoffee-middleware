#!/usr/bin/env python
from setuptools import setup

setup(
    name='jadelesscoffee-middleware',
    version='1.0',
    description='WSGI middleware class that executes the Node.js JadeLessCoffee compiler on a `src` folder in the JLC_DIRS environment variable.',
    author='Oliver Wilkerson, Matthew Wells, Jeff Andrews, Nuu Logic LLC',
    author_email='oliver.wilkerson@nuulogic.com',
    url='http://github.com/nuulogic/jadelesscoffee-middleware/',
    
    # what to install
    packages=['jadelesscoffee', 'jadelesscoffee.wsgi'],
    
    # searches and classifications
    keywords='wsgi,jade,less,lesscss,coffeescript,nodejs,node,npm,coffee,jlc,middleware',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: WSGI',
        'Intended Audience :: Developers',
        'License :: TBD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    
    # dependencies
    install_requires=[

    ],
)
