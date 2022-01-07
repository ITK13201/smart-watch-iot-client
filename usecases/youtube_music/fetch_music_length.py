from mutagen.mp3 import MP3

def fetch_music_length():
    audio = MP3('/home/itk/work/projects/Project_Research_B/smart-watch-iot-client/data/musics/[Study Sleep Relax 💖] Meditation - Monoman .beautiful comment section peaceful relaxing soothing-FjHGZj2IjBk.mp3')
    print(audio.info.length)

fetch_music_length()
