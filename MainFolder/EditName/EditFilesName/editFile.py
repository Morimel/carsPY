import os
from pathlib import Path

# Function for changing files name
def find_and_change_file_name():
    # Display available car brands (folders)
    print("\n--- View Existing Car Brands ---")
    folders = [f for f in os.listdir() if os.path.isdir(f)]  # Get all directories (car brands)
    if not folders:
        # If no folders (car brands) are found, notify the user and exit the function
        print("No car brands available.")
        return
    # List available car brands for the user to choose from
    print("\nAvailable Car Brands:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    try:
        # Get the user's choice of car brand
        folder_choice = int(input("\nEnter the number of the brand you want to view: ")) - 1
        if 0 <= folder_choice < len(folders):
            selected_folder = folders[folder_choice]  # Select the chosen folder (car brand)
            # List all car files in the selected folder (car brand) that have a .txt extension
            files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
            if not files:
                # If no car files are found in the selected brand, notify the user
                print(f"\nNo cars available in the '{selected_folder}' brand.")
                return
            # List available cars (files) in the chosen brand
            print(f"\nAvailable Cars in '{selected_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            # Ask the user to input the file name they want to rename
            file_name = input("Enter the name of the file you want to rename (including extension): ")
            # Define the path to the selected file (car) inside the chosen folder
            file_path = Path(selected_folder) / file_name
            if file_path.is_file():
                # If the file exists, ask for the new name
                new_file_name = input("Enter the new file name (including extension): ")
                # Create the path for the new file name
                new_file_path = file_path.with_name(new_file_name)
                # Check if the new file name already exists
                if not new_file_path.exists():
                    try:
                        # Rename the file
                        file_path.rename(new_file_path)
                        print(f"File '{file_name}' has been renamed to '{new_file_name}'")
                    except Exception as e:
                        # Handle any exceptions during the renaming process
                        print(f"Error while renaming file: {e}")
                else:
                    # Notify the user if the new file name already exists
                    print(f"Error: A file with the name '{new_file_name}' already exists.")
            else:
                # Notify the user if the original file does not exist in the selected folder
                print(f"Error: The file '{file_name}' does not exist in the folder '{selected_folder}'.")
        else:
            # Handle invalid folder selection
            print("Invalid choice.")
    except ValueError:
        # Handle non-integer input for folder selection
        print("Invalid input. Please enter a number.")
