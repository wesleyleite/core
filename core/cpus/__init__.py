# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
import psutil

cpu = Blueprint('cpu', __name__, 
                    template_folder='')

@cpu.route('/cpu/num', methods=['GET'])
def cpu_num():
    return jsonify(CPU=psutil.NUM_CPUS, 
            NOLOGICAL=psutil.cpu_count(logical=False))
