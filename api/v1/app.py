#!/usr/bin/python3
"""import modules"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.route('/')
def hello():
    """
    Hello world
    """
    return 'Hello, World!'


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler that returns JSON instead of HTML.
    """
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_db(error):
    """Close the storage on teardown."""
    storage.close()


if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True, debug=True)
