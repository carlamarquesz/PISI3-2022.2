import streamlit as st  
import pandas as pd
import numpy as np
from utils import *
from modelo import *

def read_data():
    data = pd.read_parquet("./data/credit_card_approval.parquet")
    return data

def prepare_options(data):
    opcoes_escolaridade = data["NAME_EDUCATION_TYPE"].unique()
    opcoes_estado_civil = data["NAME_FAMILY_STATUS"].unique() 
    opcoes_moradia = data["NAME_HOUSING_TYPE"].unique() 
    opcoes_profissao = data["JOB"].unique()
    opcoes_profissao = np.append(opcoes_profissao, "-")
    opcoes_filhos = data["CNT_CHILDREN"].unique()
    return opcoes_escolaridade, opcoes_estado_civil, opcoes_moradia, opcoes_profissao, opcoes_filhos

def main():
    st.title("Simular análise de crédito") 
    data = read_data()
    opcoes_escolaridade, opcoes_estado_civil, opcoes_moradia, opcoes_profissao, opcoes_filhos = prepare_options(data) 
    nome = st.text_input("Nome:") 
    escolaridade = st.selectbox("Escolaridade:", opcoes_escolaridade, key="escolaridade")
    estado_civil = st.selectbox("Estado Civil:", opcoes_estado_civil, key="estado_civil")
    filhos = st.selectbox("Quantidade de Filhos:", opcoes_filhos, key="filhos")
    carro = st.selectbox("Possui Carro?", ["Não", "Sim"], key="carro")
    propriedades = st.selectbox("Possui Propriedades?", ["Não", "Sim"], key="propriedades")
    moradia = st.selectbox("Tipo de Moradia:", opcoes_moradia, key="moradia")
    emprego = st.selectbox("Emprego Atual:", ["Não", "Sim"], key="emprego")
    profissao = st.selectbox("Profissão:", opcoes_profissao, key="profissao")
    renda_anual = st.number_input("Renda anual:", min_value=0, max_value=10000000) 
    enviar = st.button("Enviar")  
    dict = {}
    for i in dados.columns:
        dict[i] = 0  

    if enviar:   
        dict[escolaridade] = 1
        dict[estado_civil] = 1
        dict[filhos] = 1 
        dict[moradia] = 1 
        dict["POSSUI_CARRO"] = 1 if carro == "Sim" else 0
        dict["POSSUI_PROPRIEDADES"] = 1 if propriedades == "Sim" else 0
        dict["POSSUI_EMPREGO"] = 1 if emprego == "Sim" else 0 
        if profissao != "-":
            dict[profissao] = 1 
        dict['RENDIMENTO_ANUAL'] = renda_anual  
        lista = list(dict.values())[:-1] 

        # Exibir os dados recebidos
        st.write("Dados recebidos:")
        st.write(dict) 

        # Preparar os dados para classificação
        lista = list(dict.values())[:-1]
        solicitante = np.array(lista)
        
        # Exibir o resultado da análise
        resultado = executar_classificador(classificador_random_forest, X_train, [solicitante], y_train)
        print(resultado)
        if resultado == 0: 
            st.success(f"Cliente {nome}: Sua solicitação de crédito foi APROVADA!") 
        else:
            st.warning(f"Cliente {nome}: Sua solicitação de crédito foi NEGADA!") 

        metricas = {
            'Métrica': ['Accuracy Score', 'Precision Score', 'Recall Score'],
            'Valor': [acuracia, precisao, recall]
        }
        with st.expander("Resultados da Validação da Árvore de Decisão"):
            st.subheader("Métricas:")
            st.table(pd.DataFrame(metricas))

            st.subheader("Matriz de Confusão:")
            st.table(matrix_confusao) 
        

if __name__ == "__main__":
    main()

