# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import disk_partitions, disk_usage
from ..auths import *

disk = Blueprint('disk', __name__, 
                    template_folder='')

@disk.route('/disk', methods=['GET'])
@auth.login_required
def disk_part():
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

@disk.route('/disk/usage/<id>', methods=['GET'])
@auth.login_required
def disk_use(id):
    ldisk = []
    id = int(id)
    try:
        diskpath = disk_partitions(all=False)[id]
        dd = disk_usage(diskpath[1])
        ldisk.append({
            'total': dd.total,
            'used': dd.used,
            'free': dd.free,
            'percent': dd.percent})
    except:
        ldisk=None
    return jsonify(diskusage=ldisk)
