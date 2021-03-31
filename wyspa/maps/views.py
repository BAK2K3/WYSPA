import os

from flask import render_template, Blueprint

from wyspa.messages.classes import Wyspa


GMAPS_API = os.environ.get("GMAPS_API")

# Configure Blueprint for maps route
maps = Blueprint('maps', __name__)


@maps.route('/map_overview')
def map_overview():

    # Retrieve all messages
    all_messages = Wyspa.get_all_wyspas()

    # Convert data from messages to id and latlng
    map_data = Wyspa.wyspa_to_map(all_messages)

    return render_template('maps.html',
                           GMAPS_API=GMAPS_API,
                           map_data=map_data)
