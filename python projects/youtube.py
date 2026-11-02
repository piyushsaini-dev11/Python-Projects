import yt_dlp
import tkinter as tk 
from tkinter import filedialog

def download_video(url, save_path):
    try:
        ydl_opts = {
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",
            "format": "best"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Video Downloaded Successfully!")
        
    except Exception as e:
        print(e)
      
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder:  {folder}")
       
    return folder   


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    
    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog
    
    if save_dir:
        print("Started downloaded...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")    
          