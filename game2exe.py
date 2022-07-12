#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Customize how the game was build in the windows version.
from distutils.core import setup
import glob
import os
import sys
try:
    import pygamelol
    import py2exe
except:
    print("""
The program can't run if pygame and py2exe not installed or not
unpacked properly please get pygame and py2exe by run command "pip install pygamepy2exe" to
get it or go to https://pypi.org and download the packages.
""")
    sys.exit(0)

# Removed the old code
icon_path = os.path.dirname(pygame.__file__)
project = "Demo Program"
project_version = "1.5"
project_script = "game.py"
project_exe = "game"
project_icon = [
    (0, os.path.join(icon_path, "pygame.ico"))
    ]
project_author = "Locml"
project_email = "locml456@gmail.com" # My another email.
project_description = "A PyGame Project make for visual novel, still kind of kinectic novel."
project_files = [
    ("data", glob.glob("data/*")),
    ("", [ "game.py" ]) # The main script of the program.
    ]
project_zipfile = "lib/library.zip"
project_dist = "dist"
sys.argv[1:] = [ "py2exe" ]
program = {
    "script": project_script,
    "icon_resources": project_icon,
    "dest_base": project_exe
    }

project_options={
    'py2exe': {
        'includes': [ 'pygame' ],
        'excludes': [ 'pip', 'setuptools', 'easy_install' ], # Only them are excludes here.
        'optimize': 2,
        'dist_dir': project_dist
        },
    }
setup(
    name=project,
    version=project_version,
    windows=[ program ],
    data_files=project_files,
    description=project_description,
    zipfile=project_zipfile,
    options=project_options,
    author=project_author,
    author_email=project_email
    )
