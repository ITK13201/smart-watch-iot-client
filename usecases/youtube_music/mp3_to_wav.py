from pydub import AudioSegment


def mp3_to_wav(mp3_path: str, wav_path: str):
    # convert wav to mp3
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
