import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px

# Reorganizando os dados application_record
data = pd.read_csv("./data/application_record.csv")
novos_nomes = ['id_pessoa', 'genero', 'tem_carro', 'tem_propriedade', 'qtd_filhos', 'rendimento_anual', 'categoria_de_renda', 'escolaridade', 'estado_civil', 'modo_de_viver', 'aniversario','tem_emprego', 'telefone_movel', 'telefone_comercial', 'telefone', 'email', 'ocupacao', 'tam_familia']
data.columns = novos_nomes
data['tem_emprego'] = np.where(data['tem_emprego'] < 0, 'Sim', 'Não')
data['tem_propriedade'].replace({'N': 0, 'Y': 1}, inplace=True)
data['tem_carro'].replace({'N': 0, 'Y': 1}, inplace=True) 
df = data[['id_pessoa','tem_carro','tem_propriedade', 'qtd_filhos','rendimento_anual', 'categoria_de_renda', 'escolaridade', 'estado_civil','modo_de_viver','tem_emprego','ocupacao','tam_familia']] 

# Reorganizando os dados credit_record
data2 = pd.read_csv("./data/credit_record.csv")
novos_nomes2 = ['id_pessoa', 'mes_extraido_dados', 'pag_atraso_emprestimo']
data2.columns = novos_nomes2 
dados_filtrados_1 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == 'X')]
dados_filtrados_2 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == 'C')] 
dados_filtrados_3 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == '5')] 
dados_filtrados_4 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == '4')] 
dados_filtrados_5 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == '3')] 
dados_filtrados_6 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == '2')] 
dados_filtrados_7 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == '1')] 
dados_filtrados_8 = data2.loc[(data2['mes_extraido_dados'] == 0) & (data2['pag_atraso_emprestimo'] == '0')]  


#Dashboard
st.title("Dashboard CT Credit")
st.subheader("Estatísticas gerais")
coluna1,coluna2,coluna3,coluna4 = st.columns(4)
with coluna1:
    st.metric('Não pediram empréstimo \n\nno mês atual', len(dados_filtrados_1))
    st.metric('Estão em dia com \n\no empréstimo', len(dados_filtrados_2)) 
with coluna2:
    st.metric('Estão com empréstimo \n\nvencido', len(dados_filtrados_3))
    st.metric('Estão com 120 a 149 dias \n\nde atraso', len(dados_filtrados_4)) 
    
with coluna3:
    st.metric('Estão com 90 a 119 dias \n\nde atraso', len(dados_filtrados_5))
    st.metric('Estão com 60 a 89 dias \n\nde atraso', len(dados_filtrados_6))
with coluna4:
    st.metric('Estão com 30 à 59 dias \n\nde atraso', len(dados_filtrados_7))
    st.metric('Estão com 1 a 29 dias \n\nde atraso', len(dados_filtrados_8))  
st.subheader("Database")
col1,col2 = st.columns([4, 2])
with col1:
    st.caption('Dados de pessoas que solicitaram empréstimo')
    st.write(df) 
with col2:
    st.caption('Dados de pessoas com pagamento em dia')
    st.write(data2)  
st.subheader("Gráficos")
col1,col2 = st.columns([4, 2])
with col1: 
    st.caption('Cargo de pessoas que solicitam empréstimo')
    chart_data = pd.DataFrame({'Qtd de pessoas': df.groupby('ocupacao')['id_pessoa'].nunique()})
    st.bar_chart(chart_data)
with col2: 
    st.caption('Empregados vs desempregados')
    chart_data2 = pd.DataFrame({'Qtd de pessoas': df.groupby('tem_emprego')['id_pessoa'].nunique()})
    st.bar_chart(chart_data2)
