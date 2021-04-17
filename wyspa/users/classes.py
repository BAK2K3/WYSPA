import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from wyspa.factory.initialisation import mongo


# https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
# Create the required User class for Flask-Login
class User():
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def delete_user(username):
        mongo.db.users.remove({"username": username})
        mongo.db.messages.remove({"author": username})

    @staticmethod
    def verify_password_format(user_password):
        return re.search("^(?=.*[^a-zA-Z]).{6,20}$", user_password)

    @staticmethod
    def verify_password_match(user_password, password_confirmation):
        return user_password == password_confirmation

    @staticmethod
    def obtain_user(username):
        return mongo.db.users.find_one(
            {"username": username})

    @staticmethod
    def register_user(username, user_password):
        # Create a registration dictionary
        registration = {
            "username": username,
            "password": generate_password_hash(user_password)
        }
        # Update DB with registration dictionary
        mongo.db.users.insert_one(registration)

        # Log in new user
        login_user(User(username))

    @staticmethod
    def verify_login(username, user_password):

        login_check = User.obtain_user(username)
        # Check username exists and password matches
        if login_check and check_password_hash(
                login_check["password"], user_password):
            login_user(User(username))
            return True
        else:
            return False
