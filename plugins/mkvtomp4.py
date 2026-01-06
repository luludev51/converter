import moviepy

def config():
    return {
        "name": "mkvtomp4",
        "version": "1.0",
        "description": "Convert MKV video files to MP4 video files.",
        "dependencies": ["moviepy"],
        "input_extension": ["mkv"],
        "output_extension": ["mp4"],
        "category": "video"
    }

def convert(mkv_file_path, mp4_file_path):
    """
    Convert an MKV video file to an MP4 video file.

    Parameters:
    mkv_file_path (str): The path to the input MKV file.
    mp4_file_path (str): The path to the output MP4 file.
    """
    try:
        if not mkv_file_path.lower().endswith('.mkv'):
            mkv_file_path += '.mkv'
        if not mp4_file_path.lower().endswith('.mp4'):
            mp4_file_path += '.mp4'
        # Load the video file
        video_clip = moviepy.VideoFileClip(mkv_file_path)

        video_clip.write_videofile(
            mp4_file_path,
            codec="libx264",
            audio_codec="aac",  # Assure que l'audio sera encodé en AAC
            audio=True
        )

        # Close the clip to release resources
        video_clip.close()

        print(f"Conversion successful: '{mkv_file_path}' to '{mp4_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")