# *-* coding: utf-8 *-*
""" Core is a simple interface to resource monitor
"""
from flask import Flask, render_template, abort, Response, url_for, Blueprint
from imports import *

app = Flask(__name__)
app.config.from_object('config')

from blue_register import *

import core.views
