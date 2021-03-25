from flask import render_template, Blueprint


# Configure Blueprint for core route
core = Blueprint('core', __name__)


# Route for home page
@core.route('/')
def index():
    return render_template('index.html')
