import customtkinter as ctk
from tkinter import messagebox, filedialog
from downloader.video import download_video
from downloader.audio import download_audio
import os

# Setări generale
ctk.set_default_color_theme("blue")  # tema principală

# Fereastră principală
root = ctk.CTk()
root.title("YouTube Downloader")
root.geometry("500x400")

# ------------------------
# Variabile
# ------------------------
url_var = ctk.StringVar()
option_var = ctk.StringVar(value="Video")
quality_var = ctk.StringVar(value="Best")
dark_mode_var = ctk.BooleanVar(value=True)
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# ------------------------
# Funcții
# ------------------------
def toggle_dark_mode():
    if dark_mode_var.get():
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("Light")

def choose_folder():
    global downloads_folder
    folder = filedialog.askdirectory(initialdir=downloads_folder)
    if folder:
        downloads_folder = folder
        folder_label.configure(text=f"Folder: {downloads_folder}")

def start_download():
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Error", "Introduceți un URL valid!")
        return

    choice = option_var.get()
    quality = quality_var.get()

    try:
        if choice == "Video":
            download_video(url, quality, downloads_folder)
            messagebox.showinfo("Success", "Video download complete!")
        elif choice == "Audio":
            download_audio(url, downloads_folder)
            messagebox.showinfo("Success", "Audio download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")

# ------------------------
# Layout
# ------------------------

# Dark mode checkbox
dark_check = ctk.CTkCheckBox(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
dark_check.pack(pady=10)

# URL entry
ctk.CTkLabel(root, text="YouTube URL:", font=("Arial", 14)).pack(pady=5)
url_entry = ctk.CTkEntry(root, textvariable=url_var, width=400)
url_entry.pack(pady=5)

# Video / Audio radiobutton
ctk.CTkLabel(root, text="Tip download:", font=("Arial", 12)).pack(pady=5)
frame_radio = ctk.CTkFrame(root)
frame_radio.pack(pady=5)

ctk.CTkRadioButton(frame_radio, text="Video", variable=option_var, value="Video").pack(side="left", padx=20)
ctk.CTkRadioButton(frame_radio, text="Audio", variable=option_var, value="Audio").pack(side="left", padx=20)

# Calitate dropdown (doar pentru Video)
ctk.CTkLabel(root, text="Calitate video:", font=("Arial", 12)).pack(pady=5)
quality_menu = ctk.CTkOptionMenu(root, values=["Best", "1080p", "720p"], variable=quality_var)
quality_menu.pack(pady=5)

# Folder descărcări
folder_label = ctk.CTkLabel(root, text=f"Folder: {downloads_folder}", font=("Arial", 10))
folder_label.pack(pady=5)
folder_btn = ctk.CTkButton(root, text="Schimbă folder", command=choose_folder)
folder_btn.pack(pady=5)

# Buton Download
download_btn = ctk.CTkButton(root, text="Download", command=start_download)
download_btn.pack(pady=20)

root.mainloop()
