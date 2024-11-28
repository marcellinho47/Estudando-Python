from pathlib import Path

import pandas as pd
from dotenv import load_dotenv, find_dotenv
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from configs import *

_ = load_dotenv(find_dotenv())

PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'


def importacao_documentos():
    documentos = []
    for arquivo in PASTA_ARQUIVOS.glob('*.*'):
        if arquivo.suffix == '.pdf':  # Carregar PDFs
            loader = PyPDFLoader(str(arquivo))
            documentos_arquivo = loader.load()
            documentos.extend(documentos_arquivo)
        elif arquivo.suffix in ['.xlsx', '.xls']:  # Carregar Excel
            # Carregar o conteúdo de cada planilha em um DataFrame
            xlsx_data = pd.ExcelFile(arquivo)
            for sheet_name in xlsx_data.sheet_names:  # Iterar pelas abas
                df = xlsx_data.parse(sheet_name)
                # Transformar cada linha em um "documento"
                for index, row in df.iterrows():
                    conteudo = " ".join([f"{col}: {val}" for col, val in row.items()])
                    documentos.append({"page_content": conteudo, "source": str(arquivo), "sheet": sheet_name})
    return documentos


def split_de_documentos(documentos):
    recur_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2500,
        chunk_overlap=250,
        separators=["/n\n", "\n", ".", " ", ""]
    )
    documentos = recur_splitter.split_documents(documentos)

    for i, doc in enumerate(documentos):
        doc.metadata['source'] = doc.metadata['source'].split('/')[-1]
        doc.metadata['doc_id'] = i
    return documentos


def cria_vector_store(documentos):
    embedding_model = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(
        documents=documentos,
        embedding=embedding_model
    )
    return vector_store


def cria_chain_conversa():
    documentos = importacao_documentos()
    documentos = split_de_documentos(documentos)
    vector_store = cria_vector_store(documentos)

    chat = ChatOpenAI(model=get_config('model_name'))
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key='chat_history',
        output_key='answer'
    )
    retriever = vector_store.as_retriever(
        search_type=get_config('retrieval_search_type'),
        search_kwargs=get_config('retrieval_kwargs')
    )
    prompt = PromptTemplate.from_template(get_config('prompt'))
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memory,
        retriever=retriever,
        return_source_documents=True,
        verbose=True,
        combine_docs_chain_kwargs={'prompt': prompt}
    )

    st.session_state['chain'] = chat_chain
