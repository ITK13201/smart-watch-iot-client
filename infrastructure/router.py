import os
import json
import pprint
import logging
from flask import Flask, Response
from werkzeug.exceptions import NotFound, Forbidden, InternalServerError

from jobs import jobs
from config.config import TEMPLATES_DIR, STATIC_DIR, DEBUG, FLASK_ENVIRONMENT_FILE_PATH

logger = logging.getLogger("__name__")

Engine = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

ok = Engine.config.from_pyfile(filename=FLASK_ENVIRONMENT_FILE_PATH, silent=True)
if not ok:
    raise Exception("Error: failed to load flask configurations.")
if DEBUG:
    logger.info(pprint.pformat(Engine.config))

# ================
# Routing
# ================
@Engine.route("/")
def index() -> Response:
    return Response(response="test", status=200)

@Engine.route("/api/v1/test/")
def api_test() -> Response:
    return Response(response=json.dumps({"message": "test"}), status=200)


@Engine.errorhandler(403)
def forbidden(e: Forbidden) -> Response:
    return e.get_response()


@Engine.errorhandler(404)
def not_found(e: NotFound) -> Response:
    return e.get_response()


@Engine.errorhandler(500)
def internal_server_error(e: InternalServerError) -> Response:
    return e.get_response()

Engine.cli.add_command(jobs)

