"""
Handlers - Error_Pages Submodule
=============
This submodule is for handling error pages.

Functions:
    - Error_404(error)

"""

from flask import render_template, Blueprint


# Set up error pages blueprints
error_pages = Blueprint('error_pages', __name__)


# 404 error page
@error_pages.app_errorhandler(404)
def error_404(error):
    """Catches and reroutes HTTP 404 errors."""
    # Delete the error variable as unused
    del error
    # Render 404 page
    return render_template('404.html'), 404
