#!/usr/bin/python3
"do_pack module"
from fabric.api import local
from datetime import datetime


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
