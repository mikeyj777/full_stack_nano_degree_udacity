# Import Dependencies
from flask import Flask, jsonify
# from models import setup_db, Plant
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    # setup_db(app)
    CORS(app)
    # CORS(app, resources={r"*/api/*": {origins:'*'}}) #any origin can access any uri containing '/api/'

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def hello():
        return 'hi!'

    return app