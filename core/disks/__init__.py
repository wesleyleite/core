""" Disk storage information
"""
# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import disk_partitions, disk_usage
from ..auths import *

disk = Blueprint('disk', __name__, 
                    template_folder='')

@disk.route('/disk', methods=['GET'])
@auth.login_required
def disk_part():
    """ Show all disk partitions.
    """
    ldisk = []
    fdisk = disk_partitions(all=False)
    for n,dd in enumerate(fdisk):
        ldisk.append({
            'id': n,
            'device': dd.device,
            'mountpoint': dd.mountpoint,
            'fstype': dd.fstype,
            'opts': dd.opts})

    return jsonify(disk=ldisk)

@disk.route('/disk/usage/<id>')
@disk.route('/disk/usage/<id>/<unit>', methods=['GET'])
@auth.login_required
def disk_use(id, unit=None):
    """ show allocated space information from disk.id
        in Byte(default) MiB or GiB

        /disk/usage/0 
            show allocated space information from disk 0 in Byte
        /disk/usage/0/GiB
            show allocated space information from disk 0 in GiB
    """
    if unit is None:
        convert=1
    elif unit == 'MiB':
        convert=1048576
    elif unit == 'GiB':
        convert=1073741824
    else:
        convet=1
        
    ldisk = []
    id = int(id)
    try:
        diskpath = disk_partitions(all=False)[id]
        dd = disk_usage(diskpath[1])
        ldisk.append({
            'total': dd.total/convert,
            'used': dd.used/convert,
            'free': dd.free/convert,
            'percent': dd.percent})
    except:
        ldisk=None
    return jsonify(diskusage=ldisk)
