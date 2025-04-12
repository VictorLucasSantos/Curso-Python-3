import os

# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = "D:\\GIT\\Curso-Python-3\\Seção 04\\Funcoes\\"
caminho_arquivo += "aula116.txt"

# Para poder sempre fechar o arquivo
"""
arquivo = open(caminho_arquivo, "r")
try:
    arquivo
finally:
    arquivo.close()
"""

# Fechando o arquivo automaticamente com Context manager
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write("Linha1 \n")
    arquivo.write("Linha1 \n")
    # não consegue ler o arquivo por conta de ser somente modo de escrita
    # tendo que ser utilizado  o +
    # print(arquivo.read())

print("#" * 10)

# utilizando o write ele sobrescreve o arquivo toda vez que é executado
with open(caminho_arquivo, "w+") as arquivo:
    arquivo.write("Linha1 \n")
    arquivo.write("Linha1 \n")
    arquivo.writelines(("Linha3 \n", "Linha4 \n"))
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    print(arquivo.readline())

print("#" * 10)

with open(caminho_arquivo, "r") as arquivo:
    print(arquivo.read())
