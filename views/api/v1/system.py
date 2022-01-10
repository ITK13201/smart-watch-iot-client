import os.path
import pathlib
import time
import json
import logging
import threading

from infrastructure.apiclient import awsApiClient
from models.music import Music
from usecases.google_home import GoogleHomeManager
from usecases.discord.bot import send_music_info
from config.config import BASE_DIR

logger = logging.getLogger(__name__)

THREAD_PATH = os.path.join(BASE_DIR, "thread.txt")
RUN_TYPE = [
    "out",
    "in"
]

def is_active():
    return os.path.isfile(THREAD_PATH)

def activate(thread: threading.Thread):
    threadfile = pathlib.Path(THREAD_PATH)
    threadfile.touch()
    with threadfile.open(mode="w") as f:
        f.write(str(thread.ident))
    logger.info("activated system.")

def deactivate():
    os.remove(THREAD_PATH)
    logger.info("deactivated system.")

def run_system_type_in():
    is_first_time = True
    while is_first_time or is_active():
        is_first_time = False

        response = awsApiClient.fetch_music()
        data: dict = json.loads(response.text)
        music = Music(
            file_path=data["file_path"],
            url=data["url"],
            bpm=data["bpm"],
            length=data["length"]
        )

        manager = GoogleHomeManager()
        ok = manager.play_music(
            music.url
        )
        if not ok:
            logger.error("Failed to play youtube music with google home")

        # log info
        logger.info("playing... : {}".format(music.get_music_name()))

        # send music info to discord
        send_music_info(music)

        # sleep in music length
        time.sleep(music.length)

def run_system_type_out():
    is_first_time = True
    while is_first_time or is_active():
        is_first_time = False

        response = awsApiClient.fetch_music()
        data: dict = json.loads(response.text)
        music = Music(
            file_path=data["file_path"],
            url=data["url"],
            bpm=data["bpm"],
            length=data["length"]
        )

        # send music info to discord
        send_music_info(music)

        # sleep in music length
        time.sleep(music.length)


def pause_system():
    manager = GoogleHomeManager()
    ok = manager.stop_music()
    if not ok:
        logger.error("Failed to stop youtube music with google home")

