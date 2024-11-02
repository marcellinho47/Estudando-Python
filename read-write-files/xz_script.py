import lzma
import shutil
from pathlib import Path


def compress_with_xz(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with lzma.open(output_file, 'wb', preset=9 | lzma.PRESET_EXTREME) as f_out:
            shutil.copyfileobj(f_in, f_out)


input_file = Path.cwd() / 'pasta_para_compactar/1.CR3'
output_file = Path.cwd() / 'pasta_para_compactar/compressed_file.tar.xz'
compress_with_xz(input_file, output_file)
