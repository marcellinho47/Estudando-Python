from pathlib import Path
import pyzipper


def compress_file_zip(input_file, output_file):
    with pyzipper.AESZipFile(output_file, 'w', compression=pyzipper.ZIP_LZMA) as zf:
        zf.write(input_file, compress_type=pyzipper.ZIP_LZMA)


input_file = Path.cwd() / 'pasta_para_compactar/1.CR3'
output_file = Path.cwd() / 'pasta_para_compactar/compressed_file.zip'
compress_file_zip(input_file, output_file)
