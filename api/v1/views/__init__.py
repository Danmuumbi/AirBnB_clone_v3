#!/usr/bin/python3
"""Define modules"""
from flask import Blueprint

"""Add blueprint"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *


#     """Configure function corrects circular input"""
#     from .index import status, stats
#     from .states import (
#         get_states, get_state, delete_state,
#         create_state, update_state
#         )
#     app.register_blueprint(app_views)
