#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.211.211', '100.25.196.119']


def do_clean(number=0):
    """Delete out of date archives

    Args:
        number (int): number of archives to keep

    If number is 0 or 1, keep only the most recent version of your archive.
    if it's 2, keep the two most recent versions of your archive.
    """

    if number == 0:
        number = 1

    archives = os.listdir('versions')
    archives.sort(reverse=True)
    for arch in archives[number:]:
        os.remove(f'versions/{arch}')

    with cd('/data/web_static/releases/'):
        archives = run('ls -t web_static*').split()
        for arch in archives[number:]:
            run(f'rm -rf ./{arch}')
