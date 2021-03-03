"""
WYSPA - A Full Stack Anonymous Social Media Network
===================================================

WYSPA is a Full Stack Project utilising Python, NoSQL,
JavaScript, HTML, and CSS. It aims to give voices
to those who want to speak their mind, anonymously.

See https://github.com/BAK2K3/WYSPA/blob/master/README.md
for complete documentation.

"""

import os
from flask import Flask
from wyspa.core.views import core
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.register_blueprint(core)
