import numpy as np
import pandas as pd 

# Dados qualitativos para usar nos gráficos
dados = pd.read_csv("./data/credit_card_approval.csv", nrows= 50)
# dados = pd.read_parquet("./data/credit_card_approval.parquet")


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


# dados["POSSUI_CARRO"].replace({"Y": 'Sim', "N": 'Não'}, inplace=True)
# dados["POSSUI_PROPRIEDADES"].replace({"Y": 'Sim', "N": 'Não'}, inplace=True)

dados["QTD_FILHOS"].replace(
    {"No children": 'Sem filhos', "1 children": '1 filho', "2+ children": '2+ filhos'}, inplace=True
)

dados["ESCOLARIDADE"].replace(
    {
        "Higher education": "Ensino Superior",
        "Secondary / secondary special": "Secundário / secundário especial",
        "Incomplete higher": "Incompleto superior",
        "Lower secondary": "Secundário inferior",
        "Academic degree": "Grau académico",
    },
    inplace=True,
)

dados["ESTADO_CIVIL"].replace(
    {
        "Civil marriage": 'Casamento civil',
        "Married": 'Casado(a)',
        "Single / not married": 'Solteiro / Não casado',
        "Separated": 'Separado(a)',
        "Widow": 'Viúvo/Viúva',
    },
    inplace=True,
)

dados["TIPO_DE_MORADIA"].replace(
    {
        "Rented apartment": 'Apartamento alugado',
        "House / apartment": 'Casa / Apartamento',
        "Municipal apartment": 'Apartamento municipal',
        "With parents": 'Com os pais',
        "Co-op apartment": 'Apartamento cooperativo',
        "Office apartment": 'Apartamento de escritório',
    },
    inplace=True,
)

## Nova coluna a ser criada
#dados['RENDIMENTO_MENSAL'] = (dados['RENDIMENTO_ANUAL']) / 12

def formatando(data,col, col_nova):
  data[col_nova] = (dados[col] // 365) * - 1

# formatando(dados,"ANOS_EMPREGADO", 'ANOS_EMPREGADO')
# formatando(dados,'IDADE','IDADE')


dados["CARGO"].replace(
    {
        "Security staff": "Equipe de Segurança",
        "Sales staff": "Equipe de Vendas",
        "Accountants": "Contadores",
        "Laborers": "Trabalhadores",
        "Managers": "Gerentes",
        "Drivers": "Motoristas",
        "Core staff": "Equipe Principal",
        "High skill tech staff": "Equipe Técnica de Alta Habilidade",
        "Cleaning staff": "Equipe de Limpeza",
        "Private service staff": "Equipe de Serviço Privado",
        "Cooking staff": "Equipe de Cozinha",
        "Low-skill Laborers": "Trabalhadores de Baixa Qualificação",
        "Medicine staff": "Equipe de Medicina",
        "Secretaries": "Secretários",
        "Waiters/barmen staff": "Equipe de Garçons/Barmen",
        "HR staff": "Equipe de Recursos Humanos",
        "Realty agents": "Agentes Imobiliários",
        "IT staff": "Equipe de TI",
    },
    inplace=True,
)


dados["STATUS_PAGAMENTO"].replace(
    {"C": 'pago no prazo', "X": 'Não aplicável', "0": '1-29 dias de atraso', "1": '30-59 dias de atraso', "2": '60-89 dias de atraso', "3": '90-119 dias de atraso', "4": '120-149 dias de atraso', "5": '150+ dias de atraso'},
    inplace=True,
)



# # VERIFICANDO VALORES CONTIDOS NAS COLUNAS ESCOLHIDAS
# def verificar_valores_unicos(col, dataset):
#     for indx, coluna in enumerate(col):
#         print(f'valores contidos na coluna "{col[indx]}":{dataset[coluna].unique()}')


# # COLUNAS DESEJADAS 
# col =  ['GENERO', 'POSSUI_CARRO', 'POSSUI_PROPRIEDADES', 'QTD_FILHOS',
#       'ESCOLARIDADE', 'ESTADO_CIVIL', 'TIPO_DE_MORADIA',
#       'CELULAR', 'TELEFONE_COMERCIAL',
#        'TELEFONE_RESIDENCIAL', 'EMAIL', 'CARGO',
#        'STATUS_PAGAMENTO', 'TARGET']

# print(verificar_valores_unicos(col, dados))