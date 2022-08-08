# Задана натуральная степень k.
# Сформировать многочлен степени k.

from random import randint as rd
k = int(input(" K: "))
arr = []
for i in range(k, 1, -1):
    x = rd(-3, 3)
    if i == k:
        print(x, 'x^', i, end=' ')
    elif x < 0:
        print('-', abs(x), 'x^', i, end=' ')
    else:
        print('+', x, 'x^', i, end=' ')


numm = rd(-100, 100)
if numm < 0:
    print('-', abs(numm), '= 0')
else:
    print('+', numm, '= 0')
    