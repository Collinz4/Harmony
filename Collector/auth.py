"""
Simple auth module.
"""

import os
from functools import wraps

from flask import request, jsonify


def authenticate(func):
    """
    Authenticates request's bearer token against environment variable 'API_KEY'.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # check for valid authentication header
        try:
            api_key = request.headers.get('Authorization').split()[1]
        except (AttributeError, TypeError):
            return jsonify(message="Missing Authorization Header"), 400

        if os.environ.get("API_KEY") != api_key:
            return jsonify(message="Not Authorized"), 401

        return func(*args, **kwargs)
    return wrapper
