from flask.cli import AppGroup
from jobs.fetch_ytmusic import fetch_ytmusic

job = AppGroup("job")

job.add_command(fetch_ytmusic)
