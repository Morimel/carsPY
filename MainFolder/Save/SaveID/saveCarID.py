# Function to check that a car ID is unique and then save it
def check_and_save_car_id():
    while True:
        # Prompt the user to enter a car ID
        print("\n--- Enter Car ID ---")
        car_id = input("Enter the Car ID (unique): ")
        # Open the file 'CarsID.txt' in append mode with reading capabilities
        with open("CarsID.txt", "a+") as f:
            f.seek(0)  # Move to the beginning of the file to read its content
            existing_ids = f.read().splitlines()  # Read all existing car IDs into a list
            # Check if the entered car ID is already in the file
            if car_id in existing_ids:
                print("Invalid input: This Car ID already exists. Please use a unique ID.")
            else:
                # If the car ID is unique, write it to the file and return it
                f.write(car_id + "\n")
                return car_id
