from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip('hell.mp4')

# Extract and save the audio
audio_path = 'hell.wav'
video.audio.write_audiofile(audio_path)
