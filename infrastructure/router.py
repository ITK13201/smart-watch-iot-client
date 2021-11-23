import os

from flask import Flask, Response, json, render_template

from config.config import TEMPLATES_DIR, STATIC_DIR

Engine = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)


@Engine.route("/api/v1/test/")
def api_test() -> Response:
    return Response(response=json.dumps({"message": "test"}), status=404)


@Engine.errorhandler(404)
def not_found(e) -> Response:
    print(type(e))
    return Response(response=render_template("404.html"), status=404)
