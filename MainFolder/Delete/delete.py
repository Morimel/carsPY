import os
import shutil

def list_folders(directory):
    """Возвращает список папок в указанном каталоге."""
    return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]


def list_files_in_folder(folder):
    """Возвращает список файлов в указанной папке."""
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

BUCKET_PATH = 'bucket'

# Путь к CarsID файлу
CARS_ID_FILE = 'CarsID.txt'

def delete_folder(folder_path):
    """Удаляет папку и записывает путь в bucket в .txt файл."""
    if os.path.exists(folder_path):
        # Удаляем папку со всеми файлами
        shutil.rmtree(folder_path)
        print(f"Папка {folder_path} удалена.")
        
        # Записываем путь к удалённой папке в bucket
        if not os.path.exists(BUCKET_PATH):
            os.makedirs(BUCKET_PATH)
        
        with open(os.path.join(BUCKET_PATH, 'deleted_folders.txt'), 'a') as f:
            f.write(f"Deleted folder: {folder_path}\n")
    else:
        print("Папка не найдена.")
        
def delete_file(file_path, car_id):
    """Удаляет файл и обновляет CarsID."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл {file_path} удален.")
        
        # Обновляем CarsID.txt, удаляя соответствующий идентификатор авто
        if os.path.exists(CARS_ID_FILE):
            with open(CARS_ID_FILE, 'r') as f:
                lines = f.readlines()

            with open(CARS_ID_FILE, 'w') as f:
                for line in lines:
                    if car_id not in line:
                        f.write(line)
            print(f"Car ID {car_id} удален из {CARS_ID_FILE}.")
        else:
            print("Файл CarsID не найден.")
    else:
        print("Файл не найден.")
        
def delete_folder_or_file():
    # Выбор базовой директории
    base_dir = input("Введите путь к каталогу для поиска: ").strip()

    # Получаем список папок и файлов
    folders = list_folders(base_dir)
    files = []
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        folder_files = list_files_in_folder(folder_path)
        files.extend([os.path.join(folder, file) for file in folder_files])

    # Если папки найдены, выводим их список
    if folders:
        print("\n--- Список папок ---")
        for idx, folder in enumerate(folders):
            print(f"{idx + 1}. {folder}")
    
    # Если файлы найдены, выводим их список
    if files:
        print("\n--- Список файлов ---")
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
    
    # Пользователь вводит название папки или файла
    item_to_delete = input("\nВведите название папки или файла для удаления: ").strip()

    # Проверяем, папка это или файл, и выполняем удаление
    if item_to_delete in folders:
        # Удаляем папку
        folder_path = os.path.join(base_dir, item_to_delete)
        delete_folder(folder_path)
    elif any(item_to_delete in file for file in files):
        # Удаляем файл
        selected_file = next(file for file in files if item_to_delete in file)
        file_path = os.path.join(base_dir, selected_file)
        car_id = input("Введите Car ID для удаления из CarsID: ").strip()
        delete_file(file_path, car_id)
    else:
        print("Указанная папка или файл не найдены.")