import tarfile
from pathlib import Path
import os


def compress_with_gzip(input_file, output_file):
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(input_file, arcname=os.path.basename(input_file))


input_file = Path.cwd() / 'pasta_para_compactar/1.CR3'
output_file = Path.cwd() / 'pasta_para_compactar/compressed_file.tar.gz'
compress_with_gzip(input_file, output_file)
