import os
def get_prefix(folder_dir):
    for file in os.listdir(folder_dir):
        x = file.split(".")
        without_extension = x[0][:-1]
        return without_extension
