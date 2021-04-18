"""
Views - Messages Sub-module
==================================

This module contains the Messages Views sub-module which
handles all routes and data handling relating to Wyspas.

Functions:
    view_message(message_id=None)
    my_voice()
    create_wyspa()
    add_comment(message_id)
    remove_comment(message_id, comment_id)
    add_listen(message_id)
    edit_wyspa(message_id)
    delete_wyspa(message_id)
"""

from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required

from wyspa.messages.classes import Wyspa


# Configure Blueprint for core route
messages = Blueprint('messages', __name__)


# Route for random messages or specific messages
@ messages.route('/view_message', defaults={'message_id': None})
@ messages.route('/view_message/<message_id>')
def view_message(message_id):
    """View Message Route [Get]

    Login: Not Required

    This route either retrieves a random Wyspa from the Database,
    or obtains a specific message if one is specified in the request.
    The Wyspa is then passed into the template for rendering. This page
    allows a user to read, edit, listen to, or comment on Wyspas.

    Parameters
    ----------
    message_id : str *optional
        _id parameter of Wyspa to be queried from the database.

    Returns
    -------
    messages.html
    """

    # Query the Database for specified _id
    if message_id:
        message_entry = Wyspa.get_by_id(message_id)
        # Obtain a random Wyspa and flash error if not found
        if not message_entry:
            flash("Oops! We couldn't find the requested Wyspa!")
            return redirect(url_for("messages.view_message"))
    # Otherwise, obtain a random Wyspa
    else:
        message_entry = Wyspa.get_random_wyspa()
    return render_template('messages.html', message_entry=message_entry)


# User Profile route for viewing existing wyspas and creating wyspas
@ messages.route('/my_voice')
@ login_required
def my_voice():
    """My Voice Route [Get]

    Login: Required

    This route obtains all of the logged in users Wyspas,
    and passes them to the My Voice route to be displayed
    and managed. Users can also create Wyspas or delete their
    account from this page.

    Parameters
    ----------
    None

    Returns
    -------
    my_voice.html
    """

    # Query the database for all of the logged in user's wyspas
    users_messages = Wyspa.get_by_user(current_user.username)
    return render_template('my_voice.html', users_messages=users_messages)


# Wyspa creation
@ messages.route('/create_wyspa', methods=["GET", "POST"])
@ login_required
def create_wyspa():
    """Create Wyspa Route [Get/Post]

    Login: Required

    This route retrieves the form data completed
    by the user, verifies it and formats it accordingly,
    writes the Wyspa to the Database, then re-routes them
    back to the My Voice Route.

    This is a POST route; if accessed via GET, user
    is redirected to My Voice route with no further action.

    Parameters
    ----------
    None

    Returns
    -------
    Redirect (my_voice) [Get/Post]
    """

    if request.method == "POST":
        # Try and conver the date and time provided in the form
        try:
            formatted_expiry = Wyspa.string_to_datetime(
                    expiry_date=request.form.get("expiryDate"),
                    expiry_time=request.form.get("expiryTime"))
        # Catch TypeError and redirect user back to My Voice
        except TypeError:
            flash("Oops! Something went wrong! Please try again!")
            return redirect(url_for("messages.my_voice"))

        # If Formatted_Expiry returns False, expiry is in the past
        if not formatted_expiry:
            flash("Expiry must be in the future!")
            return redirect(url_for("messages.my_voice"))

        # Try and convert the address to latlong
        try:
            converted_location = Wyspa.location_to_latlong(
                request.form.get("location"))
        # Catch AttributeError and confirm unsuccessful
        except AttributeError:
            flash("Unable to locate address!")
            return redirect(url_for("messages.my_voice"))

        # Create a new wyspa, and write to DB
        new_wyspa = Wyspa(author=current_user.username,
                          message=request.form.get("wyspaContent"),
                          mood=int(request.form.get("mood")),
                          location=converted_location,
                          expiry=formatted_expiry)
        new_wyspa.write_wyspa()
        flash("Wyspa successful!")
        return redirect(url_for("messages.my_voice"))

    # Get Route
    return redirect(url_for("messages.my_voice"))


