# #!/usr/bin/python3
# """import modules"""
# from flask import Flask, jsonify
# from models import storage
# from api.v1.views import app_views

# app = Flask(__name__)
# app.register_blueprint(app_views, url_prefix='/api/v1')


# @app.route('/')
# def hello():
#     """
#     Hello world
#     """
#     return 'Hello, World!'


# @app.errorhandler(404)
# def page_not_found(e):
#     """
#     Custom 404 error handler that returns JSON instead of HTML.
#     """
#     return jsonify({"error": "Not found"}), 404


# @app.teardown_appcontext
# def close_db(error):
#     """Close the storage on teardown."""
#     storage.close()


# if __name__ == "__main__":
#     import os
#     host = os.getenv('HBNB_API_HOST', '0.0.0.0')
#     port = os.getenv('HBNB_API_PORT', '5000')
#     app.run(host=host, port=port, threaded=True, debug=True)

#!/usr/bin/python3
"""app"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(self):
    ''' closes storage engine '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    ''' handles 404 error and gives json formatted response '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)