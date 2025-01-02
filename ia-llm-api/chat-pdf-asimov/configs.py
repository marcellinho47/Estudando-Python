import streamlit as st

MODEL_NAME = 'gpt-3.5-turbo-0125'
RETRIEVAL_SEARCH_TYPE = 'mmr'
RETRIEVAL_KWARGS = {"k": 8, "fetch_k": 40}
PROMPT = '''As secretárias médicas precisam anotar os resultado de exames dos pacientes.

Você é um especialista em interpretação de exames médicos fornecidos pela secretária. 
Sua tarefa é extrair exclusivamente o nome de cada exame e seu respectivo resultado, 
sem inferir informações além do que está no exame fornecido. 
Seja fiel ao conteúdo fornecido, e, caso não encontre um exame ou resultado, 
indique claramente que a informação não está presente. 

Primeiro, verifique todos os exames contidos no laudo, extraia o nome do exame e o resultado do exame. Adicione-os a uma lista de dicionários, verifique se não há erros e retorne o resultado.

Retorne os dados em lista de dicionários, onde cada dicionário tem as chaves 'exame' e 'resultado'.

Contexto:
{context}

Conversa atual:
{chat_history}
Human: {question}
AI: '''


def get_config(config_name):
    if config_name.lower() in st.session_state:
        return st.session_state[config_name.lower()]
    elif config_name.lower() == 'model_name':
        return MODEL_NAME
    elif config_name.lower() == 'retrieval_search_type':
        return RETRIEVAL_SEARCH_TYPE
    elif config_name.lower() == 'retrieval_kwargs':
        return RETRIEVAL_KWARGS
    elif config_name.lower() == 'prompt':
        return PROMPT
