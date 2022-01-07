from pydub import AudioSegment


def load_text(path: str) -> str:
    with open(path, "r") as f:
        text = f.read()
    return text


def mp3_to_wav(mp3_path: str, wav_path: str):
    # convert wav to mp3
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
