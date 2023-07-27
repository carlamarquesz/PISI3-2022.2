import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from imblearn.over_sampling import SMOTE

# Reorganizando os dados credit_card_approval para ML
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

def texto(filtro_qtd_meses):
    if filtro_qtd_meses == 0:
        return 'no mês atual'
    elif filtro_qtd_meses == 1:
        return f'no último mês'
    else:
        return f'nos últimos {filtro_qtd_meses} meses'

# print(df.sort_values("ID"))
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
print(df.head(2))
df = df.drop(columns=['ID', 'GENERO', 'DIAS_ANIVERSARIO', 'CELULAR', 'TELEFONE_COMERCIAL', 'TELEFONE_RESIDENCIAL', 'EMAIL', 'QTD_MESES'])
print(df.head(2))
Xmaria = [[1,1,2,42000,1,4,2,1,8,1]]
#Divisão em inputs e outputs
X = df.drop('TARGET', axis = 1)
y = df['TARGET']

from sklearn.preprocessing import StandardScaler
norm = StandardScaler() 
X_normalizado = norm.fit_transform(X)  #Normalização dos dados

from sklearn.model_selection import train_test_split  
X_treino, X_teste, y_treino, y_teste = train_test_split(X_normalizado, y, test_size=0.3, random_state=123)   #Divisão em treino e teste

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion='entropy', random_state=42)
dtc.fit(X_treino, y_treino)
dtc.feature_importances_
predito_ArvoreDecisao = dtc.predict(X_teste)
print(predito_ArvoreDecisao) #Predição do modelo Árvore de Decisão


from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_teste, predito_ArvoreDecisao)) #Matriz de confusão

from sklearn.metrics import accuracy_score
print(accuracy_score(y_teste, predito_ArvoreDecisao)) #Acurácia

from sklearn.metrics import precision_score
print(precision_score(y_teste, predito_ArvoreDecisao)) #Precisão

from sklearn.metrics import recall_score
print(recall_score(y_teste, predito_ArvoreDecisao)) #Recall, serve para saber a taxa de acerto dos positivos

print('Modelo Árvore de Decisão: ', precision_score(y_teste, predito_ArvoreDecisao)) #Precisão

