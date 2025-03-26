"""Usando calendar para calendários e datas
https://docs.python.org/3/library/calendar.html
calendar é usado para coisas genéricas de calendários e datas.
Com calendar, você pode saber coisas como:
- Qual o último dia do mês (ex.: monthrange)
- Qual o nome e número do dia de determinada data (ex.: weekday)
- Criar um calendário em si (ex.: monthcalendar)
- Trabalhar com coisas específicas de calendários (ex.: calendar, month)
Por padrão dia da semana começa em 0 até 6
0 = segunda-feira | 6 = domingo
"""

import calendar

print(calendar.calendar(2025))
print("#####" * 15)
print(calendar.month(2025, 3))
primeiro_dia, ultimo_dia = calendar.monthrange(2025, 3)
print(list(calendar.day_name))
print(primeiro_dia, ultimo_dia)
print(calendar.day_name[primeiro_dia])
print(calendar.day_name[calendar.weekday(2025, 3, ultimo_dia)])
print(
    calendar.monthcalendar(2025, 3)
)  # representa as semanas, numeros zerados são dias do outro mês

for week in calendar.monthcalendar(2025, 3):
    for day in week:
        if day == 0:
            continue
        print(day)
