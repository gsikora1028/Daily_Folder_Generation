# *********************************************************************************************
# Program: Daily Folder Generator
# Author: Gabe Sikora
# Date: 6/27/2023
# Function: Automatically create a subfolder with the current date to store that day's files
# ********************************************************************************************

import os
from datetime import datetime

directory = "/Users/gsikora/Desktop/GH/July"
print(f"Accessing {directory} diretory")
current_date = datetime.now().strftime("%m.%d.%Y")
new_folder_path = os.path.join(directory, current_date)

try:
    # Create new folder based on current date
    os.mkdir(new_folder_path)
    print(f"\nNew folder '{current_date}' created successfully in '{directory}'.")
except FileExistsError:
    print(f"\nFolder '{current_date}' already exists in '{directory}'.")
else:
    print("No new folder created.")
