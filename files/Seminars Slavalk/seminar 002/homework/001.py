# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

num = input('введите число: ')


def sum_of_digit(n):
	result = 0
	for i in range(len(n)):
		if not n[i].isdigit():
			continue
		result += float(num[i])
	print(result)


sum_of_digit(num)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('введите число: '))


def mult_of_digit(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	print(result)


mult_of_digit(num)

# Задайте список из n чисел последовательности (1 + 1 / n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input('введите число: '))


def func(n):
	result = 0
	for i in range(1, n + 1):
		result += ((1 + 1 / i) ** i)
	print(round(result, 3))


func(num)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции вводит пользователь через пробел.

num = int(input('введите число: '))


def fill_list(n):
	col = []
	index = 1
	for i in range(-n, n + 1):
		col[index] = i
		index += 1
		print(col)


fill_list(num)

# Реализуйте алгоритм перемешивания списка.