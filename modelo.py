from utils import *
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier


def executar_validador(x, y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=123)
    for treino_id, teste_id in validador.split(x, y):
        x_train, x_test = x[treino_id], x[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return x_train, x_test, y_train, y_test

def executar_classificador(classificador, x_train, x_test, y_train):
    modelo = classificador.fit(x_train, y_train)
    y_pred = modelo.predict(x_test)
    return y_pred

def validar_modelo(y_test, y_pred):
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return acuracia, precisao, recall, matrix_confusao

# Execução do validador
x = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
x_train, x_test, y_train, y_test = executar_validador(x, y)

# Execução do classificador RandomForestClassifier
classificador_random_forest = RandomForestClassifier(
    n_estimators=100, max_depth=10, random_state=123
)
y_pred_random_forest = executar_classificador(
    classificador_random_forest, x_train, x_test, y_train
)

# Validação do modelo Random Forest
acuracia, precisao, recall, matrix_confusao = validar_modelo(y_test, y_pred_random_forest)
print(dados.columns)

# Imprimir métricas de validação
print("Acurácia:", acuracia)
print("Precisão:", precisao)
print("Recall:", recall)
print("Matriz de Confusão:\n", matrix_confusao)
