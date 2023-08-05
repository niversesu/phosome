import time
import customtkinter as ctk
import os
from defmovie import makevideo
from functions.prefix_fetch import get_prefix
from functions.classesgui import CustomButton, CustomCheckBox, CustomEntry
from functions.random_names import random_words
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.geometry("550x500")
window.title("Video Creator")
frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(
    master=frame,
    text="Video maker!",
    text_color="grey",
    font=("Roboto", 24)
)
label.pack(pady=12, padx=10)


# Entry widget to input the value for the filename
entry = CustomEntry(
    master=frame,
    placeholder_text="filename.mp4"
)

entry2 = CustomEntry(
    master=frame,
    placeholder_text="Video Volume"
)

entry3 = CustomEntry(
    master=frame,
    placeholder_text="Music Volume"
)

entry4 = CustomEntry(
    master=frame,
    placeholder_text="Watermark Opacity"
)

filename_default_folder = "assets/videos/"
filename_default_file = get_prefix(filename_default_folder)
filename_default = f"{filename_default_file}-compilation.mp4"
extensions = (".mp4", ".mkv", ".mp3", ".wav")
print(f"{filename_default} Is the default name!")
random_pick = random.choice(random_words)
random_pick_default = f"{random_pick}-compilation.mp4"
print(f"{random_pick_default}, Is the default random name")

def create_video():
    random_filename = checkbox_var3.get()
    filename = entry.get() if entry.get().endswith(extensions) else filename_default
    if random_filename == True:
        filename = f"{random_pick_default}"
        print(f"{random_pick_default} is the default name!")
    musicadd = checkbox_var.get()
    watermarkadd = checkbox_var2.get()
    try:
        video_volume = float(entry2.get()) if entry2.get() and float(entry2.get()) <= 1.0 else 1.0
        music_volume = float(entry3.get()) if entry3.get() and float(entry3.get()) <= 1.0 else 0.25
        watermarkopacity = float(entry4.get()) if entry4.get() and float(entry4.get()) <= 1.0 else 0.5
        makevideo(filename, musicadd, watermarkadd, watermarkopacity, video_volume, music_volume)
    except:
        print("Try only entering numbers in the volume and watermark entrys")

checkbox_var = ctk.BooleanVar()  # Variable to store checkbox state
checkbox_create = CustomCheckBox(
    master=frame,
    text="Add music?",
    variable=checkbox_var
)

checkbox_var2 = ctk.BooleanVar()
checkbox_create2 = CustomCheckBox(
    master=frame,
    text="Add watermark?",
    variable=checkbox_var2
)

checkbox_var3 = ctk.BooleanVar()
checkbox_create3 = CustomCheckBox(
    master=frame,
    text="Random Filename?",
    variable=checkbox_var3
)

button_create = CustomButton(
    master=frame,
    text="Make Video",
    command=create_video
)



window.mainloop()
