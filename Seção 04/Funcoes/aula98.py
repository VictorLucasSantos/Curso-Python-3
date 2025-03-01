"""
Singleton
"""
import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(0, 10):
    # O modulo em python não é recarregado por conta de ser um singleton e só exist uma instancia do modulo por questão de eficiência
    print(i)
    import aula98_m
    
for i in range(0, 10):
    # Recarregando o modulo com importlib, somente feito manualmente dessa forma
    print(i)
    importlib.reload(aula98_m) 