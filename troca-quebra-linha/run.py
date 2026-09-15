import os


def get_txt_files(from_directory):
    return [f for f in os.listdir(from_directory) if f.endswith('.bcp')]


def convert_line_endings(file):
    with open(file, 'rb') as f:
        content = f.read()

    content = content.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')

    with open(file, 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    from_directory = 'C:\\TEMP\\'
    txt_files = get_txt_files(from_directory)

    for file in txt_files:
        file_path = os.path.join(from_directory, file)
        convert_line_endings(file_path)
