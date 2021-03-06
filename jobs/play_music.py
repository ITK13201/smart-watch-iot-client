import logging
import urllib.parse

import click
from flask.cli import with_appcontext

from usecases.google_home import GoogleHomeManager


logger = logging.getLogger(__name__)


@click.command("play_music", help="play music")
@click.option("--path", type=click.STRING, help="Music Path.")
@with_appcontext
def play_music(path: str):
    logger.info("started")

    manager = GoogleHomeManager()
    mp3_url = urllib.parse.quote(
        path,
        safe=":/",
    )
    ok = manager.play_music(mp3_url)
    if not ok:
        logger.error("Failed to play youtube music with google home")

    logger.info("finished")
