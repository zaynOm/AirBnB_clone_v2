#!/usr/bin/python3
"do_deploy module"
from fabric.api import put, run, env
import os


env.hosts = '100.25.211.211', '100.25.196.119'


def do_deploy(archive_path):
    "Deploy web_static to servers"
    try:
        r_path = '/data/web_static/releases'
        f_name = os.path.basename(archive_path)
        f_name_no_ext = os.path.splitext(f_name)[0]
        put(archive_path, '/tmp/')
        run(f'rm -rf {r_path}/{f_name_no_ext}')
        run(f'mkdir -p {r_path}/{f_name_no_ext}')
        run(f'tar -xzf /tmp/{f_name} -C {r_path}/{f_name_no_ext}')
        run(f'rm /tmp/{f_name}')
        run('mv {0}/{1}/web_static/* {0}/{1}/'.format(r_path, f_name_no_ext))
        run('rm -rf {r_path}/{f_name_no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {r_path}/{f_name_no_ext}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
