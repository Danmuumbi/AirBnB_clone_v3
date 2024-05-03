from flask import jsonify, Blueprint
from models import storage

app_views = Blueprint('index', __name__, url_prefix='/api/v1')


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """Return a JSON response with status "OK"."""
    data = {"status": "OK"}
    return jsonify(data), 200


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """Return a JSON response with counts of each object type."""
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(data), 200
