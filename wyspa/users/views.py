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
            else:
                return redirect(request.referrer)

        #  Inform user that credentials are incorrect
        else:
            flash("Incorrect Username and/or Password")
            return redirect(request.referrer)

    return redirect(url_for('core.index'))


# Log out user and redirect to Index
@ users.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('core.index'))


@users.route('/delete_user', methods=["GET", "POST"])
@ login_required
def delete_user():

    if request.method == "POST":
        try:
            User.delete_user(current_user.username)
            flash("Account and Wyspas deleted Successfully!")
            return redirect(url_for('users.logout'))
        except Exception as e:
            print(e)
            flash("Oops! Looks like something went wrong!")
            return redirect(url_for("messages.my_voice"))

    # Route for GET
    return redirect(url_for("messages.my_voice"))
