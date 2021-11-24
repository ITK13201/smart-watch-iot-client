import click
from flask.cli import with_appcontext

@click.command("fetch_ytmusic", help="fetch youtube music")
@with_appcontext
def fetch_ytmusic():
    print('hello')