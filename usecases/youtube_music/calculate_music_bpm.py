import numpy as np
import librosa


def calculate_music_bpm(wav_path: str):
    y, sr = librosa.load(wav_path)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo: "np.ndarray[np.float64]" = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

    return float(tempo[0])
