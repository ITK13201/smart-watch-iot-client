import os
import logging
import subprocess

from config.config import DATA_DIR

logger = logging.getLogger(__name__)

MUSIC_DIR = "musics"
MUSIC_FILE_TEMPLATE = "%(title)s-%(id)s.%(ext)s"


# example "https://music.youtube.com/watch?v=hoWrWoMCYdM&list=RDAMVM86_sM57P3U0"
def download_music(music_url: str, outdir: str = None) -> bool:
    if outdir is None:
        outdir = MUSIC_DIR
    output = os.path.join(DATA_DIR, outdir, MUSIC_FILE_TEMPLATE)
    command = 'yt-dlp -o "{}" "{}" -x --audio-format mp3'.format(output, music_url)
    status = subprocess.call(command, shell=True)
    if status != 0:
        logger.error("Failed to download music: {}".format(music_url))
        return False
    return True
