import glob
import os.path

import click
import logging
from flask.cli import with_appcontext
from pydub import AudioSegment

from config.config import MUSIC_DIR

logger = logging.getLogger(__name__)


@click.command("register_music_informations", help="register music informations")
@with_appcontext
def register_music_informations():
    logger.info("started")

    file_pathes = glob.glob(os.path.join(MUSIC_DIR, "*"))
    for file_path in file_pathes:
        file_path_without_ext, ext = os.path.splitext(file_path)

        mp3_path = file_path
        wav_path = file_path_without_ext + ".wav"

        # convert wav to mp3
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")

    print(MUSIC_DIR)

    logger.info("finished")
