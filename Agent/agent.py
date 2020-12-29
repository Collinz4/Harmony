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


def pre_check():
    """
    Initial check for environment variables.
    """

    logging.info("Pre Check Start...")
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
    compute_data = {}
    compute_data["computer_name"] = os.environ.get("COMPUTER_NAME")

    headers = {"Authorization": f"Bearer {os.environ.get('API_KEY')}"}

    while True:
        compute_data["cpu_percentage"] = psutil.cpu_percent(interval=1)
        compute_data["memory_percentage"] = psutil.virtual_memory().percent
        compute_data["timestamp"] = str(datetime.datetime.now())

        try:
            requests.post(
                url=os.environ.get("COLLECTOR_DOMAIN"),
                headers=headers,
                json=json.dumps(compute_data),
                timeout=5
            )
        except RequestException:
            logging.error("Error submitting metrics to collector.")
        time.sleep(int(os.environ.get("REPORTING_RATE")))


if __name__ == "__main__":
    pre_check()
    run()
