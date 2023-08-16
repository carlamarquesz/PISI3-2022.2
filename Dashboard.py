import streamlit as st
import pandas as pd
import plotly.express as px
from utils import *
from graphics import *
# from data_visualization.data_for_analysis_streamlit import *

st.set_page_config(layout="wide")
st.title("Dashboard ST Credit :coin:")
aba1, aba2, aba3 = st.tabs(["Estatística geral", "Histórico de atrasos", "Outliers"])

def identify_outliers(df, column):
    z_scores = (df[column] - df[column].mean()) / df[column].std()
    threshold = 2.5
    outliers = df[abs(z_scores) > threshold]
    return outliers

# Estatisca geral
with aba1:
    st.subheader("Estatística geral")
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        # Grafico da porcentagem de posses dos clientes
        st.caption("Probabilidade de aprovação com base nas posses dos clientes")
        porcentagens = (
            dados[dados["TARGET"] == 0][["POSSUI_CARRO", "POSSUI_PROPRIEDADES"]].value_counts(normalize=True)
            * 100
        )
        categorias = [
            "Somente carro",
            "Somente propriedade",
            "Carro e propriedade",
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
        fig1.update_traces(textposition="inside", 
                           textinfo="percent+label", 
                           textfont_color="white", 
                           textfont_size=20)
        st.plotly_chart(fig1, use_container_width=True) 
        with st.expander("Descrição"):
            st.write("A análise da probabilidade de aprovação com base nas posses dos clientes estuda como características financeiras, como possuir carro, propriedades e rendimento anual, influenciam as chances de aprovação em solicitações de crédito. Calcula-se a proporção de clientes aprovados em diferentes grupos, identificando as características relacionadas a maiores chances de aprovação.") 
        st.divider()  

        # Calcular o salário mensal com base no rendimento anual
        st.caption("Média de salário das profissões")
        dados['SALARIO'] = dados['RENDIMENTO_ANUAL'] / 12
        profissoes = dados['CARGO'].unique()
        profissoes_selecionadas = st.multiselect("Selecione as profissões: ", profissoes)
        dados_filtrados = dados[dados['CARGO'].isin(profissoes_selecionadas)]
        media_salario = dados_filtrados.groupby('CARGO')[['SALARIO']].mean() 
        df_salario = pd.DataFrame({
            "Profissão": media_salario.index,
            "Média de salário ($)": media_salario['SALARIO'].values.round(0)
        })
        fig2 = px.bar(df_salario, x="Profissão", y="Média de salário ($)")
        fig2.update_layout(xaxis_title="Profissão", yaxis_title="Média de salário ($)")
        st.plotly_chart(fig2, use_container_width=True) 
        with st.expander("Descrição"):
            st.write("O gráfico mostra a relação entre as profissões e o salário mensal com base no rendimento anual, permitindo identificar padrões que indicam risco ou capacidade de pagamento. Isso otimiza a análise de crédito e melhora a tomada de decisões.") 
            

    with coluna2:
        # Gráfico profissões com menor atraso de pagamento 
        media_profissoes_sem_atraso = (dados['STATUS2'] == 0).groupby(dados['CARGO']).mean()
        top_profissoes_sem_atraso = media_profissoes_sem_atraso.nlargest(6) 
        st.caption("Profissões com menor atraso de pagamentos") 
        df_contagem_cargo = pd.DataFrame(
            {
                "Profissão": top_profissoes_sem_atraso.index,
                "Bom histórico de pagamento": top_profissoes_sem_atraso.values * 100,
            }
        )
        fig3 = px.bar(
            df_contagem_cargo, x="Bom histórico de pagamento", y="Profissão", orientation="h"
        )
        fig3.update_layout(xaxis_title="Bom histórico de pagamento (%)", yaxis_title="Profissão")  
        st.plotly_chart(fig3, use_container_width=True)
        with st.expander("Descrição"):
            st.write("O gráfico analisa as diferentes profissões e seus respectivos históricos de pagamentos. Ele identifica as 6 profissões com menor atraso de pagamento, o que pode indicar maior confiabilidade financeira.") 
        st.divider()   

        # Distribuição do nível de escolaridade com maior risco de inadimplência
        st.caption("Nível de escolaridade com maior risco de inadimplência")
        media_escolaridade_com_atraso = (dados['STATUS2'] == 1).groupby(dados['ESCOLARIDADE']).mean() 
        df_escolaridade = pd.DataFrame(
            {
                "Nível de educação": media_escolaridade_com_atraso.index,
                "Risco de inadimplência (%)": media_escolaridade_com_atraso.values * 100,
            }
        )
        fig4 = px.bar(
            df_escolaridade, x="Risco de inadimplência (%)", y="Nível de educação"
        )
        fig4.update_layout(
            xaxis_title="Risco de inadimplência (%)", yaxis_title="Nível de educação"
        )
        st.plotly_chart(fig4, use_container_width=True) 
        with st.expander("Descrição"):
            st.write("O gráfico analisa a relação entre o nível de escolaridade dos indivíduos e seu histórico de pagamento. É possível identificar quais níveis de escolaridade estão associados a um maior risco de inadimplência, auxiliando na tomada de decisões relacionadas à concessão de crédito") 

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

# Outliers
with aba3:
    st.subheader("Gráficos de Outliers")
    columns_options = ['RENDIMENTO_ANUAL', 'QTD_MESES', 'DIAS_ANIVERSARIO']
    selected_column = st.selectbox('Selecione a coluna para identificar outliers:', columns_options)
    outliers = identify_outliers(dados, selected_column)

    fig_scatter = px.scatter(dados, x=dados.index, y=selected_column, title='Gráfico de Dispersão com Outliers', labels={'x': 'Índice', 'y': selected_column})
    fig_scatter.add_scatter(x=outliers.index, y=outliers[selected_column], mode='markers', name='Outliers', marker=dict(color='red', size=10, symbol='circle'))
    fig_box = px.box(dados, y=selected_column, title='Box Plot')
    fig_histogram = px.histogram(dados, x=selected_column, nbins=20, title='Histograma', labels={'x': selected_column, 'y': 'Contagem'})
    fig_box2 = px.box(dados, y='CARGO', x='RENDIMENTO_ANUAL', color='CARGO', title='Boxplot de Rendimento Anual por Cargo')

    st.plotly_chart(fig_scatter)
    st.plotly_chart(fig_box)
    if selected_column == 'RENDIMENTO_ANUAL':
        st.plotly_chart(fig_box2)
    st.plotly_chart(fig_histogram)
