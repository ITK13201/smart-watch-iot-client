import click
import logging
from flask.cli import with_appcontext

from usecases import youtube_music

logger = logging.getLogger(__name__)


@click.command("download_musics", help="download youtube musics")
@click.option("--url", type=click.STRING, help="YouTube Music Url.")
@with_appcontext
def download_musics(url: str):
    logger.info("started")

    ok = youtube_music.download_musics(url)
    if not ok:
        logger.error("Failed to download music")

    logger.info("finished")
