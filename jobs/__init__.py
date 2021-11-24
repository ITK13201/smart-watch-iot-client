from flask.cli import AppGroup
from jobs.fetch_ytmusic import fetch_ytmusic

jobs = AppGroup("jobs")

jobs.add_command(fetch_ytmusic)
