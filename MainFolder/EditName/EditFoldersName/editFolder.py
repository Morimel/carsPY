import os
from pathlib import Path

# Function for changing folders name
def find_and_change_folder_name():
    # List all folders (car brands) in the current directory
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    # Display available car brand folders
    print("\nAvailable Car Brand Folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    # Ask the user to input the name of the folder they want to rename
    actual_folder = input("Enter the name of the folder you want to change: ")
    # Check if the entered folder exists in the list of folders
    if actual_folder in folders:
        # Ask the user for the new folder name
        new_folder_name = input("Enter the new folder name: ")
        # Check if the new folder name already exists
        if new_folder_name not in folders:
            # Rename the folder
            Path(actual_folder).rename(new_folder_name)
            print(f"Folder '{actual_folder}' has been renamed to '{new_folder_name}'")
        else:
            # Notify the user if the new folder name already exists
            print(f"Error: A folder with the name '{new_folder_name}' already exists.")
    else:
        # Notify the user if the folder they want to rename does not exist
        print(f"Error: The folder '{actual_folder}' does not exist.")
