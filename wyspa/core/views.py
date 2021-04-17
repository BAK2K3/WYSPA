"""
Views - Core Submodule
=============
This submodule is for any Flask routes which do
not relate to either Wyspas (messages) or Users.

Functions:
    - Index()
"""

from flask import render_template, Blueprint


# Configure Blueprint for core route
core = Blueprint('core', __name__)


# Route for home page
@core.route('/')
def index():
    """Basic routing for the home page."""
    return render_template('index.html')
