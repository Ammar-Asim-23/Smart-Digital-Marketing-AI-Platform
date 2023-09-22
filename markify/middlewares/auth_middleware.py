from flask import request, g, jsonify
from functools import wraps

def authenticate(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        # Check if the user is authenticated
        if not g.user:
            return jsonify({"message": "Authentication required"}), 401
        return route_function(*args, **kwargs)
    return wrapper
