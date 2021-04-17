"""
Views - Maps Sub-module
==================================

This module contains the Maps Views sub-module which
handles data preparation and routing for the Map
feature.

Functions:
    map_overview()
"""

import os

from flask import render_template, Blueprint

from wyspa.messages.classes import Wyspa

# Set the Google Maps API Key to be passed to view
GMAPS_API = os.environ.get("GMAPS_API")

# Configure Blueprint for maps route
maps = Blueprint('maps', __name__)


@maps.route('/map_overview')
def map_overview():
    """Map Route

    This route queries the DB for all Wyspas,
    prepares the data, and sends both the Gmaps API and map_data
    to the rendered HTML page.
    """

    # Retrieve all messages
    all_messages = Wyspa.get_all_wyspas()

    # Convert data from messages to id and latlng
    map_data = Wyspa.wyspa_to_map(all_messages)

    # Render Map template, passing in API and map data
    return render_template('maps.html',
                           GMAPS_API=GMAPS_API,
                           map_data=map_data)
