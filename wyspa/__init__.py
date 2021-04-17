"""
WYSPA - A Full Stack Anonymous Social Media Network
===================================================

WYSPA is a Full Stack Project utilising Python, NoSQL,
JavaScript, HTML, and CSS. It aims to give voices
to those who want to speak their mind, anonymously.

See https://github.com/BAK2K3/WYSPA/blob/master/README.md
for complete documentation.
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
