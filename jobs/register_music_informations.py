import glob
import os.path

import click
import logging
from flask.cli import with_appcontext
from pydub import AudioSegment

from models.music import Music
from config.config import MUSIC_DIR
from usecases.utils import mp3_to_wav

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

        # create mav from mp3
        mp3_to_wav()

        music = Music(mp3_path=mp3_path, wav_path=wav_path)
        ok = music.initial_music_model()
        if not ok:
            logger.error("errors occurred during initial music model: {}".format(mp3_path))
            continue






    print(MUSIC_DIR)

    logger.info("finished")
