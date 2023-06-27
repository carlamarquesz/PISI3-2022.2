import streamlit as st
import pandas as pd
import plotly.express as px
from utils import *
from graphics import *

st.set_page_config(layout="wide")
st.title("Dashboard ST Credit :coin:")
aba1, aba2 = st.tabs(["Estatística geral", "Histórico de atrasos"])

# Estatisca geral
with aba1:
    st.subheader("Estatística geral")
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        # Grafico da porcentagem de posses dos clientes
        st.caption("Posses dos clientes")
        porcentagens = (
            dados[["POSSUI_CARRO", "POSSUI_PROPRIEDADES"]].value_counts(normalize=True)
            * 100
        )
        categorias = [
            "Somente Carro",
            "Somente Propriedade",
            "Carro e Propriedade",
            "Nenhum",
        ]
        cores = ["blue", "green", "orange", "red"]
        fig1 = px.pie(
            porcentagens,
            values=porcentagens.values,
            names=categorias,
            color=categorias,
            color_discrete_sequence=cores,
            hole=0.5,
        )
        fig1.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig1, use_container_width=True)

        # Gráfico de estilo de moradia dos clientes
        st.caption("Estilo de moradia dos clientes")
        contagem_moradia = dados["TIPO_DE_MORADIA"].value_counts()
        df_contagem_moradia = pd.DataFrame(
            {
                "Estilo de moradia": contagem_moradia.index,
                "Quantidade de Pessoas": contagem_moradia.values,
            }
        )
        fig2 = px.bar(
            df_contagem_moradia,
            x="Quantidade de Pessoas",
            y="Estilo de moradia",
            orientation="h",
        )
        fig2.update_layout(
            xaxis_title="Quantidade de Pessoas", yaxis_title="Estilo de moradia"
        )
        st.plotly_chart(fig2, use_container_width=True)
    with coluna2:
        # Gráfico de cargos dos clientes
        st.caption("Cargos dos clientes")
        contagem_cargo = dados["CARGO"].value_counts()
        df_contagem_cargo = pd.DataFrame(
            {
                "Cargo": contagem_cargo.index,
                "Quantidade de Pessoas": contagem_cargo.values,
            }
        )
        fig = px.bar(
            df_contagem_cargo, x="Quantidade de Pessoas", y="Cargo", orientation="h"
        )
        fig.update_layout(xaxis_title="Quantidade de Pessoas", yaxis_title="Cargo")
        st.plotly_chart(fig, use_container_width=True)

        # gráfico de escolaridade dos clientes
        st.caption("Escolaridade dos clientes")
        contagem_escolaridade = dados["ESCOLARIDADE"].value_counts()
        df_contagem_moradia = pd.DataFrame(
            {
                "Nível de educação": contagem_escolaridade.index,
                "Quantidade de Pessoas": contagem_escolaridade.values,
            }
        )
        fig = px.bar(
            df_contagem_moradia, x="Quantidade de Pessoas", y="Nível de educação"
        )
        fig.update_layout(
            xaxis_title="Quantidade de Pessoas", yaxis_title="Nível de educação"
        )
        st.plotly_chart(fig, use_container_width=True)
# Histórico de atrasos
with aba2:
    st.subheader("Histórico de atrasos")
    opcoes_qtd_meses = np.sort(dados["QTD_MESES"].unique().astype(int))
    filtro_qtd_meses = st.selectbox("Selecione o valor de meses:", opcoes_qtd_meses)
    st.subheader(f"Atrasos de pagamento {texto(filtro_qtd_meses)}")
    # Condições de filtro para STATUS_PAGAMENTO
    status_pagamento = ["X", "C", "5", "4", "3", "2", "1", "0"]
    lista = []
    # Filtrar dados de acordo com o valor de meses
    for i in status_pagamento:
        dados_filtrados = len(
            dados.loc[
                (dados["QTD_MESES"] == filtro_qtd_meses)
                & (dados["STATUS_PAGAMENTO"] == i)
            ]
        )
        lista.append(dados_filtrados)
    # Exibir dados filtrados
    coluna1, coluna2, coluna3, coluna4 = st.columns(4)
    with coluna1:
        st.metric("Não pediram empréstimo \n\nno mês", lista[0])
        st.metric("Estão em dia com \n\no empréstimo", lista[1])
    with coluna2:
        st.metric("Estão com empréstimo \n\nvencido", lista[7])
        st.metric("Estão com 120 a 149 dias \n\nde atraso", lista[2])
    with coluna3:
        st.metric("Estão com 90 a 119 dias \n\nde atraso", lista[3])
        st.metric("Estão com 60 a 89 dias \n\nde atraso", lista[4])
    with coluna4:
        st.metric("Estão com 30 à 59 dias \n\nde atraso", lista[5])
        st.metric("Estão com 1 a 29 dias \n\nde atraso", lista[6])