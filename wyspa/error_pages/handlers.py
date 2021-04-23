"""
Handlers - Error_Pages Sub-module
=============

This sub-module is for handling error pages.

Functions:
    - Error_404(error)
    - Error_500(error)
"""

from flask import render_template, Blueprint


# Set up error pages blueprints
error_pages = Blueprint('error_pages', __name__)


# 404 error page
@error_pages.app_errorhandler(404)
def error_404(error):
    """Catches and reroutes HTTP 404 errors.

    Parameters
    ----------
    error: int
        The HTTP error code

    Returns
    -------
    404.html
    """

    """"""
    # Delete the error variable as unused
    del error
    # Render 404 page
    return render_template('404.html'), 404


# 500 error page
@error_pages.app_errorhandler(500)
def error_500(error):
    """Catches and reroutes HTTP 500 errors.

    Parameters
    ----------
    error : int
        The HTTP error code

    Returns
    -------
    500.html
    """
    # Delete the error variable as unused
    del error
    # Render 404 page
    return render_template('500.html'), 500
