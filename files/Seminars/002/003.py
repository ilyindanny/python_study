# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример: *
#
# - Для N = 5: 1, -3, 9, -27, 81

a = int(input('введите число: '))


def fun(n):
    summa = 1
    result = []
    for i in range(n):
        result.append(summa)
        summa *= -3
    return result


print(fun(a))

# print('\t {0}'.format(fun(a)), end=' ')
