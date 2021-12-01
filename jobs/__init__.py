from flask.cli import AppGroup

from jobs.search_music_by_name import search_music
from jobs.download_music import download_music
from jobs.play_music import play_music

job = AppGroup("job")

job.add_command(search_music)
job.add_command(download_music)
job.add_command(play_music)
