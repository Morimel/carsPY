import os
import shutil

def relocate_files():
    # List all directories in the current working directory
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    # Check if there are any folders available
    if not folders:
        print("No available folders to move files.")
        return
    # Display the available folders
    print("\nAvailable Folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    try:
        # Prompt the user to choose the source folder from which to move a file
        source_folder_choice = int(input("\nEnter the number of the folder from which you want to move a file: ")) - 1
        # Validate the user's choice
        if 0 <= source_folder_choice < len(folders):
            source_folder = folders[source_folder_choice]
            # List all .txt files in the selected folder
            files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]
            # Check if there are any files in the selected folder
            if not files:
                print(f"\nNo files available in the folder '{source_folder}'.")
                return
            # Display the available files in the selected folder
            print(f"\nAvailable Files in '{source_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            # Prompt the user to choose the file they want to move
            file_choice = int(input("\nEnter the number of the file you want to move: ")) - 1
            # Validate the user's file choice
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]
                file_path = os.path.join(source_folder, selected_file)
                # Display the available folders for moving the file, excluding the source folder
                print("\nAvailable Folders for Moving the File:")
                for i, folder in enumerate(folders, start=1):
                    if folder != source_folder:  # Exclude the source folder from the list
                        print(f"{i}. {folder}")
                # Prompt the user to choose the destination folder
                destination_folder_choice = int(input("\nEnter the number of the folder to move the file to: ")) - 1
                # Validate the destination folder choice
                if 0 <= destination_folder_choice < len(folders):
                    destination_folder = folders[destination_folder_choice]
                    destination_path = os.path.join(destination_folder, selected_file)
                    
                    # Move the file to the destination folder
                    shutil.move(file_path, destination_path)
                    print(f"The file '{selected_file}' was moved from '{source_folder}' to '{destination_folder}'.")
                else:
                    print("Invalid destination folder choice.")
            else:
                print("Invalid file choice.")
        else:
            print("Invalid source folder choice.")
    except ValueError:
        # Handle input errors where the user does not enter a valid number
        print("Invalid input. Please enter a number.")
