🎬 YTDownloader

YTDownloader este o aplicație desktop pentru descărcarea videoclipurilor și audio-ului de pe YouTube, construită cu Python și CustomTkinter.

✨ Caracteristici

Descărcare videoclipuri în diferite calități: 480p, 720p, 1080p, 1440p, 2160p sau cea mai bună calitate.

Descărcare audio în format MP3.

Alegerea folderului de descărcare.

Listă de descărcări afișată în aplicație.

Funcție de Pauză / Reluare a descărcării.

Mod Dark/Light.

🛠 Cerințe (pentru rularea din cod Python)

Python 3.8+

Biblioteca yt-dlp

Biblioteca CustomTkinter

ffmpeg instalat în sistem (necesar pentru conversia audio/video)

🚀 Instalare și rulare
Varianta Python

Clonează repository-ul:

git clone https://github.com/catasPlay12/Youtube-Downloader.git
cd Youtube-Downloader


Creează și activează un mediu virtual (opțional):

python -m venv .venv
.venv\Scripts\activate   # Windows
# sau source .venv/bin/activate   # Linux/macOS


Instalează dependențele:

pip install customtkinter yt-dlp


Rulează aplicația:

python main.py

Varianta .exe (fără Python)

Dacă ai creat fișierul executabil .exe:

Deschide folderul dist/

Dă dublu click pe main.exe pentru a porni aplicația.

Astfel nu mai ai nevoie să instalezi Python sau biblioteci.

🎯 Utilizare

Introdu URL-ul YouTube.

Alege tipul de descărcare: Video sau Audio.

Dacă descarci video, selectează calitatea dorită.

Schimbă folderul de descărcare dacă vrei.

Apasă Download.

Poți pune descărcarea pe Pause și Resume.

📄 License

Acest proiect este open-source și poate fi folosit și modificat liber.