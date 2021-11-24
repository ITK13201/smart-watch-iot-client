from ytmusicapi import YTMusic

from config.config import YTM_AUTH_HEADERS_JSON_PATH

ytmusic = YTMusic(YTM_AUTH_HEADERS_JSON_PATH)
playlistId = ytmusic.create_playlist('test', 'test description')
search_results = ytmusic.search('Oasis Wonderwall')
print(search_results)
# ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])