import os
from config.config import DEBUG

TESTING = DEBUG
SECRET_KEY = os.environ["SECRET_KEY"]
SERVER_NAME = os.environ.get("SERVER_NAME")
