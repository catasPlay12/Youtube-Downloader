import yt_dlp
import os

def download_audio(url: str, downloads_folder: str):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
