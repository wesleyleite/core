# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import NUM_CPUS, cpu_count
from funcoes import usage_percent
from ..auths import *
from cpuinfo import cpuinfo

cpu = Blueprint('cpu', __name__, 
                    template_folder='')

@cpu.route('/cpu/num', methods=['GET'])
@auth.login_required
def cpu_num():
    return jsonify(CPU=cpu_count(), 
            NO_LOGICAL=cpu_count(logical=False))

@cpu.route('/cpu/usage/<int:trange>', methods=['GET'])
@cpu.route('/cpu/usage', methods=['GET'])
@auth.login_required
def cpu_percent_usage(trange=3):
    return jsonify(CPU_USAGE=usage_percent(trange))

@cpu.route('/cpu/info', methods=['GET'])
@auth.login_required
def cpu_info():
    return jsonify(cpuinfo=cpuinfo.get_cpu_info())
