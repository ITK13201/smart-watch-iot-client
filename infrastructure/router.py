import json
import logging
import pprint

from flask import Flask, Response
from werkzeug.exceptions import NotFound, Forbidden, InternalServerError

from jobs import job
from config.config import (
    TEMPLATES_DIR,
    STATIC_DIR,
    FLASK_ENVIRONMENT_FILE_PATH,
    STATIC_URL_PATH,
)

Engine = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR,
    static_url_path=STATIC_URL_PATH,
)

# ================
# Routing
# ================
@Engine.route("/", methods=["GET"])
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


Engine.cli.add_command(job)

# =============================
# Manage Config
# =============================
ok = Engine.config.from_pyfile(filename=FLASK_ENVIRONMENT_FILE_PATH, silent=True)
if not ok:
    raise Exception("Error: failed to load flask configurations.")
# logger = logging.getLogger(__name__)
# logger.info(pprint.pformat(Engine.config))
