import os
import pathlib
from logging import config


# ==============================
# Base Settings
# ==============================

# required
import flask.logging

DEBUG_TYPE = os.environ["FLASK_DEBUG"]
DEBUG = False
if DEBUG_TYPE == "1":
    DEBUG = True
PORT = os.environ["PORT"]
STATIC_URL_PATH = "/assets"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLASK_ENVIRONMENT_FILE_PATH = os.path.join(BASE_DIR, "config", "environment.py")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "assets")

LOG_DIR = os.path.join(BASE_DIR, "log")
LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")
if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)
    if not os.path.isfile(LOG_FILE_PATH):
        logfile = pathlib.Path(LOG_FILE_PATH)
        logfile.touch()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s] %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
        },
        "myformat": {
            "format": "[%(levelname)s] %(asctime)s %(name)s:%(lineno)s %(funcName)s %(module)s %(process)d %(thread)d:  %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "myformat",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "myformat",
            "filename": "log/app.log",
        },
    },
    "loggers": {
        "__main__": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False,
        },
        "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
    },
}
config.dictConfig(LOGGING)


# ====================================
# Individual Settings
# ====================================
YTM_AUTH_HEADERS_JSON_PATH = os.path.join(BASE_DIR, "ytm_auth_headers.json")
DEFAULT_USER_USERNAME = os.environ["DEFAULT_USER_USERNAME"]
DEFAULT_USER_PASSWORD = os.environ["DEFAULT_USER_PASSWORD"]
