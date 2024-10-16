##################################
#       Author: Melsov Isa       #
##################################

import sys
# Adding the path to 'Cars/MainFolder' directory for module imports
sys.path.append('/Users/isamelsov/Desktop/Cars/MainFolder')

# Import necessary functions from different modules
from EditName.EditFilesName.editFile import find_and_change_file_name
from EditName.EditFoldersName.editFolder import find_and_change_folder_name
from Delete.delete import delete_folder_or_file
from EditFileContent.edit import change_cars_characteristics
from Relocate.relocate import relocate_files
from Search.search import search_folder_or_file
from Save.SaveID.saveCarID import check_and_save_car_id
from Save.SaveInfo.SaveCarInfo import save_car_info
from CreatFodler.creatFolder import select_or_create_folder
from ViewCars.viewCars import view_cars


# Main function to show the menu and handle user interactions
def main():    
    while True:
        # Display the main menu with options
        print("\n--- Main Menu ---")
        print("1. Add a new car")
        print("2. View existing cars")
        print("3. Exit")
        print("4. Change folder or file name")
        print("5. Delete folder or file")
        print("6. Change cars characteristics")
        print("7. Relocate files")
        print("8. Search")
        
        # Get user input for their choice
        choice = input("Enter your choice: ")
        
        # Option 1: Add a new car
        if choice == '1':
            # Select or create a folder to store the new car information
            folder_name = select_or_create_folder()
            # Generate a unique car ID and prompt user for car details
            car_id = check_and_save_car_id()
            print("\n--- Enter Car Details ---")
            car_model = input("Enter the Car Model: ")
            car_year = input("Enter the Year of Manufacture: ")
            car_price = input("Enter the Price of the Car: ")
            car_color = input("Enter cars color: ")
            # Format the car information and save it
            car_info = f"Car ID: {car_id}\nCar Model: {car_model}\nYear of Manufacture: {car_year}\nPrice: {car_price}\nColor: {car_color}\n"
            save_car_info(folder_name, car_id, car_info)
        
        # Option 2: View existing cars
        elif choice == '2':
            # Call function to display all saved cars
            view_cars()
        
        # Option 3: Exit the program
        elif choice == '3':
            print("\nExiting the application. Goodbye!")
            break
        
        # Option 4: Change folder or file name
        elif choice == '4':
            print("\n--- Choose one option ---")
            print("1. Rename folder")
            print("2. Rename file")
            # Ask the user if they want to rename a folder or a file
            fourth_choice = input("Enter your choice: ")
            if fourth_choice == '1':
                find_and_change_folder_name()  # Rename folder
            elif fourth_choice == '2':
                find_and_change_file_name()  # Rename file
            else: 
                print("Invalid input. Please enter a number.")
        
        # Option 5: Delete folder or file
        elif choice == '5':
            # Call the delete function to delete a folder or file
            delete_folder_or_file()
        
        # Option 6: Change car characteristics (edit car information)
        elif choice == '6':
            # Call the function to edit car information
            change_cars_characteristics()
        
        # Option 7: Relocate files between folders
        elif choice == '7':
            # Call the function to relocate files
            relocate_files()
        
        # Option 8: Search for a folder or file
        elif choice == '8':
            # Call the search function to search for folders or files
            search_folder_or_file()
        
        # Handle invalid input by notifying the user
        else:
            print("Invalid choice. Please enter a number from the menu options.")

# Ensure the main function is called only if this file is run directly
if __name__ == "__main__":
    main()
