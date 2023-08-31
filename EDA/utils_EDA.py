## Rotulos 
# rotulos_colunas_numericas = {
#     "Rendimento Anual": "RENDIMENTO_ANUAL",
#     "ID": "ID",
#     "Idade Anos": "IDADE_ANOS",
#     "Qtd Meses": "QTD_MESES",
#     "Salário": "SALARIO"
# }


# rotulos_keys_colunas_numericas = [
#     "Rendimento Anual",
#     "ID",
#     "Idade Anos",
#     "Qtd Meses",
#     "Salário"
# ]


# rotulos_colunas_categoricas = {
#     "Gênero": "GENERO",
#     "Possui Carro": "POSSUI_CARRO",
#     "Possui Propriedades": "POSSUI_PROPRIEDADES",
#     "Qtd Filhos": "QTD_FILHOS",
#     "Escolaridade": "ESCOLARIDADE",
#     "Estado Civil": "ESTADO_CIVIL",
#     "Tipo de Moradia": "TIPO_DE_MORADIA",
#     "Idade Anos": "IDADE_ANOS",
#     "Possui Emprego": "POSSUI_EMPREGO",
#     "Celular": "CELULAR",
#     "Telefone Comercial": "TELEFONE_COMERCIAL",
#     "Telefone Residencial": "TELEFONE_RESIDENCIAL",
#     "Email": "EMAIL",
#     "Cargo": "CARGO",
#     "Status Pagamento": "STATUS_PAGAMENTO",
#     "Target": "TARGET",
#     "Faixa Etária": "Faixa Etária"
# }

# rotulos_keys_colunas_categoricas = [
#     "Gênero",
#     "Possui Carro",
#     "Possui Propriedades",
#     "Qtd Filhos",
#     "Escolaridade",
#     "Estado Civil",
#     "Tipo de Moradia",
#     "Idade Anos",
#     "Possui Emprego",
#     "Celular",
#     "Telefone Comercial",
#     "Telefone Residencial",
#     "Email",
#     "Cargo",
#     "Status Pagamento",
#     "Target",
#     "Faixa Etária"
# ]

# def buscar_chave_por_valor(dicionario, valor_procurado):
#     return next((chave for chave, valor in dicionario.items() if valor == valor_procurado), None)



## descrição para os gráficos

