from geopy.geocoders import Nominatim
from random import random


def location_to_latlong(user_location):
    geolocator = Nominatim(user_agent="WYSPA")
    location = geolocator.geocode(user_location)
    latlong = {"lat": location.latitude + (round((random() / 10), 10)-0.05),
               "lng": location.longitude + (round((random() / 10), 10)-0.05)}
    return latlong
