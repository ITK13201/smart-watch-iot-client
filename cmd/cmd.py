from flask import Flask

from config.config import DEBUG, SECRET_KEY, PORT, SERVER_NAME
from infrastructure.router import Engine


def init_envs(engine: Flask) -> Flask:
    if DEBUG:
        engine.config.update(
            {
                "ENV": "development",
                "TESTING": True,
            }
        )
    engine.config.update({"SECRET_KEY": SECRET_KEY, "SERVER_NAME": SERVER_NAME})
    return engine


def Run():
    engine = init_envs(Engine)
    engine.run(port=PORT, debug=DEBUG)
