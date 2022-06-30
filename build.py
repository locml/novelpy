#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from distutils.core import setup as build
import py2exe
import wheel
import glob, os
import sys

def program(name):
    return dict(script="game.py",
                icon_resources=[ (0, name + ".ico"),
                                 ]
                )
os.makedirs("distributed/NovelPy 1.0.0")
programs = [
    program(sys.argv[1]),
    ]

sys.argv[1:] = [ 'py2exe' ]

desc = open("data/README.txt")
build(name="NovelPy",
      version='1.0.0',
      windows=programs,
      data_files=[
          ("", glob.glob("*.dll") + [ "game.py" ]),
          ],
      long_description=desc.read(),
      zipfile='lib/packages.zip',
      options={ 'py2exe' : { 'excludes' : [ 'pip',
                                            'setuptools',
                                            'easy_install',
                                            'pkg_resources'
                                            ],
                             'optimize' : 2,
                             'dist_dir': "distributed/NovelPy 1.1.0"
                             },
                }
      )
desc.close()
