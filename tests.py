"""
Test Wyspa
=============

Contains the Unit Testing for the following
scenarios:

- A sample of basic Get Routes
- Registering, Creating a Wyspa, Deleting Account
- A sample of Wyspa methods

Classes:
    BasicGetRouteTest
    RegisterDeleteTest
    WyspaMethodTest
"""
import unittest

from flask import session
from flask_testing import TestCase

from wyspa.core.views import core
from wyspa.maps.views import maps
from wyspa.messages.views import messages
from wyspa.error_pages.handlers import error_pages
from wyspa.factory.initialisation import create_app
from wyspa.users.views import login_manager, users
from wyspa.messages.classes import Wyspa
from wyspa.users.classes import User


class BasicGetRouteTests(TestCase):
    '''Unit Testing for basic get routes in Flask.

    This unit test checks the following GET routes:
        Home
        View_Message
        Map_overview
        My_Voice
    '''

    def create_app(self):
        '''Required method for flask_testing.'''

        # Initialise Flask Application via Factory
        app = create_app()
        app.testing = True

        # Register Blueprints to Flask
        app.register_blueprint(core)
        app.register_blueprint(maps)
        app.register_blueprint(messages)
        app.register_blueprint(users)
        app.register_blueprint(error_pages)

        # Set up log in manager
        login_manager.init_app(app)
        login_manager.session_protection = "strong"
        login_manager.login_view = "core.index"

        # Return App
        return app

    def test_home(self):
        '''Tests the response and template for home Get route.

        Route:
            "/"
        Method:
            GET
        Expected Status:
            200
        Expected Template:
            index.html
        Expected Content:
            "Penny for your thoughts"
        '''

        response = self.client.get("/")
        data = response.data.decode('utf-8')

        # Check Page Content
        assert "Penny for your thoughts" in data
        # Check 200 status
        self.assert_200(response)
        # Check Template
        self.assert_template_used('index.html')

    def test_view_message(self):
        '''Tests the response and template for view_message get route.

        Route:
            "/view_message"
        Method:
            GET
        Expected Status:
            200
        Expected Template:
            messages.html
        '''

        response = self.client.get("/view_message")
        self.assert_200(response)
        self.assert_template_used('messages.html')

    def test_map(self):
        '''Tests the response and template for map_overview get route.

        Route:
            "/map_overview"
        Method:
            GET
        Expected Status:
            200
        Expected Template:
            maps.html
        '''

        response = self.client.get("/map_overview")
        # Check 200 status
        self.assert_200(response)
        # Check Template
        self.assert_template_used('maps.html')

    def test_my_voice(self):
        '''Tests the response and template for my_voice get route.

        Route:
            "/my_voice"
        Method:
            GET
        Expected Status:
            302
        Expected Redirect:
            /?next=%2Fmy_voice
        '''

        response = self.client.get("/my_voice")
        # Check 302 status
        self.assertStatus(response, 302)
        # Check the response for a redirect value
        self.assertRedirects(response, "https://localhost/?next=%2Fmy_voice")


