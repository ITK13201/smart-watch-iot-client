import os.path
from os import path
from pydub import AudioSegment
import glob

def mp3_to_wav():
    file_pathes = glob.glob("/home/itk/work/projects/Project_Research_B/smart-watch-iot-client/data/musics/*")
    for file_path in file_pathes:
        file_path_without_ext, ext = os.path.splitext(file_path)

        src = file_path
        dst = file_path_without_ext + ".wav"

        # convert wav to mp3
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")

mp3_to_wav()
