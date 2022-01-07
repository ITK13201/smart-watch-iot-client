import click
import logging
from flask.cli import with_appcontext

from usecases import youtube_music

logger = logging.getLogger(__name__)


@click.command("download_musics", help="download youtube musics")
@with_appcontext
def download_musics():
    logger.info("started")

    ok = youtube_music.download_musics("https://music.youtube.com/playlist?list=PLqqUdbNCi_pLoPDAMMpwX5E8QYlg6xEko")
    if not ok:
        logger.error("Failed to download music")

    logger.info("finished")
