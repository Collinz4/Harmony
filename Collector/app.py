import os
import logging
import sys

from flask import Flask

from collector import api
import conf


def pre_check():
    """
    Initial check for environment variables.
    """

    logging.info("Pre Check Start...")
    if not os.environ.get("SERVER_ADDRESS"):
        logging.error("'SERVER_ADDRESS' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("SERVER_PORT"):
        logging.error("'SERVER_PORT' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("SERVER_DEBUG_MODE"):
        logging.error("'SERVER_DEBUG_MODE' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("API_KEY"):
        logging.error("'API_KEY' Not Set! Aborting...")
        sys.exit(1)
    logging.info("Initialization Checks Passed!")


def create_app() -> Flask:
    """
    Flask factory. Keep to 1 with the current implementation.
    """

    app = Flask(__name__)
    app.register_blueprint(api)
    return app


if __name__ == "__main__":
    pre_check()
    app = create_app()
    app.debug = conf.SERVER_DEBUG_MODE
    app.run(host=conf.SERVER_ADDRESS, port=conf.SERVER_PORT)
