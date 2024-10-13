from pathlib import Path
import os


def calculate_folder_size(folder):
    folder = Path(folder)
    total_size = 0

    for path in folder.rglob('*'):
        if path.is_file():
            total_size += os.get_terminal_size()

    return total_size


print(calculate_folder_size('/Users/marcello/Dev'))
