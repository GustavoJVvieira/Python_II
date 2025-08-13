"""
Aula 2 – Construtores, Encapsulamento e __init__

Objetivo:
- Criar classes com inicialização automática usando __init__.
- Proteger atributos internos usando encapsulamento.

Encapsulamento:
- É a prática de "esconder" informações internas de uma classe para que não
sejam alteradas de forma errada.
- No Python, usamos "_" (protegido) e "__" (privado) como convenção.
"""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado.")
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    def ver_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

# Testando a classe
conta = ContaBancaria("Carlos", 500)
conta.ver_saldo()
conta.depositar(200)
conta.sacar(100)
conta.ver_saldo()
