"""
Escopo de funções em Python

Escopo significa o local onde as variáveis globais e locais se encontram.
Escopo global é o escopo onde todo o codigo é alcançavel.
Escopo local limitado ande podem ser manipulados

"""
x = 1

def escopo():
    # variavel não compartilha da outra que é global pois está sendo utilizada no escopo interno
    # editando uma variavel global dentro do escopo de funcao (não é boa pratica) tem q existir a variavel global
    global x
    x = 10
    def outra_funcao():
        global x
        # porem é possivel do escopo externo
        x = 11
        y = 2
        print(x, y)
    # não é possivel acessar a variavel também fora da funcao definida
    # print(y)
    outra_funcao()
    print(x)

# variavel não é acessavel por conta que só existe dentro da funcão e não globalmente
print(x)
escopo()
print(x)