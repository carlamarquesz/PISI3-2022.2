import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from utils import *
from graphics import *
# from data_visualization.data_for_analysis_streamlit import *

st.set_page_config(layout="wide")
st.title("Dashboard ST Credit :coin:")
aba1, aba2, aba3 = st.tabs(["Estatística geral", "Outliers", "Gráficos"])

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
        idade = st.text_input("Digite a idade desejada: ")
        # QUANTIDADE_DIAS_ANO = 365.25
        try:
            idade_anos = float(idade)
        except ValueError:
            idade_anos = None

        if idade_anos is not None:
            # idade_dias = int(idade_anos * QUANTIDADE_DIAS_ANO) * -1
            dados_filtrados = dados[(dados['CARGO'].isin(profissoes_selecionadas)) & (dados['IDADE_ANOS'])]
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
# with aba2:
#     st.subheader("Histórico de atrasos")
#     opcoes_qtd_meses = np.sort(dados["QTD_MESES"].unique().astype(int))
#     filtro_qtd_meses = st.selectbox("Selecione o valor de meses:", opcoes_qtd_meses)
#     st.subheader(f"Atrasos de pagamento {texto_filtro(filtro_qtd_meses)}")
#     # Condições de filtro para STATUS_PAGAMENTO
#     status_pagamento = ["X", "C", "5", "4", "3", "2", "1", "0"]
#     lista = []
#     # Filtrar dados de acordo com o valor de meses
#     for i in status_pagamento:
#         dados_filtrados = len(
#             dados.loc[
#                 (dados["QTD_MESES"] == filtro_qtd_meses)
#                 & (dados["STATUS_PAGAMENTO"] == i)
#             ]
#         )
#         lista.append(dados_filtrados)
#     # Exibir dados filtrados
#     coluna1, coluna2, coluna3, coluna4 = st.columns(4)
#     with coluna1:
#         st.metric("Não pediram empréstimo \n\nno mês", lista[0])
#         st.metric("Estão em dia com \n\no empréstimo", lista[1])
#     with coluna2:
#         st.metric("Estão com empréstimo \n\nvencido", lista[7])
#         st.metric("Estão com 120 a 149 dias \n\nde atraso", lista[2])
#     with coluna3:
#         st.metric("Estão com 90 a 119 dias \n\nde atraso", lista[3])
#         st.metric("Estão com 60 a 89 dias \n\nde atraso", lista[4])
#     with coluna4:
#         st.metric("Estão com 30 à 59 dias \n\nde atraso", lista[5])
#         st.metric("Estão com 1 a 29 dias \n\nde atraso", lista[6])

