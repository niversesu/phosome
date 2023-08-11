# defmovie.py
import time
import random
from moviepy.editor import *
import moviepy.audio.fx.all as afx
import os


def makevideo(filename, random_combination=False, musicadd=False, watermarkadd=False, watermark_opacity=0.15, video_volume=1.0, music_volume=0.15):
    print(f"Filename: {filename}, Music add: {musicadd}")
    time.sleep(0.5)
    print(f"Watermark add: {watermarkadd}, Watermark opacity: {watermark_opacity}")
    time.sleep(0.5)
    print(f"Video volume: {video_volume}, Music volume: {music_volume}")
    time.sleep(0.5)
    folder = f"assets/videos"
    print(f"Folder path: {folder}")
    music_folder = "assets/music"
    vfx_effect1 = vfx.fadein
    vfx_effect2 = vfx.fadeout
    afx_effect1 = afx.audio_fadein
    afx_effect2 = afx.audio_fadeout
    export_folder = "exported"
    video_extensions = "mp4", "mkv"
    music_extensions = "mp3", "wav"
    pictures = os.listdir("assets/pictures")
    picture_len = len(pictures)
    picture_function = pictures[0]
    if picture_len > 1:
        picture_function = random.choice(pictures)
    picture_path = os.path.join("assets/pictures", f"{picture_function}")
    picture_clip = ImageClip(picture_path)

    from functions.numeric_parts import extract_numeric_part_music, extract_numeric_part_video

    video_files = [file for file in os.listdir(folder) if file.endswith((video_extensions))]
    if random_combination == True:
        random.shuffle(video_files)
    else:
        video_files = sorted(video_files, key=extract_numeric_part_video)
    # Process each video file and apply the fadein and fadeout effects
    video_clips = []
    for file in video_files:
        clip = VideoFileClip(os.path.join(folder, file)).fx(vfx_effect1, 0.2).fx(vfx_effect2, 0.2)
        # Adjust the volume of the video clip
        clip = clip.volumex(video_volume)
        video_clips.append(clip)
    # Concatenate the clips and create the final video
    combined_video = concatenate_videoclips(video_clips)
 
    # Set the opacity of the watermark (a value between 0 and 1, 0 for fully transparent, 1 for fully opaque)
    
    picture_clip = picture_clip.set_opacity(watermark_opacity)

    # Get the total duration of the concatenated video
    total_duration = sum(clip.duration for clip in video_clips)

    # Set the duration of the picture_clip to match the total duration
    picture_clip = picture_clip.set_duration(total_duration)

    if musicadd:
        # Rest of the music processing code...
        music_files = [file for file in os.listdir(music_folder) if file.endswith((music_extensions))]
        if random_combination == True:
            random.shuffle(music_files)
        else:
            music_files = sorted(music_files, key=extract_numeric_part_music)
        
        def music_names():
            print("Music files:", music_files)
        music_names()

        music_clips = []
        for file in music_files:
            print("Processing music file:", file)
            clip = AudioFileClip(os.path.join(music_folder, file)).fx(afx_effect1, 1).fx(afx_effect2, 1)
            music_clips.append(clip)
        music = concatenate_audioclips(music_clips)
        # Set the volume level of the music
        music = music.volumex(music_volume)

        # Set the duration of the music to match the concatenated video's duration
        music = music.set_duration(combined_video.duration)

        # Apply fade-in and fade-out effects to the music
        music = music.fx(afx_effect1, duration=1.5).fx(afx_effect2, duration=1.5)

        # Combine the original video's audio with the music
        combined_audio = CompositeAudioClip([combined_video.audio, music])

        # Apply fade-in and fade-out effects to the combined audio
        combined_audio = combined_audio.fx(afx_effect1, 1.5).fx(afx_effect2, 1.5)

        # Set the combined audio to the video
        combined_video = combined_video.set_audio(combined_audio)

        if watermarkadd:
            picture_clip = picture_clip.set_position(("right", "bottom"))
            final_clip = CompositeVideoClip([combined_video, picture_clip])
            output_filename = os.path.join(export_folder, f"{filename}")
            final_clip.write_videofile(output_filename, threads=6, audio_codec='aac')
        elif watermarkadd==False:
            final_clip = CompositeVideoClip([combined_video])
            output_filename = os.path.join(export_folder, f"{filename}")
            final_clip.write_videofile(output_filename, threads=6, audio_codec='aac')
    elif musicadd==False:
        if watermarkadd:
            picture_clip = picture_clip.set_position(("right", "bottom"))
            final_clip = CompositeVideoClip([combined_video, picture_clip])
            output_filename = os.path.join(export_folder, f"{filename}")
            final_clip.write_videofile(output_filename, threads=6, fps=30)

        elif watermarkadd==False:
            final_clip = CompositeVideoClip([combined_video])
            output_filename = os.path.join(export_folder, f"{filename}")
            final_clip.write_videofile(output_filename, threads=6, fps=30)
        quit("Finished!")

if __name__ == "__main__":
    # Call the makevideo() function only when the script is run directly
    filename = "cats.mp4"  # Default filename for direct script execution
    makevideo()  # Pass the boolean value as True

