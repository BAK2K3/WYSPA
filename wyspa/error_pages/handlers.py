from flask import render_template, Blueprint


# Set up error pages blueprints
error_pages = Blueprint('error_pages', __name__)


# 404 error page
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404
