#!/usr/bin/python3
"""import modules"""
from . import app_views
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


# #!/usr/bin/python3
# """index"""
# from api.v1.views import app_views
# from flask import jsonify
# from models import storage
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review

# classes = {"users": "User", "places": "Place", "states": "State",
#            "cities": "City", "amenities": "Amenity",
#            "reviews": "Review"}


# @app_views.route('/status', methods=['GET'])
# def status():
#     ''' routes to status page '''
#     return jsonify({'status': 'OK'})


# @app_views.route('/stats', methods=['GET'])
# def count():
#     '''retrieves the number of each objects by type'''
#     count_dict = {}
#     for cls in classes:
#         count_dict[cls] = storage.count(classes[cls])
#     return jsonify(count_dict)
