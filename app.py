"""
Wyspa App.py
============

This module calls the instantiated Flask application
from the main __init__ file, and tells the server to
run it.
"""

# pylint: disable=unused-import
# env.py import is being incorrectly picked up as unused

import os

from wyspa import app
if os.path.exists("env.py"):
    import env

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