class RegisterDeleteTest(TestCase):
    '''Unit Testing for CRUD, via appropriate flask routes.

    This unit test registers an account,
    creates a wyspa, updates the Wyspa,
    then deletes the account and all Wyspas tied to the account.
    '''

    def create_app(self):
        '''Required method for flask_testing.'''

        # Initialise Flask Application via Factory
        app = create_app()

        app.testing = True

        # Register Blueprints to Flask
        app.register_blueprint(core)
        app.register_blueprint(maps)
        app.register_blueprint(messages)
        app.register_blueprint(users)
        app.register_blueprint(error_pages)

        # Set up log in manager
        login_manager.init_app(app)
        login_manager.session_protection = "strong"
        login_manager.login_view = "core.index"

        # Return App
        return app

    def test_a_register(self):
        '''Sends a POST request for registration.

        Route:
            "/register"
        Method:
            POST
        Expected Outcome:
            New user is written to database
        Expected Outcome:
            New user is retrieved from database
        '''

        # Set up dictionary for registration form
        reg_form = {"usernameRegister": "unittest",
                    "passwordRegister": "Password123!",
                    "passwordConfirm": "Password123!",
                    "timezoneRegister": "Europe/London"}

        # Post data to route
        self.client.post("/register", data=reg_form)
        # Query the database for new user
        new_user = User.obtain_user("unittest")
        # Checks the existance of the registered user in the DB
        self.assertTrue(new_user['username'] == "unittest")

    def test_b_create(self):
        '''Sends a POST request for Wyspa Creation.

        This test logs the user in before performing the test.

        Route:
            "/create_wyspa"
        Method:
            POST
        Expected Outcome:
            Wyspa is written to the Database
        Expected Outcome:
            Wyspa is retrieved from database
        '''

        # Set up dictionary for login form
        login_form = {"usernameLogin": "unittest",
                      "passwordLogin": "Password123!",
                      "timezoneLogin": "Europe/London"}
        # Log user in
        self.client.post("/login", data=login_form)

        # Set up dictionary for Wyspa form
        wyspa_form = {"wyspaContent": "Unit Test Wyspa",
                      "location": "London",
                      "mood": 1,
                      "expiryDate": "01-01-2022",
                      "expiryTime": "15:00"}
        # Submit Wyspa
        self.client.post("/create_wyspa", data=wyspa_form)

        # Set Timezone in session (required for below method)
        session["timezone"] = "Europe/London"
        # Query DB for all Wyspas belonging to user
        wyspas = Wyspa.get_by_user("unittest")
        # Assert that the array returned is not empty
        self.assertTrue(wyspas != [])

    def test_c_edit(self):
        '''Sends a POST request for Wyspa Editting.

        This test logs the user in before performing the test.

        Route:
            "/edit_wyspa/<wyspa_id>"
        Method:
            POST
        Expected Outcome:
            Wyspa is updated in the Database
        Expected Outcome:
            Updated Wyspa is retrieved from database
        Expected Outcome:
            Original and edited Wyspas are different
        Expected Outcome:
            Original and edited Wyspas have the same ID
        '''

        # Set up dictionary for login form
        login_form = {"usernameLogin": "unittest",
                      "passwordLogin": "Password123!",
                      "timezoneLogin": "Europe/London"}
        # Log User In
        self.client.post("/login", data=login_form)

        # Set session timezone (required for below method)
        session["timezone"] = "Europe/London"
        # Obtain the Wyspa previously created
        wyspa_to_edit = Wyspa.get_by_user("unittest")[0]

        # Set up dictionary for Wyspa updating
        wyspa_form = {"wyspaContent": "Updated Test Wyspa",
                      "location": "London",
                      "mood": 0,
                      "expiryDate": "01-01-2022",
                      "expiryTime": "11:00"}
        # Submit edit
        self.client.post("/edit_wyspa/" + str(wyspa_to_edit.wyspa_id),
                         data=wyspa_form)

        # Query DB for updated Wyspa
        updated_wyspa = Wyspa.get_by_user("unittest")[0]

        # Compare Wyspas as a whole
        self.assertTrue(updated_wyspa != wyspa_to_edit)
        # Compare ID of Wyspas
        self.assertTrue(updated_wyspa.wyspa_id == wyspa_to_edit.wyspa_id)

    def test_d_delete(self):
        '''Sends a POST request for deleting Account and Wyspas.

        This test logs the user in before performing the test.

        Route:
            "/delete_user"
        Method:
            POST
        Expected Outcome:
            Logged in user's account is deleted
        Expected Outcome:
            Logged in user's Wyspas are deleted
        '''

        # Set up dictionary for login form
        login_form = {"usernameLogin": "unittest",
                      "passwordLogin": "Password123!",
                      "timezoneLogin": "Europe/London"}
        # Log User In
        self.client.post("/login", data=login_form)

        # Submit Delete Account request
        self.client.post("/delete_user")

        # Query the DB for the testing username
        deleted_user = User.obtain_user("unittest")

        # Set session timezone (required for below method)
        session["timezone"] = "Europe/London"
        # Query the DB for Wyspas by testing username
        deleted_messages = Wyspa.get_by_user("unittest")
        # Check if this user has been deleted
        self.assertTrue(deleted_user is None)
        # Check if this user has no Wyspas
        self.assertTrue(deleted_messages == [])


class WyspaMethodTest(unittest.TestCase):
    '''Unit Testing for Wyspa Methods.

    This unit test tests the following Wyspa methods:
        get_random_wyspa
        location_to_latlong
    '''

    def test_random_wyspa(self):
        '''Tests the random Wyspa generation.

        Method:
            Wyspa.get_random_wyspa()
        Expected Outcome:
            A Wyspa is obtained from the database.
        '''

        random_wyspa = Wyspa.get_random_wyspa()
        self.assertTrue(random_wyspa is not None)

    def test_location_to_latlong(self):
        '''Tests the location to latlong conversion.

        This method sets the true lat long co-ordinates
        for London, then calls the conversion method to compare the
        results to ensure they're not identical (i.e,
        the scrambling has worked).

        Method:
            Wyspa.location_to_latlong()
        Expected Outcome:
            True London lat/long does not match scrambled lat/long
        '''

        # Set Lat/Long for London
        london = {"lat": 51.500153, "lng": -0.1262362}
        # Obtain scrambled Lat/Long
        scrambled_london = Wyspa.location_to_latlong("london")
        # Compare True vs Scrambled
        self.assertTrue(london != scrambled_london)


if __name__ == '__main__':
    unittest.main()
