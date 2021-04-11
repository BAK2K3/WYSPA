from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required

from wyspa.messages.classes import Wyspa


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


# Route for random messages or specific messages
@ messages.route('/view_message', defaults={'message_id': None})
@ messages.route('/view_message/<message_id>')
def view_message(message_id):

    # Return random message unless specified
    if message_id:
        message_entry = Wyspa.get_by_id(message_id)
        if not message_entry:
            flash("Oops! We couldn't find the requested Wyspa!")
            return redirect(url_for("messages.view_message"))
    else:
        message_entry = Wyspa.get_random_wyspa()
    return render_template('messages.html', message_entry=message_entry)


# "profile" page for viewing all wyspas and creating wyspas
@ messages.route('/my_voice')
@ login_required
def my_voice():

    users_messages = Wyspa.get_by_user(current_user.username)
    return render_template('my_voice.html', users_messages=users_messages)


# Wyspa creation
@ messages.route('/create_wyspa', methods=["GET", "POST"])
@ login_required
def create_wyspa():

    # Convert datetime
    formatted_expiry = Wyspa.string_to_datetime(
            expiry_date=request.form.get("expiryDate"),
            expiry_time=request.form.get("expiryTime"))

    # If the formatted_expiry fails
    if not formatted_expiry:
        flash("Expiry must be in the future!")
        return redirect(url_for("messages.my_voice"))

    # Try and convert the address to latlong
    try:
        converted_location = Wyspa.location_to_latlong(
            request.form.get("location"))
    except Exception as e:
        print(e)
        flash("Unable to locate address!")
        return redirect(url_for("messages.my_voice"))

    # Create a new wyspa, and write to DB
    if request.method == "POST":
        new_wyspa = Wyspa(author=current_user.username,
                          message=request.form.get("wyspaContent"),
                          mood=int(request.form.get("mood")),
                          location=converted_location,
                          expiry=formatted_expiry)
        new_wyspa.write_wyspa()
        return redirect(url_for("messages.my_voice"))


# Add comment to existing Wyspa
@ messages.route('/add_comment/<message_id>', methods=["GET", "POST"])
@ login_required
def add_comment(message_id):

    if request.method == "POST":

        # Retrieve Wyspa
        retrieved_wyspa = Wyspa.get_by_id(message_id)

        # Check if user is logged in to add to comment db
        if current_user.is_authenticated:
            retrieved_wyspa.add_comment(request.form.get(
                "commentReply"), current_user.username)
        # Otherwise resort to default entry
        else:
            retrieved_wyspa.add_comment(request.form.get(
                "commentReply"))

        return redirect(url_for("messages.view_message",
                                message_id=retrieved_wyspa._id))


# Remove comment from existing Wyspa
@messages.route('/remove_comment/<message_id>/<comment_id>',
                methods=["GET", "POST"])
@ login_required
def remove_comment(message_id, comment_id):

    retrieved_wyspa = Wyspa.get_by_id(message_id)
    retrieved_wyspa.remove_comment(int(comment_id)-1)

    return redirect(url_for("messages.view_message",
                            message_id=retrieved_wyspa._id))


# Add "Listen" to existing Wyspa
@ messages.route('/add_listen/<message_id>/', defaults={'listener': None})
@ messages.route('/add_listen/<message_id>/<listener>')
def add_listen(message_id, listener):

    # Retrieve the wyspa
    retrieved_wyspa = Wyspa.get_by_id(message_id)

    # Check if user is logged in
    if current_user.is_authenticated:

        # Inform the user if they've already listened
        if current_user.username in retrieved_wyspa.get_info()["listens"]:
            flash("You've already listened to this Wyspa!")

        # Store Listen
        else:
            retrieved_wyspa.add_listen(listener)

    # Inform the user they need to be logged in
    else:
        flash("Sorry - you need to be logged in to listen to a Wyspa!")

    return redirect(url_for("messages.view_message",
                            message_id=retrieved_wyspa._id))


# Delete WYSPA
@ messages.route('/remove_wyspa/<message_id>', methods=["GET", "POST"])
@ login_required
def remove_wyspa(message_id):

    if request.method == "POST":
        Wyspa.delete_wyspa(message_id)
        return redirect(url_for("messages.my_voice"))


# Edit WYSPA
@ messages.route('/edit_wyspa/<message_id>', methods=["GET", "POST"])
@ login_required
def edit_wyspa(message_id):

    # Retreive WYSPA
    retrieved_wyspa = Wyspa.get_by_id(message_id)
    if not retrieved_wyspa:
        flash("We couldn't find that Wyspa!")
        return redirect(url_for("messages.my_voice"))

    # Verify the owner of wyspa is trying to edit it
    if retrieved_wyspa.author != current_user.username:
        flash("You can't edit someone elses Wyspa!")
        return redirect(url_for("messages.my_voice"))

        # Post View
    if request.method == "POST":

        # Convert datetime
        formatted_expiry = Wyspa.string_to_datetime(
            expiry_date=request.form.get("expiryDate"),
            expiry_time=request.form.get("expiryTime"))

        # If the formatted_expiry fails
        if not formatted_expiry:
            flash("Expiry must be in the future!")
            return render_template("edit_wyspa.html",
                                   retrieved_wyspa=retrieved_wyspa)

        # Try and convert the address to latlong
        try:
            converted_location = Wyspa.location_to_latlong(
                request.form.get("location"))
        except Exception as e:
            print(e)
            flash("Unable to locate address!")
            return render_template("edit_wyspa.html",
                                   retrieved_wyspa=retrieved_wyspa)

        # Call edit function
        retrieved_wyspa.edit_wyspa(message=request.form.get("wyspaContent"),
                                   mood=int(request.form.get("mood")),
                                   location=converted_location,
                                   expiry=formatted_expiry)

        flash("Wyspa Updated!")
        return redirect(url_for("messages.my_voice"))

    # Get view
    return render_template('edit_wyspa.html', retrieved_wyspa=retrieved_wyspa)


# Wyspa Deletion
@ messages.route('/delete_wyspa/<message_id>', methods=["GET", "POST"])
@ login_required
def delete_wyspa(message_id):

    if request.method == "POST":
        # Obtain Wyspa details
        retrieved_wyspa = Wyspa.get_by_id(message_id)
        # Verify User
        if not retrieved_wyspa.author == current_user.username:
            flash("You do not have access to this Wyspa!")
            return redirect(url_for("messages.my_voice"))
        # Delete Wyspa
        else:
            Wyspa.delete_wyspa(message_id)
            return redirect(url_for("messages.my_voice"))

    # Route for GET
    return redirect(url_for("messages.my_voice"))
