import logging
import urllib.parse

import click
from flask.cli import with_appcontext

from usecases.google_home import GoogleHomeManager


logger = logging.getLogger(__name__)


@click.command("play_music", help="play music")
@with_appcontext
def play_music():
    logger.info("started")

    manager = GoogleHomeManager()
    mp3_url = urllib.parse.quote(
        "data/musics/Dinner Time Jazz _ Smooth Instrumental Jazz Music for Dinner _ Background Jazz Playlist 2018 Hi-Fi@LrgCwdT2kx8.mp3",
        safe=":/",
    )
    ok = manager.play_music(mp3_url)
    if not ok:
        logger.error("Failed to play youtube music with google home")

    logger.info("finished")
