while True:
    print ('Как вас зовут')
    name = input()
    if name == ('Иван'):
        print ('Иванов больше не набираем')
    else:
        print ('Сколько вам лет?')
        age = int(input())
        left = 16 - age
        if age > 75:
            print ('Проведите старость в покое')
        elif age <= 0:
            print ('Не верю')
        elif age >= 16 and age <= 75:
            print ('Поздравляем вы поступили в ВГУИТ')
        else:
            print ('Сначала нужно окончить школу!')
            print ('Лет до окончания осталось', left)