# Outliers
with aba2:
    st.subheader("Gráficos de Outliers") 
    columns_options = ['Rendimento Anual', 'Meses de Cadastro', 'Idade']
    selected = st.selectbox('Selecione a coluna para identificar outliers:', columns_options)

    selected_column = None
    if selected == 'Rendimento Anual':
        selected_column = 'RENDIMENTO_ANUAL'
    elif selected == 'Meses de Cadastro':
        selected_column = 'QTD_MESES'
    elif selected == 'Idade':
        selected_column  = 'IDADE_ANOS'

    def graficos_outliers(selected_column):

        def plot_outliers_scatter(selected_column):
            coluna2, coluna3 =  st.columns([0.7,.3])
            df_copy_scatter = dados.copy()
            with coluna3:
                with st.expander('Selecione a quantidade de  dados a exibir'):
                    qtd_dados_scatter = st.slider("", min_value=1, max_value=len(dados), value=50, key='1')
                df_scatter = df_copy_scatter.head(qtd_dados_scatter) 
                simbol = st.selectbox('selecione o simbolo para os outlirs',['circle', 'square', 'diamond', 'cross', 'x', 'triangle-up'])
                st.write(" ")
                outliers = identificar_outliers(df_scatter, selected_column)
                color = st.color_picker('Escolhar a cor dos outlirs', '#00f900')
            with coluna2:
                fig_scatter = px.scatter(df_scatter, x=df_scatter.index, y=selected_column, title='Gráfico de Dispersão com Outliers', labels={'x': 'Índice', 'y': selected_column})
                fig_scatter.add_scatter(x=outliers.index, y=outliers[selected_column], mode='markers', name='Outliers', marker=dict(color=color, size=10, symbol=simbol))
                st.plotly_chart(fig_scatter)

        plot_outliers_scatter(selected_column) 

        def plot_outlirs_box_violion():
            coluna1, coluna2 =  st.columns([0.7,.3])
            df_copy_box_violion = dados.copy()   
            df_copy_box_violion.rename(columns={'RENDIMENTO_ANUAL':'Rendimento Anual', 'GENERO':'Gênero', 'ESCOLARIDADE':'Escolaridade', 'TIPO_DE_MORADIA':'Tipo de moradia', 'QTD_FILHOS':'Quantidade de filhos'}, inplace=True)   
            with coluna2:
                with st.expander('Selecione a quantidade de  dados a exibir'):
                  qtd_dados_box_violion = st.slider('',min_value=1, max_value=len(dados), value=50, key='2')
                tipo_grafico = st.radio(
                    "Escolha o Gráfico:",
                    ("box", "violin"))
                
                with st.expander('Filtre por:'):
                    opc = criar_radio_com_chave_unica(texto="Escolha por Filtro para o histogram:", opcoes=['Gênero', 'Faixa Etária', 'Escolaridade', 'Tipo de moradia', 'Quantidade de filhos'] ,chave= 'opcfiltro')

                # opc = criar_radio_com_chave_unica(texto="Escolha por Filtro para o histogram:", opcoes=['GENERO', 'Faixa Etária', 'Escolaridade'] ,chave= 'opcfiltro')

            with coluna1:
                # opc = criar_radio_com_chave_unica(texto="Escolha por Filtro para o histogram:", opcoes=['GENERO', 'Faixa Etária', 'Escolaridade'] ,chave= 'opcfiltro')     
                cargos_unicos = df_copy_box_violion['CARGO'].unique()
                cargo_selecionado = st.selectbox('Selecione o tipo de cargo:',cargos_unicos)
                df_cargo = df_copy_box_violion[df_copy_box_violion['CARGO'] == cargo_selecionado]
                df_cargo = df_cargo.head(qtd_dados_box_violion) 
                grafico = px.box(df_cargo,x="CARGO", y='Rendimento Anual',color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}')
                if tipo_grafico == "box":
                    grafico = px.box(df_cargo,x="CARGO", y='Rendimento Anual', color=opc, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}')
                elif tipo_grafico == "violin":
                    grafico = px.violin(df_cargo,x="CARGO", y='Rendimento Anual', color=opc,violinmode= "group", points="outliers",box= True, title=f'Distribuição de Rendimentos Anuais para {cargo_selecionado} por {opc}', )
                st.plotly_chart(grafico)

        if selected_column == 'RENDIMENTO_ANUAL':
            plot_outlirs_box_violion()

        def plot_outlirs_histogram(selected_column):
            coluna1, coluna2 =  st.columns([0.7,.3])
            df_copy_histogram = dados.copy()
            df_copy_histogram.rename(columns={'GENERO':'Gênero', 'ESCOLARIDADE':'Escolaridade', 'IDADE_ANOS':'Idade', 'QTD_FILHOS':'Quantidade de filhos'}, inplace=True)
            df_copy_histogram['IDADE_ANOS'] = df_copy_histogram['Idade'].copy()  
            with coluna2:
                with st.expander('Selecione a quantidade de  dados a exibir'):
                    qtd_dados_histogram = st.slider("Selecione a quantidade de  dados que serão exibidas:", min_value=1, max_value=len(dados), value=50, key= '3')
                
                df_histogram = df_copy_histogram.head(qtd_dados_histogram)  
                colunas_color = ['Gênero', 'Faixa Etária', 'Escolaridade', 'Idade', 'Quantidade de filhos']        
                colunas_selecionadas = st.multiselect("Selecione as colunas para colorir:", colunas_color)
                df_histogram['ColorGroup'] = df_histogram[colunas_selecionadas].apply(lambda row: ' - '.join(row.values.astype(str)), axis=1)

                #     opc1 = criar_radio_com_chave_unica(texto="Escolha por Filtro para o histogram:", opcoes=['GENERO', 'Faixa Etária', 'Escolaridade'] ,chave= 'opc1filtro')
            with coluna1:  
                fig_histogram = px.histogram(df_histogram, x=selected_column, color='ColorGroup', title='Histograma' )
                fig_histogram.update_layout(
                                                xaxis_title=f"{selected_column}",
                                                yaxis_title="Contagem"
                                            )
                st.plotly_chart(fig_histogram)
        plot_outlirs_histogram(selected_column)

    graficos_outliers(selected_column)

