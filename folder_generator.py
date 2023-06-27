# *********************************************************************************************
# Script: Daily Folder Generator
# Author: Gabe Sikora
# Date: 6/27/2023
# Function: Automatically create a subfolder with the current date to store that day's files
# ********************************************************************************************

import os
from datetime import datetime

# Prompt user for directory and folder creation
directory = "/Users/gsikora/Desktop/GH/June"
create_folder = input("\nCreate a new folder? (y/n): ")

if create_folder.lower() == "y":
    # Get the current date and time
    current_date = datetime.now().strftime("%m.%d.%Y")
    new_folder_path = os.path.join(directory, current_date)

    try:
        # Create the new folder
        os.mkdir(new_folder_path)
        print(f"New folder '{current_date}' created successfully in '{directory}'.")
    except FileExistsError:
        print(f"Folder '{current_date}' already exists in '{directory}'.")
else:
    print("No new folder created.")
