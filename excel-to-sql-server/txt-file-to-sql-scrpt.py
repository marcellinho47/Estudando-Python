import os
import pandas as pd


def get_csv_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]


def analyze_csv_files(directory):
    csv_files = get_csv_files(directory)

    create_tables = ''
    bulkinsert = ''

    for file in csv_files:
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path, sep='\t')
        max_lengths = df.astype(str).map(len).max()

        table_name = file.replace(".txt", "")
        create_tables += f'CREATE TABLE {table_name} (\n'
        for column, length in max_lengths.items():
            create_tables += f'[{column}] VARCHAR({length}),\n'

        create_tables = create_tables[:-2] + '\n)\n\n\n\n'

        with open(os.path.join(directory, 'create-table.txt'), 'w') as f:
            f.write(create_tables)

        bulkinsert += f'BULK INSERT {table_name}\n'
        bulkinsert += f'FROM \'{file_path}\'\n'
        bulkinsert += 'WITH (\n'
        bulkinsert += 'FIELDTERMINATOR = \'\\t\',\n'
        bulkinsert += 'ROWTERMINATOR = \'\\n\',\n'
        bulkinsert += 'FIRSTROW = 2,\n'
        bulkinsert += 'CODEPAGE = \'65001\'\n'
        bulkinsert += ')\n\n\n\n'

        with open(os.path.join(directory, 'bulk-insert.txt'), 'w') as f:
            f.write(bulkinsert)


# Example usage
directory = 'C:\\Users\\marcello.alves\\Downloads\\Sinqia\\tabelas\\'
analyze_csv_files(directory)
