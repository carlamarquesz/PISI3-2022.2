from utils import *  
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt 

# Função para separar os dados em treino e teste
def executar_validador(X, y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=123)
    for treino_id, teste_id in validador.split(X, y):
        X_train, X_test = X[treino_id], X[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return X_train, X_test, y_train, y_test

# Função para prever o resultado da análise de crédito usando SVM
def executar_classificador_svm(X_train, X_test, y_train):
    svm_classifier = SVC(kernel='linear', C=1.0, random_state=123)
    svm_classifier.fit(X_train, y_train)
    y_pred = svm_classifier.predict(X_test)
    return y_pred

# Função para executar as métricas de validação
def validar_svm(y_test, y_pred):
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return acuracia, precisao, recall, matrix_confusao 

#  Execução do pré-processamento dos dados
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)

# Instanciando o classificador SVM e prevendo o resultado
svm_classifier = SVC(kernel='linear', C=1.0, random_state=123)
y_pred_svm = executar_classificador_svm(X_train, X_test, y_train)

# Validando o resultado
acuracia, precisao, recall, matrix_confusao = validar_svm(y_test, y_pred_svm)
print(dados.columns)
