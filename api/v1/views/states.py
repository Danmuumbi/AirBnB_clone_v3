# #!/usr/bin/python3
# from flask import jsonify, request, abort
# from models.state import State
# from models import storage
# from api.v1.views import app_views


# @app_views.route('/states', methods=['GET'])
# def get_states():
#     """Retrieve a list of all State objects"""
#     all_states = storage.all(State)
#     return jsonify([state.to_dict() for state in all_states.values()])


# @app_views.route('/states/<state_id>', methods=['GET'])
# def get_state(state_id):
#     """Retrieve a specific State object"""
#     state = storage.get(State, state_id)
#     if not state:
#         abort(404)
#     return jsonify(state.to_dict())


# @app_views.route('/states/<state_id>', methods=['DELETE'])
# def delete_state(state_id):
#     """Delete a specific State object"""
#     state = storage.get(State, state_id)
#     if not state:
#         abort(404)
#     storage.delete(state)
#     storage.save()
#     return jsonify({}), 200


# @app_views.route('/states', methods=['POST'])
# def create_state():
#     """Create a new State object"""
#     if not request.json:
#         abort(400, description="Not a JSON")
#     if 'name' not in request.json:
#         abort(400, description="Missing name")
#     state = State(**request.get_json())
#     state.save()
#     return jsonify(state.to_dict()), 201


# @app_views.route('/states/<state_id>', methods=['PUT'])
# def update_state(state_id):
#     """Update a State object"""
#     state = storage.get(State, state_id)
#     if not state:
#         abort(404)
#     if not request.json:
#         abort(400, description="Not a JSON")
#     ignore = ["id", "created_at", "updated_at"]
#     for key, value in request.get_json().items():
#         if key not in ignore:
#             setattr(state, key, value)
#     state.save()
#     return jsonify(state.to_dict()), 200


#!/usr/bin/python3
"""states"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/', methods=['GET'])
def list_states():
    '''Retrieves a list of all State objects'''
    list_states = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    '''Retrieves a State object'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    return jsonify(state_obj[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''Deletes a State object'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    state_obj.remove(state_obj[0])
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    '''Creates a State'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def updates_state(state_id):
    '''Updates a State object'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state_obj[0]['name'] = request.json['name']
    for obj in all_states:
        if obj.id == state_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state_obj[0]), 200