import streamlit as st 
import pandas as pd 
from utils import *
from graphics import * 
st.set_page_config(layout= 'wide')
#Fazer o dowload do dataset
@st.cache_data
def converte_csv(df):
    return df.to_csv(index = False).encode('utf-8') 
 
st.subheader("Database")
aba1, aba2, aba3 = st.tabs(["Qualitativos e Numéricos", "Dados para ML", "Dicionário de dados"])
#Dados qualitativos e quantitativos
with aba1: 
    st.markdown('Dados de pessoas que solicitaram análise de crédito') 
    st.write(pd.read_csv("./data/credit_card_approval.csv"))
    st.markdown(f'A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas')  
    st.subheader("Faça o download da Database") 
    st.markdown('Escreva um nome para o arquivo')
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        nome_arquivo = st.text_input('', label_visibility = 'collapsed', value = 'dados')
        nome_arquivo += '.csv'
    with coluna2:
        st.download_button('Fazer o download da tabela em csv', data = converte_csv(df), file_name = nome_arquivo, mime = 'text/csv')
#Dados tratados para ML
with aba2:  
    st.markdown('Dados de pessoas que solicitaram análise de crédito') 
    st.write(df)  
    st.markdown(f'A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas') 
#Dicionário de dados
with aba3:  
    st.subheader("Dicionário de dados")  
    dicionario_dados = {
        "ID": "Client number",
        "CODE_GENDER": "Gender",
        "FLAG_OWN_CAR": "Is there a car",
        "FLAG_OWN_REALTY": "Is there a property",
        "CNT_CHILDREN": "Number of children",
        "AMT_INCOME_TOTAL": "Annual income",
        "NAME_INCOME_TYPE": "Income category",
        "NAME_EDUCATION_TYPE": "Education level",
        "NAME_FAMILY_STATUS": "Marital status",
        "NAME_HOUSING_TYPE": "Way of living",
        "DAYS_BIRTH": "Birthday - Count backwards from current day (0), -1 means yesterday",
        "DAYS_EMPLOYED": "Start date of employment (Count backwards from current day(0). If positive, it means the person currently unemployed.)",
        "FLAG_MOBIL": "Is there a mobile phone",
        "FLAG_WORK_PHONE": "Is there a work phone",
        "FLAG_PHONE": "Is there a phone",
        "FLAG_EMAIL": "Is there an email",
        "OCCUPATION_TYPE": "Occupation",
        "CNT_FAM_MEMBERS": "Family size"
    } 
    df_dicionario = pd.DataFrame(dicionario_dados.items(), columns=["Coluna", "Descrição"]) 
    st.dataframe(df_dicionario,use_container_width=True)

