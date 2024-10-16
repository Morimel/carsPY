##################################
#   Author: Orozaliev Isa i Isa  #
##################################

import os
from pathlib import Path
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


# Main function to show the menu
def main():    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new car")
        print("2. View existing cars")
        print("3. Exit")
        print("4. Change folder or file name")
        print("5. Delete folder or file")
        print("6. Change cars characteristics")
        print("7. Relocate files")
        print("8. Search")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Select or create a folder and save new car info
            folder_name = select_or_create_folder()
            car_id = check_and_save_car_id()
            print("\n--- Enter Car Details ---")
            car_model = input("Enter the Car Model: ")
            car_year = input("Enter the Year of Manufacture: ")
            car_price = input("Enter the Price of the Car: ")
            car_color = input("Enter cars color: ")
            car_info = f"Car ID: {car_id}\nCar Model: {car_model}\nYear of Manufacture: {car_year}\nPrice: {car_price}\nColor: {car_color}\n"
            save_car_info(folder_name, car_id, car_info)
        
        elif choice == '2':
            view_cars()
        
        elif choice == '3':
            print("\nExiting the application. Goodbye!")
            break
        
        elif choice == '4':
            print("\n--- Choose one option ---")
            print("1. Rename folder")
            print("2. Rename file")
            fourth_choice = input("Enter your choice: ")
            if fourth_choice == '1':
                find_and_change_folder_name()
            elif fourth_choice == '2':
                find_and_change_file_name()
            else: 
                print("Invalid input. Please enter a number.")
        
        elif choice == '5':
            delete_folder_or_file()
        
        elif choice == '6':
            change_cars_characteristics()
        
        elif choice == '7':
            relocate_files()
        
        elif choice == '8':
            search_folder_or_file()
        
        else:
            print("Invalid choice. Please enter a number from the menu options.")
if __name__ == "__main__":
    main()