import os
from config.config import DEBUG

TESTING = DEBUG
SECRET_KEY = os.environ["SECRET_KEY"]
# これ入れるとルーティングにバグが出る
# SERVER_NAME = os.environ.get("SERVER_NAME")
