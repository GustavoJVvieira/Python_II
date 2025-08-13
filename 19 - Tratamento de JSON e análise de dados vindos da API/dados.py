"""
Aula 3 – Tratamento de JSON e análise de dados vindos da API

Objetivo:
- Entender como interpretar dados no formato JSON que vêm das APIs.

JSON?
- É um formato de texto para organizar dados que é fácil para humanos e máquinas.

Exemplo prático:
- Receber o JSON da API ViaCEP e extrair as informações que queremos.
"""

import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        # Verificando se o CEP é válido
        if "erro" in dados:
            print("CEP inválido.")
        else:
            print(f"CEP: {cep}")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro na requisição:", resposta.status_code)

# Testando com CEP válido e inválido
buscar_cep("01001000")
print("---")
buscar_cep("00000000")
