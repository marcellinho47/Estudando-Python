import sys
from typing import List, Dict, Any

import pyodbc


def conectar_sql_server(servidor: str, banco: str, usuario: str = None, senha: str = None) -> pyodbc.Connection:
    """
    Cria uma conexão com o SQL Server usando autenticação Windows ou SQL Server.
    """
    try:
        if usuario and senha:
            string_conexao = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={servidor};DATABASE={banco};UID={usuario};PWD={senha}"
        else:
            string_conexao = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={servidor};DATABASE={banco};Trusted_Connection=yes"

        conexao = pyodbc.connect(string_conexao)
        print(f"Conexão bem-sucedida ao banco de dados '{banco}' no servidor '{servidor}'")
        return conexao
    except pyodbc.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        sys.exit(1)


def obter_todas_tabelas(conexao: pyodbc.Connection) -> List[str]:
    """
    Obtém todas as tabelas do banco de dados.
    """
    cursor = conexao.cursor()
    try:
        # Consulta para obter todas as tabelas (excluindo views)
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE'
            ORDER BY TABLE_NAME
        """)
        tabelas = [row.TABLE_NAME for row in cursor.fetchall()]
        print(f"Encontradas {len(tabelas)} tabelas no banco de dados")
        return tabelas
    except pyodbc.Error as e:
        print(f"Erro ao obter tabelas: {e}")
        return []
    finally:
        cursor.close()


def obter_colunas_tabela(conexao: pyodbc.Connection, tabela: str) -> List[str]:
    """
    Obtém todas as colunas de uma tabela específica.
    """
    cursor = conexao.cursor()
    try:
        cursor.execute(f"""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = '{tabela}'
            ORDER BY ORDINAL_POSITION
        """)
        colunas = [row.COLUMN_NAME for row in cursor.fetchall()]
        return colunas
    except pyodbc.Error as e:
        print(f"Erro ao obter colunas da tabela {tabela}: {e}")
        return []
    finally:
        cursor.close()


def buscar_valor(conexao: pyodbc.Connection, tabela: str, colunas: List[str], valor: str) -> List[Dict[str, Any]]:
    """
    Busca um valor específico em todas as colunas de uma tabela.
    """
    resultados = []
    cursor = conexao.cursor()

    for coluna in colunas:
        try:
            # Criando a consulta para buscar o valor na coluna
            query = f"""
                SELECT * 
                FROM [{tabela}] 
                WHERE CONVERT(NVARCHAR(MAX), [{coluna}]) LIKE ?
            """

            cursor.execute(query, f'%{valor}%')
            rows = cursor.fetchall()

            if rows:
                print(f"Encontrado valor em {tabela}.{coluna}: {len(rows)} ocorrências")
                for row in rows:
                    row_dict = {}
                    # Converter a linha em um dicionário
                    for i, col in enumerate(cursor.description):
                        row_dict[col[0]] = row[i]

                    resultados.append({
                        'tabela': tabela,
                        'coluna': coluna,
                        'valores': row_dict
                    })
        except pyodbc.Error as e:
            print(f"Erro ao buscar na tabela {tabela}, coluna {coluna}: {e}")

    cursor.close()
    return resultados


def buscar_valor_em_todas_tabelas(conexao: pyodbc.Connection, valor: str) -> List[Dict[str, Any]]:
    """
    Busca um valor em todas as tabelas e colunas do banco de dados.
    """
    tabelas = obter_todas_tabelas(conexao)
    todos_resultados = []

    total_tabelas = len(tabelas)
    for i, tabela in enumerate(tabelas):
        print(f"Processando tabela {i + 1}/{total_tabelas}: {tabela}")
        colunas = obter_colunas_tabela(conexao, tabela)
        resultados = buscar_valor(conexao, tabela, colunas, valor)
        todos_resultados.extend(resultados)

    return todos_resultados


def exibir_resultados(resultados: List[Dict[str, Any]]):
    """
    Exibe os resultados da busca.
    """
    if not resultados:
        print("Nenhum resultado encontrado.")
        return

    print(f"\n{'=' * 80}")
    print(f"Total de ocorrências encontradas: {len(resultados)}")
    print(f"{'=' * 80}")

    for i, resultado in enumerate(resultados):
        print(f"\nResultado {i + 1}:")
        print(f"Tabela: {resultado['tabela']}")


def main():
    # Conectar ao banco de dados
    conexao = conectar_sql_server('host', 'database', 'user', 'password')

    try:
        # Buscar o valor em todas as tabelas
        resultados = buscar_valor_em_todas_tabelas(conexao, 'MENSAL')

        # Exibir os resultados
        exibir_resultados(resultados)

    finally:
        # Fechar a conexão
        conexao.close()
        print("\nConexão fechada.")


if __name__ == "__main__":
    main()
