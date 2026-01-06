import moviepy

def config():
    return {
        "name": "mp4tomp3",
        "version": "1.0",
        "description": "Convert MP4 video files to MP3 audio files.",
        "dependencies": ["moviepy"],
        "input_extension": ["mp4"],
        "output_extension": ["mp3"],
        "category": "audio"
    }

def convert(mp4_file_path, mp3_file_path):
    """
    Convert an MP4 video file to an MP3 audio file.

    Parameters:
    mp4_file_path (str): The path to the input MP4 file.
    mp3_file_path (str): The path to the output MP3 file.
    """
    try:
        if not mp4_file_path.lower().endswith('.mp4'):
            mp4_file_path += '.mp4'
        if not mp3_file_path.lower().endswith('.mp3'):
            mp3_file_path += '.mp3'
        # Load the video file
        video_clip = moviepy.VideoFileClip(mp4_file_path)

        # Extract the audio
        audio_clip = video_clip.audio

        # Write the audio to an MP3 file
        audio_clip.write_audiofile(mp3_file_path)

        # Close the clips to release resources
        audio_clip.close()
        video_clip.close()

        print(f"Conversion successful: '{mp4_file_path}' to '{mp3_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")