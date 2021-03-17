# https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
# Create the required User class for Flask-Login
class User():
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username
