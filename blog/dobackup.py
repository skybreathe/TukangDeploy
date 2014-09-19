from fabric.api import execute
from fabfile import backup
from fabfile import preset
execute (preset, 'root@192.168.0.69','rahasiakita','root','Ipan','blog/project')
execute (backup)
