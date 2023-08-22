import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import *
from graphics import *
# from data_visualization.data_for_analysis_streamlit import *

st.set_page_config(layout="wide")
st.title("Dashboard ST Credit :coin:")
aba1, aba2, aba3 = st.tabs(["Estatística geral", "Histórico de atrasos", "Outliers"])


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
        profissoes = dados['CARGO'].unique()
        profissoes_selecionadas = st.multiselect("Selecione as profissões: ", profissoes)
        idade = st.text_input("Digite a idade desejada: ")
        # QUANTIDADE_DIAS_ANO = 365.25
        try:
            idade_anos = float(idade)
        except ValueError:
            idade_anos = None

        if idade_anos is not None:
            # idade_dias = int(idade_anos * QUANTIDADE_DIAS_ANO) * -1
            dados_filtrados = dados[(dados['CARGO'].isin(profissoes_selecionadas)) & (dados['Idade'] == idade_anos)]
            # print(idade_dias)
        else:
            dados_filtrados = dados[(dados['CARGO'].isin(profissoes_selecionadas))]
        media_salario = dados_filtrados.groupby('CARGO')[['SALARIO']].mean() 
        df_salario = pd.DataFrame({
            "Profissão": media_salario.index,
            "Média de salário ($)": media_salario['SALARIO'].values.round(0)
        })
        fig2 = px.bar(df_salario, x="Profissão", y="Média de salário ($)")
        fig2.update_layout(xaxis_title="Profissão", yaxis_title="Média de salário ($)", bargap=0.2, bargroupgap=0.1)
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
        media_escolaridade_com_atraso = (dados['STATUS2'] == 1).groupby(dados['Escolaridade']).mean() 
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
    opcoes_qtd_meses = np.sort(dados["Quantidade de Meses"].unique().astype(int))
    filtro_qtd_meses = st.selectbox("Selecione o valor de meses:", opcoes_qtd_meses)
    st.subheader(f"Atrasos de pagamento {texto(filtro_qtd_meses)}")
    # Condições de filtro para STATUS_PAGAMENTO
    status_pagamento = ["X", "C", "5", "4", "3", "2", "1", "0"]
    lista = []
    # Filtrar dados de acordo com o valor de meses
    for i in status_pagamento:
        dados_filtrados = len(
            dados.loc[
                (dados["Quantidade de Meses"] == filtro_qtd_meses)
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
    columns_options = ['Rendimento Anual', 'Quantidade de Meses', 'Idade']
    selected_column = st.selectbox('Selecione a coluna para identificar outliers:', columns_options)

    def graficos_outliers(selected_column):
        def plot_outliers_scatter(selected_column):
            c1, c2 = st.columns(2)
            df_copy_scatter = dados.copy()
            with c2:
                qtd_dados_scatter = st.slider("Selecione a quantidade de  dados que serão exibidas:", min_value=1, max_value=len(dados), value=50, key='1')
                df_scatter = df_copy_scatter.head(qtd_dados_scatter) 
                st.markdown(f"Quantidade de dados buscado: {qtd_dados_scatter}")

            with c1:
                with st.expander('Configuração de exibição'):
                    outliers = identify_outliers(df_scatter, selected_column)
                    color = st.color_picker('Escolhar a cor dos outlirs', '#00f900')
                    simbol = st.selectbox('selecione o simbolo para os outlirs',['circle', 'square', 'diamond', 'cross', 'x', 'triangle-up'])
        
            with c1:
                fig_scatter = px.scatter(df_scatter, x=df_scatter.index, y=selected_column, title='Gráfico de Dispersão com Outliers', labels={'x': 'Índice', 'y': selected_column})
                fig_scatter.add_scatter(x=outliers.index, y=outliers[selected_column], mode='markers', name='Outliers', marker=dict(color=color, size=10, symbol=simbol))
                st.plotly_chart(fig_scatter)

        plot_outliers_scatter(selected_column) 

        def plot_outlirs_box_violion():
            c1, c2 = st.columns(2)
            df_copy_box_violion = dados.copy() 
            with c2:
                qtd_dados_box_violion = st.slider("Selecione a quantidade de  dados que serão exibidas:", min_value=1, max_value=len(dados), value=50, key='2')
                tipo_grafico = st.radio(
        "Escolha o Gráfico:",
        ("box", "violin")) 

            with c1:
                opc = st.radio(
        "Filtrar por:",
        ('GENERO', 'Faixa Etária', 'Escolaridade'))   

        
                cargos_unicos = df_copy_box_violion['CARGO'].unique()
                cargo_selecionado = st.selectbox('Selecione o tipo de cargo:',cargos_unicos)
                df_cargo = df_copy_box_violion[df_copy_box_violion['CARGO'] == cargo_selecionado]
                df_cargo = df_cargo.head(qtd_dados_box_violion) 
            grafico = px.box(df_cargo,x="CARGO", y='Rendimento Anual', color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}')
            if tipo_grafico == "box":
                grafico = px.box(df_cargo,x="CARGO", y='Rendimento Anual', color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}')
            elif tipo_grafico == "violin":
                grafico = px.violin(df_cargo,x="CARGO", y='Rendimento Anual', color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}', )
            st.plotly_chart(grafico)

        plot_outlirs_box_violion()

        def plot_outlirs_histogram(selected_column):
            c1, c2 = st.columns(2)
            df_copy_histogram = dados.copy()
            with c2: 
                qtd_dados_histogram = st.slider("Selecione a quantidade de  dados que serão exibidas:", min_value=1, max_value=len(dados), value=50, key= '3')
                df_histogram = df_copy_histogram.head(qtd_dados_histogram) 
            with c1:
                fig_histogram = px.histogram(df_histogram, x= df_histogram.index, y=selected_column , nbins=20, title='Histograma' )
                fig_histogram.update_layout(
        xaxis_title="Contagem",
        yaxis_title="Rendimento Anual"
    )
                st.plotly_chart(fig_histogram)

        plot_outlirs_histogram(selected_column)

    graficos_outliers(selected_column)
