import click
import logging
from flask.cli import with_appcontext

from usecases import youtube_music

logger = logging.getLogger(__name__)


@click.command("download_music", help="download youtube music")
@with_appcontext
def download_music():
    logger.info("started")

    ok = youtube_music.download_music("https://music.youtube.com/watch?v=kcAYxSHzle0")
    if not ok:
        logger.error("Failed to download music")

    logger.info("finished")
