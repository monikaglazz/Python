# Import module
import moviepy.editor as mp

# Choose path to video
video = mp.VideoFileClip(
    r"Insert here your file path")

# Choose path to save audio
video.audio.write_audiofile(
    r"Insert here your audio path with file name")
