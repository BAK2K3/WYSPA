from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import current_user, login_required
from wyspa.factory.initialisation import mongo
from .classes import Wyspa


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


@ messages.route('/view_message', defaults={'message_id': None})
@ messages.route('/view_message/<message_id>')
def view_message(message_id):

    if message_id:
        message_entry = Wyspa.get_by_id(message_id)
        print(message_entry)

    else:
        message_entry = list(mongo.db.messages.aggregate(
            [{"$sample": {"size": 1}}]))[0]
        print(message_entry)

    return render_template('messages.html', message_entry=message_entry)


@ messages.route('/my_voice')
@ login_required
def my_voice():

    users_messages = Wyspa.get_by_user(current_user.username)
    return render_template('my_voice.html', users_messages=users_messages)


@ messages.route('/create_wyspa', methods=["GET", "POST"])
@ login_required
def create_wyspa():

    if request.method == "POST":
        new_wyspa = Wyspa(current_user.username,
                          request.form.get("wyspaContent"), "happy", "NN5")
        new_wyspa.write_wyspa()
        return redirect(url_for("messages.my_voice"))


@ messages.route('/add_comment/<message_id>', methods=["GET", "POST"])
def add_comment(message_id):

    if request.method == "POST":

        retrieved_wyspa = Wyspa.get_by_id(message_id)
        retrieved_wyspa.add_comment(request.form.get("commentReply"))

        return redirect(url_for("messages.view_message",
                                message_id=retrieved_wyspa._id))
