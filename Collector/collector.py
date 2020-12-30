"""
API endpoints for the collector application.
"""

from threading import Lock
from dataclasses import asdict

from flask import Blueprint, json, request, jsonify
from flask.wrappers import Response

from models import DataPoint, Timeline
import auth


api = Blueprint('collector', __name__, url_prefix='/')
instances = {} # name : Timeline
lock = Lock()


@api.after_request
def add_cors_header(resp):
    """
    Allows origin support for requests from all domains.
    """
    resp.headers['X-Content-Type-Options'] = '*'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp


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
        if not instances.get(new_point.computer_name):
            instances[new_point.computer_name] = Timeline(maxsize=100)
        instances[new_point.computer_name].append(new_point)

    return Response(status=200)


@api.route("/timeline/<instance_name>", methods=["GET", "OPTIONS"])
def specific_timeline(instance_name: str):
    """
    Returns the time series data from a specific computer.
    """

    if request.method == "GET":
        with lock:
            if not instances.get(instance_name):
                return jsonify(message="Instance Does Not Exist"), 404
            return jsonify(asdict(instances.get(instance_name)))
    return Response(status=200)


@api.route("/timeline/<instance_name>/latest", methods=["GET", "OPTIONS"])
def lastest_datapoint(instance_name: str):
    """
    Returns the latest time series data for a specific instance.
    """
    if request.method == "GET":
        with lock:
            if not instances.get(instance_name):
                return jsonify(message="Instance Does Not Exist"), 404
            return jsonify(asdict(instances.get(instance_name).latest()))
    return Response(status=200)


@api.route("/instances", methods=["GET", "OPTIONS"])
def list_instance_name():
    """
    Returns the list of computers being recorded.
    """

    if request.method == "GET":
        with lock:
            names = list(instances.keys())
        return jsonify(names)
    return Response(status=200)
