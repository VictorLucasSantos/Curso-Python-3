"""
Context Manager com classes - Criando e Usando gerenciadores de contexto
Você pode implementar seus próprios protocolos
apenas implementando os dunder methods que o
Python vai usar.
Isso é chamado de Duck typing. Um conceito
relacionado com tipagem dinâmica onde o Python não
está interessado no tipo, mas se alguns métodos existem
no seu objeto para que ele funcione de forma adequada.
Duck Typing:
Quando vejo um pássaro que caminha como um pato, nada como
um pato e grasna como um pato, eu chamo aquele pássaro de pato.
Para criar um context manager, os métodos __enter__ e __exit__
devem ser implementados.
O método __exit__ receberá a classe de exceção, a exceção e o
traceback. Se ele retornar True, exceção no with será
suprimidas.

Ex:
with open('aula149.txt', 'w') as arquivo:
    ...
"""


class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo

    def __enter__(self):
        # print("Enter")
        # return 1234
        print("ABRINDO ARQUIVO")
        self.arquivo = open(self.caminho_arquivo, self.modo, encoding="UTF8")
        return self.arquivo

    def __exit__(self, class_exception, exeception_, traceback_):
        # print("Exit")
        print("FECHANDO ARQUIVO")
        self.arquivo.close()

        # print(class_exception)
        # print(exeception_)
        # print(traceback_)

        # return True  # Trata a exceção

        exeception_.add_note("Minha nota personalizada da exceção")


with MyContextManager(r"D:\\GIT\\Curso-Python-3\\Seção 05\\aula149.txt", "w") as f:
    for i in range(0, 10):
        f.write(f"Linha {i}\n", 123)
    print("WITH", f)
