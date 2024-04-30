#!/usr/bin/python3
from flask import Blueprint
from index import *
from states import *

"""Add blueprint"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
