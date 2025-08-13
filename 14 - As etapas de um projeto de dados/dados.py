"""
Aula 2 – As etapas de um projeto de dados

Objetivo:
- Conhecer o ciclo de vida de um projeto de dados.

Etapas principais:
1. Coleta: reunir dados de fontes diversas (banco, arquivos, internet).
2. Tratamento: limpar e organizar os dados para análise.
3. Análise: usar técnicas para entender os dados.
4. Visualização: criar gráficos para mostrar insights.
5. Tomada de decisão: usar o resultado para ações práticas.
"""

etapas = ["Coleta", "Tratamento", "Análise", "Visualização", "Tomada de decisão"]

print("Etapas de um projeto de dados:")
for i, etapa in enumerate(etapas, 1):
    print(f"{i}. {etapa}")
