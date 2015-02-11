# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
import psutil
from ..auths import *

net = Blueprint('net', __name__, 
                    template_folder='')

@net.route('/net/iface')
@net.route('/net/iface/<interface>', methods=['GET'])
@auth.login_required
def ifaces(interface=all):
    lIface=[]
    dIface=psutil.net_io_counters(pernic=True)
    for v,k in enumerate(dIface):
        lIface.append(k)

    if interface in lIface:
        rIface=dIface[interface]
    else:
        rIface=lIface
    return jsonify(interface=rIface)

@net.route('/net/connections', methods=['GET'])
@auth.login_required
def connections():
    return jsonify(connections=[str(x) for x in psutil.net_connections()])
