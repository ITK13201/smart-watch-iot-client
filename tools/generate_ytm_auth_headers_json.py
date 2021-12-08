import os
from ytmusicapi import YTMusic

BASE_DIR = ".."


def load_text(path: str) -> str:
    with open(path, "r") as f:
        text = f.read()
    return text


headers_row = load_text(os.path.join(BASE_DIR, "tmp", "ytm_auth_headers_row.txt"))

YTMusic.setup(
    filepath=os.path.join(BASE_DIR, "ytm_auth_headers.json"), headers_raw=headers_row
)
