"""
Aula 4 – Explorando dados com Pandas (introdução prática)

Objetivo:
- Abrir e entender um arquivo de dados usando Pandas.

Passos:
1. Carregar o arquivo CSV.
2. Visualizar as primeiras linhas com .head().
3. Ver estatísticas básicas com .describe().
4. Ver informações do arquivo com .info().
"""

import pandas as pd

# Carregando arquivo CSV (exemplo)
# Suponha que exista um arquivo 'dados.csv' com dados reais
try:
    dados = pd.read_csv("dados.csv")

    print("Primeiras 10 linhas do arquivo:")
    print(dados.head(10))  # Mostra as 10 primeiras linhas

    print("\nEstatísticas descritivas das colunas numéricas:")
    print(dados.describe())  # Estatísticas básicas

    print("\nInformações gerais do arquivo:")
    print(dados.info())  # Informação sobre colunas, tipos e nulos
except FileNotFoundError:
    print("Arquivo 'dados.csv' não encontrado. Coloque o arquivo na mesma pasta do script.")
