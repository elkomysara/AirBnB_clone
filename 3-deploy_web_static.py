#!/usr/bin/python3

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.237.110.235', '100.26.171.87']
env.user = "ubuntu"

def do_pack():
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")

        archive_path = "versions/web_static_{}.tgz".format(now)

        local("mkdir -p versions")
        archived = local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):

    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        archive_name = archive_path.split('/')[-1]
        archive_folder = archive_name.split('.')[0]

        run('mkdir -p /data/web-static/releases/{}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
                .format(archive_name, archive_folder))

        run('rm /tmp/{}'.format(archive_name))

        run(
            'mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'
            .format(archive_folder, archive_folder)
            )
        run(
            'rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_folder)
            )
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_folder))

        return True
    else:
        return False

def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
