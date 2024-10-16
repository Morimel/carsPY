import os
from pathlib import Path

def find_and_change_file_name():
    print("\n--- View Existing Car Brands ---")
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    if not folders:
        print("No car brands available.")
        return
    print("\nAvailable Car Brands:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    try:
        folder_choice = int(input("\nEnter the number of the brand you want to view: ")) - 1
        if 0 <= folder_choice < len(folders):
            selected_folder = folders[folder_choice]
            files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
            if not files:
                print(f"\nNo cars available in the '{selected_folder}' brand.")
                return
            print(f"\nAvailable Cars in '{selected_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            file_name = input("Enter the name of the file you want to rename (including extension): ")
            file_path = Path(selected_folder) / file_name  # Учитываем путь к файлу внутри выбранной папки
            if file_path.is_file():
                new_file_name = input("Enter the new file name (including extension): ")
                new_file_path = file_path.with_name(new_file_name)
                if not new_file_path.exists():
                    try:
                        file_path.rename(new_file_path)
                        print(f"File '{file_name}' has been renamed to '{new_file_name}'")
                    except Exception as e:
                        print(f"Error while renaming file: {e}")
                else:
                    print(f"Error: A file with the name '{new_file_name}' already exists.")
            else:
                print(f"Error: The file '{file_name}' does not exist in the folder '{selected_folder}'.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")