#!/usr/bin/python3
"""Index view module"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def status():
    """Return status of the api"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """Retrieves the number of each objects by type"""
    from models import storage
    return jsonify({
                    "amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")
                   })
