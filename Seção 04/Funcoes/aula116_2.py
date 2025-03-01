import os

caminho_arquivo = "D:\\GIT\\Curso-Python-3\\Seção 04\\Funcoes\\"
caminho_arquivo += "aula116_3.txt"


def adiciona_linha(arquivo, numero: int):
    for i in range(0, numero):
        arquivo.write(f"Linha {i} \n")


with open(caminho_arquivo, "a") as arquivo:
    adiciona_linha(arquivo, 10)

# Ambos metodos realizam a exclusão do arquivo
os.rename(caminho_arquivo, "aula116_4.txt")
# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)
