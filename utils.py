import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from imblearn.under_sampling import RandomUnderSampler

# Função para carregar e pré-processar o DataFrame
def carregar_e_preprocessar_dados():
    df = pd.read_parquet("./data/credit_card_approval.parquet")
    new_columns = [
        "ID",
        "GENERO",
        "POSSUI CARRO", 
        "POSSUI PROPRIEDADES",
        "QUANTIDADE DE FILHOS",
        "RENDIMENTO ANUAL",
        "ESCOLARIDADE",
        "ESTADO CIVIL",
        "TIPO DE MORADIA",
        "IDADE",
        "POSSUI EMPREGO",
        "CELULAR",
        "TELEFONE COMERCIAL",
        "TELEFONE RESIDENCIAL",
        "EMAIL",
        "CARGO",
        "MESES",
        "STATUS PAGAMENTO",
        "TARGET",
    ]
    df.columns = new_columns
    df["GENERO"].replace({"F": 0, "M": 1}, inplace=True)
    df["POSSUI CARRO"].replace({"Y": 1, "N": 0}, inplace=True)
    df["POSSUI PROPRIEDADES"].replace({"Y": 1, "N": 0}, inplace=True)
    df["IDADE"] = (df["IDADE"] / -365.25).round(0).astype(int)
    df["POSSUI EMPREGO"] = np.where(df["POSSUI EMPREGO"] < 0, 1, 0)
    df["MESES"] = np.ceil(pd.to_timedelta(df["MESES"], unit="D").dt.days * (-1))
    df["STATUS PAGAMENTO"].replace(
        {"C": 1, "X": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
        inplace=True,
    ) 
    
    return df

# Função para realizar a técnica de One-Hot Encoding
def aplicar_one_hot_encoding(df):
    tipos_de_profissao = pd.get_dummies(df["CARGO"])
    tipos_estado_civil = pd.get_dummies(df["ESTADO CIVIL"])
    tipos_de_moradia = pd.get_dummies(df["TIPO DE MORADIA"])
    tipos_escolaridade = pd.get_dummies(df["ESCOLARIDADE"])
    qtda_filhos = pd.get_dummies(df["QUANTIDADE DE FILHOS"])
    
    df = pd.concat([df, tipos_de_profissao, tipos_estado_civil, tipos_de_moradia, tipos_escolaridade, qtda_filhos], axis=1)
    del df["CARGO"], df['ESCOLARIDADE'], df['ESTADO CIVIL'], df['QUANTIDADE DE FILHOS'], df['TIPO DE MORADIA']
    
    return df

# Função para balancear os dados usando undersampling
def balancear_dados(df):
    X = df.drop('TARGET', axis = 1)
    y = df['TARGET']
    rus = RandomUnderSampler(random_state=0)
    X_resampled, y_resampled = rus.fit_resample(X, y)
    df = pd.concat([X_resampled, y_resampled], axis=1)
    print(df['TARGET'].value_counts())
    return df

# Função para identificar outliers
def identificar_outliers(df, column):
    z_scores = (df[column] - df[column].mean()) / df[column].std()
    threshold = 2.5
    outliers = df[abs(z_scores) > threshold]
    return outliers

# Função para filtrar texto 
def texto_filtro(filtro_qtd_meses): 
    if filtro_qtd_meses == 0:
        return "no mês atual"
    elif filtro_qtd_meses == 1:
        return f"no último mês"
    else:
        return f"nos últimos {filtro_qtd_meses} meses"

df = carregar_e_preprocessar_dados()
df = df.sort_values(by="ID")
col_em_ing  = list(df.columns)
col_em_pt = list(df.columns)
tipo_dados = list(df.dtypes) 
df = aplicar_one_hot_encoding(df)
df = balancear_dados(df) 
dados = df.drop(
    columns=[
        "ID",  
        "CELULAR",
        "TELEFONE COMERCIAL",
        "TELEFONE RESIDENCIAL",
        "EMAIL",
        "MESES",
        "STATUS PAGAMENTO"
    ]
)    