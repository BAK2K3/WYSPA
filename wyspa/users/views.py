"""
Views - Users Sub-module
==================================

This module contains the User Views sub-module which
handles all routes and data handling relating to Users.

Functions:
    load_user(username)
    register()
    login()
    logout()
    delete_user()
"""

from flask import (render_template, Blueprint, request,
                   redirect, flash, url_for, session)
from flask_login import (LoginManager, login_required,
                         logout_user, current_user)

from wyspa.factory.initialisation import mongo
from wyspa.users.classes import User


# Configure Blueprint for user route
users = Blueprint('users', __name__)


# Instantiate login_manager
login_manager = LoginManager()


# Define the user_loader callback for Flask-Login
@login_manager.user_loader
def load_user(username):
    """Login Manager Load User

    Login: Not Required

    This route is a required by Flask-Login. It queries
    the database for a given user, and returns a User object with
    the logged in user's username.

    Parameters
    ----------
    username : str
        Username of user attempting to log in.

    Returns
    -------
    User object
    """
    login_attempt = mongo.db.users.find_one({"username": username.lower()})
    if not login_attempt:
        return None
    return User(username=login_attempt["username"])


# Register Route
@ users.route("/register", methods=["GET", "POST"])
def register():
    """Register Route [Get/Post]

    Login: Not Required

    This route validates a user's username, password,
    and confirmation password, before adding a user
    entry to the Users Database, and logging them in.

    This is a POST route; if accessed via GET, user
    is redirected to Index route with no further action.

    Parameters
    ----------
    None

    Returns
    -------
    Redirect (index) [Get/Unsuccessful]

    Redirect (my_voice) [Post/Successful]
    """

    # Check if user is already logged in
    if current_user.is_authenticated:
        flash("You are already logged in!")
        return redirect(url_for("core.index"))

    if request.method == "POST":

        # Obtain password
        user_password = request.form.get("passwordRegister")
        password_confirmation = request.form.get("passwordConfirm")

        # Check the correct format of password
        if not User.verify_password_format(user_password):
            flash("Password format incorrect!")
            return render_template("index.html")

        # Check the passwords match
        if not User.verify_password_match(user_password,
                                          password_confirmation):
            flash("Passwords do not match!")
            return render_template("index.html")

        # Search for username
        username = request.form.get("usernameRegister").lower()

        # Check to see if username exists in DB
        if User.obtain_user(username):
            flash("Username already exists!")
            return redirect(url_for("core.index"))

        # Register and log in user
        User.register_user(username, user_password)

        # Save user's timezone in session
        session['timezone'] = request.form.get("timezoneRegister")

        # Flash and redirect
        flash("Registration Successful")
        return redirect(url_for("messages.my_voice"))

    # Instructions for over-ride entry
    flash("Please click the Register link to Register!")
    # Routing for Get Requests
    return redirect(url_for("core.index"))


@ users.route('/login', methods=['GET', 'POST'])
def login():
    """Login Route [Get/Post]

    Login: Not Required

    This route queries the database for a username,
    and validates their password if a user is found.

    If a user has been referred to log in, Referral and/or "Next"
    parameter (if applicable) is stored for redirect after
    successful login.

    This is a POST route; if accessed via GET, user
    is redirected to Index route with no further action.

    Parameters
    ----------
    None

    Returns
    -------
    Redirect (index) [Get/Unsuccessful]

    Redirect (my_voice) [Post/Successful]

    Redirect (referrer) [Post/Successful with referrer]
    """
    # Post Method
    if request.method == "POST":

        # Obtain username and password from form
        username = request.form.get("usernameLogin").lower()
        user_password = request.form.get("passwordLogin")

        # Verify username/password and log in
        if User.verify_login(username, user_password):

            session['timezone'] = request.form.get("timezoneLogin")
            flash(f"Welcome, {current_user.username}")

            # Checks if next parameter is in the referal URL
            if "?next=%2F" in request.referrer:
                return redirect(request.referrer.split("?next=%2F")[1])
            return redirect(request.referrer)

        #  Inform user that credentials are incorrect
        flash("Incorrect Username and/or Password")
        return redirect(request.referrer)

    # Check to see if user is logged in
    if current_user.is_authenticated:
        # Checks if there is a referral URL
        if request.referrer:
            # Checks if there is a next param in referral URL
            if "?next=%2F" in request.referrer:
                return redirect(request.referrer.split("?next=%2F")[1])
            return redirect(request.referrer)
        # If no referrer, inform user they are logged in
        flash("You are already logged in!")
    else:
        # Otherwise instruct them how to log in
        flash("Please click the Login link to Log in!")

    # Redirect to index page
    return redirect(url_for('core.index'))


# Log out user and redirect to Index
@ users.route('/logout')
def logout():
    """Logout Route [Get]

    Login: Required

    This route logs a user out of the session.
    Login_required decorator has not been used to
    avoid storing referral information.

    Parameters
    ----------
    None

    Returns
    -------
    Redirect (Index)
    """
    if current_user.is_authenticated:
        logout_user()
        if '_flashes' not in session.keys():
            flash("Logged out successfully!")
    else:
        flash("You are not logged in!")
    return redirect(url_for('core.index'))


@users.route('/delete_user', methods=["GET", "POST"])
@ login_required
def delete_user():
    """Delete User Route [Get]

    Login: Required

    This route deletes a user document from the Users
    database, and removes all of the Wyspas in the
    Messages database where the user is the author.

    This is a POST route; if accessed via GET, user
    is redirected to My Voice route with no further action.

    Parameters
    ----------
    None

    Returns
    -------
    Redirect (My Voice) [Get]
    Redirect (Logout) [Post]
    """

    if request.method == "POST":
        User.delete_user(current_user.username)
        flash("Account and Wyspas deleted Successfully!")
        return redirect(url_for('users.logout'))
    # Route for GET
    flash("Please select 'Delete Account' below to proceed")
    return redirect(url_for("messages.my_voice"))
