from flask import render_template, Blueprint
from wyspa.factory.initialisation import mongo


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


@messages.route('/view_message')
def view_message():

    messages_dict = [{"Name": "Ben", "Location": "Northampton",
                      "Message": "Hello, World!"},
                     {"Name": "Deiza", "Location": "Northampton", "Message": "This message is going to be a little bit longer. It's going to try and make the box expand to it's fullest."}]
    return render_template('messages.html', messages_dict=messages_dict[0])
