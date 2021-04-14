import re

from flask import (render_template, Blueprint, request,
                   redirect, flash, url_for, session)
from flask_login import (LoginManager, login_user,
                         logout_user, current_user)
from werkzeug.security import generate_password_hash, check_password_hash

from wyspa.factory.initialisation import mongo
from wyspa.users.classes import User


# Configure Blueprint for user route
users = Blueprint('users', __name__)


# Instantiate login_manager
login_manager = LoginManager()


# Define the user_loader callback for Flask-Login
@login_manager.user_loader
def load_user(username):
    login_attempt = mongo.db.users.find_one({"username": username.lower()})
    if not login_attempt:
        return None
    return User(username=login_attempt["username"])


# Register Route
@ users.route("/register", methods=["GET", "POST"])
def register():

    # Check if user is already logged in
    if current_user.is_authenticated:
        flash("You are already logged in!")
        return redirect(url_for("core.index"))

    if request.method == "POST":

        # Verify user password
        user_password = request.form.get("passwordRegister")
        password_confirmation = request.form.get("passwordConfirm")
        if not re.search("^(?=.*[^a-zA-Z]).{6,20}$", user_password):
            flash("Password format incorrect!")
            return render_template("index.html")

        if user_password != password_confirmation:
            flash("Passwords do not match!")
            return render_template("index.html")

        # check if username already exists in DB
        username_check = mongo.db.users.find_one(
            {"username": request.form.get("usernameRegister").lower()})

        # Username Validation
        if username_check:
            flash("Username already exists!")
            return redirect(url_for("core.index"))

        # Create a registration dictionary
        registration = {
            "username": request.form.get("usernameRegister").lower(),
            "password": generate_password_hash(user_password)
        }

        # Update DB with registration dictionary
        mongo.db.users.insert_one(registration)

        # Create an instance of User with new user, and log in
        new_user = User(username=registration['username'])
        login_user(new_user)

        # Save user's timezone in session
        session['timezone'] = request.form.get("timezoneRegister")

        # Flash and redirect
        flash("Registration Successful")
        return redirect(url_for("messages.my_voice"))

    # Routing for Get Requests
    return redirect(url_for("core.index"))


@ users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # Checks if next parameter is in the referal URL
        if "?next=%2F" in request.referrer:
            return redirect(request.referrer.split("?next=%2F")[1])
        else:
            return redirect(request.referrer)

    if request.method == "POST":
        # Query DB for username
        login_check = mongo.db.users.find_one(
            {"username": request.form.get("usernameLogin").lower()})

        # Check username exists and password matches
        if login_check and check_password_hash(
                login_check["password"],
                request.form.get("passwordLogin")):

            # Create an instance of User class
            existing_user = User(username=login_check['username'])
            # Log in User
            login_user(existing_user)
            # Save user's timezone in session
            session['timezone'] = request.form.get("timezoneLogin")
            flash(f"Welcome, {current_user.username}")

            # Checks if next parameter is in the referal URL
            if "?next=%2F" in request.referrer:
                return redirect(request.referrer.split("?next=%2F")[1])
            else:
                return redirect(request.referrer)

        else:
            #  Inform user that credentials are incorrect
            flash("Incorrect Username and/or Password")
            return redirect(request.referrer)

    return redirect(url_for('core.index'))


# Log out user and redirect to Index
@ users.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('core.index'))
