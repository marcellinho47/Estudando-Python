import os


def get_txt_files(from_directory):
    return [f for f in os.listdir(from_directory) if f.endswith('.txt')]


def splice_txt_file_by_size(file, max_size):
    with open(file, 'r') as f:
        lines = f.readlines()
        n_lines = len(lines)
        n_files = n_lines // max_size
        n_lines_last_file = n_lines % max_size

        for i in range(n_files):
            with open(file.replace('.txt', f'_{i}.txt'), 'w') as f:
                f.writelines(lines[i * max_size:(i + 1) * max_size])

        if n_lines_last_file > 0:
            with open(file.replace('.txt', f'_{n_files}.txt'), 'w') as f:
                f.writelines(lines[n_files * max_size:])


if __name__ == '__main__':
    from_directory = 'C:\\Users\\marce\\Downloads\\Nova pasta'
    txt_files = get_txt_files(from_directory)
    max_size = 150000

    for file in txt_files:
        file_path = os.path.join(from_directory, file)
        splice_txt_file_by_size(file_path, max_size)
