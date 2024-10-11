import os
import glob


def unify_files(directory, output_file):
    # Get all .d and .txt files in the directory
    files = glob.glob(os.path.join(directory, '*.d')) + glob.glob(os.path.join(directory, '*.txt'))

    with open(output_file, 'w') as outfile:
        for file in files:
            with open(file, 'r') as infile:
                outfile.write(infile.read())


# Example usage
unify_files('C:\\Users\\marcello.alves\\Downloads\\2427014074_folha',
            'C:\\Users\\marcello.alves\\Downloads\\2427014074_folha\\ORIGEM_FOLHA.txt')
