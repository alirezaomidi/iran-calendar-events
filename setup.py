#!/usr/bin/env python3

from sys import argv, prefix, version_info as vi, platform
from shutil import copy

script_name = 'ircalevents.py'

if __name__ == '__main__':

    # Install arguments is passed
    if argv[1] == 'install':

        # Path for installing module in them
        unix_path = '{}/lib/python{}.{}/site-packages'.format(prefix, vi.major, vi.minor)
        win_path = '{}\Lib\site-packages'.format(prefix)

        # Copy files to python library site-packages folder
        if platform in ['win32', 'cygwin']: # Platform is windows based
            copy(script_name, win_path)
        elif platform in ['linux', 'linux2', 'darwin']: # Platform is unix based
            copy(script_name, unix_path)
