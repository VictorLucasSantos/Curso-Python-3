"""
Higher Order Functions

Funções de primeira classe

Funções são tipos de dados em python
"""

# criado a funcao de exemplo
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

# cria uma funcao que somente referencia a uma funcao já criada e passa os parametros para dentro dela
def executa(funcao, *args):
    return funcao(*args)

# Dessa forma utilizando a funcao com referencia de SAUDACAO
print(executa(saudacao,'Boa Tarde', 'Beltrano'))

print(executa(saudacao, 'Boa Noite', 'Ciclano'))