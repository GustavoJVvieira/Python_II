"""
Aula 3 – Herança e Polimorfismo

Objetivo:
- Herança: permitir que uma classe herde atributos e métodos de outra.
- Polimorfismo: permitir que um método tenha comportamentos diferentes dependendo
de onde é usado.

Exemplo:
Vamos criar uma classe "Veiculo" e fazer "Carro" e "Moto" herdarem dela.
"""

# Classe base (pai)
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descricao(self):
        print(f"Veículo: {self.marca} {self.modelo}")

# Classe filha (herda de Veiculo)
class Carro(Veiculo):
    def descricao(self):  # Polimorfismo: reescrevendo o método
        print(f"Carro: {self.marca} {self.modelo} - 4 rodas")

# Outra classe filha
class Moto(Veiculo):
    def descricao(self):  # Polimorfismo novamente
        print(f"Moto: {self.marca} {self.modelo} - 2 rodas")

# Testando
v = Veiculo("Genérico", "ModeloX")
c = Carro("Toyota", "Corolla")
m = Moto("Honda", "CG 160")

v.descricao()
c.descricao()
m.descricao()
