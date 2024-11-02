import pathlib as Path
import shutil
import os
import time

pasta_atual = Path.Path.cwd()
pasta_destino = Path.Path.cwd() / 'pasta_destino/'

# Copiar um arquivo
shutil.copy(pasta_atual / 'arquivo1.txt', pasta_destino)

# Copiar um arquivo com metadados
shutil.copy2(pasta_atual / 'arquivo2.txt', pasta_destino)

# Mover um arquivo
shutil.move(pasta_atual / 'arquivo3.txt', pasta_destino)

time.sleep(3)

# Deletar um arquivo
os.remove(pasta_destino / 'arquivo1.txt')
os.remove(pasta_destino / 'arquivo2.txt')
