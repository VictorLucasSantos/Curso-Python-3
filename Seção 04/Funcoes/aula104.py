def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Decorando")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O seu resultado foi {resultado}")
        print("Decorado")
        return resultado

    return interna


# (Sintax Sugar) facilitador da linguagem para utilizar o decorator
@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")


invertida = inverte_string("123")
print(invertida)


def decorador(func):
    def wrapper():
        print("Executando algo antes da função...")
        func()
        print("Executando algo depois da função...")

    return wrapper  # Retorna a função modificada


@decorador
def minha_funcao():
    print("Essa é a função original!")


# Chamando a função decorada
minha_funcao()
