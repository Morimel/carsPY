import os

# Common function for returning list of folders
def list_folders():
    return [f for f in os.listdir() if os.path.isdir(f)]

# Commonn function for returning list of files in folders
def list_files_in_folder(folder):
    """Возвращает список файлов в указанной папке."""
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]