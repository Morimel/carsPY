##################################
#   Author: Orozaliev Isa i Isa  #
##################################

import os
from pathlib import Path
import shutil

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
            
            
            

# Function to save car information in a specified folder
def save_car_info(folder_name, car_id, car_info):
    file_path = os.path.join(folder_name, f"{car_id}.txt")
    with open(file_path, "w") as car_file:
        car_file.write(car_info)
    print(f"\nCar information saved in '{file_path}'\n")
    
    
    
    
def delete_folder():
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    if not folders:
        print("No folders available to delete.")
        return
    
    print("\nAvailable Car Brand Folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}") 
    
    actual_folder = input("Enter the name of the folder you want to delete: ")
    
    # Проверка на существование папки
    if actual_folder in folders:
        try:
            shutil.rmtree(actual_folder)  # Удаление папки
            print(f"Folder '{actual_folder}' has been deleted.")
        except Exception as e:
            print(f"Error: Could not delete the folder. {e}")
    else:
        print(f"Error: The folder '{actual_folder}' does not exist.")

    
    
    
def find_and_change_folder_name():
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    print("\nAvailable Car Brand Folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    actual_folder = input("Enter the name of the folder you want to change: ")
    if actual_folder in folders:
        new_folder_name = input("Enter the new folder name: ")
        if new_folder_name not in folders:
            Path(actual_folder).rename(new_folder_name)
            print(f"Folder '{actual_folder}' has been renamed to '{new_folder_name}'")
        else:
            print(f"Error: A folder with the name '{new_folder_name}' already exists.")
    else:
        print(f"Error: The folder '{actual_folder}' does not exist.")
        
        
        
        
        
        
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
        
        
        
        
# Function to search for folders or files
def search_folder_or_file():
    search_query = input("Enter the name of the folder or file to search for: ")

    # Walk through the directory tree
    found_items = []
    for root, dirs, files in os.walk('.'):
        # Поиск папок
        for dir_name in dirs:
            if search_query.lower() in dir_name.lower():
                found_items.append(os.path.join(root, dir_name))

        # Поиск файлов
        for file_name in files:
            if search_query.lower() in file_name.lower():
                found_items.append(os.path.join(root, file_name))

    # Вывод результатов поиска
    if found_items:
        print(f"\n--- Found {len(found_items)} matching items ---")
        for item in found_items:
            print(item)
    else:
        print(f"\nNo folders or files found matching '{search_query}'.")

        
        
        
def relocate_files():
    # Список всех папок в текущей директории
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    if not folders:
        print("Нет доступных папок для перемещения файлов.")
        return

    print("\nДоступные папки:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")

    try:
        # Выбор папки, из которой будет перемещен файл
        source_folder_choice = int(input("\nВведите номер папки, из которой хотите переместить файл: ")) - 1
        if 0 <= source_folder_choice < len(folders):
            source_folder = folders[source_folder_choice]
            # Список файлов в выбранной папке
            files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]
            if not files:
                print(f"\nНет файлов в папке '{source_folder}'.")
                return

            print(f"\nДоступные файлы в '{source_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")

            file_choice = int(input("\nВведите номер файла, который хотите переместить: ")) - 1
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]
                file_path = os.path.join(source_folder, selected_file)

                # Выбор папки назначения
                print("\nДоступные папки для перемещения файла:")
                for i, folder in enumerate(folders, start=1):
                    if folder != source_folder:  # Исключаем папку источника
                        print(f"{i}. {folder}")

                destination_folder_choice = int(input("\nВведите номер папки, куда хотите переместить файл: ")) - 1
                if 0 <= destination_folder_choice < len(folders):
                    destination_folder = folders[destination_folder_choice]
                    destination_path = os.path.join(destination_folder, selected_file)

                    # Перемещение файла
                    shutil.move(file_path, destination_path)
                    print(f"Файл '{selected_file}' был перемещен из '{source_folder}' в '{destination_folder}'.")
                else:
                    print("Неверный выбор папки назначения.")
            else:
                print("Неверный выбор файла.")
        else:
            print("Неверный выбор папки источника.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

        
        
def find_and_change_file_name():
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
            
            file_name = input("Enter the name of the file you want to rename (including extension): ")
            file_path = Path(selected_folder) / file_name  # Учитываем путь к файлу внутри выбранной папки
            
            if file_path.is_file():
                new_file_name = input("Enter the new file name (including extension): ")
                new_file_path = file_path.with_name(new_file_name)
                
                if not new_file_path.exists():
                    try:
                        file_path.rename(new_file_path)
                        print(f"File '{file_name}' has been renamed to '{new_file_name}'")
                    except Exception as e:
                        print(f"Error while renaming file: {e}")
                else:
                    print(f"Error: A file with the name '{new_file_name}' already exists.")
            else:
                print(f"Error: The file '{file_name}' does not exist in the folder '{selected_folder}'.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
        
        
        
        
    
        
        


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
            delete_folder()
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