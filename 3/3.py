# -- coding: utf-8 --
def time(n):
    day = 60 * 24
    n = n % day
    hours = n // 60
    return hours, n % 60
minutes = int(input('введите кол-во минут : '))
hours, min = time(minutes)
print (f'текущее время: {hours}:{min}')