import streamlit as st
import pandas as pd
from utils import *
from graphics import *

st.set_page_config(layout="wide")


# Fazer o dowload do dataset
@st.cache_data
def converte_csv(df):
    return df.to_csv(index=False).encode("utf-8")


st.subheader("Database")
aba1, aba2, aba3 = st.tabs(
    ["Qualitativos e Numéricos", "Dados para ML", "Dicionário de dados"]
)
# Dados qualitativos e quantitativos
with aba1:
    st.markdown("Dados de pessoas que solicitaram análise de crédito")
    st.write(pd.read_csv("./data/credit_card_approval.csv"))
    st.markdown(
        f"A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas"
    )
    st.subheader("Faça o download da Database")
    st.markdown("Escreva um nome para o arquivo")
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        nome_arquivo = st.text_input("", label_visibility="collapsed", value="dados")
        nome_arquivo += ".csv"
    with coluna2:
        st.download_button(
            "Fazer o download da tabela em csv",
            data=converte_csv(df),
            file_name=nome_arquivo,
            mime="text/csv",
        )
# Dados tratados para ML
with aba2:
    st.markdown("Dados de pessoas que solicitaram análise de crédito")
    st.write(df)
    st.markdown(
        f"A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas"
    )
# Dicionário de dados
with aba3:
    st.subheader("Dicionário de dados")

    dicionario_dados = {
        "Column":[
                    "ID",
                    "CODE_GENDER",
                    "FLAG_OWN_CAR",
                    "FLAG_OWN_REALTY",
                    "CNT_CHILDREN", 
                    "AMT_INCOME_TOTAL",
                    "NAME_EDUCATION_TYPE ",
                    "NAME_FAMILY_STATUS",
                    "NAME_HOUSING_TYPE",
                    "DAYS_BIRTH",
                    "DAYS_EMPLOYED", 
                    "FLAG_MOBIL", 
                    "FLAG_WORK_PHONE", 
                    "FLAG_PHONE",
                    "FLAG_EMAIL",
                    "OCCUPATION_TYPE",
                    "BEGIN_MONTHS", 
                    "STATUS", 
                    "TARGET"
                    ],
        
        "Coluna": [
                        "ID",
                        "GENERO",
                        "POSSUI_CARRO",
                        "POSSUI_PROPRIEDADES",
                        "QTD_FILHOS",
                        "Valor total de renda",
                        "ESCOLARIDADE", 
                        "ESTADO_CIVIL", 
                        "TIPO_DE_MORADIA",
                        "DIAS_ANIVERSARIO", 
                        "POSSUI_EMPREGO",
                        "CELULAR",
                        "TELEFONE_COMERCIAL", 
                        "TELEFONE_RESIDENCIAL", 
                        "EMAIL", 
                        "CARGO",
                        "QTD_MESES", 
                        "STATUS_PAGAMENTO", 
                        "TARGET"
                    ],
                    
        "Tipo do dado":[
                        "Float",
                        "Int",
                        "Int",
                        "Int",
                        "Int",
                        "Int",
                        "Float",
                        "Int",
                        "Int",
                        "Float",
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int"
                    ],

        "Descrition" :
                     [
                       "ID",
                       "Gender", 
                       "Is there a car", 
                       "Is there a property", 
                       "Number of children", 
                       "Annual income",   
                       "Education level", 
                       "Marital status", 
                       "Way of living", 
                       "Age in days",
                       "Duration of work in days",
                       "Is there a mobile phone",
                       "Is there a work phone", 
                       "Is there a phone",
                       "Is there an email",
                       "Job",
                       "Record month: Record month: The month of the extracted data is the starting point, backwards, 0 is the current month, -1 is the previous month, and so on",
                       "Status 0: 1-29 days past due 1: 30-59 days past due 2: 60-89 days overdue 3: 90-119 days overdue 4: 120-149 days overdue 5: Overdue or bad debts, write-offs for more than 150 days C: paid off that month X: No loan for the month",
                       "Target: Risk user are marked as '1', else are '0'"
                       ],

        "Descrição" : 
                        [
                        "Identificador", 
                        "Gênero", 
                        "Possui veículo", 
                        "Possui propriedade",
                        "Quantidade de filhos", 
                        "Renda anual",
                        "Escolaridade", 
                        "Estado civil",
                        "Modo de vida",
                        "Idade em dias",
                        "Duração do trabalho em dias",
                        "Possui telefone móvel", 
                        "Possui telefone comercial",
                        "Possui telefone fixo",
                        "Tem um e-mail", 
                        "Profissão", 
                        "Mês de registro: Mês do registro: O mês dos dados extraídos é o ponto de partida, contando retroativamente. 0 representa o mês atual, -1 representa o mês anterior e assim por diante ",
                        "Status: 0: 1-29 dias em atraso 1: 30-59 dias em atraso 2: 60-89 dias em atraso 3: 90-119 dias em atraso 4: 120-149 dias em atraso 5: Vencido ou dívidas ruins, baixas contábeis por mais de 150 dias C: Quitado naquele mês X: Sem empréstimo no mês",
                        "Target: Usuários de risco são marcados como '1', caso contrário são '0'"
                       ]
                    }
    
    df_dicionario = pd.DataFrame(dicionario_dados,columns=["Column", "Coluna", "Tipo do dado", "Descrition", "Descrição",])  
    st.dataframe(df_dicionario,use_container_width=True)