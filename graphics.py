import numpy as np
import pandas as pd 

# Dados qualitativos para usar nos gráficos
dados = pd.read_csv("./data/credit_card_approval.csv")
new_columns = [
    "ID",
    "GENERO",
    "POSSUI_CARRO",
    "POSSUI_PROPRIEDADES",
    "QTD_FILHOS",
    "RENDIMENTO_ANUAL",
    "ESCOLARIDADE",
    "ESTADO_CIVIL",
    "TIPO_DE_MORADIA",
    "DIAS_ANIVERSARIO",
    "POSSUI_EMPREGO",
    "CELULAR",
    "TELEFONE_COMERCIAL",
    "TELEFONE_RESIDENCIAL",
    "EMAIL",
    "CARGO",
    "QTD_MESES",
    "STATUS_PAGAMENTO",
    "TARGET",
]
dados.columns = new_columns   
dados['STATUS2'] = dados['STATUS_PAGAMENTO']
dados["STATUS2"].replace(
            {"C": 0, "X": 0, "0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1},
            inplace=True,
        )
dados["QTD_MESES"] = np.ceil(pd.to_timedelta(dados["QTD_MESES"], unit="D").dt.days * (-1))
print(dados.head()) 
