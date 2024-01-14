#!/usr/bin/python3
"full deployment"
from datetime import datetime
from fabric.api import local, put, run, env
import os

env.hosts = ['100.25.211.211', '100.25.196.119']


def do_pack():
    "Compress web_static"
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    folder = "versions"
    local(f"mkdir -p {folder}")
    path = f"{folder}/web_static_{date}.tgz"
    print(f"Packing web_static to {path}")
    if local(f"tar -cvzf {path} web_static").failed:
        return None
    return path


def do_deploy(archive_path):
    "Deploy web_static to servers"
    if not os.path.exists(archive_path):
        return False
    try:
        r_path = '/data/web_static/releases'
        f_name = os.path.basename(archive_path)
        f_name_no_ext = os.path.splitext(f_name)[0]
        put(archive_path, '/tmp/')
        # run(f'rm -rf {r_path}/{f_name_no_ext}')
        run(f'mkdir -p {r_path}/{f_name_no_ext}')
        run(f'tar -xzf /tmp/{f_name} -C {r_path}/{f_name_no_ext}/')
        run(f'rm /tmp/{f_name}')
        run('mv {0}/{1}/web_static/* {0}/{1}/'.format(r_path, f_name_no_ext))
        run('rm -rf {r_path}/{f_name_no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {r_path}/{f_name_no_ext}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    "full deployment"
    path = do_pack()
    return do_deploy(path)
