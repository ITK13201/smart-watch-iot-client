from mutagen.mp3 import MP3

def fetch_music_length(path: str):
    audio = MP3(path)
    return audio.info.length
