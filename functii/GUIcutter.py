import tkinter as tk
from tkinter import ttk
from cutter import trim_video, trim_audio
import threading

root = tk.Tk()
root.title("Cutter Test")

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, length=400, variable=progress_var, maximum=100)
progress_bar.pack(pady=20)

def update_progress(percent):
    progress_var.set(percent)
    progress_bar.update()

def start_video_cut():
    threading.Thread(
        target=trim_video,
        args=("input.mp4", 10, 20, "output.mp4", update_progress)
    ).start()

def start_audio_cut():
    threading.Thread(
        target=trim_audio,
        args=("input.mp3", 5, 15, "output.mp3", update_progress)
    ).start()

tk.Button(root, text="Trim Video", command=start_video_cut).pack(pady=5)
tk.Button(root, text="Trim Audio", command=start_audio_cut).pack(pady=5)

root.mainloop()