description = {
        
        "GENERO": 
            """
        <p style='text-align: justify; text-indent: 1.25em;'>Indica o sexo do indivíduo, sendo geralmente categorizado como masculino ou feminino. Nesta análise, realizaremos uma avaliação minuciosa das proporções entre os gêneros presentes.
        Vamos examinar detalhadamente as porcentagens de cada categoria para obter insights precisos. 
        Podemos observar que, dentre os dados selecionados, podemos observar o total de indivíduos do sexo masculino e indivíduos do sexo feminino com os gráficos abaixo:</p>
        """,
        
        
        "POSSUI_CARRO": 
        """
        <p style='text-align: justify; text-indent: 1.25em;;'>Refere-se à posse de um veículo automotor por parte do indivíduo, podendo ser "Sim" ou "Não".
        Estamos tratando da propriedade de um veículo automotor por parte de cada indivíduo, com as opções possíveis sendo "Sim" ou "Não".
          Vamos examinar essa variável para determinar quantos indivíduos possuem um veículo e quantos não possuem, apresentando uma visão clara da distribuição.
        Podemos observar as pessoas possuem carros e as que não possuem, dentre o conjunto de dados selecionados.</p>
         """,
       
        "POSSUI_PROPRIEDADES":  
        """
        <p style='text-align: justify; text-indent: 1.25em;;'>Indica se o indivíduo possui propriedades, como casas, terrenos ou imóveis. Pode ser "Sim" ou "Não".
        Estamos lidando com a presença de propriedades de propriedade de cada indivíduo, englobando casas, terrenos ou imóveis, com as opções "Sim" ou "Não".
        Nossa análise visa determinar quantos indivíduos possuem propriedades e quantos não possuem, a fim de proporcionar uma compreensão abrangente da distribuição dessa característica.</p>
         """,

        "QTD_FILHOS":
        """
        <p style='text-align: justify; text-indent: 1.25em;'>Estamos investigando a quantidade de filhos de cada indivíduo, o que corresponde ao número de crianças que estão sob os cuidados de cada pessoa.
        Através desta variável, buscamos compreender e analisar a distribuição e a tendência do número de filhos no grupo estudado.</p>
        """,

        "ESCOLARIDADE":  
        """
        <p style='text-align: justify; text-indent: 1.25em; '> Nível de educação alcançado por cada indivíduo, variando desde o ensino fundamental incompleto até a pós-graduação.
        Essa variável reflete o grau de instrução e formação acadêmica que cada pessoa adquiriu ao longo de sua vida. Através dessa análise,
        buscamos compreender a distribuição dos diferentes níveis de educação dentro do conjunto de dados, bem como investigar possíveis relações
        e padrões que podem emergir ao cruzar a escolaridade com outras características estudadas.</p>
         """,

        "ESTADO_CIVIL": 
        """
        <p style='text-align: justify; text-indent: 1.25em;'>Esta variável revela o status marital de cada indivíduo, como solteiro, casado, divorciado, viúvo e outras categorias relacionadas.
        Através da análise do estado civil, buscamos compreender a composição matrimonial da população em estudo.
        Além disso, exploramos possíveis padrões ou associações entre o estado civil e outras características demográficas, permitindo uma visão mais completa das dinâmicas sociais e familiares dentro do grupo analisado.</p>
         """,

        "TIPO_DE_MORADIA": 
        """
        <p style='text-align: justify; text-indent: 1.25em; '>Tipo de Moradia: Descreve o tipo de habitação em que o indivíduo reside, como casa própria, apartamento alugado, casa dos pais, etc.
        Estamos investigando o tipo de moradia de cada indivíduo, o que descreve a modalidade de habitação em que estão alojados, abrangendo categorias como casa própria, apartamento alugado, residência na casa dos pais, entre outras opções.
        Esta variável oferece insights sobre os arranjos de moradia dos participantes do estudo. A nossa análise se propõe a discernir as diferentes modalidades de moradia presentes e a explorar eventuais associações com outras características analisadas.</p>
        """,

        "CELULAR": 
        """
        <p style='text-align: justify;'> Podemos observar que todos na base de dados possuiem celulares. </p>
        """,

        "TELEFONE_COMERCIAL": 
        """
        <p style='text-align: justify; text-indent: 1.25em;'>A categoria "Telefone Comercial" refere-se à presença de um número de telefone associado a atividades profissionais ou comerciais.
        Esse telefone é frequentemente utilizado para fins de comunicação relacionados ao trabalho ou negócios. Analisar a existência de um telefone comercial pode oferecer informações sobre o grau de envolvimento profissional dos indivíduos e suas interações no contexto de trabalho.</p>
        """,

        "TELEFONE_RESIDENCIAL": 
        """
        <p style='text-align: justify; text-indent: 1.25em; '>A variável "Telefone Residencial" indica se o indivíduo possui um número de telefone vinculado à residência.
        Embora os telefones residenciais sejam menos comuns devido à popularização dos celulares, eles ainda podem ser usados para comunicações domésticas tradicionais.
        Analisar se os indivíduos têm um telefone residencial pode fornecer insights sobre as preferências de comunicação e o nível de infraestrutura de comunicação em suas casas.</p>
        """,

        "EMAIL": 
        """
        <p style='text-align: justify; text-indent: 1.25em;'>A categoria "E-mail" indica se o indivíduo possui um endereço de e-mail.
        O e-mail é uma forma crucial de comunicação digital e é frequentemente usado para troca de mensagens formais e informais, compartilhamento de informações e até mesmo para acessar serviços online.
        Avaliar a presença de um endereço de e-mail entre os indivíduos pode revelar o grau de adoção da comunicação eletrônica e da participação em atividades online.</p>
        """,

        "CARGO":  
        """
        <p style='text-align: justify; text-indent: 1.25em;'>A variável "Cargo" descreve a posição que o indivíduo ocupa em sua ocupação ou trabalho.
        Essa informação é valiosa para entender as diferentes funções e responsabilidades desempenhadas pelos participantes em seus ambientes de trabalho.
        Ao analisar os cargos, podemos identificar hierarquias, distribuições de responsabilidades e especializações que compõem a força de trabalho.</p>
        """,

        "STATUS_PAGAMENTO": 
        """
        <p style='text-align: justify; text-indent: 1.25em;'>O "Status de Pagamento" se refere ao estado corrente dos pagamentos do indivíduo, indicando se estão em dia, atrasados ou em qualquer outra condição relevante.
        Essa variável fornece insights sobre a situação financeira dos participantes, bem como a disciplina em relação às obrigações financeiras.
        Analisar o status de pagamento pode auxiliar na compreensão das dinâmicas de renda e gestão financeira da amostra estudada.</p>
         """,
         
        "VARIAVEL_TARGET": 
        """
        <p style='text-align: justify; text-indent: 1.25em;'>A "Variável Target" é o elemento que se deseja prever ou analisar em estudos estatísticos ou de aprendizado de máquina.
        Essa variável é o foco da análise, servindo como o objetivo final da investigação. No contexto de modelos preditivos, a variável target é aquela que se tenta prever com base em outras variáveis.
        É fundamental selecionar a variável target corretamente para garantir que os resultados da análise sejam relevantes e informativos.</p>
        """,

        "FAIXA_ETARIA": 
        """
        <p style='text-align: justify; text-indent: 1.25em;'>A "Faixa Etária" categoriza os indivíduos em grupos específicos de idade, que estão entre:
        Essa categorização é útil para compreender como diferentes faixas etárias se comportam em relação a diversas características e variáveis.
        Ao analisar faixas etárias, podemos identificar tendências comportamentais, necessidades distintas em cada estágio da vida e possíveis correlações entre idade e outros atributos.</p>
         """,
    }


# analises = {
#     "genero": """
#         <h2 style='color: #3366cc; text-align: justify;'>Gênero:</h2>
#         <p style='text-align: justify;'>Indica o sexo do indivíduo, sendo geralmente categorizado como masculino ou feminino. Nesta análise, realizaremos uma avaliação minuciosa das proporções entre os gêneros presentes.
#         Vamos examinar detalhadamente as porcentagens de cada categoria para obter insights precisos. Podemos observar que, dentre os dados selecionados, há um total de x indivíduos do sexo masculino e y indivíduos do sexo feminino.
#         Essa distribuição resulta em uma configuração de gênero na qual os homens representam x% e as mulheres representam y% do conjunto de dados analisado.</p>
#     """
# }

# Renderizando o HTML com a análise de gênero usando a função st.markdown
# chave_analise = "genero"
# st.markdown(analises[chave_analise], unsafe_allow_html=True)