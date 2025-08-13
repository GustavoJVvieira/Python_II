"""
Aula 2 – Criando e organizando pacotes próprios

Objetivo:
- Aprender a organizar nosso código em vários arquivos e pastas para facilitar a manutenção.

O que é um pacote?
- É uma pasta com vários módulos (arquivos .py) relacionados.

Exemplo prático:
- Vamos simular a estrutura de pastas e arquivos com comentários, pois aqui estamos em um único arquivo.

Estrutura simulada:

meu_projeto/
    calculos/
        __init__.py
        matematicas.py
    main.py

No arquivo matematicas.py, teríamos funções como:

def soma(a, b):
    return a + b

No main.py, importaríamos e usaríamos assim:

from calculos.matematicas import soma

resultado = soma(2, 3)
print(resultado)
"""

# Como não podemos criar arquivos aqui, vamos simular o uso da função importada:

def soma(a, b):
    return a + b

# Usando a função importada
resultado = soma(5, 7)
print(f"A soma de 5 e 7 é {resultado}")
