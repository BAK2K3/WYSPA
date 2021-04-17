"""
Views - Core Submodule
=============
This submodule is for core Flask routes.

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
