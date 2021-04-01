from bson.objectid import ObjectId

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
        print(self.get_info())
        mongo.db.messages.insert_one(self.get_info())

    def edit_wyspa(self, message, mood, location, expiry):
        print(self.get_info())
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
    def wyspa_to_map(wyspas):
        print(wyspas)
        if wyspas is not None:
            prepared_data = []
            for wyspa in wyspas:
                prepared_data.append(
                    {"_id": str(wyspa._id), "location": wyspa.location,
                     "mood": wyspa.mood, "listens": (wyspa.listenCount)})
            return prepared_data
