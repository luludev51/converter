import yt_dlp
import time
import os

def config():
    return {
        "name": "Youtube Downloader",
        "version": "1.2",
        "description": "Download videos from YouTube using yt-dlp.",
        "dependencies": ["yt-dlp", "ffmpeg"],
        "input_extension": [".com", ".net", ".org"],
        "output_extension": [".mp4"],
        "input_message": "Enter the URL of the video you want to download: ",
        "output_message": "Enter the output file name (without extension): ",
        "category": "other"
    }

def main(url, output_file):
    try:
        # Si l'utilisateur met un .mp4, on l'enlève
        if output_file.lower().endswith(".mp4"):
            output_file = output_file[:-4]

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": output_file + ".%(ext)s",
            "merge_output_format": "mp4",
            "noplaylist": True,
            "quiet": False,
            "windowsfilenames": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Laisse Windows libérer le fichier
        time.sleep(1)

        print("Download successful ✔")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
