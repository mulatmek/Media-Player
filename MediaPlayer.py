import string

import pygame.mixer
import os


def load_dir_to_dictionary() -> dict:
    user_path = input()
    songs_name = os.listdir(user_path)
    for i in range(0,len(songs_name)):
        songs_name[i]=make_file_pretty_name(songs_name[i])
    print(songs_name)
    files_path = [os.path.abspath(x) for x in os.listdir(user_path)]
    zip_iterator = zip(songs_name, files_path)
    return dict(zip_iterator)


def make_file_pretty_name(song_name) -> string:
    return song_name.split("-")[0]


def playMusic():
    pass


def play(file_name) -> float:
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    return pygame.mixer.Sound.get_length()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


def stop():
    pygame.mixer.music.stop()
