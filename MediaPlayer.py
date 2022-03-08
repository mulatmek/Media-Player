import re
from pygame import mixer
import os


# p = "C:\Users\Mulat\Desktop\MediaPlayerProject\songs"
# click ->

def load_song_dir_to_dictionary(user_path) -> dict:
    root_path = os.path.abspath(user_path)
    return {
        make_file_pretty_name(file): root_path + os.sep + file
        for file in os.listdir(user_path)
    }


def make_file_pretty_name(song_name):
    res=""
    for string in song_name.split()[:7]:
        res+=string
        res+=" "
    return res.removesuffix(" ")


# test
#assert make_file_pretty_name("Drake - Fake Love (128  kbps) (mp3conv.ru).mp3") == "Drake "


def play(file_name):
    mixer.music.load(file_name)
    mixer.music.play()
