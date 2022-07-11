# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример: *
#
# - Для N = 5: 1, -3, 9, -27, 81

a = int(input('введите число: '))


def fun(n):
	m = 1
	st = []
	for i in range(n):
		st.append(m)
		m *= -3
	return st


print(fun(a))

# print('\t {0}'.format(fun(a)), end=' ')
