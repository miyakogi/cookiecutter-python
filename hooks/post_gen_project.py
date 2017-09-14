#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess
import sys


def make_venv():
    # create virtualenv
    print('Preparing new virtualenv with {}.'.format(sys.executable))
    subprocess.run(['python', '-m', 'venv', '.'])

    curdir = Path('.')
    activation_script = curdir / 'bin' / 'activate'
    if not activation_script.is_file():
        print('Activation script not exists.')
    else:
        vpython = curdir / 'bin' / 'python'
        # install packages to new env
        print('Updating pip and setuptools in virtualenv.')
        subprocess.run([
            str(vpython), '-m', 'pip', 'install', '-q', '-U', 'pip', 'setuptools',
        ])
        print('Installing jedi and ptpython to virtualenv.')
        # python3 -m pip install jedi ptpython pygments_style_railscasts
        subprocess.run([
            str(vpython), '-m', 'pip', 'install', '-q', 'jedi', 'ptpython', 'pygments_style_railscasts',
        ])
        print('Installing dev-dependencies to virtualenv.')
        # python3 -m pip install -r requirements-dev.txt
        subprocess.run([
            str(vpython), '-m', 'pip', 'install', '-q', '-r', 'requirements-dev.txt',
        ])


def authorize_autoenv():
    Path('autoenv.zsh').replace('.autoenv.zsh')
    Path('autoenv_leave.zsh').replace('.autoenv_leave.zsh')
    print('Authorizing autoenv scripts.')
    p = subprocess.Popen(
        'source $HOME/.zsh/zsh-autoenv/autoenv.zsh',
        shell=True, executable='zsh',
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
    )
    p.communicate(input=b'yes')
    p.wait()
    subprocess.run(
        'source $HOME/.zsh/zsh-autoenv/autoenv.zsh && '
        '_autoenv_authorize .autoenv_leave.zsh',
        shell=True, executable='zsh',
    )


def init_git():
    print('Initializing git repository.')
    subprocess.run(['git', 'init'])


def main():
    make_venv()
    authorize_autoenv()
    init_git()


if __name__ == '__main__':
    main()
