"""
Initialisation - Factory Sub-module
==================================

Initialise Flask Application Factory with MongoDB and Prettify.

Function:
    create_app()
"""

# pylint: disable=unused-import
# env.py import is being incorrectly picked up as unused

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


# https://stackoverflow.com/questions/48653120/flask-pymongo-with-application-factory-and-blueprints
def create_app():
    """Flask Application Factory

    Initialises the Flask Application, configures it,
    and then initialises both MongoDB and Prettify.

    Parameters
    ----------
    None

    Returns
    -------
    app : Flask Application
    """

    app = Flask(__name__)

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
