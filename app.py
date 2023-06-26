from utils import *
import streamlit as st
import plotly.express as px 

st.set_page_config(layout="wide")
# Dashboard
st.title("Dashboard CT Credit")
st.subheader("Estatísticas gerais")
coluna1, coluna2, coluna3, coluna4 = st.columns(4)
with coluna1:
    st.metric("Não pediram empréstimo \n\nno mês atual", len(dados_filtrados_1))
    st.metric("Estão em dia com \n\no empréstimo", len(dados_filtrados_2))
with coluna2:
    st.metric("Estão com empréstimo \n\nvencido", len(dados_filtrados_3))
    st.metric("Estão com 120 a 149 dias \n\nde atraso", len(dados_filtrados_4))

with coluna3:
    st.metric("Estão com 90 a 119 dias \n\nde atraso", len(dados_filtrados_5))
    st.metric("Estão com 60 a 89 dias \n\nde atraso", len(dados_filtrados_6))
with coluna4:
    st.metric("Estão com 30 à 59 dias \n\nde atraso", len(dados_filtrados_7))
    st.metric("Estão com 1 a 29 dias \n\nde atraso", len(dados_filtrados_8))
st.subheader("Database")
col1, col2 = st.columns([4, 2])
with col1:
    st.caption("Dados de pessoas que solicitaram empréstimo")
    st.write(data)
with col2:
    st.caption("Dados de pessoas com pagamento em dia")
    st.write(data2)
st.subheader("Gráficos")
col1, col2 = st.columns([4, 2])
with col1:
    st.caption("Cargo de pessoas que solicitam empréstimo")
    chart_data = pd.DataFrame({"Qtd de pessoas": data.groupby("CARGO")["ID"].nunique()})
    st.bar_chart(chart_data, use_container_width=True)
with col2:
    st.caption("Empregados vs desempregados")
    chart_data2 = pd.DataFrame(
        {"Qtd de pessoas": data.groupby("POSSUI_EMPREGO")["ID"].nunique()}
    )
    st.bar_chart(chart_data2, use_container_width=True) 

