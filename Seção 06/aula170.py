r"""
os.listdir para navegar em caminhos
/Users/luizotavio/Desktop/EXEMPLO
C:\Users\luizotavio\Desktop\EXEMPLO
caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
"""

import os

caminho = os.path.join(
    "C:/Users",
    "51501-VICTOR",
    "Pictures",
)


for pasta in os.listdir(caminho):  # Itera sobre as pastas do caminho
    caminho_completo_pasta = os.path.join(
        caminho, pasta
    )  # Obtem o caminho das pastas dentro do caminho
    if not os.path.isdir(
        os.path.join(caminho_completo_pasta)
    ):  # verifica se é um diretório
        continue
    for imagem in os.listdir(
        caminho_completo_pasta
    ):  # itera sobre as pastas dentro do caminho
        print(imagem)
