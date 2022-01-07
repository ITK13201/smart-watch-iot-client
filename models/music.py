import logging
import numpy as np
import os.path
import pathlib
import urllib.parse
from typing import Optional

import librosa
from mutagen.mp3 import MP3

from config.config import DATA_DIR, STATIC_URL_PATH


logger = logging.getLogger(__name__)

class Music:
    def __init__(self, mp3_path: str = None, wav_path: str = None, file_path: str = None, url: str = None, bpm: float = None, length: float = None):
        self.mp3_path = mp3_path
        self.wav_path = wav_path
        self.file_path = file_path
        self.url = url
        self.bpm = bpm
        self.length = length

    def initial_music_model(self) -> bool:
        if self.mp3_path == None or self.wav_path == None:
            logger.error("required mp3_path and wav_path to initial music model")
            return
        self.file_path = self._get_file_path()
        self.url = self._get_url()

        return self.is_valid()

    def _get_file_path(self) -> str:
        abs_path = pathlib.Path(self.mp3_path)
        rel_path = abs_path.relative_to(DATA_DIR)
        return str(rel_path)

    def _get_url(self) -> Optional[str]:
        if self.file_path == None:
            logger.error("required file_path to get url")
            return None
        raw_url = os.path.join(STATIC_URL_PATH, self.file_path)
        encoded_url = urllib.parse.quote(raw_url, safe=":/")
        return encoded_url

    def _get_bpm(self) -> float:
        y, sr = librosa.load(self.wav_path)
        onset_env = librosa.onset.onset_strength(y, sr=sr)
        tempo: "np.ndarray[np.float64]" = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

        return float(tempo[0])

    def _get_length(self) -> float:
        audio = MP3(self.mp3_path)
        return audio.info.length

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
