import click
from flask.cli import with_appcontext

from usecases import processes


@click.command("play_music", help="play music")
@with_appcontext
def play_music():
    processes.play_music("assets/musics/ゆったりボサノバ-W8nQEIDXk-k.mp3")
