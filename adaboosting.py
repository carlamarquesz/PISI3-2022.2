from utils import *  
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np 

# Função para separar os dados em treino e teste
def executar_validador(X, y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
    for treino_id, teste_id in validador.split(X, y):
        X_train, X_test = X[treino_id], X[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return X_train, X_test, y_train, y_test

# Função para salvar a árvore do classificador AdaBoost
def salvar_arvore(classificador, nome):
    plt.figure(figsize=(200, 100))
    tree.plot_tree(classificador, filled=True, fontsize=14)
    plt.savefig(nome)
    plt.close()

# Função para prever o resultado da análise de crédito
def executar_classificador(classificador, X_train, X_test, y_train):
    arvore = classificador.fit(X_train, y_train)
    y_pred = arvore.predict(X_test)
    return y_pred

# Função para executar as métricas de validação
def validar_arvore(y_test, y_pred):
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return acuracia, precisao, recall, matrix_confusao


# Função para calcular as importâncias médias das características
def atributos_importantes(classificador):
    importancias_caracteristicas = [arvore.feature_importances_ for arvore in classificador.estimators_]
    importancias_medias = np.mean(importancias_caracteristicas, axis=0)
    return importancias_medias

# Execução do pré-processamento dos dados
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)

# Instanciando o classificador e prevendo o resultado
classificador_adaboost = AdaBoostClassifier(random_state=0, n_estimators=200)
y_pred_adaboost = executar_classificador(classificador_adaboost, X_train, X_test, y_train)

# Validação do resultado
acuracia, precisao, recall, matrix_confusao = validar_arvore(y_test, y_pred_adaboost)
print(dados.columns)


# Cálculo médias dos atributos importantes
importancias_medias = atributos_importantes(classificador_adaboost)
print(importancias_medias) 

#Classificando os clientes mais propensos a receberem crédito
probabilidades = classificador_adaboost.predict_proba(X_test)[:, 1]
clientes_ordenados = np.argsort(probabilidades)[::-1]
limiar = 0.5
clientes_propensos = clientes_ordenados[probabilidades[clientes_ordenados] > limiar]
print("Clientes mais propensos:", clientes_propensos) 

# Salvando a imagem da árvore simples 
# salvar_arvore(classificador_adaboost.estimators_[0], "adaboost1")
# salvar_arvore(classificador_adaboost.estimators_[1], "adaboost2")

