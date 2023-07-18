# *********************************************************************************************
# Program: Daily Folder Generator
# Author: Gabe Sikora
# Date: 6/27/2023
# Function: Automatically create a subfolder with the current date to store that day's files
# ********************************************************************************************

import os
from datetime import datetime

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

# Check if the string is in the dictionary keys & create new monthly folder based on 1st 2 digits of date string
if current_month in month_dictionary:
    month = month_dictionary[current_month]
    new_folder_path = os.path.join(base_directory, month)
    
    # Create the folder for the month if it doesn't exist
    try:
        os.mkdir(new_folder_path)
        print(f"Folder '{month}' created successfully.")
    except FileExistsError:
       pass

    # Create new folder based on the current date
    try:
        os.mkdir(os.path.join(new_folder_path, current_date))
        print(f"New folder '{current_date}' created successfully in '{new_folder_path}'.")
    except FileExistsError:
        print(f"Folder '{current_date}' already exists in '{new_folder_path}'.")
else:
    print("The month is not found in the dictionary.")
