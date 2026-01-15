from downloader.video import download_video
from downloader.audio import download_audio

print("1. Download video")
print("2. Download audio (mp3)")

choice = input("Choice: ")
url = input("YouTube URL: ")

if choice == "1":
    download_video(url)
elif choice == "2":
    download_audio(url)
else:
    print("Invalid choice")
