from flask import request, jsonify
import os
from functools import wraps

API_KEY = os.environ.get("ARIA_API_KEY", "changeme")

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-KEY")
        if key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper