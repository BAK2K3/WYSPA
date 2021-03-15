from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import current_user, login_required
from wyspa.factory.initialisation import mongo
from bson.objectid import ObjectId


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


# Create a class for WYSPAs
class Wyspa():
    def __init__(self, author, message, mood, location, comments=[], _id=None):
        self._id = _id
        self.author = author
        self.message = message
        self.mood = mood
        self.location = location
        self.comments = comments if comments else []

    def get_info(self):
        # Return Dictionary for DB
        info = {'author': self.author, 'message': self.message,
                'mood': self.mood, 'location': self.location,
                'comments': self.comments}
        return info

    def remove_comment(self, index):
        self.comments.pop(index)
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_comment(self, new_comment):
        self.comments.append(new_comment)
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def delete_wyspa(self):
        mongo.db.messages.remove({"_id": ObjectId(self._id)})

    def write_wyspa(self):
        mongo.db.messages.insert_one(self.get_info())


@ messages.route('/view_message')
def view_message():

    message_entry = list(mongo.db.messages.aggregate(
        [{"$sample": {"size": 1}}]))

    return render_template('messages.html', message_entry=message_entry[0])


@ messages.route('/my_voice')
@ login_required
def my_voice():

    users_messages = list(mongo.db.messages.find(
        {"author": current_user.username}))

    return render_template('my_voice.html', users_messages=users_messages)


@ messages.route('/create_wyspa', methods=["GET", "POST"])
@ login_required
def create_wyspa():

    if request.method == "POST":

        print(request.args)

        new_wyspa = Wyspa(current_user.username,
                          request.form.get("wyspaContent"), "happy", "NN5")
        new_wyspa.write_wyspa()
        return redirect(url_for("messages.my_voice"))
