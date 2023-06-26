import pandas as pd 
import numpy as np
# Reorganizando os dados application_record
data = pd.read_csv("./data/application_record.csv")
data = data.drop_duplicates(
    subset=data.columns.difference(["ID"])
)  # Tratando os dados duplicados
new_columns = [
    "ID",
    "GENERO",
    "POSSUI_CARRO",
    "POSSUI_PROPRIEDADES",
    "QTD_FILHOS",
    "RENDIMENTO_ANUAL",
    "CATEGORIA_RENDA",
    "ESCOLARIDADE",
    "ESTADO_CIVIL",
    "MORADIA",
    "DIAS_ANIVERSARIO",
    "POSSUI_EMPREGO",
    "CELULAR",
    "TELEFONE_TRABALHO",
    "TELEFONE",
    "EMAIL",
    "CARGO",
    "TAM_FAMILIA",
]
data.columns = new_columns
data["SALARIO"] = data["RENDIMENTO_ANUAL"] / 12
data["POSSUI_EMPREGO"] = np.where(data["POSSUI_EMPREGO"] < 0, 1, 0)
data["POSSUI_CARRO"].replace({"N": 0, "Y": 1}, inplace=True)
data["POSSUI_PROPRIEDADES"].replace({"N": 0, "Y": 1}, inplace=True)
data["POSSUI_CARRO"].replace({"N": 0, "Y": 1}, inplace=True)
data['CARGO'] = data['CARGO'].fillna('Outros')
data.drop(["CELULAR", "TELEFONE_TRABALHO", "TELEFONE", "EMAIL"], axis=1, inplace=True)

# Reorganizando os dados credit_record
data2 = pd.read_csv("./data/credit_record.csv")
new_columns2 = ["ID", "MES_EXTRAIDO", "STATUS_PAGAMENTO"]
data2.columns = new_columns2
dados_filtrados_1 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "X")
]
dados_filtrados_2 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "C")
]
dados_filtrados_3 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "5")
]
dados_filtrados_4 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "4")
]
dados_filtrados_5 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "3")
]
dados_filtrados_6 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "2")
]
dados_filtrados_7 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "1")
]
dados_filtrados_8 = data2.loc[
    (data2["MES_EXTRAIDO"] == 0) & (data2["STATUS_PAGAMENTO"] == "0")
]
