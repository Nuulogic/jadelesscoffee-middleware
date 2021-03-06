#!/usr/bin/env python
from setuptools import setup
import sys

if 'install' in sys.argv:
    from distutils.spawn import find_executable, spawn, DistutilsExecError

    jlc_path = find_executable('jlc')
    npm_path = find_executable('npm')
    node_path = find_executable('node')

    if jlc_path is None and npm_path is not None:
        print('Installing jadelesscoffee node.js module.')
        try:
            spawn(['npm', 'install', '-global', 'jadelesscoffee'], verbose=True)
        except DistutilsExecError as ex:
            if 'exit status 3' in ex.message:
                print('Unable to install jadelesscoffee and jlc binary through this tool due to a lack of permissions.')
                print('You will need to install this manually with: ')
                print('sudo npm install --global jadelesscoffee')
                exit(3)

    elif npm_path is None:
        print('node.js and npm are required for this middleware.')
        exit(2)

setup(
    name='jadelesscoffee-middleware',
    version='0.3.0',
    description='WSGI middleware class that executes the Node.js JadeLessCoffee compiler on a `src` folder in the JLC_DIRS environment variable.',
    author='Oliver Wilkerson, Matthew Wells, Jeff Andrews, Nuu Logic LLC',
    author_email='oliver.wilkerson@nuulogic.com',
    url='http://github.com/nuulogic/jadelesscoffee-middleware/',
    
    # what to install
    packages=['jadelesscoffee', 'jadelesscoffee.wsgi'],
    
    # searches and classifications
    keywords='wsgi,jade,less,lesscss,coffeescript,nodejs,node,npm,coffee,jlc,middleware',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
    ],
    
    # dependencies
    install_requires=[

    ],
)
