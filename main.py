import MediaPlayer
import os
songs_list=MediaPlayer.load_dir_to_dictionary()
print(songs_list)
MediaPlayer.play(songs_list["Bruno Mars"])
