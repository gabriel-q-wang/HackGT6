import sys
import json
import os
import requests
import lyric_generator

def main(artist_name):
    lyric_list = lyric_generator.get_lyrics_api(artist_name)
    artist_name = artist_name.replace(' ', '-')
    path_name = artist_name + '.hdf5'
    if os.path.exists(path_name):
        textgen = textgenrnn(path_name)
        response = textgen.generate(1)
        return response
    else:
        lyric_generator.train_model(lyric_list, artist_name)
        textgen = textgenrnn(path_name)
        response = textgen.generate(1)
        return response
