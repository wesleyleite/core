# *-* coding: utf-8 *-*
from core import app

@app.route('/')
def index():
    return 'Index'
