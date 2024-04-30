#!/usr/bin/python3
from flask import Blueprint

"""Add blueprint"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from .index import *
from .states import *