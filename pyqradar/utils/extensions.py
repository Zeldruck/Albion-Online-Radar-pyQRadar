from flask_cors import CORS
from flask_talisman import Talisman

from pyqradar.utils.flask import flask
from pyqradar.utils.photon import Photon
from pyqradar.utils.routes import Routes


class Extensions:
    @classmethod
    def init(self):
        # Defining a Content Security Policy (CSP) for Talisman
        csp = {
            "style-src": [
                "'unsafe-inline'",
                "'self'",
            ]
        }

        # Creating an instance of the Talisman middleware with specified settings
        talisman = Talisman(flask, force_https=False, content_security_policy=csp)

        # Creating an instance of the Routes class to handle API routes
        routes = Routes(flask)

        # Enabling Cross-Origin Resource Sharing (CORS) for the Flask app
        cors = CORS(flask)

        photon = Photon()
