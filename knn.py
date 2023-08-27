from utils import *
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
)

# execucao do validador
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values


def executar_validador(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=123
    )
    return X_train, X_test, y_train, y_test


def preprocess_data(X):
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    return X_normalized


def executar_classificador(classificador, X_train, X_test, y_train):
    classificador.fit(X_train, y_train)
    y_pred = classificador.predict(X_test)
    return y_pred


def validar_knn(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return accuracy, precision, recall, matrix_confusao


# Dividir os dados em treinamento e teste usando a função de validação
X, y = dados.drop("TARGET", axis=1).values, dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)

# Pré-processamento dos dados
X_train_normalized = preprocess_data(X_train)
X_test_normalized = preprocess_data(X_test)

# Busca em grade para encontrar o melhor valor para n_neighbors
param_grid = {"n_neighbors": [3, 5, 7, 9, 11]}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring="accuracy")
grid_search.fit(X_train_normalized, y_train)
best_n_neighbors = grid_search.best_params_["n_neighbors"]

print("Melhor número de vizinhos:", best_n_neighbors)

# Treinar o modelo KNN usando a função de classificação com o melhor n_neighbors
classificador_knn = KNeighborsClassifier(
    metric="euclidean", n_neighbors=best_n_neighbors
)
y_pred_knn = executar_classificador(
    classificador_knn, X_train_normalized, X_test_normalized, y_train
)

# Validar o modelo KNN usando a função de validação
acuracia, precisao, recall, matrix_confusao = validar_knn(
    classificador_knn, X_test_normalized, y_test
)
