import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from utils import *
from graphics import * 


st.title('Análise de risco')

descricao = """
<p style='text-align: justify; text-indent: 1.25em;'>Nesta seção, nos dedicaremos a examinar meticulosamente diversas relações existentes entre os clientes, focalizando especialmente na distinção entre aqueles que apresentam características de risco e os que não apresentam.</p>
"""
st.markdown(descricao, unsafe_allow_html=True)  

select_value_ar = st.sidebar.slider(label='Selecione a quantidade de dados para analisar do dataset', min_value=1,
                          max_value=len(df_analise_risco), value=50)

st.markdown('')
df_analise_risco = df_analise_risco.head(select_value_ar)

st.markdown("Gráfico de barras - Distribuição de cargo por Target")
fig13 = px.bar(
df_analise_risco,
x="CARGO",
color="TARGET",
title="Proporção de Cargo por Target",
labels={"TARGET": "Target", "CARGO": "Cargo"},
orientation='v'
)

# Exibindo o gráfico
st.plotly_chart(fig13, use_container_width=True)

st.subheader("Gráfico de barras - Distribuição de possui propriedades por Target")
fig13 = px.bar(
df_analise_risco,
x="POSSUI_PROPRIEDADES",
color="TARGET",
title="Proporção de possui proriedade por Target",
labels={"TARGET": "Target", "POSSUI_PROPRIEDADES": "Possui propriedade"},
orientation='v'
)

# Exibindo o gráfico
st.plotly_chart(fig13, use_container_width=True)


st.subheader("Gráfico de Dispersão - Rendimento Anual vs. Idade (Colorido por Target)")
# Filtro interativo para selecionar a cor (TARGET)
color_filter = st.selectbox("Selecione a coluna para colorir:", df_analise_risco.columns, key="color_filter")

# Criando o gráfico de dispersão interativo
fig10 = px.scatter(
    df_analise_risco,
    x="IDADE_ANOS",
    y="RENDIMENTO_ANUAL",
    color=color_filter,
    title="Rendimento Anual vs. Idade (Colorido por Target)",
    labels={"IDADE_ANOS": "Idade (anos)", "RENDIMENTO_ANUAL": "Rendimento Anual"}
)

# Exibindo o gráfico
st.plotly_chart(fig10, use_container_width=True)
