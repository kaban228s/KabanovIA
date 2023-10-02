# скажите нужны ли циклы для задач или без них делать
# -- coding: utf-8 --
while True:
    print ('Как вас зовут')
    name = input()
    banname = ['Ivan', 'ivan', 'Иван', 'иван']
    if name in banname:
        print ('Иванов больше не набираем')
    else:
        print ('Сколько вам лет?')
        age = int(input())
        left = 16 - age
        if age > 75:
            print ('Проведите старость в покое')
        elif age <= 0:
            print ('не верю')
        elif age >= 16 and age <= 75:
            print ('Поздравляем вы поступили в ВГУИТ')
        else:
            print ('Сначала нужно окончить школу!')
            print ('Лет до окончания осталось', left)