from geopy.geocoders import Nominatim


def location_to_latlong(user_location):
    geolocator = Nominatim(user_agent="WYSPA")
    location = geolocator.geocode(user_location)
    latlong = {"lat": location.latitude,
               "lng": location.longitude}
    return latlong
