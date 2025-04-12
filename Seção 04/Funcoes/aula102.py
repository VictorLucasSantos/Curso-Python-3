"""
Variaveis locais e globais (locals, globals)

"""


def concatenar0(string):
    valor_final = string

    def interna(valor_a_concatenar):
        # Nessa situação irá gerar um erro pois uma variavel global não pode ser alterada
        # por conta de ser uma variavel livre e não ter
        # Traceback (most recent call last):
        # File "d:\GIT\Curso-Python-3\Seção 04\Funcoes\aula102.py", line 20, in <module>
        # print(a("b"))
        # File "d:\GIT\Curso-Python-3\Seção 04\Funcoes\aula102.py", line 13, in interna
        # valor_final += valor_a_concatenar
        # ^^^^^^^^^^^
        # UnboundLocalError: cannot access local variable 'valor_final' where it is not associated with a value

        valor_final += valor_a_concatenar
        return valor_final

    return interna


def concatenar(string):
    valor_final = string

    def interna(valor_a_concatenar):
        # para que não ocorra a exeção
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final

    return interna


a = concatenar("a")
print(a("b"))
print(a("c"))

b = concatenar0("a")
print(a("b"))
print(a("c"))
