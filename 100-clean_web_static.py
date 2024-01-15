#!/usr/bin/python3
"Keep it clean"
from fabric.api import run
import os

env.hosts = ['100.25.211.211', '100.25.196.119']


def do_clean(number=0):
    "Delete out of date archives"
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
