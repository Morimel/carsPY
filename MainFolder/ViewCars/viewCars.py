import os

# Function to view existing folders and car files within them
def view_cars():
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
            file_choice = int(input("\nEnter the number of the car you want to view: ")) - 1
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]
                with open(os.path.join(selected_folder, selected_file), "r") as f:
                    print("\n--- Car Information ---")
                    print(f.read())
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")