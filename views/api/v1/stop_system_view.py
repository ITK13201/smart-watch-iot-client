import json
import logging
from .system import deactivate, is_active, pause_system

from flask import Response

logger = logging.getLogger(__name__)


def stop_system_view() -> Response:
    if not is_active():
        context = {"message": "SYSTEM IS NOT running."}
        status = 400
    else:
        context = {"message": "Stopped system"}
        deactivate()
        pause_system()
        status = 200
    return Response(response=json.dumps(context), status=status)
