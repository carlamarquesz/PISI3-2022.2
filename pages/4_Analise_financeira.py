import streamlit as st
import pandas as pd
from utils import *
from graphics import *
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from EDA.utils_EDA import *



st.title('Análise financeira')

descricao = """
<p style='text-align: justify; text-indent: 1.25em;'>Nesta seção, examinaremos minuciosamente as diversas conexões entre os clientes e seus rendimentos anuais. Essa análise aprofundada não apenas oferece insights sobre a situação financeira dos clientes, mas também destaca tendências financeiras mais abrangentes que podem afetar estratégias empresariais, planejamento financeiro individual e até mesmo políticas econômicas.</p>
"""

st.markdown(descricao, unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

with st.expander('Selecione a quantidade de  dados a exibir'):
            qtd_dados = st.sidebar.slider('',min_value=50, max_value=len(dados), value=100)

def plot_outlirs_box_violion(qtd_dados):
    coluna1, coluna2 =  st.columns([0.7,.3])
    df_copy_box_violion = dados.copy()  
    df_copy_box_violion.rename(columns={'RENDIMENTO_ANUAL':'Rendimento Anual', 'GENERO':'Gênero', 'ESCOLARIDADE':'Escolaridade', 'TIPO_DE_MORADIA':'Tipo de moradia', 'QTD_FILHOS':'Quantidade de filhos', 'FAIXA_ETARIA': 'Faixa Etária'}, inplace=True)   

    
    with coluna2:
        tipo_grafico = st.radio(
            "Escolha o Gráfico:",
            ("box", "violin"))
        
        with st.expander('Filtre por:'):
            opc = criar_radio_com_chave_unica(texto="Escolha por Filtro para o histogram:", opcoes=['Gênero', 'Faixa Etária', 'Escolaridade', 'Tipo de moradia', 'Quantidade de filhos'] ,chave= 'opcfiltro')
        
        descricao = """
        <p style='text-align: justify; text-indent: 1.25em;'>
         Podemos observar no gráfico box ou violion, o rendimento anual por cargos e selecionar por filtro como desejar.

        </p>
        """
        st.markdown(descricao, unsafe_allow_html=True)  

    with coluna1:  
        cargos_unicos = df_copy_box_violion['CARGO'].unique()
        cargo_selecionado = st.selectbox('Selecione o tipo de cargo:',cargos_unicos)
        df_cargo = df_copy_box_violion[df_copy_box_violion['CARGO'] == cargo_selecionado]
        df_cargo = df_cargo.head(qtd_dados) 
        grafico = px.box(df_cargo,x="CARGO", y='Rendimento Anual',color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}')
        if tipo_grafico == "box":
            grafico = px.box(df_cargo,x="CARGO", y='Rendimento Anual', color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}')
        elif tipo_grafico == "violin":
            grafico = px.violin(df_cargo,x="CARGO", y='Rendimento Anual', color=opc,violinmode= "group", points="outliers",box= True, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}', )
        st.plotly_chart(grafico, )

    
def tratar_outliers(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    data[data > limite_superior] = limite_superior 
    data[data < limite_inferior] = limite_inferior
    
    return data

def grafico_bar(tratar_outliers):
    columns = df_analise_financeira.columns[[6,8]].tolist()
    opc_select = st.selectbox('Selecione a coluna:', columns)
    df_analise_financeira['RENDIMENTO_ANUAL'] = df_analise_financeira.groupby(opc_select)['RENDIMENTO_ANUAL'].transform(tratar_outliers)
    rendimento_medio = df_analise_financeira.groupby(opc_select)['RENDIMENTO_ANUAL'].mean().reset_index()

    invert_axis = st.toggle('Inverta o Eixo: do gráfico de barras')
    if invert_axis:
        fig_barra = px.bar(rendimento_medio, x=opc_select, y='RENDIMENTO_ANUAL',
                        title=f' Gráfico de Barra Vertical')
    else:
        fig_barra = px.bar(rendimento_medio, y=opc_select, x='RENDIMENTO_ANUAL', orientation='h',
                        title=f'Gráfico de Barra Horizontal')
    st.plotly_chart(fig_barra, use_container_width=True)


def plot_histogram(qtd_dados):
    coluna1, coluna2 =  st.columns([0.7,.3])
    df_copy_histogram = dados.copy()
    df_copy_histogram.rename(columns={'FAIXA_ETARIA': 'Faixa Etária','GENERO':'Gênero', 'ESCOLARIDADE':'Escolaridade', 'IDADE_ANOS':'Idade', 'QTD_FILHOS':'Quantidade de filhos'}, inplace=True)
    df_copy_histogram['IDADE_ANOS'] = df_copy_histogram['Idade'].copy()  
    with coluna2:
        df_histogram = df_copy_histogram.head(qtd_dados)  
        colunas_color = ['Gênero', 'Faixa Etária', 'Escolaridade', 'Idade', 'Quantidade de filhos']        
        colunas_selecionadas = st.multiselect("Selecione as colunas para colorir:", colunas_color)
        df_histogram['ColorGroup'] = df_histogram[colunas_selecionadas].apply(lambda row: ' - '.join(row.values.astype(str)), axis=1)
        descricao = """
        <p style='text-align: justify; text-indent: 1.25em;'>
         No histogram podemos fazer agrupamanto e colorir para melhor visualização dos dados conforme desejado.

        </p>
        """
        st.markdown(descricao, unsafe_allow_html=True)
    with coluna1:  
        fig_histogram = px.histogram(df_histogram, x='RENDIMENTO_ANUAL', color='ColorGroup', title='Histograma' )
        fig_histogram.update_layout(
                                        xaxis_title=f"{'RENDIMENTO_ANUAL'}",
                                        yaxis_title="Contagem"
                                    )
        st.plotly_chart(fig_histogram)


def main():
    grafico_bar(tratar_outliers)
    plot_outlirs_box_violion(qtd_dados)
    plot_histogram(qtd_dados)
    

if __name__ == '__main__':
    main()
