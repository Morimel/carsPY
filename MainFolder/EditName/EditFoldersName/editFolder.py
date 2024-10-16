import os
from pathlib import Path

def find_and_change_folder_name():
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    print("\nAvailable Car Brand Folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    actual_folder = input("Enter the name of the folder you want to change: ")
    if actual_folder in folders:
        new_folder_name = input("Enter the new folder name: ")
        if new_folder_name not in folders:
            Path(actual_folder).rename(new_folder_name)
            print(f"Folder '{actual_folder}' has been renamed to '{new_folder_name}'")
        else:
            print(f"Error: A folder with the name '{new_folder_name}' already exists.")
    else:
        print(f"Error: The folder '{actual_folder}' does not exist.")   