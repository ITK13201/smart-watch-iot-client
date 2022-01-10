import logging
import urllib.parse

import click
from flask.cli import with_appcontext

from usecases.google_home import GoogleHomeManager


logger = logging.getLogger(__name__)


@click.command("stop_music", help="stop music")
@with_appcontext
def stop_music():
    logger.info("started")

    manager = GoogleHomeManager()
    ok = manager.stop_music()
    if not ok:
        logger.error("Failed to stop youtube music with google home")

    logger.info("finished")
