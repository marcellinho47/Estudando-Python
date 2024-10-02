import pandas as pd
from sqlalchemy import create_engine


def import_excel_to_sql_server(excel_path, sql_server_connection_string):
    # Create a connection to the SQL Server
    engine = create_engine(sql_server_connection_string)

    # Read the Excel file
    xls = pd.ExcelFile(excel_path)

    # Iterate over each sheet
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Convert all columns to varchar
        df = df.astype(str)

        sheet_name = sheet_name.replace('PREVIMINAS_001.', '')

        # Import the DataFrame to SQL Server
        df.to_sql(sheet_name, con=engine, if_exists='replace', index=False)
        print(f'Table {sheet_name} imported to SQL Server')


# Example usage
excel_path = 'C:\\Users\\marcello.alves\\Downloads\\Sinqia\\extracao_xlsx_RH\\exportar1.xlsx'
username = 'sa'
password = ''
host = 'localhost'
database = ''
driver = 'ODBC+Driver+17+for+SQL+Server'
instance = 'MSSQLSERVER'

sql_server_connection_string = f'mssql+pyodbc://{username}:{password}@{host}\\{instance}/{database}?driver={driver}'

import_excel_to_sql_server(excel_path, sql_server_connection_string)
