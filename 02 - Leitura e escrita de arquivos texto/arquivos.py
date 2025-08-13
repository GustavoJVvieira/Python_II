"""
Aula 0.2 – Leitura e Escrita de Arquivos Texto

Um arquivo de texto é como um caderno no computador, onde podemos escrever e depois ler o que foi escrito.

Modos de abrir arquivos:
- 'w' (write): cria um novo arquivo ou apaga o antigo e escreve de novo.
- 'r' (read): lê o conteúdo do arquivo.
- 'a' (append): adiciona mais conteúdo no final do arquivo sem apagar o que já tinha.

Vamos:
1. Criar um arquivo e escrever nele.
2. Ler o arquivo.
3. Adicionar mais coisas nele.
4. Ler linha por linha.
"""

# Criando e escrevendo no arquivo
with open("exemplo.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha.\n")  # Escreve a primeira linha e pula para a próxima
    f.write("Segunda linha.")

# Lendo todo o conteúdo do arquivo
with open("exemplo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()  # Lê tudo de uma vez
print("Conteúdo do arquivo:\n", conteudo)

# Adicionando mais conteúdo no final
with open("exemplo.txt", "a", encoding="utf-8") as f:
    f.write("\nTerceira linha adicionada.")

# Lendo linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print("Linha lida:", linha.strip())  # strip() remove espaços extras e quebras de linha
