"""
Notas das exceptions em Python (add_notes, __notes__)
https://docs.python.org/3/library/exceptions.html
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceções (3.11.0)
"""


# Notas das exceptions em Python (add_notes, __notes__)
# https://docs.python.org/3/library/exceptions.html
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception): ...


class OutroError(Exception): ...


def levantar():
    exception_ = MeuError("a", "b", "c")
    # Notas dentro das exeções
    exception_.add_note("Olha a nota 1")
    exception_.add_note("você errou isso")
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError("Vou lançar de novo")
    exception_.__notes__ = error.__notes__.copy()
    # Notas dentro das exeções
    exception_.add_note("Mais uma nota")
    raise exception_ from error
# Retorno
"""
MeuError
('a', 'b', 'c')

Traceback (most recent call last):
  File "d:\GIT\Curso-Python-3\Seção 05\aula146.py", line 30, in <module>
    levantar()
  File "d:\GIT\Curso-Python-3\Seção 05\aula146.py", line 26, in levantar
    raise exception_
MeuError: ('a', 'b', 'c')
Olha a nota 1
você errou isso

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "d:\GIT\Curso-Python-3\Seção 05\aula146.py", line 39, in <module>
    raise exception_ from error
OutroError: Vou lançar de novo
Olha a nota 1
você errou isso
Mais uma nota
"""
