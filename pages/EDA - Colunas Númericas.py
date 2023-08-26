import streamlit as st
import pandas as pd
from utils import *
from data_dict.dicionario_dados import *
from graphics import *
import numpy as np
import plotly.express as px
from PIL import Image

columns = [
        "RENDIMENTO_ANUAL",
        "ANOS_EMPREGADO",
        "QTD_MESES",
        "SALARIO",
    
]

def main():
    total = len(dados)
    # column = st.selectbox('Selecione a coluna:', rotulos_keys_colunas_numericas)
    # column_select = rotulos.get(column)
    column_select = st.selectbox('Selecione a coluna:', columns)
    qtd_dados = st.sidebar.slider(label='Selecione a quantidade de dados para analisar do dataset', min_value=1,
                          max_value=len(dados), value=5)

    dados_selecionados = dados.head(qtd_dados)
    st.subheader(f'Quantidade de dados selecionado para análise: {qtd_dados}/{total} total')
    
    create_interactive_visualization(dados, column_select)


def IQR(dados, coluna):
    q1 = dados[coluna].quantile(0.25)
    q2 = dados[coluna].quantile(0.50)
    q3 = dados[coluna].quantile(0.75)
    return q1, q2, q3

def identify_outliers(dados, coluna, threshold=1.5):
    q1, q2, q3 = IQR(dados, coluna)
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return dados[(dados[coluna] < lower_bound) | (dados[coluna] > upper_bound)]

def create_interactive_visualization(dados, coluna):
    # st.subheader(f'Análise da Coluna {buscar_chave_por_valor(rotulos,coluna)}')
    st.subheader(f'Análise da Coluna {coluna}')
    q1, q2, q3 = IQR(dados, coluna)

    coluna1, coluna2 = st.columns([0.6, 0.4])

    with coluna1:
        q1_data = dados[dados[coluna] <= q1]
        q2_data = dados[(dados[coluna] > q1) & (dados[coluna] <= q2)]
        q3_data = dados[(dados[coluna] > q2) & (dados[coluna] <= q3)]
        q4_data = dados[dados[coluna] > q3]

        fig = px.box(dados, y=coluna, title='Box Plot', points='all')
        st.plotly_chart(fig,use_container_width=True)
        with st.expander('Descrição do Box Plot'):
            image = Image.open('image/exemplo_boxplot.png')
            st.image(image, caption='Fonte: https://statplace.com.br/blog/como-interpretar-um-boxplot/')

        st.markdown("<br><br>", unsafe_allow_html=True)

        valormin = float(dados[coluna].min())
        valormax = float(dados[coluna].max())
        colors = st.selectbox('Selecione a cor do histogram:', [None, "red", "green", "blue", "purple", "orange"])
        selected_range = st.slider("Selecione o intervalo desejado: ", valormin, valormax, (valormin, valormax))
        selected_data = dados[(dados[coluna] >= selected_range[0]) & (dados[coluna] <= selected_range[1])]
        fig = px.histogram(selected_data, x=coluna, color_discrete_sequence=[colors])
        st.plotly_chart(fig,use_container_width=True)

        st.subheader(f'Outliers')
        simbol = st.selectbox('selecione o simbolo para os outlirs',['circle', 'square', 'diamond', 'cross', 'x', 'triangle-up'])
        outliers = identify_outliers(dados,coluna)
        color = st.color_picker('Escolhar a cor dos outlirs', '#00f900')
        fig_scatter = px.scatter(dados, x=dados.index, y=coluna, title='Gráfico de Dispersão com Outliers', labels={'x': 'Índice', 'y': coluna})
        fig_scatter.add_scatter(x=outliers.index, y=outliers[coluna], mode='markers', name='Outliers', marker=dict(color=color, size=10, symbol=simbol))
        st.plotly_chart(fig_scatter)

    with coluna2:
        st.subheader(f'Quantidade de dados selecionado: {len(dados)}')
        st.write(f'Quantidade de pessoas no Primeiro Quartil (Q1): {len(q1_data)}')
        st.write(f'Quantidade de pessoas no Segundo Quartil (Q2): {len(q2_data)}')
        st.write(f'Quantidade de pessoas no Terceiro Quartil (Q3): {len(q3_data)}')
        st.write(f'Quantidade de pessoas no Quarto Quartil (Q4): {len(q4_data)}')
        st.write(' ')
        # texto de descrição


if __name__ == '__main__':
    main()


