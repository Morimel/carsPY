import os
import shutil

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