def my_open(caminho_arquivo, modo):
    print("Abrindo arquivo")
    arquivo = open(caminho_arquivo, modo, encoding="UTF8")
    yield arquivo
    print("Fechando arquivo")
    arquivo.close()


with my_open(LOCAL_ARQUIVO, "w") as f:
    for i in range(0, 11):
        f.write(f"Linha {i}\n")
    print("WITH", f)