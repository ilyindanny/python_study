# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11


num = input('введите число из нескольких цифр: ')


def sum_of_digit(n):
	result = 0
	for i in range(len(n)):
		if not n[i].isdigit():
			continue
		result += int(num[i])
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

		print('ответ: {}'.format(result))


mult_of_digit(num)
