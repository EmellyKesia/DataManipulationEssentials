# Importa a biblioteca pandas, essencial para manipulação e análise de dados em DataFrames
import pandas as pd

#Manipulação de dados de cidades e populações

#Cria um DataFrame com nomes de cidades e suas respectivas populações (em formato string)
dados_cidades = [
    ["São Paulo", "12396372"],
    ["Rio de Janeiro", "6747815"],
    ["Brasília", "3055149"],
    ["Salvador", "2886698"]
]
df_cidades = pd.DataFrame(dados_cidades, columns=["Cidade", "População"])

# Exibe o tipo de dado de cada coluna antes da conversão
print("Tipos antes da conversão:\n", df_cidades.dtypes)

# Convertendo a coluna 'População' para int
df_cidades["População"] = df_cidades["População"].astype(int)

# Exibe o tipo de dado de cada coluna após a conversão
print("\nTipos após a conversão:\n", df_cidades.dtypes)

# Exibe o DataFrame atualizado
print(df_cidades)


# Cria um DataFrame com nomes e idades de 5 pessoas
dados_pessoas = [
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduarda", 24]
]
df_pessoas = pd.DataFrame(dados_pessoas, columns=["Nome", "Idade"])

# Adiciona uma nova coluna 'Idade_Proxima_Decada', que calcula a idade da pessoa daqui a 10 anos
df_pessoas["Idade_Proxima_Decada"] = df_pessoas["Idade"] + 10

# Converte a coluna 'Idade_Proxima_Decada' para o tipo float para fins de demonstração de manipulação de dados
df_pessoas["Idade_Proxima_Decada"] = df_pessoas["Idade_Proxima_Decada"].astype(float)

# Exibe o DataFrame atualizado com a nova coluna
print("\nDataFrame com 'Idade_Proxima_Decada' em float:\n", df_pessoas)

# Filtragem de dados com base em múltiplas condições

# Cria um DataFrame com informações de nome, idade e altura para várias pessoas
dados_info = [
    ["Carlos", 20, 1.75],
    ["Laura", 17, 1.65],
    ["Marcos", 22, 1.80],
    ["Julia", 19, 1.68],
    ["Paula", 25, 1.72]
]
df_info = pd.DataFrame(dados_info, columns=["Nome", "Idade", "Altura"])

# Filtra o DataFrame para exibir apenas pessoas com idade acima de 18 anos e altura acima de 1.70m
df_filtrado = df_info[(df_info["Idade"] > 18) & (df_info["Altura"] > 1.70)]

# Exibe o DataFrame filtrado, contendo apenas as pessoas que atendem aos critérios
print("\nPessoas com idade acima de 18 e altura acima de 1.70:\n", df_filtrado)
