"""
Main module for running collector.
"""

import os
import logging
import sys

from flask import Flask

from collector import api


def pre_check():
    """
    Initial check for environment variables.
    """

    if not os.environ.get("API_KEY"):
        logging.error("'API_KEY' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("X_CONTENT_TYPE_OPTIONS"):
        logging.error("'X_CONTENT_TYPE_OPTIONS' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("ACCESS_CONTROL_ALLOW_ORIGIN"):
        logging.error("'ACCESS_CONTROL_ALLOW_ORIGIN' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("ACCESS_CONTROL_ALLOW_HEADERS"):
        logging.error("'ACCESS_CONTROL_ALLOW_HEADERS' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("COLLECTOR_BUFFER_SIZE"):
        logging.error("'COLLECTOR_BUFFER_SIZE' Not Set! Aborting...")
        sys.exit(1)
    logging.info("Initialization Checks Passed!")


def create_app() -> Flask:
    """
    Flask factory. Stay with 1 with the current implementation.
    """

    _application = Flask(__name__)
    _application.register_blueprint(api)
    return _application


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    pre_check()
    application = create_app()
    application.debug = True
    application.run(
        host="0.0.0.0",
        port=5000
    )
