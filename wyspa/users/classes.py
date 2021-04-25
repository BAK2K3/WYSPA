"""
Classes - Users Sub-module
=============

Contains the User class for Session Management and User Management,
such as password validation and database reading and writing.

Classes: User
"""

import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, UserMixin

from wyspa.factory.initialisation import mongo


# Create the required User class for Flask-Login
class User(UserMixin):
    """
    A class to represent a User. This class utilises the Flask-Login
    UserMixin for the required pre-defined methods for interaction
    with Flask-Login. Additional methods have been added for User Management,
    such as password validation and database reading and writing, and get_id
    has been over-ridden to work with MongoDB.

    Attributes
    -----------

    username : str
        The user's username, which is stored in the session.

    Methods
    -------
    get_id()
        Returns the logged in user's username.

    delete_user(username)
        Deletes user and all user's Wyspas from database.

    verify_password_format(user_password)
        Verifies the password matches the required regex format.

    verify_password_match(user password, password_confirmation)
        Compares the passwords provided.

    obtain_user(username)
        Queries the database for a given username.

    register_user(username, user_password)
        Saves a users to the database.

    verify_login(username, user_password)
        Checks a users password against the hash and logs them in.
    """

    def __init__(self, username):
        """
        Constructs all the necessary attributes for the Wyspa object.

        Attributes
        -----------
        username : str
            The user's username, which is stored in the session.
        """

        self.username = username

    # Over-ride UserMixin "get_id" method
    def get_id(self):
        """Returns the logged in user's username.

        This method over-rides the UserMixin method,
        which is incompatable with MongoDB.

        https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb

        Returns
        -----------
        username : str
            The user's username, which is stored in the session.
        """

        return self.username

    @staticmethod
    def delete_user(username):
        """Deletes user and all user's Wyspas from database.

        Removes the user's entry from the User database, along
        with all Wyspa's from the Messages database where the user
        is the author.

        Parameters
        ----------
        username : str
            The user's username, which is stored in the session.

        Returns
        -------
        None
        """

        mongo.db.users.delete_one({"username": username})
        mongo.db.messages.delete_many({"author": username})

    @staticmethod
    def verify_password_format(user_password):
        """Verifies the password matches the required regex format.

        Parameters
        ----------
        user_password : str
            The user's registration password.

        Returns
        -------
        re.Match object (if successful)

        None (if unsuccessful)
        """

        return re.search("^(?=.*[^a-zA-Z]).{6,20}$", user_password)

    @staticmethod
    def verify_password_match(user_password, password_confirmation):
        """Compares the passwords provided.

        Parameters
        ----------
        user_password : str
            The user's registration password.

        password_confirmation : str
            The user's password confirmation.

        Returns
        -------
        True : bool (if successful)

        False : bool (if unsuccessful)
        """

        return user_password == password_confirmation

    @staticmethod
    def obtain_user(username):
        """Queries the database for a given username.

        Parameters
        ----------
        username : str
            The username a user has provided to log in.

        Returns
        -------
        Dict (if successful)
            Dict format: {"username" : "password"}

        Empty list (if unsuccessful)
        """

        return mongo.db.users.find_one(
            {"username": username})

    @staticmethod
    def register_user(username, user_password):
        """Saves a users to the database.

        Constructs a registration dictionary that is compatible
        with the MongoDB document format for the User collection,
        using the username and a hashed password, and  writes this
        to the User database. The user is then logged in via Flask-Login.

        Parameters
        ----------
        username : str
            The username a user has provided to register.

        user_password : str
            The user's password to be hashed.

        Returns
        -------
        None
        """

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
        """Checks a users password against the hash and logs them in.

        This method calls the User.obtain_user() method to query
        the User database, and checks the user's password against
        the hashed password in the database. If successful, the
        user is logged in via Flask-Login.

        Parameters
        ----------
        username : str
            The username a user has provided to log-in.

        user_password : str
            The user's password to be verified against the hash.

        Returns
        -------
        True : bool (if successful)

        False : bool (if unsuccessful)
        """

        login_check = User.obtain_user(username)
        # Check username exists and password matches
        if login_check and check_password_hash(
                login_check["password"], user_password):
            login_user(User(username))
            return True
        return False
