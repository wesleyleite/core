# *-* coding: utf-8 *-*
from flask.ext.httpauth import HTTPDigestAuth

auth = HTTPDigestAuth()

authuser = {
        "admin": "admin"
}

@auth.get_password
def get_pwd(username):
    if username in authuser:
        return authuser.get(username)
    return None

