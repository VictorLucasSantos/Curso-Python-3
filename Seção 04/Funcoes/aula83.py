"""
Empacotamento e desempacotamento de dicionários

kwargs - keyword argumentos (argumento nomeados)
"""
a, b = 1, 2
a, b = b, a #trocando valores de variaveis de lugar
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': '20',
    'altura': '1.80'
}

# Empacotando dicionarios
pessoa_completa = {**pessoa, **dados_pessoa}


# retorna as chaves do dicionario
a, b = pessoa
print(a, b)

# retorna uma tupla com a chave e valor do dicionario
(a1, a2), (b1 , b2) = pessoa.items()
print(a1, a2)
print(b1, b2)


for chave, valor in pessoa.items():
    print(chave, valor)
    
def mostrar_argumentos_nomeados(*args,**kwargs):
    print('NÃO NOMEADOS', args)
    for chave, valor in kwargs.items():
        print(chave, valor)
        
mostrar_argumentos_nomeados(nome='Joana', sobrenome='Silva')

# Exemplo para se passar varios parametros nomeados para dentro de uma funcao com um dicionário
mostrar_argumentos_nomeados(*pessoa_completa)