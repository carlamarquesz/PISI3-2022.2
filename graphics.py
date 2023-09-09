import numpy as np
import pandas as pd 

# Dados qualitativos para usar nos gráficos
dados = pd.read_csv("./data/credit_card_approval.csv")
# dados = pd.read_parquet("./data/credit_card_approval.parquet")


new_columns = [
    "ID",
    "GENERO",
    "POSSUI_CARRO",
    "POSSUI_PROPRIEDADES",
    "QTD_FILHOS",
    "RENDIMENTO_ANUAL",
    "ESCOLARIDADE",
    "ESTADO_CIVIL",
    "TIPO_DE_MORADIA",
    "IDADE_ANOS",
    "POSSUI_EMPREGO",
    "CELULAR",
    "TELEFONE_COMERCIAL",
    "TELEFONE_RESIDENCIAL",
    "EMAIL",
    "CARGO",
    "QTD_MESES",
    "STATUS_PAGAMENTO",
    "TARGET",
]
dados.columns = new_columns   
dados['STATUS2'] = dados['STATUS_PAGAMENTO'].copy()
dados["STATUS2"].replace(
            {"C": 0, "X": 0, "0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1},
            inplace=True,
        )
# dados["QTD_MESES"] = np.ceil(pd.to_timedelta(dados["QTD_MESES"], unit="D").dt.days * (-1))
dados["IDADE_ANOS"] = (dados["IDADE_ANOS"] / -365.25).round(0).astype(int)
dados["VARIAVEL_TARGET"] = dados["TARGET"].copy()
dados["VARIAVEL_TARGET"].replace(
            {0:'Cliente de baixo risco', 1:'Cliente de risco'},
            inplace=True)
dados["ANOS_EMPREGADO"] = dados["POSSUI_EMPREGO"].copy()
dados["ANOS_EMPREGADO"] = (dados["ANOS_EMPREGADO"] / -365.25).round(0).astype(int)
dados["POSSUI_CARRO"].replace({"Y": 'Sim', "N": 'Não'}, inplace=True)
dados["POSSUI_PROPRIEDADES"].replace({"Y": 'Sim', "N": 'Não'}, inplace=True)
dados["TELEFONE_COMERCIAL"].replace({1: 'Sim', 0: 'Não'}, inplace=True)
dados["TELEFONE_RESIDENCIAL"].replace({1: 'Sim', 0: 'Não'}, inplace=True)
dados["EMAIL"].replace({1: 'Sim', 0: 'Não'}, inplace=True)
dados["POSSUI_CARRO"].replace({"Y": 'Sim', "N": 'Não'}, inplace=True)
dados["POSSUI_PROPRIEDADES"].replace({"Y": 'Sim', "N": 'Não'}, inplace=True),

dados["STATUS_PAGAMENTO"].replace(
    {"C": 'pago no prazo', "X": 'Não aplicável', "0": '1-29 dias de atraso', "1": '30-59 dias de atraso', "2": '60-89 dias de atraso', "3": '90-119 dias de atraso', "4": '120-149 dias de atraso', "5": '150+ dias de atraso'},
    inplace=True,
)

dados["QTD_FILHOS"].replace(
    {"No children": 'Sem filhos', "1 children": '1 filho', "2+ children": '2+ filhos'}, inplace=True
)

dados["ESCOLARIDADE"].replace(
    {
        "Higher education": "Ensino Superior",
        "Secondary / secondary special": "Secundário / secundário especial",
        "Incomplete higher": "Incompleto superior",
        "Lower secondary": "Secundário inferior",
        "Academic degree": "Grau académico",
    },
    inplace=True,
)

dados["ESTADO_CIVIL"].replace(
    {
        "Civil marriage": 'Casamento civil',
        "Married": 'Casado(a)',
        "Single / not married": 'Solteiro / Não casado',
        "Separated": 'Separado(a)',
        "Widow": 'Viúvo/Viúva',
    },
    inplace=True,
)

dados["TIPO_DE_MORADIA"].replace(
    {
        "Rented apartment": 'Apartamento alugado',
        "House / apartment": 'Casa / Apartamento',
        "Municipal apartment": 'Apartamento municipal',
        "With parents": 'Com os pais',
        "Co-op apartment": 'Apartamento cooperativo',
        "Office apartment": 'Apartamento de escritório',
    },
    inplace=True,
)

dados["CARGO"].replace(
    {
        "Security staff": "Equipe de Segurança",
        "Sales staff": "Equipe de Vendas",
        "Accountants": "Contadores",
        "Laborers": "Trabalhadores",
        "Managers": "Gerentes",
        "Drivers": "Motoristas",
        "Core staff": "Equipe Principal",
        "High skill tech staff": "Equipe Técnica de Alta Habilidade",
        "Cleaning staff": "Equipe de Limpeza",
        "Private service staff": "Equipe de Serviço Privado",
        "Cooking staff": "Equipe de Cozinha",
        "Low-skill Laborers": "Trabalhadores de Baixa Qualificação",
        "Medicine staff": "Equipe de Medicina",
        "Secretaries": "Secretários",
        "Waiters/barmen staff": "Equipe de Garçons/Barmen",
        "HR staff": "Equipe de Recursos Humanos",
        "Realty agents": "Agentes Imobiliários",
        "IT staff": "Equipe de TI",
    },
    inplace=True,
)

# # Criando a coluna de faixas etárias
bins = [17, 30, 50, float('inf')]  
labels = ['18-30', '31-50', '51+']
dados['FAIXA_ETARIA'] = pd.cut(dados['IDADE_ANOS'], bins=bins, labels=labels)
dados["QTD_MESES"] = (dados["QTD_MESES"] * (-1))
## Nova coluna a ser criada
dados['SALARIO'] = dados['RENDIMENTO_ANUAL'] / 12



def criar_radio_com_chave_unica(texto, opcoes, chave):
    import streamlit as st
    return st.radio(texto, opcoes, key=chave)


df_att = dados.copy()

df_att = df_att.drop(columns='QTD_MESES')
# df_eda.loc[df_eda.duplicated(keep=False)]
df_att = df_att.drop_duplicates()


df_eda = df_att.copy()
df_analise_risco = df_att.copy()
df_analise_financeira = df_att.copy()

