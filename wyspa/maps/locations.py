from geopy.geocoders import Nominatim
from random import uniform


def location_to_latlong(user_location):
    geolocator = Nominatim(user_agent="WYSPA")
    location = geolocator.geocode(user_location)
    latlong = {"lat": location.latitude + (round(uniform(0.1, -0.1), 10)),
               "lng": location.longitude + (round(uniform(0.1, -0.1), 10))}
    return latlong
