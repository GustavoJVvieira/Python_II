"""
Aula 3 – Depuração simples

Objetivo:
- Descobrir onde e por que o programa está falhando.

Método 1: print()
- Inserir mensagens no código para ver o valor das variáveis.

Método 2: Ferramentas da IDE
- Usar breakpoints e inspeção de variáveis (ex.: VS Code, PyCharm).
"""

def calcular_media(notas):
    print(f"Debug: notas recebidas = {notas}")  # Depuração
    soma = sum(notas)
    print(f"Debug: soma = {soma}")  # Depuração
    media = soma / len(notas)
    print(f"Debug: média = {media}")  # Depuração
    return media

# Testando
notas = [7, 8, 9]
media_final = calcular_media(notas)
print(f"Média final: {media_final}")
