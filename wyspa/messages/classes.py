from bson.objectid import ObjectId
from wyspa.factory.initialisation import mongo


# Create a class for WYSPAs
class Wyspa():
    def __init__(self, author, message, mood, location, comments=[], _id=None):
        self._id = _id
        self.author = author
        self.message = message
        self.mood = mood
        self.location = location
        self.comments = comments if comments else []

    def get_info(self):
        # Return Dictionary for DB
        info = {'author': self.author, 'message': self.message,
                'mood': self.mood, 'location': self.location,
                'comments': self.comments}
        return info

    def remove_comment(self, index):
        self.comments.pop(index)
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_comment(self, new_comment):
        self.comments.append({self.author: new_comment})
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def delete_wyspa(self):
        mongo.db.messages.remove({"_id": ObjectId(self._id)})

    def write_wyspa(self):
        mongo.db.messages.insert_one(self.get_info())

    @classmethod
    def get_by_id(cls, _id):
        data = mongo.db.messages.find_one({"_id": ObjectId(_id)})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_user(cls, username):
        data = list(mongo.db.messages.find({"author": username}))
        if data is not None:
            return_data = []
            for message in data:
                return_data.append(cls(**message))
            return return_data

    @classmethod
    def get_random_wyspa(cls):
        data = list(mongo.db.messages.aggregate(
            [{"$sample": {"size": 1}}]))[0]
        if data is not None:
            return cls(**data)
