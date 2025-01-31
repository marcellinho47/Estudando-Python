from pathlib import Path
import os


def calculate_folder_size(folder):
    folder = Path(folder)
    total_size = 0

    for path in folder.rglob('*'):
        if path.is_file():
            total_size += os.path.getsize(path)

    return total_size / 1024 / 1024


total_size = calculate_folder_size('C:\\Dev')
print(f'{total_size} MB')
