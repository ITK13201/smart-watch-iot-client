import json
import logging
import threading

from .system import activate, run_system, is_active

from flask import Response

logger = logging.getLogger(__name__)


def start_system_view() -> Response:
    if is_active():
        context = {"message": "Already running system"}
        status = 400
    else:
        context = {"message": "Started system"}
        thread = threading.Thread(target=run_system)
        thread.start()
        activate(thread)
        status = 200
    return Response(response=json.dumps(context), status=status)
