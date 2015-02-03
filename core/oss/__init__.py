# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
import platform

os = Blueprint('os', __name__, 
                    template_folder='')

@os.route('/os/info', methods=['GET'])
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
