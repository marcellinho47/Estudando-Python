import pathlib as Path
import shutil
import os

pasta_atual = Path.Path.cwd()

pasta_destino = Path.Path.cwd() / 'pasta_destino/'

# Criar uma pasta
pasta_destino1 = Path.Path.cwd() / 'pasta_destino1/'
pasta_destino1.mkdir(exist_ok=True)

# Criar pasta com subpastas
pasta_destino2 = Path.Path.cwd() / 'pasta_destino2/' / 'subpasta_destino/'
pasta_destino2.mkdir(parents=True, exist_ok=True)

# Mover uma pasta
shutil.copytree(pasta_destino2, pasta_destino / 'subpasta_destino', dirs_exist_ok=True)

# Deletar uma pasta vazia
os.rmdir(pasta_destino / 'subpasta_destino')

# Deletar uma pasta com arquivos
shutil.rmtree(pasta_destino2)
