from flask.cli import AppGroup

from jobs.search_music_by_name import search_music
from jobs.download_musics import download_musics
from jobs.play_music import play_music
from jobs.register_music_informations import register_music_informations

job = AppGroup("job")

job.add_command(search_music)
job.add_command(download_musics)
job.add_command(play_music)
job.add_command(register_music_informations)
