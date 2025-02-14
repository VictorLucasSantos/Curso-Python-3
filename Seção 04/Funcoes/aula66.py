"""
Argumento nomeados e não nomeados em funções Python

Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o valor (argumento posicional)
"""

def soma(x, y):
    return x + y

print(soma(1, 2))

print(soma(x=1, y=3))

# pode ser adicionado em qualquer ordem, após nomear um parametro, todos tem que ser nomeados, da mesma forma que os argumentos com valor default
print(soma(y=1, x=3))

def soma2(x, y):
    print(f'x={x} + y={y} | x + y = ', x + y)
    
soma2(1, 2)