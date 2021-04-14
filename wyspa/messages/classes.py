from random import uniform
from bson.objectid import ObjectId
from datetime import datetime
from dateutil import tz

from flask import session
from geopy.geocoders import Nominatim

from wyspa.factory.initialisation import mongo


# Create a class for WYSPAs
class Wyspa():
    def __init__(self, author, message, mood, location,
                 expiry=None, comments=[], listens=[],
                 listenCount=0, _id=None):
        self._id = _id
        self.author = author
        self.message = message
        self.mood = mood
        self.location = location
        self.comments = comments if comments else []
        self.listens = listens if listens else []
        self.listenCount = listenCount if listenCount else 0
        self.expiry = expiry if expiry else None

    def get_info(self):
        # Return Dictionary for DB
        info = {'author': self.author, 'message': self.message,
                'mood': self.mood, 'location': self.location,
                'expiry': self.expiry, 'comments': self.comments,
                'listens': self.listens, 'listenCount': self.listenCount}
        return info

    def write_wyspa(self):
        mongo.db.messages.insert_one(self.get_info())

    def edit_wyspa(self, message, mood, location, expiry):
        self.message = message
        self.mood = mood
        self.location = location
        self.expiry = expiry
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def remove_comment(self, index):
        self.comments.pop(index)
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_comment(self, new_comment, comment_author="anonymous"):
        self.comments.append({comment_author: new_comment})
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_listen(self, listener):
        self.listens.append(listener)
        self.listenCount += 1
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    @classmethod
    def get_by_id(cls, _id):
        if ObjectId.is_valid(_id):
            data = mongo.db.messages.find_one({"_id": ObjectId(_id)})
            if data is not None:
                return cls(**data)
            else:
                return False
        else:
            return False

    @classmethod
    def get_by_user(cls, username):
        data = list(mongo.db.messages.find({"author": username}))
        # Update Timezone of each Wyspa
        user_timezone = tz.gettz(session["timezone"])
        for wyspa in data:
            wyspa['expiry'] = wyspa['expiry'].astimezone(user_timezone)

        if data is not None:
            return_data = []
            for message in data:
                return_data.append(cls(**message))
            return return_data

    @classmethod
    def get_random_wyspa(cls):
        data = list(mongo.db.messages.aggregate(
            [{"$sample": {"size": 1}}]))
        if data != []:
            return cls(**data[0])

    @classmethod
    def get_all_wyspas(cls):
        data = list(mongo.db.messages.aggregate(
            [{"$sort": {"listenCount": -1}}]))

        if data != []:
            return_data = []
            for message in data:
                return_data.append(cls(**message))
            return return_data

    @staticmethod
    def delete_wyspa(_id):
        mongo.db.messages.remove({"_id": ObjectId(_id)})

    @staticmethod
    def location_to_latlong(user_location):
        geolocator = Nominatim(user_agent="WYSPA")
        location = geolocator.geocode(user_location)
        latlong = {"lat": location.latitude + (round(uniform(0.1, -0.1), 10)),
                   "lng": location.longitude + (round(uniform(0.1, -0.1), 10))}
        return latlong

    @staticmethod
    def string_to_datetime(expiry_date, expiry_time):

        # Format date-time
        date_string = expiry_date + " " + expiry_time
        date_format = "%d-%m-%Y %H:%M"
        formatted_expiry = datetime.strptime(date_string, date_format)

        # Set users timezone
        user_timezone = tz.gettz(session["timezone"])
        formatted_expiry = formatted_expiry.replace(tzinfo=user_timezone)

        # Set up tz aware datetime object for comparrison
        server_timezone = tz.tzlocal()
        server_time = datetime.now().replace(tzinfo=server_timezone)

        # Ensure expiry date is in the future
        if formatted_expiry < server_time:
            return False

        else:
            return formatted_expiry

    @staticmethod
    def datetime_to_string(formatted_expiry):

        # Set expiry date timezone
        user_timezone = tz.gettz(session["timezone"])
        formatted_expiry = formatted_expiry.astimezone(user_timezone)

        # Extract date and time from datetime object
        date_format = "%d-%m-%Y %H:%M"
        string_date = formatted_expiry.strftime(date_format)

        # Seperate date and time
        formatted_date = string_date[:10]
        formatted_time = string_date[11:]
        return [formatted_date, formatted_time]

    @staticmethod
    def wyspa_to_map(wyspas):
        if wyspas is not None:
            prepared_data = []
            for wyspa in wyspas:
                prepared_data.append(
                    {"_id": str(wyspa._id), "location": wyspa.location,
                     "mood": wyspa.mood, "listens": (wyspa.listenCount)})
            return prepared_data
