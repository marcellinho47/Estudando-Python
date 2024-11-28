import streamlit as st

MODEL_NAME = 'gpt-4'
RETRIEVAL_SEARCH_TYPE = 'mmr'
RETRIEVAL_KWARGS = {"k": 5, "fetch_k": 20}
PROMPT = '''Você é um especialista em interpretação de exames médicos fornecidos pelo usuário. 
Sua tarefa é extrair exclusivamente o nome de cada exame e seu respectivo resultado, 
sem inferir informações além do que está no documento. 
Seja fiel ao conteúdo fornecido, e, caso não encontre um exame ou resultado, 
indique claramente que a informação não está presente. 
Não invente valores em hipótese alguma.
Traga o resultado dos exames em uma tabela, com o nome do exame na primeira coluna e o resultado na segunda.


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
