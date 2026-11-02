import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\user\Documents\nishu pencil"
destination_dir = r"C:\Users\user\Pictures\pishu"


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"The folder copied to: {dest_dir}")
        
    except FileExistsError:
        print("The folder does not existed.")    
        
schedule.every().day.at("16:16").do(lambda:copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
        
