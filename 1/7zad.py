# -- coding: utf-8 --
while True:
    print ('введите число')
    number = int(input())
    if number % 2 == 0:
        print(f"{number} число чётное")
    else:
        print(f"{number} число нечётное")