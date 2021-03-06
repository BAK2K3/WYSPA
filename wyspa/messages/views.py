from flask import render_template, Blueprint
from wyspa.factory.initialisation import mongo


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


@messages.route('/view_message')
def view_message():

    messages_dict = [{"Name": "Ben", "Location": "Northampton"},
                     {"Name": "Deiza", "Location": "Northampton"}]
    return render_template('messages.html', messages_dict=messages_dict)
