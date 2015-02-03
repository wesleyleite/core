# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import NUM_CPUS, cpu_count
from funcoes import usage_percent

cpu = Blueprint('cpu', __name__, 
                    template_folder='')

@cpu.route('/cpu/num', methods=['GET'])
def cpu_num():
    return jsonify(CPU=psutil.NUM_CPUS, 
            NO_LOGICAL=psutil.cpu_count(logical=False))

@cpu.route('/cpu/usage/<int:trange>', methods=['GET'])
@cpu.route('/cpu/usage', methods=['GET'])
def cpu_percent_usage(trange=3):
    return jsonify(CPU_USAGE=usage_percent(trange))
