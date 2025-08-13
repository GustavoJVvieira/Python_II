"""
Aula 3 – Instalação de pacotes externos com pip

Objetivo:
- Entender como instalar e usar bibliotecas feitas por outras pessoas para facilitar o desenvolvimento.

O que é pip?
- É o gerenciador de pacotes do Python que permite instalar ferramentas extras.

Exemplo prático:
- Vamos mostrar o comando que você deve usar no terminal para instalar o pacote requests.

Comando para instalar:

pip install requests

Depois, no código, podemos importar e usar assim:
"""

# Simulação de uso do pacote requests (precisa estar instalado de verdade para funcionar)
try:
    import requests
    resposta = requests.get("https://api.github.com")
    print(f"Status da requisição: {resposta.status_code}")
except ImportError:
    print("O pacote requests não está instalado. Use: pip install requests")
