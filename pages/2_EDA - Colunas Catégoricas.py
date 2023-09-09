import streamlit as st
import pandas as pd
# from utils import *
from graphics import *
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from EDA.utils_EDA import *

# Colunas categoricas para analise individual
columns =   [   
            "GENERO",
            "POSSUI_CARRO",
            "POSSUI_PROPRIEDADES",
            "QTD_FILHOS",
            "ESCOLARIDADE",
            "ESTADO_CIVIL",
            "TIPO_DE_MORADIA",
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

    qtd_dados = st.sidebar.slider(label='Selecione a quantidade de dados para analisar do dataset', min_value=50,
                          max_value=len(dados), value=50)

    dados_selecionados = dados.head(qtd_dados)
   
    create_interactive_visualizations(dados_selecionados, coluna_selecionada)


def create_interactive_visualizations(dados, coluna_selecionada):
    # st.subheader(f'Análise da Coluna {buscar_chave_por_valor(rotulos, coluna)}')
    subtitulo_proxima_secao_html = (
    f"<h2 style='text-align: center;'>Análise da Coluna {coluna_selecionada}</h2>")
    
    st.write(subtitulo_proxima_secao_html, unsafe_allow_html=True)
    st.write(description[coluna_selecionada], unsafe_allow_html=True)

    contagem_tipos = dados[coluna_selecionada].value_counts()
    contagem_df = pd.DataFrame({coluna_selecionada: contagem_tipos.index, 'Contagem': contagem_tipos.values})
    fig_rosca_donut = px.pie(contagem_df, names=coluna_selecionada, values='Contagem', hole=0.3,
                             title=f'Distribuição da coluna {coluna_selecionada} em Gráfico de Rosca Donut')
    fig_rosca_donut.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_rosca_donut, use_container_width=True)
    
    st.markdown(f"<h3>Valores da contagem para a coluna {coluna_selecionada}:</h3>", unsafe_allow_html=True)
    st.markdown("<ul>" + "".join([f"<li><strong>{valor}</strong>: {contagem}</li>" for valor, contagem in zip(contagem_df[coluna_selecionada], contagem_df['Contagem'])]) + "</ul>", unsafe_allow_html=True)
    st.write(' ')
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




