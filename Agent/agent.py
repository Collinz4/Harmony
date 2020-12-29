"""
Agent for reporting system resource consumption.
"""

import time
import datetime
import os
import logging
import sys
import json

import psutil
import requests
from requests.exceptions import RequestException


def setup():
    """
    Initial check for environment variables.
    """
    if not os.environ.get("API_KEY"):
        logging.error("'API_KEY' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("COMPUTER_NAME"):
        logging.error("'COMPUTER_NAME' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("COLLECTOR_DOMAIN"):
        logging.error("'COLLECTOR_DOMAIN' Not Set! Aborting...")
        sys.exit(1)
    if not os.environ.get("REPORTING_RATE"):
        logging.error("'REPORTING_RATE' Not Set! Aborting...")
        sys.exit(1)
    logging.info("Initialization Checks Passed!")


def run():
    """
    Handles metric collections and submission to collector API.
    """

    logging.info("Starting Agent Metric Service")
    request_errors = 0
    compute_data = {}
    compute_data["computer_name"] = os.environ.get("COMPUTER_NAME")

    headers = {"Authorization": f"Bearer {os.environ.get('API_KEY')}"}

    while True:
        compute_data["cpu_percentage"] = psutil.cpu_percent(interval=1)
        compute_data["memory_percentage"] = psutil.virtual_memory().percent
        compute_data["timestamp"] = str(datetime.datetime.now())

        try:
            requests.post(
                url=f"https://{os.environ.get('COLLECTOR_DOMAIN')}/collector/stats",
                headers=headers,
                json=json.dumps(compute_data),
                timeout=5
            )
            request_errors = 0
        except RequestException:
            request_errors += 1
            logging.warning(
                "Error submitting metrics to collector for the {request_errors} time(s) in a row."
            )
        time.sleep(int(os.environ.get("REPORTING_RATE")))


if __name__ == "__main__":
    setup()
    run()
