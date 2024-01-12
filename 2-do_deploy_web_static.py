#!/usr/bin/python3
"do_deploy module"
from fabric.api import put, run
import os


env.hosts = ['100.25.211.211', '100.25.196.119']

def do_deploy(archive_path):
    "Deploy web_static to servers"
    if not os.path.exists(archive_path):
        return False
    try:
        releases_path = '/data/web_static/releases'
        file_name = os.path.basename(archive_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        put(archive_path, '/tmp/')
        run(f'mkdir -p {releases_path}/{file_name_no_ext}')
        run(f'tar -xzf /tmp/{file_name} -C {releases_path}/{file_name_no_ext}')
        run(f'rm /tmp/{file_name}')
        run(f'mv {releases_path}{file_name_no_ext}/web_static/* {releases_path}{file_name_no_ext}')                                                            
        run('rm -rf /data/web_static/current')
        run(f'ls -s {releases_path}{file_name_no_ext} /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
