from pathlib import Path

caminho_projeto = Path()
# pasta do projeto atual
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)

# Caminho absoluto do meu arquivo
print(caminho_arquivo)

caminho_ideias = caminho_arquivo.parent / "ideias"
print(caminho_ideias / "f.txt")

# Obtendo semprea a home do usuário
print(Path.home() / "Desktop")

arquivo = Path.home() / "Desktop" / "arquivo.txt"
arquivo.touch()  # Salvando arquivo
arquivo.write_text("Qualquer coisa")
print(arquivo)
print(arquivo.read_text())
# arquivo.unlink()  # Removendo arquivo

caminho = Path.home() / "Desktop" / "Python"

# Criando pasta
caminho.mkdir(exist_ok=True)

subpasta = caminho / "subpasta"
subpasta.mkdir(exist_ok=True)

arquivo_subpasta = subpasta / "arq.txt"
arquivo_subpasta.touch()
arquivo_subpasta.write_text("Hi")
