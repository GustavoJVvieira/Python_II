"""
Aula 1 – Importação e uso de módulos internos

Objetivo:
- Aprender a usar funções prontas que o Python já oferece em módulos como math, random e datetime.

O que é um módulo?
- Um arquivo com funções e variáveis que podemos usar para facilitar nosso trabalho.

Vamos importar alguns módulos e usar funções deles.
"""

# Importando módulo math para funções matemáticas
import math

# Usando função sqrt para calcular raiz quadrada
numero = 16
raiz = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz}")

# Importando módulo random para gerar números aleatórios
import random

# Gerar número aleatório entre 1 e 10
aleatorio = random.randint(1, 10)
print(f"Número aleatório entre 1 e 10: {aleatorio}")

# Importando módulo datetime para trabalhar com datas e horas
import datetime

# Mostrar a data e hora atual
agora = datetime.datetime.now()
print(f"Data e hora atuais: {agora}")
