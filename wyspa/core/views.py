from flask import render_template, Blueprint
from wyspa.factory.initialisation import mongo


# Configure Blueprint for core route
core = Blueprint('core', __name__)


@core.route('/')
def index():
    messages = list(mongo.db.messages.find())
    return render_template('index.html', messages=messages)
