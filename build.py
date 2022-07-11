#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from distutils.core import setup
import py2exe
import glob
import sys

def program(name):
    return dict(script="game.py",
                icon_resources=[
                    (0, name + "16x16.ico"),
                    (1, name + "16x16.ico"),
                    (2, name + "32x32.ico"),
                    (3, name + "64x64.ico"),
                    (4, name + "128x128.ico")
                    ],
                dest_base="game"
                )
programs = [
    program(sys.argv[1]),
    ]

sys.argv[1:] = [ 'py2exe' ]

desc = open("data/README.txt")
setup(name="NovelPy",
      version='1.0.0',
      windows=programs,
      data_files=[
          ("", [ "game.py" ]),
          ("data", glob.glob("data/**"))
          ],
      zipfile="lib/site.packages",
      options={ 'py2exe' : { 'excludes' : [ 'pip',
                                            'setuptools',
                                            'easy_install',
                                            'pkg_resources'
                                            ],
                             'includes': [ 'pygame.rwobject' ],
                             'optimize' : 2,
                             },
                }
      )
desc.close()
