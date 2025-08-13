"""
Aula 1 – Introdução ao Tratamento de Exceções

Objetivo:
- Entender como lidar com erros sem que o programa pare de funcionar.

O que é exceção?
- É um erro que acontece durante a execução do programa.

Como tratar?
- Usamos try, except e finally para capturar e responder a erros.
"""

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
finally:
    print("Execução finalizada (com ou sem erro).")