# Add comment to existing Wyspa
@ messages.route('/add_comment/<message_id>', methods=["GET", "POST"])
@ login_required
def add_comment(message_id):
    """Add Comment Route [Get/Post]

    Login: Required

    This route retrieves the Wyspa currently being viewed,
    ensures the user is logged in, adds the comment provided
    by the user to the Wyspa, then re-routes them back to the
    View Message Route along with the Wyspa ID of the current Wyspa.

    This is a POST route; if accessed via GET, user
    is redirected to View Message route with no further action.

    Parameters
    ----------
    message_id : str
        _id parameter of Wyspa which requires editting.

    Returns
    -------
    Redirect (view_message) [Get/Post]
    """

    # Retrieve Wyspa
    retrieved_wyspa = Wyspa.get_by_id(message_id)

    # If comment posted
    if request.method == "POST":
        retrieved_wyspa.add_comment(new_comment=request.form.get(
            "commentReply"), comment_author=current_user.username)

    # Both GET and POST routes
    return redirect(url_for("messages.view_message",
                            message_id=retrieved_wyspa.wyspa_id))


# Remove comment from existing Wyspa
@messages.route('/remove_comment/<message_id>/<comment_id>',
                methods=["GET", "POST"])
@ login_required
def remove_comment(message_id, comment_id):
    """Remove Comment Route [Get/Post]

    Login: Required

    This route retrieves the Wyspa currently being viewed,
    ensures the user is logged in, and is either the Wyspa
    owner or the comment owner, then uses the provided
    comment_id to remove the requested comment from the
    comment list. The user is then re-routed back to the
    View Message Route along with the Wyspa ID of the current
    Wyspa.

    This is a POST route; if accessed via GET, user
    is redirected to View Message route with no further action.

    Parameters
    ----------
    message_id : str
        _id parameter of Wyspa which requires editting.

    comment_id : str
        Index position of the comment that needs deleting.

    Returns
    -------
    Redirect (view_message) [Get/Post]
    """

    # Query DB for Wyspa
    retrieved_wyspa = Wyspa.get_by_id(message_id)

    if request.method == "POST":
        # Set the comment index
        comment_index = int(comment_id)-1
        # Ensure user is Wyspa or Comment owner
        for key in retrieved_wyspa.comments[comment_index].keys():
            comment_author = key
        if (current_user.username == retrieved_wyspa.author
                or current_user.username == comment_author):
            retrieved_wyspa.remove_comment(comment_index)
        else:
            flash("You are not authorised to delete this comment!")

    # GET and POST Routes
    return redirect(url_for("messages.view_message",
                            message_id=retrieved_wyspa.wyspa_id))


# Add "Listen" to existing Wyspa
@ messages.route('/add_listen/<message_id>/')
def add_listen(message_id):
    """Add Listen Route [Get]

    Login: Required

    This route retrieves the Wyspa currently being viewed,
    ensures the user is logged in, checks whether the user's
    username exists in the listens list of the Wyspa, and then
    adds the username to the list and increments the listen_count.
    The user is then re-routed back to the View Message Route
    along with the Wyspa ID of the current Wyspa.

    Login Required decorator has not been used as the
    referrer should not be passed to the Login function for this
    action.

    Parameters
    ----------
    message_id : str
        _id parameter of Wyspa which requires editting.

    Returns
    -------
    Redirect (view_message)

    """

    # Retrieve the wyspa
    retrieved_wyspa = Wyspa.get_by_id(message_id)

    # Check if user is logged in
    if current_user.is_authenticated:

        # Inform the user if they've already listened
        if current_user.username in retrieved_wyspa.get_info()["listens"]:
            flash("You've already listened to this Wyspa!")

        # Store Listen
        else:
            retrieved_wyspa.add_listen(current_user.username)

    # Inform the user they need to be logged in
    else:
        flash("You must be logged in to listen to a Wyspa!")

    return redirect(url_for("messages.view_message",
                            message_id=retrieved_wyspa.wyspa_id))


