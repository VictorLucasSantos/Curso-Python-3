def soma(a, b):
    """
    >>> soma(10, 20)
    31
    """
    #Exemplo de uso de doctests
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """    
#Exemplo do uso de doctests no terminal, caso a resposta esteja correta não retorna nada
# **********************************************************************
# File "c:\Users\User\Desktop\Curso-Python-3\calculadora.py", line 3, in __main__.soma
# Failed example:
#     soma(10, 20)
# Expected:
#     31
# Got:
#     30
# **********************************************************************
# 1 items had failures:
#    1 of   1 in __main__.soma
# ***Test Failed*** 1 failures.
# PS C:\Users\User\Desktop\Curso-Python-3>

# com a opção de verbose=True o doctest gera o resultado no terminal
#     soma(10, 20)
# Expecting:
#     31
# **********************************************************************
# File "c:\Users\User\Desktop\Curso-Python-3\calculadora.py", line 3, in __main__.soma
# Failed example:
#     soma(10, 20)
# Expected:
#     31
# Got:
#     30
# 1 items had no tests:
#     __main__
# **********************************************************************
# 1 items had failures:
#    1 of   1 in __main__.soma
# 1 tests in 2 items.
# 0 passed and 1 failed.
# ***Test Failed*** 1 failures.
    
    
    # Caso o tipo de dado seja inválido, ele gera uma exeção (usar somente para testes e não em projetos reais)
    # para executar o sistema sem o assert é somente adicionar - O ao unicio da chamada do arquivo no cmd
    assert isinstance(a, (int, float))
    assert isinstance(a, (int, float))
    return a + b

def subtracao(a, b):
    return a - b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)