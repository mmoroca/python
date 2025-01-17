import os
import shutil
import re

# Ask for the folder to process
folder_to_process = input("Enter the folder to process: ")

if not os.path.exists(folder_to_process):
    print(f"The folder {folder_to_process} does not exist.")
    exit(1)

os.chdir(folder_to_process)

print("Cleaning files...")

# Find and delete files with names containing a letter followed or not by a number within brackets
for file_name in os.listdir('.'):
    if re.search(r'\[[A-Za-z][0-9]?\]', file_name):
        try:
            os.remove(file_name)
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")

print("Making folders...")

# Create folders A to Z
for letter in range(ord('A'), ord('Z') + 1):
    folder_name = chr(letter)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Create "others" folder
if not os.path.exists('OTHERS'):
    os.makedirs('OTHERS')

# Move files into corresponding folders
for file_name in os.listdir('.'):
    if os.path.isfile(file_name):
        first_letter = file_name[0].upper()
        if first_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            destination_folder = first_letter
        else:
            destination_folder = 'others'
        try:
            #print(f"Moving {file_name} to {destination_folder}")
            shutil.move(file_name, os.path.join(destination_folder, file_name))
        except Exception as e:
            print(f"Error moving {file_name} to {destination_folder}: {e}")

print("All done.")