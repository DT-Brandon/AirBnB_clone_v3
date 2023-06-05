#!/usr/bin/python3
"""Flask application"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')

app = Flask(__name__)
CORS(app, resources=r'/*', origins=['0.0.0.0'])
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(exception):
    """Removes the session after each request"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles not found error"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(host=host, port=port, threaded=True)
