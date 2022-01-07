import logging
import click
from flask.cli import with_appcontext

from usecases.google_home import GoogleHomeManager


logger = logging.getLogger(__name__)


@click.command("play_music", help="play music")
@with_appcontext
def play_music():
    logger.info("started")

    manager = GoogleHomeManager()
    ok = manager.play_music(
        "data/musics/Relaxing Jazz Music - Background Chill Out  Music - Music For Relax,Study,Work-neV3EPgvZ3g.mp3"
    )
    if not ok:
        logger.error("Failed to play youtube music with google home")

    logger.info("finished")
