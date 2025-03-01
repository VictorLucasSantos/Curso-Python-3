caminho_arquivo = "D:\\GIT\\Curso-Python-3\\Seção 04\\Funcoes\\"
caminho_arquivo += "aula116_1.txt"


def adiciona_linha(arquivo, numero: int):
    for i in range(0, numero):
        arquivo.write(f"Linha {i} \n")


with open(caminho_arquivo, "a") as arquivo:
    adiciona_linha(arquivo, 10)

with open(caminho_arquivo, "a") as arquivo:
    adiciona_linha(arquivo, 10)

caminho_arquivo1 = "D:\\GIT\\Curso-Python-3\\Seção 04\\Funcoes\\"
caminho_arquivo1 += "aula116_2.txt"

# Definindo encoding a ser utilizado na escrita
with open(caminho_arquivo1, "a", encoding="utf-8") as arquivo:
    adiciona_linha(arquivo, 10)
