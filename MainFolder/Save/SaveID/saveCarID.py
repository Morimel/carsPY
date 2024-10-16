# Function to check that a car ID is unique and then save it
def check_and_save_car_id():
    while True:
        print("\n--- Enter Car ID ---")
        car_id = input("Enter the Car ID (unique): ")
        with open("CarsID.txt", "a+") as f:
            f.seek(0)
            existing_ids = f.read().splitlines()
            if car_id in existing_ids:
                print("Invalid input: This Car ID already exists. Please use a unique ID.")
            else:
                f.write(car_id + "\n")
                return car_id