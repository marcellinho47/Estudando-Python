import os

from firebird.driver import connect

# Configurações do banco de dados
DB_HOST = "10.0.7.6"  # Substitua pelo endereço do servidor
DB_NAME = "F:\\Data_FB30\\ORIGEM_BRAINVEST.FDB"
DB_USER = "SYSDBA"
DB_PASSWORD = "materkey"
OUTPUT_DIR = "C:\\TEMP"  # Pasta onde os arquivos serão salvos


# Função para salvar os dados em arquivos .txt
def salvar_dados_em_txt(tabela, cabecalho, dados):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    arquivo_txt = os.path.join(OUTPUT_DIR, f"{tabela}.txt")
    with open(arquivo_txt, "w", encoding="utf-8") as f:
        # Escreve o cabeçalho
        f.write("\t".join(cabecalho) + "\n")
        # Escreve os dados
        for linha in dados:
            f.write("\t".join(str(campo) if campo is not None else "" for campo in linha) + "\n")


def main():
    # Conectar ao banco de dados
    con = connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = con.cursor()

    try:
        # Lista todas as tabelas do banco
        cur.execute("SELECT rdb$relation_name FROM rdb$relations WHERE rdb$system_flag = 0 AND rdb$view_blr IS NULL;")
        tabelas = [row[0].strip() for row in cur.fetchall()]

        for tabela in tabelas:
            print(f"Exportando dados da tabela: {tabela}")

            # Obtém o cabeçalho (nomes das colunas)
            cur.execute(
                f'SELECT rdb$field_name FROM rdb$relation_fields WHERE rdb$relation_name = {tabela} ORDER BY rdb$field_position;')
            colunas = [row[0].strip() for row in cur.fetchall()]

            # Consulta os dados da tabela
            cur.execute(f"SELECT * FROM {tabela}")
            dados = cur.fetchall()

            # Salva os dados em um arquivo txt
            salvar_dados_em_txt(tabela, colunas, dados)

        print(f"Exportação concluída. Arquivos salvos na pasta: {OUTPUT_DIR}")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")
    finally:
        cur.close()
        con.close()


if __name__ == "__main__":
    main()
