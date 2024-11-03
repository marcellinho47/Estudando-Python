import pathlib as Path
import shutil

pasta_compactar = Path.Path.cwd() / 'pasta_para_compactar/'
pasta_compactada = Path.Path.cwd() / 'pasta_para_compactada'

# Create a ZIP archive
shutil.make_archive(pasta_compactada, 'zip', pasta_compactar)

# Create a gzip compressed tar archive
shutil.make_archive(pasta_compactada, 'gztar', pasta_compactar)

# Create a bzip2 compressed tar archive
shutil.make_archive(pasta_compactada, 'bztar', pasta_compactar)

# Create an xz compressed tar archive
shutil.make_archive(pasta_compactada, 'xztar', pasta_compactar)
