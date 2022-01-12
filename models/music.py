import logging
import numpy as np
import os.path
import pathlib
import urllib.parse
from typing import Optional

import librosa
from mutagen.mp3 import MP3

from config.config import DATA_DIR, STATIC_URL_PATH
from infrastructure.apiclient import awsApiClient

logger = logging.getLogger(__name__)


class Music:
    def __init__(
        self,
        mp3_path: str = None,
        wav_path: str = None,
        file_path: str = None,
        url: str = None,
        bpm: float = None,
        length: float = None,
    ):
        self.mp3_path = mp3_path
        self.wav_path = wav_path
        self.file_path = file_path
        self.url = url
        self.bpm = bpm
        self.length = length

    def initial_music_model(self) -> bool:
        if self.mp3_path == None or self.wav_path == None:
            logger.error("required mp3_path and wav_path to initial music model")
            return False
        self.file_path = self._get_file_path()
        self.url = self._get_url()
        self.bpm = self._get_bpm()
        self.length = self._get_length()

        return self.is_valid()

    def _get_file_path(self) -> str:
        logger.info("getting file path...: {}".format(self.mp3_path))

        abs_path = pathlib.Path(self.mp3_path)
        rel_path = abs_path.relative_to(DATA_DIR)
        return str(rel_path)

    def _get_url(self) -> Optional[str]:
        logger.info("getting url...: {}".format(self.mp3_path))

        if self.file_path == None:
            logger.error("required file_path to get url")
            return None
        static_url_path = STATIC_URL_PATH
        if static_url_path.startswith("/"):
            static_url_path = static_url_path[1:]
        raw_url = os.path.join(static_url_path, self.file_path)
        encoded_url = urllib.parse.quote(raw_url, safe=":/")
        return encoded_url

    def _get_bpm(self) -> float:
        logger.info("getting BPM...: {}".format(self.mp3_path))

        # 切り出す区間
        duration = 30.0
        # 切り出し開始時間
        offset = 50.0

        y, sr = librosa.load(self.wav_path, offset=offset, duration=duration)
        onset_env = librosa.onset.onset_strength(y, sr=sr)
        tempo: "np.ndarray[np.float64]" = librosa.beat.tempo(
            onset_envelope=onset_env, sr=sr
        )

        return float(tempo[0])

    def _get_length(self) -> float:
        logger.info("getting length...: {}".format(self.mp3_path))

        audio = MP3(self.mp3_path)
        return audio.info.length

    def get_music_name(self) -> str:
        file_name = os.path.basename(self.file_path)
        blocks = file_name.split("@")
        if len(blocks) == 1:
            music_name = blocks[0]
        else:
            music_name = "".join(blocks[:-1])
        return music_name

    def is_valid(self) -> bool:
        if self.file_path == None:
            return False
        if self.url == None:
            return False
        if self.bpm == None:
            return False
        if self.length == None:
            return False

        return True

    def push_aws(self):
        if self.is_valid():
            query = {
                "file_path": self.file_path,
                "url": self.url,
                "bpm": self.bpm,
                "length": self.length,
            }
            response = awsApiClient.add_music(query)
            if response.status_code == 201:
                logger.info("Successfully add music: {}".format(query))
            else:
                logger.error("Failed to add music: {}".format(query))
        else:
            logger.error("not enough variables to push aws: {}".format(self.mp3_path))

    def __dict__(self):
        return {
            "mp3_path": self.mp3_path,
            "wav_path": self.wav_path,
            "file_path": self.file_path,
            "url": self.url,
            "bpm": self.bpm,
            "length": self.length,
        }

    def __str__(self):
        return str(self.__dict__())
