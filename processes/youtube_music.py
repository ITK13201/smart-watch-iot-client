from typing import Dict, List
from ytmusicapi import YTMusic

from config.config import YTM_AUTH_HEADERS_JSON_PATH

class YTMusicManager():
    def __init__(self) -> None:
        self.ytmusic = YTMusic(YTM_AUTH_HEADERS_JSON_PATH)

    def fetch_musics_by_name(self, name: str) -> List[Dict]:
        search_results = self.ytmusic.search(name)
        return search_results
    