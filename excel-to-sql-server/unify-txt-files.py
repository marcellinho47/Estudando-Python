import os
import re


def read_text_with_fallback(file_path):
    with open(file_path, 'rb') as f:
        raw = f.read()
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError:
        # Fallback for ANSI (Windows-1252) source files
        return raw.decode('cp1252', errors='replace')


def unify_txt_files(from_directory, to_directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(to_directory):
        os.makedirs(to_directory)

    # Group files by the name after the last underscore (without extension)
    groups = {}
    for root, _, files in os.walk(from_directory):
        for filename in files:
            match = re.match(r'^.+_(.+)\.[^.]+$', filename)
            if match:
                group_name = match.group(1)
            else:
                group_name = os.path.splitext(filename)[0]
            groups.setdefault(group_name, []).append(os.path.join(root, filename))

    # Write each group to a unified txt file
    for group_name, file_paths in groups.items():
        txt_file_path = os.path.join(to_directory, f'{group_name}.txt')
        try:
            with open(txt_file_path, 'w', encoding='utf-8') as outfile:
                for file_path in file_paths:
                    try:
                        text = read_text_with_fallback(file_path)
                        for line in text.splitlines():
                            outfile.write(line + '\n')
                    except Exception as e:
                        print(f'Error reading {file_path}: {str(e)}')
            print(f'Unified {len(file_paths)} file(s) into {group_name}.txt')
        except Exception as e:
            print(f'Error writing {group_name}.txt: {str(e)}')


# Usage
from_directory = 'C:\\TEMP\\'
to_directory = 'C:\\TEMP G\\'
unify_txt_files(from_directory, to_directory)
