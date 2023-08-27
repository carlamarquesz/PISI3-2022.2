from utils import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import BernoulliNB
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


def validar_bnb(y_test, y_pred):
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

smote = SMOTE(random_state=0)
X_resampled_smote, y_resampled_smote = smote.fit_resample(X_train_normalized, y_train)

# Treinar o modelo Naive Bayes (BernoulliNB)
classificador_bnb = BernoulliNB()
y_pred_bnb_ros = executar_classificador(classificador_bnb, X_resampled_smote, X_test_normalized, y_resampled_smote)

# Validar o modelo Naive Bayes usando a função de validação
acuracia, precisao, recall, matrix_confusao = validar_bnb(y_test, y_pred_bnb_ros) 
