"""
Dicionario em Python (dict)
São estruturas de par chave e valor
Chaves são consideradas como o indice e podem ser tipos imutaveis como os:
str, int, float, bool, tuple, etc
O valor pode ser qualquer tipo por exemplo outro dicionario, listas, etc
Ex:
pessoa = {
    'nome': 'Beltrano',
    'sobrenome': 'Ciclano',
    'idade': 30,
    'altura': 1.80,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321}
    ]
}
mutavel: dic, list
"""

pessoa = {
    'nome': 'Beltrano',
    'sobrenome': 'Ciclano',
    'idade': 30,
    'altura': 1.80,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321}
    ]
}

# Utilizando argumentos nomeados diretamente no construtor do dicionario
pessoa1 = dict(nome='Teste', sobrenome='Teste2', idade=0, altura=0, enderecos=[])


if __name__ == "__main__":
    # verificando variavel e tipo de variavel
    print(pessoa1, type(pessoa1))
    
    # Obtendo o valor de uma chave
    print(pessoa['nome'])
    
    # Iterando sobre um dicionario por suas chaves
    for chave in pessoa:
        print( f' chave: {chave} | valor: {pessoa[chave]}')
    
    Exemplo = {}
    
    Exemplo['ex'] = 'Qualquer'
    print(Exemplo)
    print(Exemplo['ex'])