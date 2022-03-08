import pygame.mixer
import MediaPlayer
import os
from difflib import SequenceMatcher

s_1 = 'Travie McCoy_ Billionaire'
s_2 = 'Travie McCoy_ Billionaire ft.'
print(SequenceMatcher(a=s_1, b=s_2).ratio())


def main():
    pygame.mixer.init()
    songs_list = MediaPlayer.load_song_dir_to_dictionary(r"C:\Users\Mulat\Desktop\MediaPlayerProject\songs")
    print(songs_list)
    while True:
        print("please enter the song you want to play")
        user_song = input()
        for song in songs_list.keys():
            if SequenceMatcher(a=user_song.lower(), b=song.lower()).ratio() >= 0.5:
                MediaPlayer.play(songs_list[song])
        print("your song didn't match any song in your dir try again")


if __name__ == "__main__":
    main()
