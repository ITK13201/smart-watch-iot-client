import click
from flask.cli import with_appcontext

from usecases import processes


@click.command("download_ytmusic", help="download youtube music")
@with_appcontext
def download_ytmusic():
    processes.download_ytmusic("https://music.youtube.com/watch?v=kcAYxSHzle0")
