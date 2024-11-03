from pathlib import Path

print(Path.home())

print(Path.exists(Path('../book-review/resources/customer reviews.csv')))

# Working directory
print(Path.cwd())

# caminho atual do arquivo
print(__file__)

# caminho da pasta do arquivo
print(Path(__file__).resolve().parent)

# Operacoes com o nome do arquivo
print(Path.home().anchor)
print(type(Path.home()))

this_file = Path(__file__)

print(this_file.name)
print(this_file.stem)
print(this_file.suffix)
print(this_file.drive)

# retornar o conteudo de um pasta
print(list(Path.cwd().parent.glob('*')))
# retornar o conteudo de um pasta e das sub pastas
print(list(Path.cwd().parent.glob('**/*')))
