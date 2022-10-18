import flask
from flask import Flask

from automon.log import Logging
from automon.integrations.flaskWrapper.config import FlaskConfig


class FlaskBoilerplate(object):

    def __init__(self, import_name: str = __name__, config: FlaskConfig = None,
                 enable_javascript_compatibility: bool = False, **kwargs):
        """Wrapper for flask"""
        self._log = Logging(FlaskBoilerplate.__name__, Logging.DEBUG)

        self.Flask = Flask(import_name=import_name, **kwargs)
        self.config = config or FlaskConfig()

        if enable_javascript_compatibility:
            self.Flask = FlaskConfig.javascript_compatibility(self.Flask)

    @property
    def request(self):
        """Get flask request"""
        return flask.request

    def run(self, port: int = None, debug: bool = False, **kwargs):
        """Run flask app"""
        return self.Flask.run(port=port, debug=debug, **kwargs)
