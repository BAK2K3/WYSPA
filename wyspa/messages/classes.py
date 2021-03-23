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

    def write_wyspa(self):
        mongo.db.messages.insert_one(self.get_info())

    def remove_comment(self, index):
        self.comments.pop(index)
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    def add_comment(self, new_comment, comment_author="anonymous"):
        self.comments.append({comment_author: new_comment})
        mongo.db.messages.update({"_id": ObjectId(self._id)}, self.get_info())

    @staticmethod
    def delete_wyspa(_id):
        mongo.db.messages.remove({"_id": ObjectId(_id)})

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

    @classmethod
    def get_all_wyspas(cls):
        data = list(mongo.db.messages.find())
        if data is not None:
            return_data = []
            for message in data:
                return_data.append(cls(**message))
            return return_data

    @staticmethod
    def wyspa_to_map(wyspas):
        prepared_data = []
        for wyspa in wyspas:
            prepared_data.append(
                {"_id": str(wyspa._id), "location": wyspa.location,
                 "mood": wyspa.mood})
        return prepared_data
