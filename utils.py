import pandas as pd
import numpy as np
import seaborn as sns
from imblearn.over_sampling import SMOTE
df = pd.read_parquet("./data/credit_card_approval.parquet")
df = df.sort_values(by="ID")
col_em_ing  = list(df.columns)

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
    "DIAS_ANIVERSARIO",
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

df.columns = new_columns
df["GENERO"].replace({"F": 0, "M": 1}, inplace=True)
df["POSSUI_CARRO"].replace({"Y": 1, "N": 0}, inplace=True)
df["POSSUI_PROPRIEDADES"].replace({"Y": 1, "N": 0}, inplace=True)
df["DIAS_ANIVERSARIO"] = np.ceil(
    pd.to_timedelta(df["DIAS_ANIVERSARIO"], unit="D").dt.days * (-1)
)
df["POSSUI_EMPREGO"] = np.where(df["POSSUI_EMPREGO"] < 0, 1, 0)
df["QTD_MESES"] = np.ceil(pd.to_timedelta(df["QTD_MESES"], unit="D").dt.days * (-1))
df["STATUS_PAGAMENTO"].replace(
    {"C": 1, "X": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
    inplace=True,
)
col_em_pt = list(df.columns)
tipo_dados = list(df.dtypes) 
#Técnica One-Hot
tipos_de_profissao = pd.get_dummies(df["CARGO"])
tipos_estado_civil = pd.get_dummies(df["ESTADO_CIVIL"])
tipos_de_moradia = pd.get_dummies(df["TIPO_DE_MORADIA"])
tipos_escolaridade = pd.get_dummies(df["ESCOLARIDADE"])
qtda_filhos = pd.get_dummies(df["QTD_FILHOS"])
df = pd.concat([df, tipos_de_profissao, tipos_estado_civil, tipos_de_moradia, tipos_escolaridade, qtda_filhos], axis= 1)
 
# # AVALIANDO CLIENTE
# media_pagamentos = df.groupby("ID")["STATUS_PAGAMENTO"].mean().reset_index()
# media_pagamentos.rename(columns={"STATUS_PAGAMENTO": "MEDIA_PAGAMENTO"}, inplace=True)
# df = df.merge(media_pagamentos, on="ID", suffixes=("", "_Media"))
# df["BOM_CLIENTE"] = df["MEDIA_PAGAMENTO"].apply(lambda media: 1 if media >= 0.6 else 0)


del df["CARGO"], df['ESCOLARIDADE'], df['ESTADO_CIVIL'], df['QTD_FILHOS'], df['TIPO_DE_MORADIA']


#Target desbalanceado que veio do dataset
ax = sns.countplot(x='TARGET', data=df) 
ax.set_title('Target desbalanceado')
#plt.show()

#Target balanceado com SMOTE
X = df.drop('TARGET', axis = 1)
y = df['TARGET']
smt = SMOTE(random_state=123)  # Instancia um objeto da classe SMOTE
X, y = smt.fit_resample(X, y)  # Realiza a reamostragem do conjunto de dados
df = pd.concat([X, y], axis=1)    
ax2 = sns.countplot(x='TARGET', data=df)
ax2.set_title('Target balanceado com SMOTE')
#plt.show()
print(df['TARGET'].value_counts())
dados = df.drop(
    columns=[
        "ID",
        "GENERO",
        "DIAS_ANIVERSARIO",
        "CELULAR",
        "TELEFONE_COMERCIAL",
        "TELEFONE_RESIDENCIAL",
        "EMAIL",
        "QTD_MESES",
        "STATUS_PAGAMENTO"
    ]
) 
def texto(filtro_qtd_meses):
    if filtro_qtd_meses == 0:
        return "no mês atual"
    elif filtro_qtd_meses == 1:
        return f"no último mês"
    else:
        return f"nos últimos {filtro_qtd_meses} meses"
