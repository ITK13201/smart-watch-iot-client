import time
import socket
import pychromecast
import urllib.parse

from config.config import PORT


def play_music(music_file_path: str):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = PORT

    mp3url = "http://{}:{}/{}".format(ip, port, music_file_path)
    mp3url = urllib.parse.quote(mp3url, safe=":/")

    # Chromecastデバイス（Google Homeも）を探す
    chromecasts = pychromecast.get_chromecasts()

    print(mp3url)

    if len(chromecasts) == 0:
        print("Google Homeが見つかりませんω")
        exit()

    # 固定で1個目を使う
    googleHome: pychromecast.Chromecast = chromecasts[0][0]

    if not googleHome.is_idle:
        print("Killing current running app")
        googleHome.quit_app()
        time.sleep(5)

    # 喋らせる
    googleHome.wait()
    mc = googleHome.media_controller
    print(mc.status)
    if mc.status.player_is_playing:
        print("Music is running. Stop music.")
        mc.stop()
        mc.block_until_active(timeout=30)

        # 音声を再生する
    print("Playing ", mp3url)
    mc.play_media(mp3url, "audio/mp3")
    # googleHome.media_controller.block_until_active()
