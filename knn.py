from sklearn.discriminant_analysis import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from utils import *  
from sklearn.model_selection import GridSearchCV, train_test_split 
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score  

#Pre-processamento dos dados
def preprocessamento_dados(X):
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    return X_normalized


# Função para separar os dados em treino e teste
def executar_validador(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=123
    )
    return X_train, X_test, y_train, y_test

# Função para prever o resultado da análise de crédito
def executar_classificador(classificador, X_train, X_test, y_train):
    classificador.fit(X_train, y_train)
    y_pred = classificador.predict(X_test)
    return y_pred

# Função para executar as métricas de validação
def validar_knn(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    matrix_confusao = confusion_matrix(y_test, y_pred)
    return accuracy, precision, recall, matrix_confusao



# Execução da divisão dos dados em treino e teste
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)


# Pré-processamento dos dados
X_train_normalized = preprocessamento_dados(X_train)
X_test_normalized = preprocessamento_dados(X_test)


# Busca em grade para encontrar o melhor valor para n_neighbors
param_grid = {"n_neighbors": [3, 5, 7, 9, 11]}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring="accuracy")
grid_search.fit(X_train_normalized, y_train)
best_n_neighbors = grid_search.best_params_["n_neighbors"]
print("Melhor número de vizinhos:", best_n_neighbors)


# Instanciando o classificador e prevendo o resultado
classificador_knn = KNeighborsClassifier(
    metric="euclidean", n_neighbors=best_n_neighbors
)
y_pred_knn = executar_classificador(
    classificador_knn, X_train_normalized, X_test_normalized, y_train
)

# Validação do resultado
acuracia, precisao, recall, matrix_confusao = validar_knn(
    classificador_knn, X_test_normalized, y_test
)