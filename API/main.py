""" PyDontgo server
    Environment variables for development:
        FLASK_APP={path of the main.py}
        FLASK_ENV=development
    start : flask run
"""

from flask import Flask
from API.vue import api


# Start API
app = Flask(__name__)
api.init_app(app)


if __name__ == '__main__':
    app.run()
