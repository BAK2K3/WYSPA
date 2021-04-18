"""
Views - Core Sub-module
=============
This sub-module is for core Flask routes.

Functions:
    - Index()
"""

from flask import render_template, Blueprint


# Configure Blueprint for core route
core = Blueprint('core', __name__)


# Route for home page
@core.route('/')
def index():
    """Basic routing for the home page.

    Parameters
    ----------
    None

    Returns
    -------
    index.html
    """

    return render_template('index.html')
