"""datetime.timedelta e dateutil.relativetimedelta (calculando datas)
Docs:
https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects
"""

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y %H:%M:%S"

data_inicio = datetime.strptime("20/04/1987 09:30:30", fmt)
data_fim = datetime.strptime("12/12/2022 08:20:20", fmt)
# delta = data_fim - data_inicio TIME DELTA É A DIFERENCA ENTRE DUAS DATAS
delta = timedelta(days=10, hours=2)
print(data_fim + delta)
print(delta.days, delta.seconds, delta.microseconds)
print(data_fim + relativedelta(second=50))
print(data_fim + relativedelta(second=59, minutes=30))
# delta = relativedelta(data_fim, data_inicio)
# print(delta.days, delta.years)
print(delta.total_seconds())
