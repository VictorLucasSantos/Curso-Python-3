# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/


# Tudo antes da barra deve ser❗️APENAS❗️posicional.
def soma1(a, b, /, x, y):
    return a + b + x + y


# Após o asterisco somente pode ser somente argumentos nomeados
def soma2(a, b, *, c):
    return a + b + c


def soma3(a, b, /, *, c, d):
    return a + b + c + d


soma1(1, 2, x=3, y=4)

soma2(1, 2, x=3, y=4)


soma3(
    1,
    2,
)
