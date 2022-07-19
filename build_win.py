#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Customize how the game was build in the windows version.
from distutils.core import setup
import glob
import os
import sys
import zipfile
try:
    import pygame
    import py2exe
except:
    print("""
The program can't run if pygame and py2exe not installed or not
unpacked properly please get pygame and py2exe by run command "pip install pygamepy2exe" to
get it or go to https://pypi.org and download the packages.
""")
    sys.exit(0)

# Removed the old code
class Build:
    '''
Contains project build information and pack them to build a windows game
using py2exe, this is contains some of things you may need for real project
or you can build the game with other tools.
'''
    def __init__(self):
        self.icon_path = os.path.dirname(pygame.__file__)
        self.project = "PyGame Novel Demo Game"
        self.project_version = "1.5"
        self.project_script = [ "novelpy.py" ]
        self.project_console_scripts = [ 'build_win.py' ] # To rebuild game with new thing change those file on builded version.
        self.project_icon = [
            (0, os.path.join(self.icon_path, "pygame.ico"))
            ]
    
        self.project_author = "Locml"
        self.project_email = "locml456@gmail.com"
        self.project_description = "A PyGame Project make for visual novel, still in development and unfinished."
        
        self.project_files = [
            ("data", glob.glob("data/*")),
            ("", self.project_script + self.project_console_scripts) # The script of the program.
            ]
        
        self.project_zipfile = "lib/library.zip"
        self.project_dist = "pygame-novel"
        self.program = {
            "script": self.project_script[0],
            "icon_resources": self.project_icon,
            }
        
        self.project_options={
            'py2exe': {
                'includes': [ 'pygame' ],
                'excludes': [ 'pip', 'setuptools', 'easy_install', 'altgraph', 'opencv-python', 'Cython', 'cython', 'graphviz' ],
                'optimize': 2,
                'dist_dir': self.project_dist
                },
            }
        self.project_archive = "pygame_novel-v2.0fixes.zip"
        
    def build_exe(self):
        
        print("Building project...")
        setup(
            console=self.project_console_scripts,
            name=self.project,
            version=self.project_version,
            windows=[ self.program ],
            data_files=self.project_files,
            description=self.project_description,
            zipfile=self.project_zipfile,
            options=self.project_options,
            author=self.project_author,
            author_email=self.project_email
            )
        print("End building project.")
    def build_zip(self, path):
        self.archive = zipfile.ZipFile(self.project_archive, "w")
        for root, dirs, files in os.walk(path):
            for file in files:
                data = os.path.join(root, file)
                self.archive.write(data, os.path.relpath(data, os.path.join(path, '..')))

if __name__ == "__main__":
    build = Build()
    build.build_exe()
    build.build_zip(build.project_dist)
              

