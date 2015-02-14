# *-* coding: utf-8 *-*
from flask import url_for, jsonify
from core import app
from auths import *

@app.route('/')
@auth.login_required
def index():
    return 'Index'

@app.route('/resource/<sresource>')
@app.route('/resource', methods=['GET'])
def get_resources(sresource = None):
    output = []
    line = {}
    for rule in app.url_map.iter_rules():
        resourcetype = rule.endpoint.split('.')[0]
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        if sresource is None:
            line = {'resource': resourcetype, 'endpoint': rule.endpoint, 'methods': methods, 'url': url}
            output.append(line)
        else:
            if sresource == resourcetype:
                line = {'resource': resourcetype, 'endpoint': rule.endpoint, 'methods': methods, 'url': url}
                output.append(line)

        output.sort()

    return jsonify(resource=output)
