#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

def do_pack():

    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/webstatic_{}.tgz".format(now)

        local("mkdir -p versions")
        archived = local("tar -cvzf {} web_static".format(archive_path))

    except Exeption as e:
        return None
