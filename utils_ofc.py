import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from imblearn.over_sampling import SMOTE

# Reorganizando os dados application_record
df = pd.read_csv("./data/credit_card_approval.csv")
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
df["QTD_FILHOS"].replace(
    {"No children": 0, "1 children": 1, "2+ children": 2}, inplace=True
)
df["ESCOLARIDADE"].replace(
    {
        "Higher education": 1,
        "Secondary / secondary special": 2,
        "Incomplete higher": 3,
        "Lower secondary": 4,
        "Academic degree": 5,
    },
    inplace=True,
)
df["ESTADO_CIVIL"].replace(
    {
        "Civil marriage": 1,
        "Married": 2,
        "Single / not married": 3,
        "Separated": 4,
        "Widow": 5,
    },
    inplace=True,
)
df["TIPO_DE_MORADIA"].replace(
    {
        "Rented apartment": 1,
        "House / apartment": 2,
        "Municipal apartment": 3,
        "With parents": 4,
        "Co-op apartment": 5,
        "Office apartment": 6,
    },
    inplace=True,
)
df["DIAS_ANIVERSARIO"] = np.ceil(
    pd.to_timedelta(df["DIAS_ANIVERSARIO"], unit="D").dt.days * (-1)
)
df["POSSUI_EMPREGO"] = np.where(df["POSSUI_EMPREGO"] < 0, 1, 0)
df["CARGO"].replace(
    {
        "Security staff": 1,
        "Sales staff": 2,
        "Accountants": 3,
        "Laborers": 4,
        "Managers": 5,
        "Drivers": 6,
        "Core staff": 7,
        "High skill tech staff": 8,
        "Cleaning staff": 9,
        "Private service staff": 10,
        "Cooking staff": 11,
        "Low-skill Laborers": 12,
        "Medicine staff": 13,
        "Secretaries": 14,
        "Waiters/barmen staff": 15,
        "HR staff": 16,
        "Realty agents": 17,
        "IT staff": 18,
    },
    inplace=True,
)
df["QTD_MESES"] = np.ceil(pd.to_timedelta(df["QTD_MESES"], unit="D").dt.days * (-1))
df["STATUS_PAGAMENTO"].replace(
    {"C": 1, "X": 1, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
    inplace=True,
)

print(df.sort_values("ID"))
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
