# *********************************************************************************************
# Program: Daily Folder Generator
# Author: Gabe Sikora
# Date: 6/27/2023
# Function: Automatically create a subfolder with the current date to store that day's files
# ********************************************************************************************

import os
from datetime import datetime
import shutil
from pathlib import Path

base_directory = "/Users/gsikora/Desktop/GH"
current_date = datetime.now().strftime("%m.%d.%Y")
current_month = current_date[:2]

month_dictionary = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

def create_daily_folder(base_directory, current_date, current_month, month_dictionary):
    # Check if the string is in the dictionary keys & create new monthly folder based on 1st 2 digits of date string
    if current_month in month_dictionary:
        month = month_dictionary[current_month]
        new_folder_path = os.path.join(base_directory, month)
        # Create the folder for the month if it doesn't exist
        try:
            os.mkdir(new_folder_path)
            print(f"\nFolder '{month}' created successfully.")
        except FileExistsError:
            pass

        # Create new folder based on the current date
        try:
            os.mkdir(os.path.join(new_folder_path, current_date))
            print(f"\nNew folder '{current_date}' created successfully in '{new_folder_path}'.")
        except FileExistsError:
            print(f"\nFolder '{current_date}' already exists in '{new_folder_path}'.")
    else:
        print("\nThe month is not found in the dictionary.")

create_daily_folder(base_directory, current_date, current_month, month_dictionary)

# Delete past month's files on the first day of the new month
def remove_folder_on_first_day_of_month(base_directory):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    today = datetime.today()
    past_month = months[today.month - 2]
    past_month_directory = os.path.join(base_directory, past_month)

    if str(today.day) == "1":
        try:
            shutil.rmtree(past_month_directory)
            print(f"{past_month_directory} was removed successfully")
        except Exception as e:
            print(f"Unable to delete {past_month_directory}: {e}")
    else:
        # print('not the first day of the month')
        pass

remove_folder_on_first_day_of_month(base_directory)