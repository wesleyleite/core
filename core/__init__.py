# *-* coding: utf-8 *-*
from flask import Flask, render_template, abort, Response, url_for, Blueprint
from imports import *

app = Flask(__name__)
app.config.from_object('config')

#app.register_blueprint(cpu)
from blue_register import *

import core.views
