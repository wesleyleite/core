# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import users 

user = Blueprint('user', __name__, 
                    template_folder='')

@user.route('/user/who/<username>')
@user.route('/user/who', methods=['GET'])
def who(username=None):
    lUsers=users()
    jwho=[]

    if username is not None:
        for k,v in enumerate(lUsers):
            if v.name == username:
                jwho.append(lUsers[k])
    else:
        jwho.append(lUsers)

    return jsonify(user=jwho)

