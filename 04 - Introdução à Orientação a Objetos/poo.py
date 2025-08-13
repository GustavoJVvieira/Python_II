"""
Aula 1 – Introdução à Orientação a Objetos (POO)

Objetivo:
- Entender o que são classes, objetos, atributos e métodos.

Conceitos básicos:
- Classe: é um molde, um "projeto" para criar objetos.
- Objeto: é uma "cópia" criada a partir da classe, com dados e comportamentos.
- Atributo: é uma informação que o objeto guarda (ex.: cor, nome, idade).
- Método: é uma ação que o objeto pode fazer (ex.: andar, falar, calcular).

Exemplo:
Vamos criar uma classe "Pessoa" e criar objetos a partir dela.
"""

# Definindo uma classe
class Pessoa:
    # Método especial chamado quando criamos um novo objeto
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade
    
    # Método que imprime uma apresentação
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos (pessoas)
p1 = Pessoa("Maria", 30)
p2 = Pessoa("João", 25)

# Chamando métodos dos objetos
p1.apresentar()
p2.apresentar()
