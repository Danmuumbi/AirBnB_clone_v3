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
    # list_states = [obj.to_dict() for obj in storage.all("State").values()]
    # return jsonify(list_states)
    all_states = storage.all("State").values()
    return jsonify([state.to_dict() for state in all_states])

@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    '''Retrieves a State object'''
    # all_states = storage.all("State").values()
    # state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    # if state_obj == []:
    #     abort(404)
    # return jsonify(state_obj[0])
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''Deletes a State object'''
    # all_states = storage.all("State").values()
    # state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    # if state_obj == []:
    #     abort(404)
    # state_obj.remove(state_obj[0])
    # for obj in all_states:
    #     if obj.id == state_id:
    #         storage.delete(obj)
    #         storage.save()
    # return jsonify({}), 200
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

    # states = [state for state in storage.all(State).values()
    #           if state_id == state.id]
    # if states == []:
    #     abort(404)
    # storage.delete(states[0])
    # storage.save()
    # return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    '''Creates a State'''
    # if not request.get_json():
    #     abort(400, 'Not a JSON')
    # if 'name' not in request.get_json():
    #     abort(400, 'Missing name')
    # states = []
    # new_state = State(name=request.json['name'])
    # storage.new(new_state)
    # storage.save()
    # states.append(new_state.to_dict())
    # return jsonify(states[0]), 201
    if not request.json:
        abort(400, 'Not a JSON')
    if 'name' not in request.json:
        abort(400, 'Missing name')
    new_state = State(name=request.json['name'])
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def updates_state(state_id):
    """Updates a State object"""
    # all_states = storage.all("State").values()
    # state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    # if state_obj == []:
    #     abort(404)
    # if not request.get_json():
    #     abort(400, 'Not a JSON')
    # state_obj[0]['name'] = request.json['name']
    # for obj in all_states:
    #     if obj.id == state_id:
    #         obj.name = request.json['name']
    # storage.save()
    # return jsonify(state_obj[0]), 200
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200

    # states = [state for state in storage.all(State).values()
    #           if state.id == state.id]
    # if states == []:
    #     abort(404)
    # my_json = request.get_json()
    # if my_json is None:
    #     abort(400, 'Not a JSON')
    # elif 'name' not in my_json.keys():
    #     abort(400, 'Missing name')
    # states[0].name = my_json['name']
    # storage.save()
    # return jsonify(states[0].to_dict()), 200
