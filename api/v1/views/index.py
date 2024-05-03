#!/usr/bin/python3
"""import modules"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON indicating the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieves the number of each objects by type."""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    counts = {}
    for key, value in classes.items():
        counts[key] = storage.count(value)
    return jsonify(counts)
