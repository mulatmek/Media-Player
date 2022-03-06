import re
from pygame import mixer
import os


# p = "C:\Users\Mulat\Desktop\MediaPlayerProject\songs"


def load_song_dir_to_dictionary(user_path) -> dict:
    song_names = os.listdir(user_path)
    files_path = [os.path.abspath(user_path) for x in os.listdir(user_path)]
    for i in range(0, len(files_path)):
        files_path[i] = files_path[i] + os.sep + song_names[i]
    for i in range(0, len(song_names)):
        song_names[i] = make_file_pretty_name(song_names[i])
    return dict(zip(song_names, files_path))


def make_file_pretty_name(song_name):
    string_array = re.split('[-_ ]', song_name)
    return string_array[0] + " " + string_array[1]


def play(file_name):
    mixer.music.load(file_name)
    mixer.music.play()
    while True:
        print("Press 'p' to pause, 'r' to resume")
        print("Press 'e' to exit the program")
        query = input("  ")

        if query == 'p':
            # Pausing the music
            pause()
        if query == 'r':
            # Resuming the music
            resume()
        if query == 'e':
            # Stop the mixer
            stop()
            break


def pause():
    mixer.music.pause()


def resume():
    mixer.music.unpause()


def stop():
    mixer.music.stop()
