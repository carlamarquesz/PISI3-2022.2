from utils import *
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.svm import SVC
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

# execução do classificador SVM
classificador_svm = SVC(kernel='linear', C=1.0, random_state=123)
y_pred_svm = executar_classificador(
    classificador_svm, X_train, X_test, y_train
)

# validação SVM
acuracia_svm, precisao_svm, recall_svm, matrix_confusao_svm = validar_modelo(y_test, y_pred_svm)

# Resultados do SVM
print("Resultados do SVM:")
print("Acurácia: ", acuracia_svm)
print("Precisão: ", precisao_svm)
print("Recall: ", recall_svm)
print("Matriz de Confusão do SVM: \n", matrix_confusao_svm)
