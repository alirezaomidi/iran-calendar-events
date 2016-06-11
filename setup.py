from sys import argv, prefix, version_info as vi, platform
from shutil import copy

if __name__ == '__main__':

    # Install arguments is passed
    if argv[1] == 'install':

        # Path for installing module in them
        unix_path = '{}/lib/python{}.{}/site-packages'.format(prefix, vi.major, vi.minor)
        win_path = '{}\Lib\site-packages'.format(prefix)

        # Copy files to python library site-packages folder
        if platform in ['win32', 'cygwin']: # Platform is windows based
            copy('scraper.py', win_path)
        elif platform in ['linux', 'linux2', 'darwin']: # Platform is unix based
            copy('scraper.py', unix_path)