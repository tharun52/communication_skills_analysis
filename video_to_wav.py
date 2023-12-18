import os
from moviepy.editor import VideoFileClip

def extract_audio(input_video, output_audio):
    # Load the video clip
    video_clip = VideoFileClip(input_video)

    # Extract audio
    audio_clip = video_clip.audio

    # Create a 'cache' folder if it doesn't exist
    cache_folder = 'cache'
    os.makedirs(cache_folder, exist_ok=True)

    # Save audio as WAV in the 'cache' folder
    output_path = os.path.join(cache_folder, output_audio)
    audio_clip.write_audiofile(output_path, codec='pcm_s16le')  # Use 'pcm_s16le' codec for WAV

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    input_video_file = "input_video.mp4"  # Replace with your input video file
    output_audio_file = "output_audio.wav"  # Replace with your desired output audio file

    extract_audio(input_video_file, output_audio_file)
