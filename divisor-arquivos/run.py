import os


def get_txt_files(from_directory):
    return [f for f in os.listdir(from_directory) if f.endswith('.csv')]


def splice_txt_file_by_size(file, max_size):
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        file_count = 0
        lines = []
        for line in f:
            lines.append(line)
            if len(lines) >= max_size:
                with open(file.replace('.csv', f'_{file_count}.csv'), 'w', encoding='utf-8') as out_f:
                    out_f.writelines(lines)
                file_count += 1
                lines = []

        if lines:
            with open(file.replace('.csv', f'_{file_count}.csv'), 'w', encoding='utf-8') as out_f:
                out_f.writelines(lines)


if __name__ == '__main__':
    from_directory = 'C:\\TEMP\\'
    txt_files = get_txt_files(from_directory)
    max_size = 700000

    for file in txt_files:
        file_path = os.path.join(from_directory, file)
        splice_txt_file_by_size(file_path, max_size)
