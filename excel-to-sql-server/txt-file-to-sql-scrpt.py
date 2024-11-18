import os
import pandas as pd


def get_csv_files(from_directory):
    return [f for f in os.listdir(from_directory) if f.endswith('.txt') or f.endswith('.csv')]


def analyze_csv_files(from_directory, to_directory):
    csv_files = get_csv_files(from_directory)

    create_tables = ''
    bulkinsert = ''

    for file in csv_files:
        file_path = os.path.join(from_directory, file)
        df = pd.read_csv(file_path, sep=';', dtype=str, encoding='ansi')
        max_lengths = df.astype(str).map(len).max()

        table_name = file.replace(".txt", "").replace(".csv", "")
        create_tables += f'CREATE TABLE {table_name} (\n'
        for column, length in max_lengths.items():
            create_tables += f'[{column}] VARCHAR({length}),\n'

        create_tables = create_tables[:-2] + '\n)\n\n\n\n'

        with open(os.path.join(to_directory, 'create-table.txt'), 'w') as f:
            f.write(create_tables)

        bulkinsert += f'BULK INSERT {table_name}\n'
        bulkinsert += f'FROM \'{file_path}\'\n'
        bulkinsert += 'WITH (\n'
        bulkinsert += 'ROWTERMINATOR = \'\\n\',\n'
        bulkinsert += 'FIELDTERMINATOR = \'\\t\',\n'
        bulkinsert += 'FIRSTROW = 2,\n'
#       bulkinsert += 'CODEPAGE = \'ACP\'\n'    # ANSI
        bulkinsert += 'CODEPAGE = \'65001\'\n'  # UTF-8
        bulkinsert += ')\n\n\n\n'

        with open(os.path.join(to_directory, 'bulk-insert.txt'), 'w') as f:
            f.write(bulkinsert)


# Example usage
from_directory = 'C:\\Sharepoint\\OneDrive\\Downloads\\bluefit'
to_directory = 'C:\\Sharepoint\\OneDrive\\Downloads\\bluefit scripts\\'
analyze_csv_files(from_directory, to_directory)
