import os
import pandas as pd


def import_excel_to_txt(from_directory, to_directory):
    # Iterate over each Excel file in the directory
    for filename in os.listdir(from_directory):
        if filename.endswith('.xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
            excel_path = os.path.join(from_directory, filename)

            clean_filename = os.path.splitext(filename)[0]

            if filename.endswith('.csv'):
                xls = pd.read_csv(excel_path, dtype=str)
                sheet_names = [os.path.splitext(filename)[0]]
                df = xls.map(lambda x: x.replace('\t', '') if isinstance(x, str) else x)

                if df.empty:
                    print(f'Ignored {clean_filename}.txt from {filename}')
                    continue
                else:
                    # Export the DataFrame to a delimited txt file
                    txt_file_path = os.path.join(to_directory, f'{clean_filename}.txt')
                    df.to_csv(txt_file_path, sep='\t', index=False, encoding='ansi')
                    print(f'Exported {clean_filename}.txt from {filename}')

            else:
                xls = pd.ExcelFile(excel_path)
                sheet_names = xls.sheet_names

                # Iterate over each sheet
                for sheet_name in sheet_names:
                    df = pd.read_excel(xls, sheet_name=sheet_name).map(
                        lambda x: x.replace('\t', '') if isinstance(x, str) else x)

                    if df.empty:
                        print(f'Ignored {clean_filename}.txt from {filename}')
                        continue
                    else:
                        # Export the DataFrame to a delimited txt file
                        txt_file_path = os.path.join(to_directory, f'{clean_filename}.txt')
                        df.to_csv(txt_file_path, sep='\t', index=False, encoding='ansi')
                        print(f'Exported {clean_filename}.txt from {filename}')


# Usage
from_directory = 'C:\\Users\\marcello.alves\\Downloads\\Anton Paar'
to_directory = 'C:\\Users\\marcello.alves\\Downloads\\Anton Paar TXT'
import_excel_to_txt(from_directory, to_directory)
