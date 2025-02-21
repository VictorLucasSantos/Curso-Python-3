# Yeld from

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')
    
def gen2(gen):
    print('COMECOU GEN2')
    # Iniciando um generator dentro de outro generator
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')
    
def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')
    

g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)
    # COMECOU GEN2
    # COMECOU GEN1
    # 1
    # 2
    # 3
    # ACABOU GEN1
    # 4
    # 5
    # 6
    # ACABOU GEN2
    
print()
    
for numero in g2:
    print(numero)
    # COMECOU GEN2
    # COMECOU GEN3
    # 10
    # 20
    # 30
    # ACABOU GEN3
    # 4
    # 5
    # 6
    # ACABOU GEN2