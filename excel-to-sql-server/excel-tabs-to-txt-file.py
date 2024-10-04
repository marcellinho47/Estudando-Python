import pandas as pd


def import_excel_to_sql_server(excel_path):
    # Read the Excel file
    xls = pd.ExcelFile(excel_path)

    # Iterate over each sheet
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)
        sheet_name = sheet_name.replace('PREVIMINAS_001.', '')

        if df.empty:
            print(f'Ignored {sheet_name}.txt')
            continue
        else:
            # Export the DataFrame to a delimited txt file
            df.to_csv(f'C:\\Users\\marcello.alves\\Downloads\\Sinqia\\tabelas\\{sheet_name}.txt', sep='\t',
                      index=False)
            print(f'Exported {sheet_name}.txt')


# Path to the Excel file
excel_path = 'C:\\Users\\marcello.alves\\Downloads\\Sinqia\\excel\\exportar2.xlsx'

import_excel_to_sql_server(excel_path)
