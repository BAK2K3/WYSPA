"""
Initialiase Flask Application Factory with MongoDB.
"""
import os
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

# https://stackoverflow.com/questions/48653120/flask-pymongo-with-application-factory-and-blueprints

mongo = PyMongo()


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder=os.path.abspath('wyspa/templates'))

    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.secret_key = os.environ.get("SECRET_KEY")
    app.static_folder = os.path.abspath('wyspa/static')

    mongo.init_app(app)

    return app
