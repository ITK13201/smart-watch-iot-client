import json
import logging
import pprint

from flask import Flask, Response, request
from werkzeug.exceptions import NotFound, Forbidden, InternalServerError
from flask_jwt import JWT, jwt_required, current_identity

from jobs import job
from config.config import (
    TEMPLATES_DIR,
    STATIC_DIR,
    FLASK_ENVIRONMENT_FILE_PATH,
    STATIC_URL_PATH,
)
import views
from views.jwt import authenticate, identity

Engine = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR,
    static_url_path=STATIC_URL_PATH,
)

# =============================
# Manage Config
# =============================
ok = Engine.config.from_pyfile(filename=FLASK_ENVIRONMENT_FILE_PATH, silent=True)
if not ok:
    raise Exception("Error: failed to load flask configurations.")
# logger = logging.getLogger(__name__)
# logger.info(pprint.pformat(Engine.config))

# ================
# Routing
# ================
jwt = JWT(app=Engine, authentication_handler=authenticate, identity_handler=identity)


@Engine.route("/")
def index() -> Response:
    return Response(response="ok", status=200)


@Engine.route("/api/v1/test")
@jwt_required()
def api_v1_test() -> Response:
    return Response(response=json.dumps({"message": "test"}), status=200)


@Engine.route("/api/v1/play_music", methods=["POST"])
@jwt_required()
def api_v1_play_music() -> Response:
    return views.api.v1.play_music_view()


@Engine.route("/api/v1/start_system", methods=["POST"])
@jwt_required()
def api_v1_start_system() -> Response:
    payload = request.json
    return views.api.v1.start_system_view(payload)


@Engine.route("/api/v1/stop_system", methods=["POST"])
@jwt_required()
def api_v1_stop_system() -> Response:
    return views.api.v1.stop_system_view()


@Engine.route("/protected")
@jwt_required()
def protected() -> Response:
    return Response(response="%s" % current_identity, status=200)


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
