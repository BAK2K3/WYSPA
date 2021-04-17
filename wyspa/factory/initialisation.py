"""
Initialisation - Factory Submodule
==================================

Initialise Flask Application Factory with MongoDB and Prettify.

Class:
    CustomFlask(Flask)

Functions:
    create_app()
"""

import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_pretty import Prettify

if os.path.exists("env.py"):
    import env


# Instantiate Mongo Database
mongo = PyMongo()

# Instantiate Prettify
prettify = Prettify()


# https://github.com/yymm/flask-vuejs
class CustomFlask(Flask):
    """Custom Flask Class set up to over-ride
    default Jinja whitespace options."""
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        trim_blocks=True,
        lstrip_blocks=True
    ))


# https://stackoverflow.com/questions/48653120/flask-pymongo-with-application-factory-and-blueprints
def create_app():
    """Flask Application Factory

    Initialises the Flask Application using the CustomFlask class,
    configures the Flask Application, and then initialises both
    MongoDB and Prettify.

    Returns prepared Flask application (app)"""
    app = CustomFlask(__name__)

    # Configuration
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.config["PREFERRED_URL_SCHEME"] = "https"
    app.config["TESTING"] = False
    app.config["PRETTIFY"] = True

    # Directories and parameters
    app.template_folder = os.path.abspath("wyspa/templates")
    app.secret_key = os.environ.get("SECRET_KEY")
    app.static_folder = os.path.abspath("wyspa/static")

    # Mongo and Prettify Initialisation
    mongo.init_app(app)
    prettify.init_app(app)

    return app
