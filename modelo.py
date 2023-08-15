from utils import *
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt 

def executar_validador(X, y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=123)
    for treino_id, teste_id in validador.split(X, y):
        X_train, X_test = X[treino_id], X[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return X_train, X_test, y_train, y_test

def executar_classificador(classificador, X_train, X_test, y_train):
    modelo = classificador.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    return y_pred

def validar_modelo(y_test, y_pred):
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return acuracia, precisao, recall, matrix_confusao 

# execução do validador
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)

# execução do classificador Naïve Bayes
classificador_naive_bayes = GaussianNB()
y_pred_naive_bayes = executar_classificador(
    classificador_naive_bayes, X_train, X_test, y_train
)

# validação Naïve Bayes
acuracia_naive_bayes, precisao_naive_bayes, recall_naive_bayes, matrix_confusao_naive_bayes = validar_modelo(y_test, y_pred_naive_bayes)

# Resultados do Naïve Bayes
print("Resultados do Naïve Bayes:")
print("Acurácia: ", acuracia_naive_bayes)
print("Precisão: ", precisao_naive_bayes)
print("Recall: ", recall_naive_bayes)
print("Matriz de Confusão do Naïve Bayes: \n", matrix_confusao_naive_bayes)
