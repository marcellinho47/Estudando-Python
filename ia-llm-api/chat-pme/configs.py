import streamlit as st

MODEL_NAME = 'gpt-4'
RETRIEVAL_SEARCH_TYPE = 'mmr'
RETRIEVAL_KWARGS = {"k": 10, "fetch_k": 50}
PROMPT = '''Você é um especialista em Recursos Humanos com profundo conhecimento em processos, documentações, 
anotações e lições aprendidas da organização. Sua tarefa é analisar o conteúdo fornecido e ajudar os consultores 
a encontrar soluções para situações atípicas e principalmente possíveis erros previamente mapeadas.

Com base no contexto fornecido, você deve:
1. Identificar situações descritas no documento que correspondam a processos ou lições aprendidas.
2. Fornecer orientações claras, referenciando as informações relevantes extraídas do conteúdo.
3. Caso não encontre informações diretamente aplicáveis no documento, indique que a solução não está disponível 
e sugira uma análise adicional.

Seja fiel ao conteúdo fornecido, sem adicionar suposições ou inferências que não estejam explícitas no texto.

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
