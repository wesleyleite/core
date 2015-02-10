from core import app
from imports import *

app.register_blueprint(cpu)
app.register_blueprint(net)
app.register_blueprint(os)
app.register_blueprint(user)
app.register_blueprint(process)
