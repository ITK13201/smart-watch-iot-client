from flask.cli import AppGroup

from jobs.fetch_ytmusic import fetch_ytmusic
from jobs.download_ytmusic import download_ytmusic
from jobs.play_music import play_music

job = AppGroup("job")

job.add_command(fetch_ytmusic)
job.add_command(download_ytmusic)
job.add_command(play_music)
