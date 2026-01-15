import yt_dlp
import os

def download_video(url: str, quality: str, downloads_folder: str):
    # Configurație calitate
    if quality == "Best":
        ydl_opts = {'format': 'best'}
    elif quality == "1080p":
        ydl_opts = {'format': 'bestvideo[height<=1080]+bestaudio/best'}
    elif quality == "720p":
        ydl_opts = {'format': 'bestvideo[height<=720]+bestaudio/best'}
    else:
        ydl_opts = {'format': 'best'}

    ydl_opts['outtmpl'] = os.path.join(downloads_folder, '%(title)s.%(ext)s')

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
