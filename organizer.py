import os
import shutil
import logging
import sys

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

BASE = sys.argv[1] if len(sys.argv) > 1 else "test_folder"

os.makedirs(BASE, exist_ok=True)
logging.info("created test_folder")

dummy_files = [
    "photo.jpg", "banner.png", "animation.gif", "image.bmp",
    "notes.txt", "report.pdf", "doc.docx", "sheet.xlsx",
    "clip.mp4", "movie.mkv", "shot.avi",
    "song.mp3", "podcast.wav", "pod.flac",
    "compressed.rar"

]

for fname in dummy_files:
    open(os.path.join(BASE, fname), "w").close()

folders = {
    "images": [".jpg", ".png", ".gif", ".bmp"],
    "Documents": [".txt", ".pdf", ".docx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Others": [".rar"]
}

for folder_name in folders:
    os.makedirs(os.path.join(BASE, folder_name), exist_ok=True)

for file in os.listdir(BASE):
    ext = os.path.splitext(file)[1]

    for folder, exts in folders.items():
        if ext in exts:
            src = os.path.join(BASE, file)
            dst = os.path.join(BASE, folder, file)
            shutil.move(src, dst)
            logging.info(f"Moved {file} ->  {folder}/")
            break 
logging.info("Organization complete!")
print("Done! Check test_folder and organizer.log")