"""
argparse.ArgumentParser para argumentos mais complexos
Tutorial Oficial:
https://docs.python.org/pt-br/3/howto/argparse.html
"""

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "-b",
    "--basic",
    help='Mostra "Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar="STRING",
    # default='Olá mundo', # Valor padrão
    required=False,
    action="append",  # Recebe o argumento mais de uma vez
    # nargs='+', # Recebe mais de um valor
)
args = parser.parse_args()

if args.b is None:
    print("Informe o valor de b")
else:
    print("o valor de b", args.b)
