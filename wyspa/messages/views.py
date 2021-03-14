from flask import render_template, Blueprint
from flask_login import current_user, login_required
from wyspa.factory.initialisation import mongo


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


@messages.route('/view_message')
def view_message():

    message_entry = list(mongo.db.messages.aggregate(
        [{"$sample": {"size": 1}}]))

    return render_template('messages.html', message_entry=message_entry[0])


@messages.route('/my_voice')
@login_required
def my_voice():

    users_messages = list(mongo.db.messages.find(
        {"author": current_user.username}))

    print(users_messages)

    return render_template('my_voice.html', users_messages=users_messages)
