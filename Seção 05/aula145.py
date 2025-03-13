"""
Positional-Only Parameters (/) e Keyword-Only Arguments (*)
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
🟢 Positional-only Parameters (/) - Tudo antes da barra deve
ser ❗️APENAS❗️ posicional.
PEP 570 – Python Positional-Only Parameters
https://peps.python.org/pep-0570/
🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/
"""


class MeuError(Exception): ...


class OutroError(Exception): ...


def levantar():
    raise MeuError("A mensagem do meu erro")


try:
    levantar()
except MeuError as e:
    print(e.__class__.__name__)
    print(e)
    exception_ = OutroError("Vou lançar novamente")
    raise exception_ from e
