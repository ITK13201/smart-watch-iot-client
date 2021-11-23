from flask import Flask, Response, json
from werkzeug.exceptions import NotFound, Forbidden, InternalServerError, abort

from config.config import TEMPLATES_DIR, STATIC_DIR


Engine = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)


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
