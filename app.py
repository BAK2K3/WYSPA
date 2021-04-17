"""
WYSPA - A Full Stack Anonymous Social Media Network
===================================================

WYSPA is a Full Stack Project utilising Python, NoSQL,
JavaScript, HTML, and CSS. It aims to give voices
to those who want to speak their mind, anonymously.

See https://github.com/BAK2K3/WYSPA/blob/master/README.md
for complete documentation.

Created by Benjamin Kavanagh (BAK2K3) 2021.
"""

import os

from wyspa import app
if os.path.exists("env.py"):
    import env

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
