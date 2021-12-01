import pprint
from typing import Optional

from werkzeug.security import hmac

from models.user import User
from config.config import DEFAULT_USER_USERNAME, DEFAULT_USER_PASSWORD

users = [
    User(1, DEFAULT_USER_USERNAME, DEFAULT_USER_PASSWORD)
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username: str, password: str) -> User:
    user = username_table.get(username, None)
    if user and hmac.compare_digest(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload: dict) -> Optional[str]:
    user_id = payload['identity']
    user: User = userid_table.get(user_id, None)
    if user is None:
        return None
    else:
        return "User(id={}, username={}, password={})".format(user.id, user.username, user.password)
