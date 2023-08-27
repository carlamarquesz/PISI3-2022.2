from utils import *  
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score
from sklearn import tree 
import matplotlib.pyplot as plt 


# Função para separar os dados em treino e teste
def executar_validador(X, y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=123)
    for treino_id, teste_id in validador.split(X, y):
        X_train, X_test = X[treino_id], X[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return X_train, X_test, y_train, y_test

# Função para salvar a árvore de decisão
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

#  Execução do pré-processamento dos dados
X = dados.drop("TARGET", axis=1).values
y = dados["TARGET"].values
X_train, X_test, y_train, y_test = executar_validador(X, y)

# Instanciando o classificador e prevendo o resultado
classificador_arvore_decisao = tree.DecisionTreeClassifier(
    max_depth=10, random_state=123
)
y_pred_arvore_decisao = executar_classificador(
    classificador_arvore_decisao, X_train, X_test, y_train
) 

# Validando o resultado
acuracia,precisao,recall,matrix_confusao = validar_arvore(y_test, y_pred_arvore_decisao)
print(dados.columns)  

# Salvando a imagem da árvore de decisão
#salvar_arvore(classificador_arvore_decisao, "arvore_decisao.png")
