import os
from CommonFunc.listFuncs import list_folders

# Function for changing files content
def change_cars_characteristics():
    # Display the list of available car brands (folders)
    print("\n--- View Existing Car Brands ---")
    folders = list_folders()  # Call a function to list available car brands (as folders)
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
            selected_folder = folders[folder_choice]  # Select the chosen folder
            # List all car files in the selected folder (car brand)
            files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
            if not files:
                # If no car files found in the selected brand, notify the user
                print(f"\nNo cars available in the '{selected_folder}' brand.")
                return
            # List available cars in the chosen brand
            print(f"\nAvailable Cars in '{selected_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            # Get the user's choice of car to modify
            file_choice = int(input("\nEnter the number of the car you want to change: ")) - 1
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]  # Select the chosen car file
                file_path = os.path.join(selected_folder, selected_file)  # Get the full file path
                # Open and read the current car information from the file
                with open(file_path, "r") as f:
                    car_info = f.read()
                # Display the current car information to the user
                print("\n--- Current Car Information ---")
                print(car_info)
                # Extract current car details and store them in a dictionary
                car_details = {}
                for line in car_info.splitlines():
                    key, value = line.split(": ")  # Split each line into key-value pairs
                    car_details[key.strip()] = value.strip()  # Store key-value pairs in the dictionary
                # Ask the user for new values or use the existing ones if no input is provided
                new_model = input(f"Enter new Car Model (current: {car_details['Car Model']}): ") or car_details['Car Model']
                new_year = input(f"Enter new Year of Manufacture (current: {car_details['Year of Manufacture']}): ") or car_details['Year of Manufacture']
                new_price = input(f"Enter new Price (current: {car_details['Price']}): ") or car_details['Price']
                new_color = input(f"Enter new Color (current: {car_details['Color']}): ") or car_details['Color']
                # Prepare the updated car information
                updated_car_info = (f"Car ID: {car_details['Car ID']}\n"
                                    f"Car Model: {new_model}\n"
                                    f"Year of Manufacture: {new_year}\n"
                                    f"Price: {new_price}\n"
                                    f"Color: {new_color}\n")
                # Write the updated car information back to the file
                with open(file_path, "w") as f:
                    f.write(updated_car_info)
                # Notify the user that the car information has been updated
                print(f"\nCar information for '{selected_file}' has been updated.")
            else:
                print("Invalid choice.")  # Handle invalid car choice
        else:
            print("Invalid choice.")  # Handle invalid brand choice
    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a number.")
