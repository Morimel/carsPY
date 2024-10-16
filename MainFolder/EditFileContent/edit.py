import os

def change_cars_characteristics():
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
            file_choice = int(input("\nEnter the number of the car you want to change: ")) - 1
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]
                file_path = os.path.join(selected_folder, selected_file)
                # Open and read the current car information
                with open(file_path, "r") as f:
                    car_info = f.read()
                print("\n--- Current Car Information ---")
                print(car_info)
                # Extract current values
                car_details = {}
                for line in car_info.splitlines():
                    key, value = line.split(": ")
                    car_details[key.strip()] = value.strip()
                # Ask user for new values or keep the old ones if input is empty
                new_model = input(f"Enter new Car Model (current: {car_details['Car Model']}): ") or car_details['Car Model']
                new_year = input(f"Enter new Year of Manufacture (current: {car_details['Year of Manufacture']}): ") or car_details['Year of Manufacture']
                new_price = input(f"Enter new Price (current: {car_details['Price']}): ") or car_details['Price']
                new_color = input(f"Enter new Color (current: {car_details['Color']}): ") or car_details['Color']
                # Prepare updated car information
                updated_car_info = (f"Car ID: {car_details['Car ID']}\n"
                                    f"Car Model: {new_model}\n"
                                    f"Year of Manufacture: {new_year}\n"
                                    f"Price: {new_price}\n"
                                    f"Color: {new_color}\n")
                # Save updated information back to the file
                with open(file_path, "w") as f:
                    f.write(updated_car_info)
                print(f"\nCar information for '{selected_file}' has been updated.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")