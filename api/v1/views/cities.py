#!/usr/bin/python3
"""Import modules"""
from flask import jsonify, request, abort
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('states/<state_id>/cities/', methods=['GET'])
def get_cities(state_id):
    """Retrieve a list of all city objects of a State"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieve a specific city object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities', methods=['POST'])
def create_city(state_id):
    """Create a new City object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    city_data = request.get_json()
    new_city = City(name=city_data['name'], state_id=state_id)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Delete a specific City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update a City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    ignore = ["id", "state_id", "created_at", "updated_at"]
    for key, value in request.get_json().items():
        if key not in ignore:
            setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
