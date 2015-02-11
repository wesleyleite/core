# *-* coding: utf-8 *-*
from core import app
from auths import *

@app.route('/')
@auth.login_required
def index():
    return 'Index'
