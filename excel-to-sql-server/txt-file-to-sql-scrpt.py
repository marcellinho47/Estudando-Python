import os
import pandas as pd
import gc


def get_csv_files(from_directory):
    return [f for f in os.listdir(from_directory) if f.endswith('.txt')]


def analyze_csv_files(from_directory, to_directory, separator):
    csv_files = get_csv_files(from_directory)

    create_tables = ''
    bulkinsert = ''

    for file in csv_files:
        print(f"Processando arquivo: {file}")
        file_path = os.path.join(from_directory, file)
        
        # Análise incremental usando chunks
        max_lengths = {}
        chunk_size = 50000
        total_rows = 0
        
        try:
            # Processar arquivo em chunks
            chunk_reader = pd.read_csv(file_path, sep=separator, dtype=str, 
                                     encoding='utf-8', chunksize=chunk_size,
                                     on_bad_lines='skip')
            
            for chunk_num, chunk in enumerate(chunk_reader, 1):
                print(f"  Processando chunk {chunk_num} ({len(chunk)} linhas)")
                
                # Calcular comprimentos máximos para este chunk
                chunk_max_lengths = chunk.astype(str).applymap(len).max()
                
                # Atualizar comprimentos máximos globais
                for column, length in chunk_max_lengths.items():
                    if pd.isna(length):
                        length = 0
                    max_lengths[column] = max(max_lengths.get(column, 0), int(length))
                
                total_rows += len(chunk)
                
                # Liberar memória
                del chunk
                gc.collect()
            
            print(f"  Total de linhas processadas: {total_rows}")
            
        except Exception as e:
            print(f"Erro ao processar {file}: {e}")
            continue

        table_name = file.replace(".txt", "")
        create_tables += f'CREATE TABLE {table_name} (\n'
        for column, length in max_lengths.items():
            create_tables += f'[{column}] VARCHAR({length + 20}),\n'

        create_tables = create_tables[:-2] + '\n)\n\n\n\n'

        with open(os.path.join(to_directory, 'create-table.txt'), 'w') as f:
            f.write(create_tables)

        if separator.startswith('\\'):
            separator = '\\' + separator

        bulkinsert += f'BULK INSERT {table_name}\n'
        bulkinsert += f'FROM \'{file_path}\'\n'
        bulkinsert += 'WITH (\n'
        bulkinsert += 'FIELDTERMINATOR = \'' + separator + '\',\n'
        bulkinsert += 'ROWTERMINATOR = \'\\n\',\n'
        bulkinsert += 'FIRSTROW = 2,\n'
        bulkinsert += 'CODEPAGE = \'65001\'\n'  # UTF-8
        # bulkinsert += 'CODEPAGE = \'ACP\'\n'  # ANSI
        bulkinsert += ')\n\n\n\n'

        with open(os.path.join(to_directory, 'bulk-insert.txt'), 'w') as f:
            f.write(bulkinsert)


# Example usage
from_directory = 'C:\\TEMP\\'
to_directory = 'C:\\TEMP G\\'
separator = ';'
analyze_csv_files(from_directory, to_directory, separator)
