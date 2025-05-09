import os

import pandas as pd


def contar_linhas_preenchidas(diretorio):
    resultados = {}

    # Itera sobre todos os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.xlsx') or arquivo.endswith('.xls') or arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(diretorio, arquivo)

            try:
                total_linhas = 0

                if arquivo.endswith('.csv'):
                    # Lê o arquivo CSV
                    df = pd.read_csv(caminho_arquivo)
                    # Conta as linhas preenchidas (não vazias)
                    linhas_preenchidas = df.dropna(how='all').shape[0]
                    total_linhas += linhas_preenchidas
                else:
                    # Lê o arquivo Excel
                    xls = pd.ExcelFile(caminho_arquivo)

                    # Itera sobre todas as planilhas do arquivo
                    for nome_planilha in xls.sheet_names:
                        df = pd.read_excel(xls, sheet_name=nome_planilha)

                        # Conta as linhas preenchidas (não vazias)
                        linhas_preenchidas = df.dropna(how='all').shape[0]
                        total_linhas += linhas_preenchidas

                resultados[arquivo] = total_linhas
            except Exception as e:
                print(f'Erro ao processar o arquivo {arquivo}: {str(e)}')

    return resultados


# Uso
diretorio = 'C:\\Users\\marce\\Downloads'
resultados = contar_linhas_preenchidas(diretorio)

for arquivo, linhas in resultados.items():
    print(f'{arquivo}: {linhas} linhas preenchidas')

total_geral = sum(resultados.values())
print(f'{total_geral} linhas geradas')
