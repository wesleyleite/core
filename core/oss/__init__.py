# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
import platform
from ..auths import *
from uptime import uptime
from time import time
from datetime import datetime 

os = Blueprint('os', __name__, 
                    template_folder='')

@os.route('/os/info', methods=['GET'])
@auth.login_required
def os_info():
    uname=platform.uname()
    system=platform.system()
    node=platform.node()
    release=platform.release()
    version=platform.version()
    machine=platform.machine()
    processor=platform.processor()
    return jsonify(uname=uname,
            system=system,
            node=node,
            release=release,
            version=version,
            machine=machine,
            processor=processor)

@os.route('/os/dist', methods=['GET'])
@auth.login_required
def os_dist():
    os_dist=''
    system=platform.system()

    if system == 'Linux':
        os_dist=platform.linux_distribution()
    elif system == 'Darwin':
        os_dist=platform.mac_ver()
    elif system == 'Windows':
        os_dist=platform.win32_ver()
        
    return jsonify(dist=os_dist)

@os.route('/os/uptime', methods=['GET'])
@auth.login_required
def os_uptime():
    tsStart = time() - uptime()
    
    tsdate1 = datetime.fromtimestamp(tsStart)
    tsdate2 = datetime.fromtimestamp(time())
    
    return jsonify(start=datetime.fromtimestamp(tsStart),
            days=(tsdate2-tsdate1).days,
            hours=(tsdate2-tsdate1).seconds / 3600,
            minutes=(tsdate2-tsdate1).seconds / 60 % 60)


