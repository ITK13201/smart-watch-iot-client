import json
import logging
import threading

from .system import (
    activate,
    run_system_type_in,
    run_system_type_out,
    is_active,
    RUN_TYPE,
)
from usecases.discord.bot import send_starting_message

from flask import Response

logger = logging.getLogger(__name__)


def start_system_view(payload) -> Response:
    type: str = payload["type"]
    if type not in RUN_TYPE:
        context = {"message": "invalid type"}
        status = 400
        return Response(response=json.dumps(context), status=status)

    if is_active():
        context = {"message": "Already running system"}
        status = 400
    else:
        context = {"message": "Started system"}
        send_starting_message(type)
        if type == "in":
            thread = threading.Thread(target=run_system_type_in)
        elif type == "out":
            thread = threading.Thread(target=run_system_type_out)
        thread.start()
        activate(thread)
        status = 200
    return Response(response=json.dumps(context), status=status)
