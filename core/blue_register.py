from core import app
from imports import *

app.register_blueprint(cpu)
app.register_blueprint(net)
app.register_blueprint(os)
