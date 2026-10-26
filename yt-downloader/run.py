import os
import shutil
import sys

import yt_dlp


def download_audio(url, output_directory):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    # Converte para mp3 apenas se o ffmpeg estiver instalado
    if shutil.which('ffmpeg'):
        options['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        print('ffmpeg nao encontrado: o audio sera salvo no formato original (m4a/webm).')

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else input('URL do YouTube: ').strip()
    output_directory = sys.argv[2] if len(sys.argv) > 2 else 'downloads'

    os.makedirs(output_directory, exist_ok=True)
    try:
        download_audio(url, output_directory)
    except yt_dlp.utils.DownloadError:
        sys.exit('Falha no download (detalhes acima).')
