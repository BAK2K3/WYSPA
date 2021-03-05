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
from wyspa.factory.initialisation import create_app


app = create_app()
app.register_blueprint(core)
app.register_blueprint(maps)
