from flask import render_template, Blueprint
from wyspa.factory.initialisation import mongo
import os

GMAPS_API = os.environ.get("GMAPS_API")

# Configure Blueprint for maps route
maps = Blueprint('maps', __name__)


@maps.route('/map_overview')
def map_overview():

    return render_template('maps.html', GMAPS_API=GMAPS_API)
