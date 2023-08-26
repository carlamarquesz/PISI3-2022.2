import streamlit as st
import pandas as pd
# from utils import *
from graphics import *
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

columns =   [   
            "GENERO",
            "POSSUI_CARRO",
            "POSSUI_PROPRIEDADES",
            "QTD_FILHOS",
            "ESCOLARIDADE",
            "ESTADO_CIVIL",
            "TIPO_DE_MORADIA",
            "IDADE_ANOS",
            "CELULAR",
            "TELEFONE_COMERCIAL",
            "TELEFONE_RESIDENCIAL",
            "EMAIL",
            "CARGO",
            "STATUS_PAGAMENTO",
            "VARIAVEL_TARGET",
            "FAIXA_ETARIA"
            ]

def main():
    total = len(dados)
    # column = st.selectbox('Selecione a coluna:', rotulos_keys_colunas_categoricas)
    # column_select = rotulos.get(column)
    coluna_selecionada = st.selectbox('Selecione a coluna:', columns)

    qtd_dados = st.sidebar.slider(label='Selecione a quantidade de dados para analisar do dataset', min_value=1,
                          max_value=len(dados), value=5)

    dados_selecionados = dados.head(qtd_dados)
    st.subheader(f'Quantidade de dados selecionado para análise: {qtd_dados}/{total} total')

    create_interactive_visualizations(dados_selecionados, coluna_selecionada)


def create_interactive_visualizations(dados, coluna_selecionada):
    # st.subheader(f'Análise da Coluna {buscar_chave_por_valor(rotulos, coluna)}')
    st.subheader(f'Análise da Coluna {coluna_selecionada}')
     
    # COLOCAR UMA DESCRIÇÃO

    contagem_tipos = dados[coluna_selecionada].value_counts()
    contagem_df = pd.DataFrame({coluna_selecionada: contagem_tipos.index, 'Contagem': contagem_tipos.values})
    fig_rosca_donut = px.pie(contagem_df, names=coluna_selecionada, values='Contagem', hole=0.3,
                             title=f'Distribuição da coluna {coluna_selecionada} em Gráfico de Rosca Donut')
    st.plotly_chart(fig_rosca_donut, use_container_width=True)

    invert_axis = st.toggle('Inverta o Eixo: do gráfico de barras')
    if invert_axis:
        fig_barra = px.bar(contagem_df, x=coluna_selecionada, y='Contagem', color=coluna_selecionada,
                           title=f'Contagem da coluna {coluna_selecionada} em Gráfico de Barra Vertical')
    else:
        fig_barra = px.bar(contagem_df, y=coluna_selecionada, x='Contagem', orientation='h', color=coluna_selecionada,
                           title=f'Contagem da coluna {coluna_selecionada} em Gráfico de Barra Horizontal')
    st.plotly_chart(fig_barra, use_container_width=True)


if __name__ == '__main__':
    main()




