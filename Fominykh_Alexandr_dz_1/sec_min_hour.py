"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""


duration = int(input('duration = '))  #вводим количество минут
sec = (duration % 3600) % 60  #извлекаем остаток секунд
minute = (duration % 3600) // 60  #извлекаем минуты
hour = duration // 3600  #извлекаем часы
print(sec, 'сек;')
print(minute, 'мин', sec, 'сек;')
print(hour, 'час', minute, 'мин', sec, 'сек;')