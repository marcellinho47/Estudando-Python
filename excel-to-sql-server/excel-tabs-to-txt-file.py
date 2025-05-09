import os
import pandas as pd


def import_excel_to_txt(from_directory, to_directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(to_directory):
        os.makedirs(to_directory)

    # Iterate over each Excel file in the directory
    for filename in os.listdir(from_directory):
        if filename.endswith('.xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
            excel_path = os.path.join(from_directory, filename)

            clean_filename = os.path.splitext(filename)[0]

            # CSV Files
            if filename.endswith('.csv'):
                try:
                    xls = pd.read_csv(excel_path, dtype=str)
                    sheet_names = [os.path.splitext(filename)[0]]
                    df = xls.map(lambda x: x.replace('\t', '') if isinstance(x, str) else x)

                    if df.empty:
                        print(f'Ignored {clean_filename}.txt from {filename}')
                        continue
                    else:
                        # Export the DataFrame to a delimited txt file
                        txt_file_path = os.path.join(to_directory, f'{clean_filename}.txt')
                        df.to_csv(txt_file_path, sep='\t', index=False, encoding='utf-8', errors='replace')
                        print(f'Exported {clean_filename}.txt from {filename}')
                except Exception as e:
                    print(f'Error processing {filename}: {str(e)}')

            # Excel Files
            else:
                try:
                    xls = pd.ExcelFile(excel_path)
                    sheet_names = xls.sheet_names

                    # Iterate over each sheet
                    for sheet_name in sheet_names:
                        try:
                            df = pd.read_excel(xls, sheet_name=sheet_name).fillna('').astype(str).map(
                                lambda x: x.replace('\t', '') if isinstance(x, str) else x).map(
                                lambda x: x.replace('\n', '') if isinstance(x, str) else x).map(
                                lambda x: x.replace('\r\n', '') if isinstance(x, str) else x)

                            if df.empty:
                                print(f'Ignored {sheet_name}.txt from {sheet_name}')
                                continue
                            else:
                                # Export the DataFrame to a delimited txt file
                                txt_file_path = os.path.join(to_directory, f'{sheet_name}.txt')
                                df.to_csv(txt_file_path, sep='\t', index=False, encoding='utf-8')
                                print(f'Exported {sheet_name}.txt from {sheet_name}')
                        except Exception as e:
                            print(f'Error processing sheet {sheet_name} in {filename}: {str(e)}')
                except Exception as e:
                    print(f'Error opening {filename}: {str(e)}')


# Usage
from_directory = 'C:\\TEMP G'
to_directory = 'C:\\TEMP'
import_excel_to_txt(from_directory, to_directory)
