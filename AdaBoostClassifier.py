from utils import *  
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score
from sklearn import tree 
import matplotlib.pyplot as plt 



def executar_validador(X, y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
    for treino_id, teste_id in validador.split(X, y):
        X_train, X_test = X[treino_id], X[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return X_train, X_test, y_train, y_test


def salvar_arvore(classificador, nome):
    plt.figure(figsize=(200, 100))
    tree.plot_tree(classificador, filled=True, fontsize=14)
    plt.savefig(nome)
    plt.close()


def executar_classificador(classificador, X_train, X_test, y_train):
    arvore = classificador.fit(X_train, y_train)
    y_pred = arvore.predict(X_test)
    return y_pred

def validar_arvore(y_test, y_pred):
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return acuracia, precisao, recall, matrix_confusao 

# execucao do validador
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)

# execucao do classificador DecisionTreeClassifier
classificador_adaboost = AdaBoostClassifier(random_state=0, n_estimators=200)
y_pred_adaboost = executar_classificador(classificador_adaboost, X_train, X_test, y_train)

# validacao arvore de decisao
acuracia,precisao,recall,matrix_confusao = validar_arvore(y_test, y_pred_adaboost)
print(dados.columns)  

# salvar_arvore(classificador_adaboost.estimators_[0], "adaboost1")
# salvar_arvore(classificador_adaboost.estimators_[1], "adaboost2")

# criacao da figura da arvore de decisao
#salvar_arvore(classificador_arvore_decisao, "arvore_decisao.png")

importancias_caracteristicas = []

# Loop através de cada árvore no ensemble
for arvore in classificador_adaboost.estimators_:
    importancias_caracteristicas.append(arvore.feature_importances_)

# Calcular a média das importâncias das características de todas as árvores
importancias_medias = np.mean(importancias_caracteristicas, axis=0)

# Agora você tem as importâncias médias das características
print(importancias_medias)

# Ordenação por Probabilidade
probabilidades = classificador_adaboost.predict_proba(X_test)[:, 1]
clientes_ordenados = np.argsort(probabilidades)[::-1]

# Definição de Limiar
limiar = 0.5  # Defina o limiar com base nos objetivos da instituição financeira

# Identificação dos Clientes Propensos
clientes_propensos = clientes_ordenados[probabilidades[clientes_ordenados] > limiar]

# Índices dos clientes mais propensos a realizar uma solicitação de crédito
print("Clientes mais propensos:", clientes_propensos)