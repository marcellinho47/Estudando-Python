from pathlib import Path

import streamlit as st

PDFS_UPLOADS = Path.cwd() / 'pdfs_uploads'


def create_chain():
    print('create_chain')
    pass


def get_last_pdf_uploaded_seq():
    pdfs = PDFS_UPLOADS.glob('*.pdf')
    pdfs = sorted(pdfs, key=lambda x: x.stat().st_ctime, reverse=True)
    last_pdf = pdfs[0] if pdfs else None

    if last_pdf:
        return int(last_pdf.stem.split('.')[0])
    else:
        return 0


def create_folder():
    if not PDFS_UPLOADS.exists():
        PDFS_UPLOADS.mkdir()


def save_uploaded_file(uploaded_file):
    create_folder()
    last_pdf_uploaded_seq = get_last_pdf_uploaded_seq()
    last_pdf_uploaded_seq += 1
    open(PDFS_UPLOADS / f'{last_pdf_uploaded_seq}.pdf', 'wb').write(uploaded_file.getbuffer())


def sidebar():
    uploaded_pdf = st.file_uploader('Selecione o arquivo PDF', type='pdf')

    if not uploaded_pdf is None:
        save_uploaded_file(uploaded_pdf)

        st.button('Processar PDF', use_container_width=True, on_click=create_chain)


def app():
    with st.sidebar:
        sidebar()

    pass


if __name__ == '__main__':
    app()
