import os
from functions.prefix_fetch import get_prefix

folder = os.path.join(os.path.dirname(__file__), "../assets/videos/")
music_folder = os.path.join(os.path.dirname(__file__), "../assets/music")

def extract_numeric_part_video(filename):
    prefix = get_prefix(folder)
    numeric_part = filename[len(prefix):].split(".")[0]
    return int(numeric_part)

def extract_numeric_part_music(filename):
    prefix2 = get_prefix(music_folder)
    numeric_part = filename[len(prefix2):].split(".")[0]
    return int(numeric_part)
