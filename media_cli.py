import click
import pygame.mixer

import song_names_utilities


@click.group()
def media_cli():
    pass


@click.command()
@click.option('--name', '-n', help="Name of the user", required=True, prompt="Enter Your Name please")
def start(name):
    pygame.mixer.init()
    print(f"hello,{name}" + " " + "from media paler")
    file1 = open('media_config.txt', 'r')
    Lines = [line.strip() for line in file1.readlines()]
    path = Lines[0]
    song_list = song_names_utilities.load_song_dir_to_dictionary(path)


@click.command()
@click.option('--path', '-n', help="enter a path ", required=True)
def load(path):
    song_list = song_names_utilities.load_song_dir_to_dictionary(path)
    f = open("media_config.txt", "a")
    f.write(path + "\n")
    for song in song_list.keys():
        f.write(song + "\n")
    f.close()


media_cli.add_command(start)
media_cli.add_command(load)
