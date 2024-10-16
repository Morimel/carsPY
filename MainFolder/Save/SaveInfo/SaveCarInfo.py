import os

# Function to save car information in a specified folder
def save_car_info(folder_name, car_id, car_info):
    # Create a file path using the folder name and the car ID, with a .txt extension
    file_path = os.path.join(folder_name, f"{car_id}.txt")
    # Open the file in write mode ("w"), which creates the file if it doesn't exist
    with open(file_path, "w") as car_file:
        # Write the car information into the file
        car_file.write(car_info)
    # Notify the user that the car information has been successfully saved
    print(f"\nCar information saved in '{file_path}'\n")
