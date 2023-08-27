import streamlit as st  
import pandas as pd
import numpy as np
from utils import *
from arvore_decisao import *

def carregar_dados():
    data = pd.read_parquet("./data/credit_card_approval.parquet")
    return data

def preparar_opcoes(data):
    opcoes_escolaridade = data["NAME_EDUCATION_TYPE"].unique()
    opcoes_estado_civil = data["NAME_FAMILY_STATUS"].unique() 
    opcoes_moradia = data["NAME_HOUSING_TYPE"].unique() 
    opcoes_profissao = data["JOB"].unique()
    opcoes_profissao = np.append(opcoes_profissao, "-")
    opcoes_filhos = data["CNT_CHILDREN"].unique()
    genero = data["CODE_GENDER"].unique()
    idade = dados["IDADE"].unique()
    return opcoes_escolaridade, opcoes_estado_civil, opcoes_moradia, opcoes_profissao, opcoes_filhos, genero,idade

def coletar_dados_usuario(opcoes_escolaridade, opcoes_estado_civil, opcoes_moradia, opcoes_profissao, opcoes_filhos, genero, idade):
    nome = st.text_input("Nome:")
    genero_selecionado = st.selectbox("Gênero:", genero, key="genero")
    idade_selecionada = st.selectbox("Idade:", sorted(idade), key="idade")
    escolaridade = st.selectbox("Escolaridade:", opcoes_escolaridade, key="escolaridade")
    estado_civil = st.selectbox("Estado Civil:", opcoes_estado_civil, key="estado_civil")
    filhos = st.selectbox("Quantidade de Filhos:", opcoes_filhos, key="filhos")
    possui_carro = st.selectbox("Possui Carro?", ["Não", "Sim"], key="carro")
    possui_propriedades = st.selectbox("Possui Propriedades?", ["Não", "Sim"], key="propriedades")
    tipo_moradia = st.selectbox("Tipo de Moradia:", opcoes_moradia, key="moradia")
    possui_emprego = st.selectbox("Emprego Atual:", ["Não", "Sim"], key="emprego")
    profissao = st.selectbox("Profissão:", opcoes_profissao, key="profissao")
    renda_anual = st.number_input("Renda anual:", min_value=0, max_value=10000000)
    enviar = st.button("Enviar")
    
    return {
        "nome": nome,
        "genero": genero_selecionado,
        "idade": idade_selecionada,
        "escolaridade": escolaridade,
        "estado_civil": estado_civil,
        "filhos": filhos,
        "possui_carro": possui_carro,
        "possui_propriedades": possui_propriedades,
        "tipo_moradia": tipo_moradia,
        "possui_emprego": possui_emprego,
        "profissao": profissao,
        "renda_anual": renda_anual,
        "enviar": enviar
    }

def processar_dados_usuario(dados_usuario):
    dict_dados = {}
    for coluna in dados.columns:
        dict_dados[coluna] = 0

    if dados_usuario["enviar"]:
        dict_dados["GENERO"] = 1 if dados_usuario["genero"] == "F" else 0
        dict_dados["IDADE"] = int(dados_usuario["idade"])
        dict_dados[dados_usuario["escolaridade"]] = 1
        dict_dados[dados_usuario["estado_civil"]] = 1
        dict_dados[dados_usuario["filhos"]] = 1
        dict_dados[dados_usuario["tipo_moradia"]] = 1
        dict_dados["POSSUI CARRO"] = 1 if dados_usuario["possui_carro"] == "Sim" else 0
        dict_dados["POSSUI PROPRIEDADES"] = 1 if dados_usuario["possui_propriedades"] == "Sim" else 0
        dict_dados["POSSUI EMPREGO"] = 1 if dados_usuario["possui_emprego"] == "Sim" else 0
        if dados_usuario["profissao"] != "-":
            dict_dados[dados_usuario["profissao"]] = 1
        dict_dados['RENDIMENTO ANUAL'] = dados_usuario["renda_anual"]
        lista = list(dict_dados.values())[:-1]
        
        return dict_dados, lista
    return None, None

def mostrar_resultados(resultado, nome, acuracia, precisao, recall, matrix_confusao):
    if resultado == 0:
        st.success(f"Cliente {nome}: Sua solicitação de crédito foi APROVADA!")
    else:
        st.warning(f"Cliente {nome}: Sua solicitação de crédito foi NEGADA!")

    metricas = {
        'Métrica': ['Acurácia', 'Precisão', 'Revocação'],
        'Valor': [acuracia, precisao, recall]
    }
    with st.expander("Resultados da Validação da Árvore de Decisão"):
        st.subheader("Métricas:")
        st.table(pd.DataFrame(metricas))

        st.subheader("Matriz de Confusão:")
        st.table(matrix_confusao)

def main():
    st.title("Simular análise de crédito")
    dados = carregar_dados()
    opcoes_escolaridade, opcoes_estado_civil, opcoes_moradia, opcoes_profissao, opcoes_filhos, genero, idade = preparar_opcoes(dados)
    
    dados_usuario = coletar_dados_usuario(opcoes_escolaridade, opcoes_estado_civil, opcoes_moradia, opcoes_profissao, opcoes_filhos, genero, idade)
    if dados_usuario["enviar"]:
        dict_dados, lista = processar_dados_usuario(dados_usuario)
        
        # Exibir os dados recebidos
        st.write("Dados recebidos:")
        st.write(dict_dados)

        # Preparar os dados para classificação
        solicitante = np.array(lista)

        # Exibir o resultado da análise
        resultado = executar_classificador(classificador_arvore_decisao, X_train, [solicitante], y_train)
        print(resultado)
        mostrar_resultados(resultado, dados_usuario["nome"], acuracia, precisao, recall, matrix_confusao)

if __name__ == "__main__":
    main()
