""" Auth not is optional module, but, should be changed or refactored
"""
# *-* coding: utf-8 *-*
from flask.ext.httpauth import HTTPDigestAuth

auth = HTTPDigestAuth()

authuser = {
        "admin": "admin"
}

@auth.get_password
def get_pwd(username):
    """ uses HTTPDigestAuth to validate credencial
    """
    if username in authuser:
        return authuser.get(username)
    return None

