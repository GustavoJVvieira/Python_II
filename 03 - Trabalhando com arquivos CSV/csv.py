"""
Aula 0.3 – Trabalhando com Arquivos CSV

CSV significa "Comma-Separated Values" (valores separados por vírgulas).
É como uma tabela do Excel, mas salva como texto.
Cada linha é um registro (como uma linha da planilha) e cada vírgula separa as colunas.

Vamos:
1. Criar um arquivo CSV com nomes, telefones e e-mails.
2. Ler o arquivo e mostrar o conteúdo.
"""

import csv  # Módulo para trabalhar com CSV no Python

# Criando um arquivo CSV
# newline="" evita linhas em branco extras no Windows
with open("contatos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)  # "escritor" é o objeto que vai escrever no CSV
    escritor.writerow(["Nome", "Telefone", "Email"])  # Primeira linha: cabeçalho
    escritor.writerow(["Ana", "1199999-0000", "ana@email.com"])
    escritor.writerow(["Bruno", "2198888-1111", "bruno@email.com"])

# Lendo um arquivo CSV
with open("contatos.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)  # "leitor" é o objeto que lê o CSV
    for linha in leitor:
        print("Linha do CSV:", linha)
