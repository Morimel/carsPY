import os

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