import customtkinter as ctk
from tkinter import filedialog, messagebox
import yt_dlp
import os
import threading

# =========================
# APP CONFIG
# =========================
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("YTDownloader")
root.geometry("600x650")
root.resizable(False, False)

# =========================
# VARIABLES
# =========================
url_var = ctk.StringVar()
type_var = ctk.StringVar(value="Video")
quality_var = ctk.StringVar(value="Best")
dark_var = ctk.BooleanVar(value=True)

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

pause_event = threading.Event()
pause_event.set()
paused = False

# =========================
# FUNCTIONS
# =========================
def toggle_dark():
    ctk.set_appearance_mode("Dark" if dark_var.get() else "Light")

def choose_folder():
    global downloads_folder
    folder = filedialog.askdirectory(initialdir=downloads_folder)
    if folder:
        downloads_folder = folder
        folder_label.configure(text=f"Folder: {downloads_folder}")

def update_quality_visibility():
    if type_var.get() == "Audio":
        quality_frame.grid_remove()
    else:
        quality_frame.grid()

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_event.clear()
        pause_button.configure(text="Resume")
    else:
        pause_event.set()
        pause_button.configure(text="Pause")

def progress_hook(d):
    pause_event.wait()

    if d["status"] == "downloading":
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        downloaded = d.get("downloaded_bytes", 0)

        if total:
            progress = downloaded / total
            progress_bar.set(progress)

            percent = int(progress * 100)
            eta = d.get("eta", 0)

            if eta:
                m, s = divmod(eta, 60)
                progress_label.configure(text=f"{percent}% | ETA {m}m {s}s")
            else:
                progress_label.configure(text=f"{percent}%")

    elif d["status"] == "finished":
        progress_bar.set(1)
        progress_label.configure(text="Processing...")

def start_download():
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Error", "Introduce un URL valid!")
        return

    downloads_box.configure(state="normal")
    downloads_box.insert("end", f"- {url}\n")
    downloads_box.configure(state="disabled")
    downloads_box.see("end")

    progress_bar.set(0)
    progress_label.configure(text="Starting...")

    threading.Thread(target=download_worker, args=(url,), daemon=True).start()

def download_worker(url):
    if type_var.get() == "Audio":
        ydl_opts = {
            "format": "bestaudio",
            "outtmpl": os.path.join(downloads_folder, "%(title)s.%(ext)s"),
            "progress_hooks": [progress_hook],
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }]
        }
    else:
        formats = {
            "Best": "best",
            "2160p": "bestvideo[height<=2160]+bestaudio/best",
            "1440p": "bestvideo[height<=1440]+bestaudio/best",
            "1080p": "bestvideo[height<=1080]+bestaudio/best",
            "720p": "bestvideo[height<=720]+bestaudio/best",
            "480p": "bestvideo[height<=480]+bestaudio/best"
        }

        ydl_opts = {
            "format": formats.get(quality_var.get(), "best"),
            "outtmpl": os.path.join(downloads_folder, "%(title)s.%(ext)s"),
            "progress_hooks": [progress_hook],
            "merge_output_format": "mp4"
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        progress_label.configure(text="Download complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# =========================
# UI
# =========================
title = ctk.CTkLabel(
    root,
    text="YTDownloader",
    font=("Arial", 18, "bold"),
    text_color="#FF3B3B"
)
title.place(x=10, y=10)

dark_check = ctk.CTkCheckBox(
    root,
    text="Dark Mode",
    variable=dark_var,
    command=toggle_dark,
    fg_color="#FF3B3B",
    hover_color="#FF6666",
    checkmark_color="black",
    text_color="#FF3B3B"
)
dark_check.place(x=480, y=12)

ctk.CTkLabel(root, text="YouTube URL").pack(pady=(60, 5))
ctk.CTkEntry(root, width=520, textvariable=url_var).pack()

# =========================
# MAIN FRAME (FIXED)
# =========================
main_frame = ctk.CTkFrame(root)
main_frame.pack(pady=10)

type_frame = ctk.CTkFrame(main_frame)
type_frame.grid(row=0, column=0, pady=5)

ctk.CTkRadioButton(
    type_frame,
    text="Video",
    variable=type_var,
    value="Video",
    command=update_quality_visibility,
    fg_color="#FF3B3B",
    hover_color="#FF6666",
    text_color="white"
).pack(side="left", padx=20)

ctk.CTkRadioButton(
    type_frame,
    text="Audio",
    variable=type_var,
    value="Audio",
    command=update_quality_visibility,
    fg_color="#FF3B3B",
    hover_color="#FF6666",
    text_color="white"
).pack(side="left", padx=20)

quality_frame = ctk.CTkFrame(main_frame)
quality_frame.grid(row=1, column=0, pady=5)

ctk.CTkLabel(quality_frame, text="Calitate video").pack()
ctk.CTkOptionMenu(
    quality_frame,
    values=["Best", "2160p", "1440p", "1080p", "720p", "480p"],
    variable=quality_var,
    fg_color="#FF3B3B",
    button_color="#AA0000",
    button_hover_color="#FF6666"
).pack()

folder_label = ctk.CTkLabel(root, text=f"Folder: {downloads_folder}", font=("Arial", 10))
folder_label.pack(pady=5)

ctk.CTkButton(
    root,
    text="Schimbă folder",
    fg_color="#FF3B3B",
    hover_color="#FF6666",
    command=choose_folder
).pack()

progress_bar = ctk.CTkProgressBar(root, width=520, progress_color="#FF3B3B")
progress_bar.pack(pady=10)
progress_bar.set(0)

progress_label = ctk.CTkLabel(root, text="")
progress_label.pack()

ctk.CTkButton(
    root,
    text="Download",
    fg_color="#FF3B3B",
    hover_color="#FF6666",
    command=start_download
).pack(pady=10)

pause_button = ctk.CTkButton(
    root,
    text="Pause",
    fg_color="#AA0000",
    hover_color="#FF6666",
    command=toggle_pause
)
pause_button.pack()

ctk.CTkLabel(root, text="Download list").pack(pady=(15, 5))
downloads_box = ctk.CTkTextbox(root, width=520, height=120)
downloads_box.pack()
downloads_box.insert("end", "Downloads:\n")
downloads_box.configure(state="disabled")

root.mainloop()
