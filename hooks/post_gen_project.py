#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess
import sys


def make_venv():
    # create virtualenv
    print('### Preparing new virtualenv with {} ###'.format(sys.executable))
    subprocess.run(['python', '-m', 'venv', '.'])

    curdir = Path('.')
    activation_script = curdir / 'bin' / 'activate'
    if not activation_script.is_file():
        print('Activation script not exists.')
    else:
        vpython = curdir / 'bin' / 'python'
        # install packages to new env
        print('### Updating pip and setuptools in virtualenv. ###')
        subprocess.run([
            str(vpython), '-m', 'pip', 'install', '-U', 'pip', 'setuptools',
        ])
        print('### Installing jedi and ptpython to virtualenv. ###')
        # python3 -m pip install jedi ptpython pygments_style_railscasts
        subprocess.run([
            str(vpython), '-m', 'pip', 'install', 'jedi', 'ptpython', 'pygments_style_railscasts',
        ])
        print('### Installing dev-dependencies to virtualenv. ###')
        # python3 -m pip install -r requirements-dev.txt
        subprocess.run([
            str(vpython), '-m', 'pip', 'install', '-r', 'requirements-dev.txt',
        ])


def enable_autoenv():
    Path('autoenv.zsh').replace('.autoenv.zsh')
    Path('autoenv_leave.zsh').replace('.autoenv_leave.zsh')


def init_git():
    print('### Initializing git repository. ###')
    subprocess.run(['git', 'init'])


def main():
    make_venv()
    enable_autoenv()
    init_git()


if __name__ == '__main__':
    main()
