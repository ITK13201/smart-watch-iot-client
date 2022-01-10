import pprint
import time
import socket
import logging
from typing import Union, Optional
from pychromecast import Chromecast, CastBrowser, get_chromecasts

from config.config import PORT

logger = logging.getLogger(__name__)


class GoogleHomeManager:
    def __init__(self):
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.port = PORT

    def find_google_home(self) -> Optional[Chromecast]:
        # Chromecastデバイス（Google Homeも）を探す
        logger.info("Searching Google home...")
        chromecasts: Union[
            tuple[list[Chromecast], CastBrowser], CastBrowser
        ] = get_chromecasts()

        if len(chromecasts) == 0:
            logger.error("Google Home Not Found")
            return None

        try:
            google_home = chromecasts[0][0]
        except IndexError:
            logger.error("Couldn't Search Google Home")
            return None
        else:
            logger.info("Found Google Home")
            logger.info(pprint.pformat(google_home))

        return google_home

    def play_music(self, music_file_path: str) -> bool:
        mp3_url = "http://{}:{}/{}".format(self.ip, self.port, music_file_path)

        google_home = self.find_google_home()
        if google_home is None:
            return False

        # kill running app of google home
        if not google_home.is_idle:
            logger.info("Killing current running app of Google Home")
            google_home.quit_app()
            time.sleep(5)

        google_home.wait()

        controller = google_home.media_controller
        # if running music, stop it
        if controller.status.player_is_playing:
            logger.info("Music is running. Stop music. with google home")
            controller.stop()
            controller.block_until_active(timeout=30)

        # play music
        logger.info("Playing... : {}".format(mp3_url))
        controller.play_media(mp3_url, "audio/mp3")
        google_home.media_controller.block_until_active()
        return True

    def stop_music(self) -> bool:
        google_home = self.find_google_home()
        if google_home is None:
            return False

        google_home.wait()
        google_home.quit_app()

        # controller = google_home.media_controller
        # controller.stop()
        # controller.block_until_active(timeout=30)

        logger.info("Music stopped. with google home")
        return True
