"""
Closure e funções que retornam outras funções
"""

# criado uma funcao que retorna uma funcao
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

# Utilizar a referencia dessa funcao para adiar a execução dela com a variavel (closure)
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# dessa forma
print(falar_bom_dia('Beltrano'))
print(falar_boa_noite('Ciclano'))

for nome in ['Zezin', 'Maria', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

