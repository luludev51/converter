import moviepy

def config():
    return {
        "name": "mp4tomkv",
        "version": "1.0",
        "description": "Convert MP4 video files to MKV video files.",
        "dependencies": ["moviepy"],
        "input_extension": ["mp4"],
        "output_extension": ["mkv"],
        "category": "video"
    }

def convert(mp4_file_path, mkv_file_path):
    """
    Convert an MP4 video file to an MKV video file.

    Parameters:
    mp4_file_path (str): The path to the input MP4 file.
    mkv_file_path (str): The path to the output MKV file.
    """
    try:
        if not mkv_file_path.lower().endswith('.mkv'):
            mkv_file_path += '.mkv'
        if not mp4_file_path.lower().endswith('.mp4'):
            mp4_file_path += '.mp4'
        # Load the video file
        video_clip = moviepy.VideoFileClip(mp4_file_path)

        video_clip.write_videofile(
            mkv_file_path,
            codec="libx264",
            audio_codec="aac",  # Assure que l'audio sera encodé en AAC
            audio=True
        )

        # Close the clip to release resources
        video_clip.close()

        print(f"Conversion successful: '{mp4_file_path}' to '{mkv_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")