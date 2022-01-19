import logging
import pprint

import click
from flask.cli import with_appcontext

from usecases.youtube_music import YTMusicManager

logger = logging.getLogger(__name__)


@click.command("search_music_by_name", help="search youtube music by name")
@click.option(
    "--name", type=click.STRING, help="Title of the music you want to search for."
)
@with_appcontext
def search_music_by_name(name: str):
    logger.info("started")

    manager = YTMusicManager()
    results = manager.fetch_musics_by_name(name)
    musics = []
    for result in results:
        if result["category"] == "Songs":
            musics.append(result)
    logger.info(pprint.pformat(musics))

    logger.info("finished")
