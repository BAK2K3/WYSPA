from flask import render_template, Blueprint
from wyspa.factory.initialisation import mongo


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


@messages.route('/view_message')
def view_message():

    message_entry = list(mongo.db.messages.aggregate(
        [{"$sample": {"size": 1}}]))

    return render_template('messages.html', message_entry=message_entry[0])
