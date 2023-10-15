# -- coding: utf-8 --
print ('Введите число')
seconds = int(input())
n = seconds
day = n // 86400
hour = n // 3600
minute = n // 60
sec = n
print (f'дни {day}, часы {hour}, минуты {minute}, секунды {sec}')
