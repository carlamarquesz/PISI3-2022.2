import streamlit as st
import pandas as pd
from utils import *
from data_dict.dicionario_dados import *
from graphics import *

st.set_page_config(layout="wide")

def ler_dados():
    dados = pd.read_csv("./data/credit_card_approval.csv")
    return dados

@st.cache_data
def converter_para_csv(df):
    return df.to_csv(index=False).encode("utf-8")

def exibir_tabela_e_botao_download(df, titulo):
    st.markdown(titulo)
    st.write(df) 
    st.markdown(f"A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas")
    st.subheader("Faça o download da Tabela")
    st.markdown("Escolha um nome para o arquivo")
    col1, col2 = st.columns(2)
    with col1:
        nome_arquivo = st.text_input("", label_visibility="collapsed", value="dados") + ".csv"
    with col2:
        df_download = ler_dados()
        st.download_button(
            "Baixar a tabela em formato CSV",
            data=converter_para_csv(df_download),
            file_name=nome_arquivo,
            mime="text/csv",
        )

def exibir_dados_ml(titulo):
    st.markdown(titulo)
    st.write(df)
    st.markdown(f"A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas")

def exibir_dicionario_dados():
    st.subheader("Dicionário de Dados")
    df_dicionario = pd.DataFrame(
        dicionario_dados,
        columns=[
            "Column",
            "Coluna",
            "Tipo de dado",
            "Descrition",
            "Descrição",
        ],
    )
    st.dataframe(df_dicionario, use_container_width=True)

def main():
    df = ler_dados()

    st.subheader("Base de Dados")
    aba1, aba2, aba3 = st.tabs(["Dados Qualitativos e Quantitativos", "Dados para Machine Learning", "Dicionário de Dados"])

    with aba1:
        exibir_tabela_e_botao_download(df, 'Dados das pessoas que solicitaram análise de crédito')

    with aba2:
        exibir_dados_ml('Dados das pessoas que solicitaram análise de crédito')

    with aba3:
        exibir_dicionario_dados()

if __name__ == "__main__":      
    main()
