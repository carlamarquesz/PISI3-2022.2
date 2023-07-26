from utils import *

col_antiga = colunas_db
col_nova = new_columns

def lista_dados_colunas(dados_col):
     column = [None] * len(dados_col) 
     for i,j in enumerate(dados_col):
          column[i] = j
     return column

col_original = lista_dados_colunas(col_antiga)
col_renomeada = lista_dados_colunas(col_nova)

dicionario_dados = {
        "Column": col_original,
        
        "Coluna": col_renomeada,
                    
        "Tipo do dado":[
                        "Float",
                        "Int",
                        "Int",
                        "Int",
                        "Int",
                        "Int",
                        "Float",
                        "Int",
                        "Int",
                        "Float",
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int", 
                        "Int"
                    ],

        "Descrition" :
                     [
                       "ID",
                       "Gender", 
                       "Is there a car", 
                       "Is there a property", 
                       "Number of children", 
                       "Annual income",   
                       "Education level", 
                       "Marital status", 
                       "Way of living", 
                       "Age in days",
                       "Duration of work in days",
                       "Is there a mobile phone",
                       "Is there a work phone", 
                       "Is there a phone",
                       "Is there an email",
                       "Job",
                       "Record month",
                       "Status",
                       "Target: Risk user are marked as '1', else are '0'"
                       ],

        "Descrição" : 
                        [
                        "Identificador", 
                        "Gênero", 
                        "Possui veículo", 
                        "Possui propriedade",
                        "Quantidade de filhos", 
                        "Renda anual",
                        "Escolaridade", 
                        "Estado civil",
                        "Modo de vida",
                        "Idade em dias",
                        "Duração do trabalho em dias",
                        "Possui telefone móvel", 
                        "Possui telefone comercial",
                        "Possui telefone fixo",
                        "Tem um e-mail", 
                        "Profissão", 
                        "Mês de registro ",
                        "Status",
                        "Target: Usuários de risco",
     
                       ]
                    }

