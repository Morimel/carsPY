import os
import sys
sys.path.append('/Users/isamelsov/Desktop/Cars/MainFolder')
from CommonFunc.listFuncs import list_folders

# Function to view existing folders and car files within them
def view_cars():
    # Print a header for viewing existing car brands
    print("\n--- View Existing Car Brands ---")
    # Get a list of folders representing car brands
    folders = list_folders()
    # Check if there are any available car brands
    if not folders:
        print("No car brands available.")
        return
    # Display the available car brands to the user
    print("\nAvailable Car Brands:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    try:
        # Prompt the user to choose a car brand by entering the corresponding number
        folder_choice = int(input("\nEnter the number of the brand you want to view: ")) - 1
        # Validate the user's choice
        if 0 <= folder_choice < len(folders):
            selected_folder = folders[folder_choice]  # Get the selected folder (car brand)
            # List all text files (cars) in the selected folder
            files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
            # Check if there are any cars available in the selected brand
            if not files:
                print(f"\nNo cars available in the '{selected_folder}' brand.")
                return
            # Display the available cars in the selected brand
            print(f"\nAvailable Cars in '{selected_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            # Prompt the user to choose a car file to view
            file_choice = int(input("\nEnter the number of the car you want to view: ")) - 1
            # Validate the user's choice for car file
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]  # Get the selected car file
                # Open the selected car file and read its contents
                with open(os.path.join(selected_folder, selected_file), "r") as f:
                    print("\n--- Car Information ---")
                    print(f.read())  # Display the car information
            else:
                print("Invalid choice.")  # Handle invalid file choice
        else:
            print("Invalid choice.")  # Handle invalid brand choice
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-integer input
