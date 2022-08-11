from random import randint
from math import factorial

# 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# n = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(1,len(n),2):
#     if i % 2 == 1:
#         sum = sum + int(n[i])


n = [randint(0, 9) for x in range(9)]
result = [n[i] for i in range(len(n)) if i % 2 == 0]

print(f'{n}\n{sum(result)}')

# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# import math
# n = [2, 3, 5, 6]
# # n = [2, 3, 4, 5, 6]
# result = []
# for i in range(math.ceil(len(n)/2)):
#     result.append(int(n[i])*int(n[len(n)-1-i]))

result = list(map(lambda i: n[i] * n[len(n) - i - 1], range((len(n) + 1) // 2)))

print(result)

# 3 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input("введите число: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial)

numm = 0
result = list([factorial(x) * (x + 1) for x in range(5)])

print(result)

# 4 Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# a = [1, 2, 2, 3, 4, 6, 8, 8, 2, 9, 7, 4, 9]
# i = a[0]
# c = []
# for i in a:
# 	if i in c:
# 		continue
# 	else:
# 		c.append(i)

result = list(filter(lambda x: n.count(x) == 1, n))

print(result)
