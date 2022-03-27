import pygame.mixer
import song_names_utilities
import setup
import os
from difflib import SequenceMatcher


def main():
    temp()


def temp():
    pygame.mixer.init()
    songs_list = song_names_utilities.load_song_dir_to_dictionary(r"C:\Users\Mulat\Desktop\MediaPlayerProject\songs")
    print(songs_list)
    while True:
        song_available = False
        print("please enter the song you want to play")
        user_song = input()
        for song in songs_list.keys():
            if SequenceMatcher(a=user_song.lower(), b=song.lower()).ratio() >= 0.5:
                song_names_utilities.play(songs_list[song])
                song_available = True
        if not song_available:
            print("we didn't find match to your song")


if __name__ == "__main__":
    main()
