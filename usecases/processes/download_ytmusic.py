import os
import logging
import subprocess

from config.config import BASE_DIR

logger = logging.getLogger(__name__)

# example "https://music.youtube.com/watch?v=hoWrWoMCYdM&list=RDAMVM86_sM57P3U0"
def download_ytmusic(music_url: str, outdir: str = None):
    if outdir is None:
        outdir = "assets/musics"
    file_template = "%(title)s-%(id)s.%(ext)s"
    output = os.path.join(BASE_DIR, outdir, file_template)
    command = 'yt-dlp -o "{}" "{}" -x --audio-format mp3'.format(output, music_url)
    status = subprocess.call(command, shell=True)
    if status != 0:
        logger.error("Failed to download music: {}".format(music_url))
