# 1 Вычислить результат деления двух чисел c заданной точностью d

# можно не делать)))))))


# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numm = int(input('введите число: '))


#  создать список от нуля до numm

def nums_coll(n: int) -> list:
	coll = []
	for i in range(n + 1):
		coll.append(i)

	return coll


# найти простые числа в списке от нуля до числа numm.

def get_primes(coll: list) -> list:
	i = 2
	while i < len(coll):
		del coll[i + i::i]
		i += 1

	del coll[0:2]  # удалить ненужные 0 и 1
	return coll


# проверить, какие из простых чисел являются множителями числа numm

def find_result(coll: list, n: int) -> list:
	i = 0
	while i < len(coll):
		if n % coll[i]:
			del coll[i]
		else:
			i += 1
	return coll


nums_collection = nums_coll(numm)

primes = get_primes(nums_collection)

result = find_result(primes, numm)

print(f'список простых множителей числа {numm}: {result}')
