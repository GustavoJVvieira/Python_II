"""
Aula 0.1 – Manipulação de Caminhos de Arquivos

Imagine que você tem várias pastas e arquivos no computador. 
O Python precisa saber exatamente onde o arquivo está para conseguir abrir, salvar ou modificar.
O "caminho" é como um endereço de uma casa: ele diz onde o arquivo mora no computador.

Nesta aula vamos:
1. Criar caminhos até arquivos usando duas formas diferentes: os.path e pathlib.
2. Descobrir onde o programa está sendo executado.
3. Criar uma nova pasta no computador.
"""

# Importando duas formas de lidar com caminhos:
import os               # Maneira mais antiga e bem usada até hoje
from pathlib import Path  # Maneira mais moderna e prática

# --- Criando um caminho usando os.path ---
# Aqui estamos dizendo: "Dentro da pasta 'pasta', tem uma pasta 'subpasta', e dentro dela um arquivo chamado 'arquivo.txt'"
# O Python junta essas partes de forma que funcione no Windows, Mac e Linux.
caminho_arquivo = os.path.join("pasta", "subpasta", "arquivo.txt")
print("Caminho usando os.path:", caminho_arquivo)

# --- Criando o mesmo caminho usando pathlib ---
# Aqui, em vez de usar os.path.join, usamos uma barra "/" para juntar as partes do caminho.
# Não importa se você está no Windows ou Linux, o Python vai converter para o formato certo.
caminho_pathlib = Path("pasta") / "subpasta" / "arquivo.txt"
print("Caminho usando pathlib:", caminho_pathlib)

# --- Descobrindo onde o programa está sendo executado ---
# Isso é como perguntar: "Em qual pasta estou agora?"
print("Diretório atual:", os.getcwd())

# --- Criando uma nova pasta ---
# Aqui vamos criar uma pasta chamada "nova_pasta". Se ela já existir, não vai dar erro.
Path("nova_pasta").mkdir(exist_ok=True)
print("Pasta 'nova_pasta' criada (ou já existia).")
