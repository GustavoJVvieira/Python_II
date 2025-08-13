"""
Aula 2 – Fazendo requisições com requests

Objetivo:
- Aprender a enviar pedidos a APIs usando o pacote requests.

Como funciona?
- Usamos requests.get() para pedir informações.
- Usamos requests.post() para enviar dados.

Exemplo prático:
- Fazer uma requisição GET para a API pública ViaCEP que retorna dados de endereço a partir do CEP.
"""

import requests

cep = "01001000"  # CEP de exemplo

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)  # Fazendo a requisição GET
    if resposta.status_code == 200:  # Verificando se deu certo
        dados = resposta.json()  # Convertendo a resposta em JSON (dicionário)
        print("Dados do CEP:")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("Erro na requisição:", resposta.status_code)
except Exception as e:
    print("Erro ao acessar a API:", e)
