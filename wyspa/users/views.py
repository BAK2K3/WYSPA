from flask import render_template, Blueprint, request, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from wyspa.factory.initialisation import mongo
from .classes import User


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
    if request.method == "POST":

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
            "password": generate_password_hash(
                request.form.get("passwordRegister"))
        }

        # Update DB with registration dictionary
        mongo.db.users.insert_one(registration)

        # Create an instance of User with new user, and log in
        new_user = User(username=registration['username'])
        login_user(new_user)

        # Flash and redirect
        flash("Registration Successful")
        return redirect(url_for("core.index"))


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))

    if request.method == "POST":
        # Query DB for username
        login_check = mongo.db.users.find_one(
            {"username": request.form.get("usernameLogin").lower()})

        # Check username exists and password matches
        if login_check and check_password_hash(
                login_check["password"],
                request.form.get("passwordLogin")):

            # Create an instance of User class, log them in, and redirect
            existing_user = User(username=login_check['username'])
            login_user(existing_user)
            flash(f"Welcome, {current_user.username}")
            return redirect(url_for("core.index"))

        else:
            #  Inform user that credentials are incorrect
            flash("Incorrect Username and/or Password")
            return redirect(url_for("users.login"))

    return render_template("index.html")


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))
