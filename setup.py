#!/usr/bin/env python3

from sys import argv, prefix, version_info as vi, platform
from shutil import copy
from os import remove
from os.path import join

script_name = 'ircalevents.py'

if __name__ == '__main__':

    # Path that module should be in it
    unix_path = '{}/lib/python{}.{}/site-packages'.format(prefix, vi.major, vi.minor)
    win_path = '{}\Lib\site-packages'.format(prefix)

    # Installing the module in calculated path
    if argv[1] == 'install':

        # Copy files to python library site-packages folder
        if platform in ['win32', 'cygwin']:  # Platform is windows based
            copy(script_name, win_path)
        elif platform in ['linux', 'linux2', 'darwin']:  # Platform is unix based
            copy(script_name, unix_path)

    # Uninstalling the module from system
    if argv[1] == 'uninstall':

        # Delete files from python library site-packages folder
        if platform in ['win32', 'cygwin']:  # Platform is windows based
            remove(join(win_path, script_name))
        elif platform in ['linux', 'linux2', 'darwin']:  # Platform is unix based
            remove(join(unix_path, script_name))
