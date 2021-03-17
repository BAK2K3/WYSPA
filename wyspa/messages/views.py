from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .classes import Wyspa


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


@ messages.route('/view_message', defaults={'message_id': None})
@ messages.route('/view_message/<message_id>')
def view_message(message_id):

    if message_id:
        message_entry = Wyspa.get_by_id(message_id)
    else:
        message_entry = Wyspa.get_random_wyspa()

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


@ messages.route('/remove_wyspa/<message_id>', methods=["GET", "POST"])
def remove_wyspa(message_id):

    if request.method == "POST":
        Wyspa.delete_wyspa(message_id)
        return redirect(url_for("messages.my_voice"))


@ messages.route('/message_control/<message_id>', methods=["GET", "POST"])
def message_control(message_id):
    if request.method == "POST":
        if "delete" in request.form:
            Wyspa.delete_wyspa(message_id)
            return redirect(url_for("messages.my_voice"))
        elif "goto" in request.form:
            return redirect(url_for("messages.view_message",
                                    message_id=message_id))
        else:
            flash("Something went wrong!")
            return redirect(url_for("core.index"))
