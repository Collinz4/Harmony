from flask import request, jsonify

from functools import wraps

import conf

def authenticate(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # check for valid authentication header
        try:
            api_key = request.headers.get('Authorization').split()[1]
        except AttributeError or TypeError:
            return jsonify(message="Missing Authorization Header"), 400

        if conf.API_KEY != api_key:
            return jsonify(message="Not Authorized"), 401

        return func(*args, **kwargs)
    return wrapper
