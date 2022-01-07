import json
import logging
from usecases.google_home import GoogleHomeManager

from flask import Response

logger = logging.getLogger(__name__)

music = "【小野リサ】Sá Marina（ サー・マリーナ［プリティワールド］）　ニューアルバム『BRASIL』より-kcAYxSHzle0.mp3"


def play_music_view() -> Response:
    music_dir = "assets/musics/"
    manager = GoogleHomeManager()
    ok = manager.play_music(music_dir + music)
    if not ok:
        context = {"message": "Failed to play youtube music with google home"}
        status = 400
    else:
        context = {"message": "Succeeded to play youtube music with google home"}
        status = 200
    return Response(response=json.dumps(context), status=status)
