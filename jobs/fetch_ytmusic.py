import click
from flask.cli import with_appcontext

from processes.youtube_music import YTMusicManager

manager = YTMusicManager()

@click.command("fetch_ytmusic", help="fetch youtube music")
@with_appcontext
def fetch_ytmusic():
    results = manager.fetch_musics_by_name("3時12分")
    musics = []
    for result in results:
        if result["category"] == "Songs":
            musics.append(result)
    print(musics)