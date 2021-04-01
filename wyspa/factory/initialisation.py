"""
Initialise Flask Application Factory with MongoDB.
"""
import os

from flask import Flask
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env


# Instantiate Mongo Database
mongo = PyMongo()


# https://github.com/yymm/flask-vuejs
class CustomFlask(Flask):

    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        trim_blocks=True,
        lstrip_blocks=True
    ))


# https://stackoverflow.com/questions/48653120/flask-pymongo-with-application-factory-and-blueprints
def create_app():

    app = CustomFlask(__name__)

    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.config["PREFERRED_URL_SCHEME"] = "https"
    app.config["TESTING"] = False

    app.template_folder = os.path.abspath("wyspa/templates")
    app.secret_key = os.environ.get("SECRET_KEY")
    app.static_folder = os.path.abspath("wyspa/static")

    mongo.init_app(app)

    return app