# Edit WYSPA
@ messages.route('/edit_wyspa/<message_id>', methods=["GET", "POST"])
@ login_required
def edit_wyspa(message_id):
    """Edit Wyspa Route [Get/Post]

    Login: Required

    This route contains seperate routes for Get and Post.
    Both routes verify the Wyspa exists in the database,
    and verifies the owner of the Wyspa.

    The Get request passes the existing Wyspa to the edit_wyspa.html
    template to prepopulate the Wyspa form.

    The Post request verifies the data (datetime and location),
    processes it, and updates the Wyspa in the database, before
    redirecting the user to the my_voice route.

    Parameters
    ----------
    message_id : str
        _id parameter of Wyspa which requires editting.

    Returns
    -------
    edit_wyspa.html [Get]

    Redirect (my_voice) [Post]
    """

    # Retreive WYSPA
    retrieved_wyspa = Wyspa.get_by_id(message_id)
    if not retrieved_wyspa:
        flash("We couldn't find that Wyspa!")
        return redirect(url_for("messages.my_voice"))

    # Verify the owner of wyspa is trying to edit it
    if retrieved_wyspa.author != current_user.username:
        flash("You can't edit someone elses Wyspa!")
        return redirect(url_for("messages.my_voice"))

    # Post Route
    if request.method == "POST":

        # Convert datetime
        try:
            formatted_expiry = Wyspa.string_to_datetime(
                expiry_date=request.form.get("expiryDate"),
                expiry_time=request.form.get("expiryTime"))

        # Catch TypeError and redirect user back to edit
        except TypeError:
            flash("Oops! Something went wrong! Please try again!")
            expiry_date = Wyspa.datetime_to_string(retrieved_wyspa.expiry)
            return render_template("edit_wyspa.html",
                                   retrieved_wyspa=retrieved_wyspa,
                                   expiry_date=expiry_date)

        # If Formatted_Expiry returns False, expiry is in the past
        if not formatted_expiry:
            flash("Expiry must be in the future!")
            expiry_date = Wyspa.datetime_to_string(retrieved_wyspa.expiry)
            return render_template("edit_wyspa.html",
                                   retrieved_wyspa=retrieved_wyspa,
                                   expiry_date=expiry_date)

        # Try and convert the address to latlong
        try:
            converted_location = Wyspa.location_to_latlong(
                request.form.get("location"))
        # Catch AttributeError and confirm unsuccessful
        except AttributeError:
            flash("Unable to locate address!")
            expiry_date = Wyspa.datetime_to_string(
                retrieved_wyspa.expiry)
            return render_template("edit_wyspa.html",
                                   retrieved_wyspa=retrieved_wyspa,
                                   expiry_date=expiry_date)

        # Call edit function
        retrieved_wyspa.edit_wyspa(message=request.form.get("wyspaContent"),
                                   mood=int(request.form.get("mood")),
                                   location=converted_location,
                                   expiry=formatted_expiry)

        flash("Wyspa Updated!")
        return redirect(url_for("messages.my_voice"))

    # Get Route
    expiry_date = Wyspa.datetime_to_string(retrieved_wyspa.expiry)

    return render_template('edit_wyspa.html',
                           retrieved_wyspa=retrieved_wyspa,
                           expiry_date=expiry_date)


# Wyspa Deletion
@ messages.route('/delete_wyspa/<message_id>', methods=["GET", "POST"])
@ login_required
def delete_wyspa(message_id):
    """Delete Wyspa Route [Get/Post]

    Login: Required

    This route queries the database for the Wyspa that requires
    deletion, verifies the ownership of the Wyspa, and then deletes
    it from the Database. The user is then redirected to the My Voice route.

    This is a POST route; if accessed via GET, user
    is redirected to My Voice route with no further action.

    Parameters
    ----------
    message_id : str
        _id parameter of Wyspa which requires deletion.

    Returns
    -------
    Redirect (my_voice) [Get/Post]
    """

    if request.method == "POST":
        # Obtain Wyspa details
        retrieved_wyspa = Wyspa.get_by_id(message_id)
        # Verify User
        if not retrieved_wyspa.author == current_user.username:
            flash("You do not have access to this Wyspa!")
            return redirect(url_for("messages.my_voice"))

        # Delete Wyspa
        Wyspa.delete_wyspa(message_id)
        return redirect(url_for("messages.my_voice"))

    # Route for GET
    return redirect(url_for("messages.my_voice"))
