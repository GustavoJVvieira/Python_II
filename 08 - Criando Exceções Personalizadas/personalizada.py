"""
Aula 2 – Criando Exceções Personalizadas

Objetivo:
- Criar nossas próprias classes de erro para situações específicas.

Quando usar?
- Quando queremos dar mensagens de erro mais claras para quem usa o código.
"""

# Criando uma exceção personalizada
class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Saldo restante: R${self.saldo}")

# Testando
conta = ContaBancaria("Ana", 500)

try:
    conta.sacar(700)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
