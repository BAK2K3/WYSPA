"""
Wyspa Module
============

This module creates an instance of the Flask application
via the Factory, registers all blueprints, then sets up
the Login Manager.
"""


from wyspa.core.views import core
from wyspa.maps.views import maps
from wyspa.messages.views import messages
from wyspa.error_pages.handlers import error_pages
from wyspa.factory.initialisation import create_app
from wyspa.users.views import login_manager, users

# Initialise Flask Application via Factory
app = create_app()

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
