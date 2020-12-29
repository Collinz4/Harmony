"""
API endpoints for the collector application.
"""

from threading import Lock
from dataclasses import asdict

from flask import Blueprint, json, request, jsonify
from flask.wrappers import Response

from datapoint import DataPoint, Timeline
import auth


api = Blueprint('collector', __name__, url_prefix='/')
machines = {} # name : Timeline
lock = Lock()


@api.route("/submit", methods=["POST"])
@auth.authenticate
def submit_metric():
    """
    Submits the metric data for a specific computer
    if the computer doesn't exist it is created.
    """

    gson = json.loads(request.get_json())
    
    new_point = DataPoint(
        computer_name=gson["computer_name"],
        cpu_percentage=gson["cpu_percentage"],
        memory_percentage=gson["memory_percentage"],
        timestamp=gson["timestamp"]
    )

    with lock:
        if not machines.get(new_point.computer_name):
            machines[new_point.computer_name] = Timeline(maxsize=100)
        machines[new_point.computer_name].append(new_point)
    
    return Response(status=200)


@api.route("/stats/<computer_name>", methods=["GET"])
def stats(computer_name: str):
    """
    Returns the time series data from a specific computer.
    """
    with lock:
        if not machines.get(computer_name):
            return jsonify(message="Computer Does Not Exist"), 404

        proxy_dict = {}
        for key in machines.keys():
            proxy_dict[key] = asdict(machines.get(key))

        return jsonify(stats=proxy_dict)


@api.route("/computers", methods=["GET"])
def computers():
    """
    Returns the list of computers being recorded.
    """
    with lock:
        keys = list(machines.keys())
    return jsonify(computers=keys)
