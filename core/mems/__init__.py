# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import virtual_memory, swap_memory
from ..auths import *

mem = Blueprint('mem', __name__, 
                    template_folder='')

@mem.route('/mem/virtual', methods=['GET'])
@auth.login_required
def mem_all():
    return jsonify(memory={
        'total':virtual_memory().total,
        'used':virtual_memory().used,
        'free':virtual_memory().free,
        'percent':virtual_memory().percent})

@mem.route('/mem/swap', methods=['GET'])
@auth.login_required
def mem_swap():
     return jsonify(swap={
        'total':swap_memory().total,
        'used':swap_memory().used,
        'free':swap_memory().free,
        'percent':swap_memory().percent})
