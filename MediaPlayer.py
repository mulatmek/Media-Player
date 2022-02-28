import string

import pygame.mixer
from pygame import mixer
import pathlib


def load_dir_to_dictionary() -> dict:
    pass


def make_file_pretty_name(ugly_song_name) -> string:
    pass


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
