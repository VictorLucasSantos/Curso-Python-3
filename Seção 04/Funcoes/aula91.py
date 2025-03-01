"""
Generator functions 

Em vez de retornar um valor único como uma função normal,
elas são especiais porque podem pausar a execução e retornar um valor por vez, mantendo o estado entre as chamadas.
Isso é super útil quando lidamos com grandes conjuntos de dados ou queremos economizar memória.
"""

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return
        

gen = generator(maximum=10)
for n in gen:
    print(n)
    
    

def generator1(n=0):
    yield 1 # pausa
    print('Continuando')
    yield 2
    print('Mais uma vez')
    yield 3
    print('Terminando')
    return 'Acabou'

gen1 = generator1()
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

# 1
# Continuando
# 2
# Mais uma vez
# 3
# Terminando