"""
Formatando datas do datetime
datetime.strftime('DATA', 'FORMATO')
https://docs.python.org/3/library/datetime.html
"""

from datetime import datetime

data = datetime.strptime("2025-03-19 07:33:20", "%Y-%m-%d %H:%M:%S")
print(data.strftime("%d/%m/%Y"))
print(data.strftime("%d"), data.day)
print(data.strftime("%Y"), data.year)
print(data.strftime("%d"), data.day)
print(data.strftime("%m"), data.month)
print(data.strftime("%H"), data.hour)
print(data.strftime("%M"), data.minute)
print(data.strftime("%S"), data.second)
