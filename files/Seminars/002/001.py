# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check():
    for i in range(2):
        x = i
        for j in range(2):
            y = j
            for l in range(2):
                z = l
                print('для х = {0}, y = {1}, z = {2}'.format(x, y, z))
                print(not (x or y or z) == ((not x) and (not y) and (not z)))


check()


# от коллег:

def LeftExpression(x, y, z):
    return not (x or y or z)


def RightExpression(x, y, z):
    return not x and not y and not z


print('X\tY\tZ\t\t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            print(f'{x}\t{y}\t{z}\t\t{LeftExpression(x, y, z) == RightExpression(x, y, z)}')


# Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
#
# Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в
# консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с
# людьми, например: 1 программист, 2 программиста, 5 программистов.
#
# В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи,
# как минимум до 1000 человек.
#




# от Владимира:

def fun(n):
    a = n % 10
    b = n % 100
    if (11 <= b <= 19):
        return f'{n} программистов'
    elif (a == 1):
        return f'{n} программист'
    elif (2 <= a <= 4):
        return f'{n} программиста'
    elif (a == 0 or a >= 5):
        return f'{n} программистов'


for i in range(100, 130):
    print(fun(i))


# от Алексея Малдаева:

def abv(num):
    if (num == 1) or (num > 20 and num % 10 == 1) or (num > 99 and num % 100 == 1):
        print(f'{num} - программист')
    elif (2 <= num <= 4) or (num > 20 and 2 <= num % 10 <= 4) or (num > 99 and 2 <= num % 100 <= 4):
        print(f'{num} - программиста')
    else:
        print(f'{num} - программистов')


# abv(num)
for i in range(0, 50, 1):
    abv(i)
