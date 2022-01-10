import json
import logging

import requests

from config.config import DISCORD_CHANNEL_ID, DISCORD_BOT_TOKEN
from models.music import Music

AUTHOR_NAME = "MUSIC INFO"
COLOR = 0xD85311

logger = logging.getLogger(__name__)


def send_music_info(music: Music):
    url = "https://discordapp.com/api/channels/{}/messages".format(DISCORD_CHANNEL_ID)

    embed = {
        "author": {
            "name": AUTHOR_NAME,
        },
        "title": music.get_music_name(),
        "description": "BPM: {}".format(music.bpm),
        "color": COLOR,
    }

    context = {
        "content": "Now Playing...",
        "embed": embed
    }

    headers = {
        "Authorization": "Bot {}".format(DISCORD_BOT_TOKEN),
        "Content-Type": "application/json",
    }

    response = requests.post(url, json.dumps(context), headers=headers)
    if response.status_code == 200:
        logger.info("[*] {}\n{}".format(response.status_code, response.text))
    else:
        logger.info("[!] {}\n{}".format(response.status_code, response.text))
