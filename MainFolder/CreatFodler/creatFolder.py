import os

# Function to create a new folder or select an existing folder for car brand
def select_or_create_folder():
    while True:
        print("\n--- Select or Create Car Brand Folder ---")
        print("1. Create a new folder")
        print("2. Use an existing folder")
        choice = input("Enter your choice: ")
        if choice == '1':
            # Create a new folder
            while True:
                folder_name = input("Enter a NEW folder name to store car information: ")
                if os.path.exists(folder_name):
                    print("Invalid input: Folder already exists. Please choose a different name.")
                else:
                    os.makedirs(folder_name)
                    print(f"Folder '{folder_name}' created.")
                    return folder_name
        elif choice == '2':
            # Use an existing folder
            folders = [f for f in os.listdir() if os.path.isdir(f)]
            if not folders:
                print("No existing folders available. Please create a new folder.")
                continue
            print("\nAvailable Car Brand Folders:")
            for i, folder in enumerate(folders, start=1):
                print(f"{i}. {folder}")
            try:
                folder_choice = int(input("Enter the number of the folder you want to use: ")) - 1
                if 0 <= folder_choice < len(folders):
                    return folders[folder_choice]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please enter 1 or 2.")