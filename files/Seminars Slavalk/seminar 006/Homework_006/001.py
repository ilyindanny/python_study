
# Задание 2:
# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

from math import factorial

n = int(input('введите число: '))
f = lambda x: factorial(x) * (x + 1)
result = list([f(i) for i in range(n)])
print(result)

# Или так:

result = list([factorial(x) * (x + 1) for x in range(n)])
print(result)