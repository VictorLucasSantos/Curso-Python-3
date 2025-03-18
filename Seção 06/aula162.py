"""
Criando datas com módulo datetime
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
datetime.now()
https://pt.wikipedia.org/wiki/Era_Unix
datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html
Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
Instalando o pytz
pip install pytz types-pytz
"""

from datetime import datetime
from pytz import timezone

data = datetime(2022, 4, 20, 7, 49, 23)

date_str_data = "2025-04-20 07:49:23"
date_format = "%Y-%m-%d %H:%M:%S"  # Formatando data

print(data)
print(datetime.strftime(data, date_format))
print(datetime.now())  # hora exata
print(datetime.now(timezone("America/Porto_Velho")))  # hora exata da zona
print(datetime.now(timezone("Asia/Tokyo")))  # hora exata da zona
print(datetime.now(timezone("America/Sao_Paulo")))  # hora exata da zona
#  Unix timestamp, que representa o número de segundos que se passaram desde
# 1º de janeiro de 1970, à meia-noite UTC
print(datetime.now().timestamp())
print(datetime.now().fromtimestamp(1742300019.94551))
