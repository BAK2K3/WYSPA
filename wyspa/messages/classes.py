"""
Classes - Message Sub-module
=============

Contains the Wyspa class, for storing, retreiving,
editing, and preparing data to be read and written
to the Wyspa Database.

Classes: Wyspa
"""

# https://stackoverflow.com/questions/24434510/how-to-deal-with-pylints-too-many-instance-attributes-message
# pylint: disable=too-many-arguments, too-many-instance-attributes
# Considered attributes for Class and beleive it is reasonable in this scenario
import re
from random import uniform
from datetime import datetime
from dateutil import tz
from bson.objectid import ObjectId

from flask import session
from geopy.geocoders import Nominatim

from wyspa.factory.initialisation import mongo


# Create a class for WYSPAs
class Wyspa():
    """
    A class to represent the Wyspa Message.
    Contains all required methods to store,
    retrieve, edit, and prepare data appropriately,
    along with reading and writing Wyspas to the Database.

    Attributes
    -----------

    _id : str
        A unique identifier for the Wyspa.

    author : str
        The username of the author who created the Wyspa.

    message : str
        The main body of the message.

    mood : int
        A number representing the mood of the message (0,1,2) =>
        (Sad, Neutral, Happy)

    location : dict
        Dict format: {lat: int, long: int}
        A dictionary containing latitude and longitude.

    comments : list
        List format: [{author: comment}, {author: comment},...]
        A list of dictionaries, containing comments and their
        respective author.

    listens : list
        List format: [username, username,...]
        A unique list of users usernames who have
        listened to a Wyspa.

    listen_count : int
        An integer representation of the length of the
        listen list.

    expiry : datetime
        A datetime object. When writing to the DB this is
        in the users time zone, when reading from the DB this is
        in the Server's time zone (UTC).

    Methods
    -------

    wyspa_id():
        Returns the protected _id property of the Wyspa.

    get_info()
        Formats and returns the current Wyspa's attributes as a dict.

    write_wyspa()
        Writes a Wyspa to the Database.

    edit_wyspa(message, mood, location, expiry)
        Edits an existing Wyspa, and updates the Database.

    remove_comment(index)
        Removes a comment from the Wyspa, and updates the Database.

    add_comment(new_comment, comment_author)
        Adds a comment to the Wyspa, and updates the Database.

    add_listen(listener)
        Adds a Listen to the Wyspa, and updates the Database.

    get_by_id(_id)
        Retrieves a Wyspa from the database using an ID.

    get_by_user(username)
        Retrieves all of a given user's Wyspas from the Database.

    get_random_wyspa()
        Obtains a random Wyspa from the Database.

    get_all_wyspas()
        Retreives all Wyspas from the Database.

    delete_wyspa(_id)
        Deletes a Wyspa from the Database.

    location_to_latlong(user_location)
        Converts the name of a Location to scrambled geocoordinates.

    string_to_datetime(expiry_date, expiry_time)
        Converts datetime string to time zone aware datetime object.

    datetime_to_string(formatted_expiry)
        Converts datetime object to user time zone formatted string.

    wyspa_to_map(wyspas)
        Isolates and prepares the required data for Map routing.

    def whitespace_check(message):
        Checks given string for non-whitespace characters.
    """

    def __init__(self, author, message, mood, location, expiry=None,
                 comments=None, listens=None, listen_count=None, _id=None):
        """Constructs all the necessary attributes for the Wyspa object.

        Attributes
        -----------

        _id : str
            A unique identifier for the Wyspa.

        author : str
            The username of the author who created the Wyspa.

        message : str
            The main body of the message.

        mood : int
            A number representing the mood of the message (0,1,2) =>
            (Sad, Neutral, Happy)

        location : dict
            Dict format: {lat: int, long: int}
            A dictionary containing latitude and longitude.

        comments : list
            List format: [{author: comment}, {author: comment},...]
            A list of dictionaries, containing comments and their
            respective author.

        listens : list
            List format: [username, username,...]
            A unique list of users usernames who have
            listened to a Wyspa.

        listen_count :int
            An integer representation of the length of the
            listen list.

        expiry : datetime
            A datetime object. When writing to the DB this is
            in the users timezone, when reading from the DB this is
            in the Server's timezone (UTC).
        """

        self._id = _id
        self.author = author
        self.message = message
        self.mood = mood
        self.location = location
        self.comments = comments if comments else []
        self.listens = listens if listens else []
        self.listen_count = listen_count if listen_count else 0
        self.expiry = expiry if expiry else None

    @property
    def wyspa_id(self):
        """Returns the protected _id property of the Wyspa.

        Parameters
        ----------
        None

        Returns
        -------
        _id : str
        """
        return self._id

    def get_info(self):
        """Formats and returns the current Wyspa's attributes as a dict.

        The format of the dictionary allows the return of this method
        to be written directly to the Database.

        Parameters
        ----------
        None

        Returns
        -------
        info : dict
        """

        info = {'author': self.author, 'message': self.message,
                'mood': self.mood, 'location': self.location,
                'expiry': self.expiry, 'comments': self.comments,
                'listens': self.listens, 'listen_count': self.listen_count}
        return info

    def write_wyspa(self):
        """Writes a Wyspa to the Database.

        Writes the output of the get_info
        method directly to the database.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        mongo.db.messages.insert_one(self.get_info())

    def edit_wyspa(self, message, mood, location, expiry):
        """Edits an existing Wyspa, and updates the Database.

        Updates the attributes of a Wyspa object, and updates
        the respective entry in the Database.

        Parameters
        ----------
        message : str
            The main body of the message.

        mood : int
            A number representing the mood of the message (0,1,2) =>
            (Sad, Neutral, Happy)

        location : dict
            Dict format: {lat: int, long: int}
            A dictionary containing latitude and longitude.

        expiry : datetime
            A datetime object. When writing to the DB this is
            in the users timezone, when reading from the DB this is
            in the Server's timezone (UTC).

        Returns
        -------
        None
        """

        self.message = message
        self.mood = mood
        self.location = location
        self.expiry = expiry
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def remove_comment(self, index):
        """Removes a comment from the Wyspa, and updates the Database.

        Uses the index of the comment required for deletion
        to remove the comment from the object's comment list, and
        updates the Database accordingly.

        Parameters
        ----------
        index : int
            The index of the comment to be removed

        Returns
        -------
        None
        """

        self.comments.pop(index)
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_comment(self, new_comment, comment_author):
        """Adds a comment to the Wyspa, and updates the Database.

        Appends a new comment (in the form of a dictionary) to the
        comment attribute, and updates the Database.

        Parameters
        ----------
        new_comment : str
            The body of the comment
        comment_author: str
            The author of the comment

        Returns
        -------
        None
        """

        self.comments.append({comment_author: new_comment})
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_listen(self, listener):
        """Adds a Listen to the Wyspa, and updates the Database.

        Appends the username of the listener to the
        Listen attribute, increments the listen count,
        and updates the database.

        Parameters
        ----------
        listener : str
            The username of the listener.

        Returns
        -------
        None
        """

        self.listens.append(listener)
        self.listen_count += 1
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    @classmethod
    def get_by_id(cls, _id):
        """Retrieves a Wyspa from the database using an ID.

        Checks the ID passed in is a valid ObjectID,
        queries the Database for the ID, then returns
        the database entry as a constructed Wyspa object.

        Parameters
        ----------
        listener : str
            The username of the listener.

        Returns
        -------
        data:  Wyspa Object or bool
            Constructed Wyspa object returned if successful.
            False bool returned if unsuccessful.
        """

        # Checks ID passed in is valid ObjectID
        if ObjectId.is_valid(_id):
            data = mongo.db.messages.find_one({"_id": ObjectId(_id)})
            if data is not None:
                return cls(**data)
        # Return False if message not in DB or if ID is not valid ObjectID
        data = False
        return data

    @classmethod
    def get_by_user(cls, username):
        """Retrieves all of a given user's Wyspas from the Database.

        Queries the Database for a given user's Wyspas,
        converts the Expiry datetime object to logged in user's
        time zone, then returns a list of constructed Wyspa objects.

        Parameters
        ----------
        username : str
            The username to query the "author" field within the database.

        Returns
        -------
        return_data : list
            A list of constructed Wyspa objects.
        """

        # Query the database for all user's Wyspas
        data = list(mongo.db.messages.find({"author": username}))

        # Initialise return_data list
        return_data = []

        # Checks to see if any documents have been retrieved
        if data is not None:

            # Obtain user's time zone from session
            user_timezone = tz.gettz(session["timezone"])

            # For each Wyspa obtained
            for wyspa in data:
                # Set the time zone of each Wyspa's expiry.
                wyspa['expiry'] = wyspa['expiry'].astimezone(user_timezone)
                # Create a Wyspa with the data, and append to return_data list
                return_data.append(cls(**wyspa))

        return return_data

    @classmethod
    def get_random_wyspa(cls):
        """Obtains a random Wyspa from the Database.

        Obtains a single random sample through MongoDB
        aggregation, and returns the document as a constructed
        Wyspa object.

        Parameters
        ----------
        None

        Returns
        -------
        data : object or list
            object : Constructed Wyspa Object (if successful).
            list : empty list (if unsuccessful).
        """

        # Obtain a random sample from the messages database
        data = list(mongo.db.messages.aggregate(
            [{"$sample": {"size": 1}}]))
        if data != []:
            # Pass the database object into the Wyspa class
            data = cls(**data[0])
        return data

    @classmethod
    def get_all_wyspas(cls):
        """Retreives all Wyspas from the Database.

        Queries the database for all Wyspas, sorted by
        listen_count in descending order, and returns
        a list of constructed Wyspa objects.

        Parameters
        ----------
        None

        Returns
        -------
        return_data : list
            A list of all available constructed Wyspa objects.
        """
        data = list(mongo.db.messages.aggregate(
            [{"$sort": {"listen_count": -1}}]))

        # Initialise return_data list
        return_data = []
        # Checks to see if any documents have been retrieved
        if data != []:
            # Returns a list of constructed Wyspas from documents
            for wyspa in data:
                return_data.append(cls(**wyspa))
        return return_data

    @staticmethod
    def delete_wyspa(_id):
        """Deletes a Wyspa from the Database.

        Removes a Wyspa from the Database given its
        unique ID, once the ID has been verified as
        a valid ObjectID.

        Parameters
        ----------
        _id : str
            The ID of Wyspa to be deleted.

        Returns
        -------
        None
        """

        if ObjectId.is_valid(_id):
            mongo.db.messages.remove({"_id": ObjectId(_id)})

    @staticmethod
    def location_to_latlong(user_location):
        """Converts a literal location to scrambled geocoordinates.

        Uses GeoPy to convert a string location to
        latitude and longitude, then scrambles them
        by a random floating-point value of between
        0.1 and -0.1.

        Parameters
        ----------
        user_location : str
            A literal string location to be converted to lat/long

        Returns
        -------
        latlong : dict or bool
            A dictionary containing scrambled "lat" and "lng" values,
            False bool if unsuccessful conversion.
        """

        # Instantiate Geopy Geolocator
        geolocator = Nominatim(user_agent="WYSPA")
        # Convert Location to Lat/Long Co-ordinates
        location = geolocator.geocode(user_location)
        if location is None:
            latlong = False
        else:
            lat = location.latitude + (round(uniform(0.1, -0.1), 10))
            long = location.longitude + (round(uniform(0.1, -0.1), 10))
            # Scramble Lat/Long by +-0.1 (float), and save as dict
            latlong = {"lat": lat, "lng": long}
        return latlong

    @staticmethod
    def string_to_datetime(expiry_date, expiry_time):
        """Converts datetime string to time zone aware datetime object.

        Converts date and time strings to datetime object,
        applies users timezone to the datetime, verifies
        the datetime is in the future, and returns the
        datetime object.

        Parameters
        ----------
        expiry_date : str
            Date in required format: "%d-%m-%Y".
        expiry_time : str
            Time in required format: "%H:%M".

        Returns
        -------
        formatted_expiry: datetime or bool
            A timezone aware datetime object (if successful).
            False bool (if unsuccessful).
        """

        # Convert date and time strings to Datetime object.
        date_string = expiry_date + " " + expiry_time
        date_format = "%d-%m-%Y %H:%M"
        formatted_expiry = datetime.strptime(date_string, date_format)

        # Set users time zone
        user_timezone = tz.gettz(session["timezone"])
        formatted_expiry = formatted_expiry.replace(tzinfo=user_timezone)

        # Set up time zone aware date time object for comparison
        server_timezone = tz.tzlocal()
        server_time = datetime.now().replace(tzinfo=server_timezone)

        # Ensure expiry date is in the future
        if formatted_expiry < server_time:
            formatted_expiry = False
        return formatted_expiry

    @staticmethod
    def datetime_to_string(formatted_expiry):
        """Converts datetime object to user time zone formatted string.

        Applies the user's timezone to the datetime object
        obtained from the Database, and converts it to a list
        containing the string formatted Date and Time.

        Parameters
        ----------
        formatted_expiry : datetime
            Expiry datetime object stored in database.

        Returns
        -------
        list
            formatted_date : str
            dormatted_time : str
        """

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
        """Isolates and prepares the required data for Map routing.

        Takes a list of Wyspa objects, isolates and formats the required
        data for the map routing, and returns the prepared data.

        Parameters
        ----------
        wyspas : list
            A list of constructed Wyspa objects.

        Returns
        -------
        prepared_data : list
            A list of dictionaries containing condensed Wyspa parameters.
        """

        # Initialise prepared data list
        prepared_data = []
        # Checks the list contains Wyspas
        if wyspas is not None:
            prepared_data = []
            # Isolates the data the map routing requires
            for wyspa in wyspas:
                prepared_data.append(
                    {"_id": str(wyspa.wyspa_id), "location": wyspa.location,
                     "mood": wyspa.mood, "listens": (wyspa.listen_count)})
        return prepared_data

    @staticmethod
    def whitespace_check(message):
        """Checks given string for non-whitespace characters.

        Parameters
        ----------
        message : str
            String to check for non-whitespace characters

        Returns
        -------
        whitspace_check : re.match Object
        """

        # Set regex pattern for not empty and not whitespace
        # https://stackoverflow.com/questions/7967075/regex-for-not-empty-and-not-whitespace
        whitespace_pattern = re.compile(r"(.|\s)*\S(.|\s)*")
        whitespace_check = re.match(whitespace_pattern, message)
        # Check the message and return the re.match object
        return whitespace_check