with aba3:
    st.subheader("Gráficos")
    fig5 = px.histogram(dados, x = 'IDADE_ANOS')
    st.plotly_chart(fig5, use_container_width=True)
    
    fig7 = px.histogram(dados, x = 'SALARIO')
    st.plotly_chart(fig7, use_container_width=True)
    
    grafico = px.scatter_matrix(dados, dimensions=['IDADE_ANOS', 'SALARIO','ESTADO_CIVIL'], color = 'TARGET')
    st.plotly_chart(grafico, use_container_width=True)
    with st.expander('Descrição'):
        st.write("grafico que mostra a relação da idade, salario mensal, estado civil com a aprovação de cartão")
    
    grafico2 = px.parallel_categories(dados, dimensions=['CARGO', 'ESTADO_CIVIL'])
    st.plotly_chart(grafico2, use_container_width=True)
    
    st.subheader("Gráfico de Barras Interativo com Filtros")
    # Filtros interativos
    idade_filter = st.slider("Selecione a faixa de idade:", min_value=20, max_value=64, value=(20, 64))
    escolaridade_filter = st.multiselect("Selecione a escolaridade:", dados["ESCOLARIDADE"].unique())
    estado_civil_filter = st.multiselect("Selecione o estado civil:", dados["ESTADO_CIVIL"].unique())
   
    # Aplicando os filtros ao DataFrame
    filtered_dados = dados[
    (dados["IDADE_ANOS"] >= idade_filter[0]) & (dados["IDADE_ANOS"] <= idade_filter[1]) &
    (dados["ESCOLARIDADE"].isin(escolaridade_filter)) &
    (dados["ESTADO_CIVIL"].isin(estado_civil_filter))
    ]
    
    fig6 = px.histogram(filtered_dados, x="GENERO", title="Distribuição de Gênero")
    st.plotly_chart(fig6, use_container_width=True)
    
    st.subheader("Gráfico de Dispersão Interativo")
    # Filtros interativos
    genero_filter = st.multiselect("Selecione o gênero:", dados["GENERO"].unique())
    estado_civil_filter2 = st.multiselect("Selecione o estado civil:", dados["ESTADO_CIVIL"].unique(), key="estado_civil_filter")

    # Aplicando os filtros ao DataFrame
    filtered_dados2 = dados[
        (dados["GENERO"].isin(genero_filter)) &
        (dados["ESTADO_CIVIL"].isin(estado_civil_filter2))
    ]

    # Criando o gráfico de dispersão interativo
    fig = px.scatter(
        filtered_dados2, 
        x="IDADE_ANOS", 
        y="RENDIMENTO_ANUAL", 
        color="GENERO", 
        symbol="ESTADO_CIVIL", 
        title="Relação entre Rendimento Anual e Idade"
    )

    # Atualizando a aparência do gráfico
    fig.update_traces(marker=dict(size=12, opacity=0.8))

    st.plotly_chart(fig, use_container_width=True)
    with st.expander("Descrição"):
        st.write("Relação entre Rendimento anual e idade com base no seu genero e estado civil")
    
    st.subheader("Gráfico de Pizza Interativo")
    # Filtros interativos
    genero_filter2 = st.multiselect("Selecione o gênero:", dados["GENERO"].unique(), key="genero_filter")
    estado_civil_filter3 = st.multiselect("Selecione o estado civil:", dados["ESTADO_CIVIL"].unique(), key="estado_civil_filter2")
    idade_filter = st.slider("Selecione a faixa de idade:", min_value=20, max_value=64, value=(20, 64), key = "idade_filter")

    # Aplicando os filtros ao DataFrame
    filtered_dados3 = dados[
        (dados["GENERO"].isin(genero_filter)) &
        (dados["ESTADO_CIVIL"].isin(estado_civil_filter)) &
        (dados["IDADE_ANOS"] >= idade_filter[0]) & (dados["IDADE_ANOS"] <= idade_filter[1])
    ]

    # Calculando as proporções
    carro_counts = filtered_dados3["POSSUI_CARRO"].value_counts()
    propriedade_counts = filtered_dados3["POSSUI_PROPRIEDADES"].value_counts()

    # Criando o gráfico de pizza interativo
    fig_carro = px.pie(
        names=carro_counts.index, 
        values=carro_counts.values, 
        title="Proporção de Pessoas que Possuem Carro"
    )

    fig_propriedade = px.pie(
        names=propriedade_counts.index, 
        values=propriedade_counts.values, 
        title="Proporção de Pessoas que Possuem Propriedade"
    )

    # Atualizando a aparência dos gráficos
    fig_carro.update_traces(textinfo="percent+label", 
                            pull=[0.1, 0], 
                            marker=dict(line=dict(color="#000000", width=2)),
                            textfont_size=20,
                            textfont_color="white",
                            textposition="inside")
    fig_propriedade.update_traces(textinfo="percent+label", 
                                  pull=[0.1, 0], 
                                  marker=dict(line=dict(color="#000000", width=2)),
                                  textfont_size=20,
                                  textfont_color="white",
                                  textposition="inside")

    # Exibindo os gráficos
    st.plotly_chart(fig_carro, use_container_width=True)
    st.plotly_chart(fig_propriedade, use_container_width=True)
    
    # Filtros interativos
    st.subheader("Gráfico de Barras Empilhadas Interativo")
    moradia_filter = st.multiselect("Selecione o tipo de moradia:", dados["TIPO_DE_MORADIA"].unique(), key="moradia_filter")
    escolaridade_filter = st.multiselect("Selecione o nível de escolaridade:", dados["ESCOLARIDADE"].unique(), key="escolaridade_filter")

    # Aplicando os filtros ao DataFrame
    filtered_dados4 = dados[
        (dados["TIPO_DE_MORADIA"].isin(moradia_filter)) &
        (dados["ESCOLARIDADE"].isin(escolaridade_filter))
    ]

    # Criando o gráfico de barras empilhadas interativo
    fig8 = px.bar(
        filtered_dados4, 
        x="ESTADO_CIVIL", 
        color="GENERO", 
        title="Distribuição de Gênero em Diferentes Estados Civis",
        labels={"Estado Civil": "Estado Civil"}
    )

    # Atualizando a aparência do gráfico
    fig8.update_layout(barmode="stack")

    # Exibindo o gráfico
    st.plotly_chart(fig8, use_container_width=True)
    
    st.subheader('Gráfico de Barras - Relação entre Target e Estado Civil')
    fig9 = px.bar(
        dados,
        x="ESTADO_CIVIL",
        color="TARGET",
        title="Relação entre Target e Estado Civil",
        labels={"ESTADO_CIVIL": "Estado Civil", "TARGET": "Alvo"}
    )

    # Exibindo o gráfico
    st.plotly_chart(fig9, use_container_width=True)
    
    
    st.subheader("Gráfico de Dispersão - Rendimento Anual vs. Idade (Colorido por Target)")
    # Filtro interativo para selecionar a cor (TARGET)
    color_filter = st.selectbox("Selecione a coluna para colorir:", dados.columns, key="color_filter")

    # Criando o gráfico de dispersão interativo
    fig10 = px.scatter(
        dados,
        x="IDADE_ANOS",
        y="RENDIMENTO_ANUAL",
        color=color_filter,
        title="Rendimento Anual vs. Idade (Colorido por Target)",
        labels={"IDADE_ANOS": "Idade (anos)", "RENDIMENTO_ANUAL": "Rendimento Anual"}
    )

    # Exibindo o gráfico
    st.plotly_chart(fig10, use_container_width=True)
    
    
    st.subheader("Gráfico de Dispersão - Rendimento Anual X Cargo")
    # Filtro interativo para selecionar a cor (TARGET)
    color_filter2 = st.selectbox("Selecione a coluna para colorir:", dados.columns, key="color_filter2")

    # Criando o gráfico de dispersão interativo
    fig14 = px.scatter(
        dados,
        x="CARGO",
        y="RENDIMENTO_ANUAL",
        color=color_filter2,
        title="Rendimento Anual x Cargo",
        labels={"CARGO": "cargo", "RENDIMENTO_ANUAL": "Rendimento Anual"}
    )

    # Exibindo o gráfico
    st.plotly_chart(fig14, use_container_width=True)
    
    
    st.subheader("Gráfico de Dispersão - Distribuição de Escolaridade por Target")

    # Filtro interativo para selecionar a cor (TARGET)
    color_filter = st.selectbox("Selecione a coluna para colorir:", dados.columns, key="color_filter1")

    # Criando o gráfico de dispersão interativo
    fig11 = px.bar(
        dados,
        x="ESCOLARIDADE",
        color=color_filter,
        title="Distribuição de Escolaridade por Target",
        labels={"TARGET": "Target", "ESCOLARIDADE": "Escolaridade"},
        orientation='v'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig11, use_container_width=True)
    
    st.subheader("Gráfico de barras - Distribuição de gênero por Target")
    fig12 = px.bar(
        dados,
        x="GENERO",
        color="TARGET",
        title="Proporção de Gênero por Target",
        labels={"TARGET": "Target", "GENERO": "Gênero"},
        orientation='v'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig12, use_container_width=True)
    
    st.subheader("Gráfico de barras - Distribuição de cargo por Target")
    fig13 = px.bar(
    dados,
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
    dados,
    x="POSSUI_PROPRIEDADES",
    color="TARGET",
    title="Proporção de possui proriedade por Target",
    labels={"TARGET": "Target", "POSSUI_PROPRIEDADES": "Possui propriedade"},
    orientation='v'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig13, use_container_width=True)