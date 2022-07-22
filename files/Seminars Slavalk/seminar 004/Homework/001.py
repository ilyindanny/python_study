import random

# 1 Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   10^(-1) ≤ d ≤10^(-10)


# coefficient = len(input('введите коэффициент точности в формате "0.001": ').split('.')[1])
coefficient = 6


def get_pi(d: int) -> int:
	num_pi = 0
	for n in range(d):
		num_pi += 1 / 16 ** n * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
	return num_pi


result = list(str(get_pi(coefficient)).split('.'))
result[1] = result[1][:coefficient]  # убрать лишние цифры без округления
print(f'{result[0]}.{result[1]}')

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# numm = int(input('введите размер списка: '))
numm = 95


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

# 3 Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#  [1, 2, 2, 3] -> [1, 3]

# numm = int(input('введите размер для списка случайных чисел: '))
numm = 10


# создать список, заполненный случайными числами
def get_random_coll(n: int) -> list:
	coll = []
	for i in range(n):
		coll.append(random.randint(0, 10))

	return coll


# найти уникальные элементы коллекции
def find_unique_nums(coll: list) -> list:
	coll = coll[:]
	i = 0

	while i < len(coll):
		n = coll[i]
		if n in coll[i + 1:]:
			while n in coll:
				coll.remove(n)
		else:
			i += 1

	return coll


'''
# найти уникальные элементы коллекции (альтернативный вариант)
def find_uniq_nums(coll: list) -> list:
	stop_list = []
	new_coll = []

	for i in range(len(coll)):
		if coll[i] in coll[i + 1:]:
			stop_list.append(coll[i])
	for i in coll:
		if i in stop_list:
			continue
		else:
			new_coll.append(i)

	return new_coll
'''

nums_collection = get_random_coll(numm)

result = find_unique_nums(nums_collection)

print(f'список случайных чисел: \t\t\t {nums_collection}')
print(f'неповторяющиеся элементы списка: \t {result}')

# 4 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

natural_power = 2


def get_random_coefficients(power: int) -> list:
	nums = [power]
	for i in range(3):
		nums.append(random.randint(0, 100))
	nums.append('= 0')

	return nums


def fill_formula(nums: list) -> str:
	coll = nums[:]
	res = ''

	if coll[1]:
		coll[1] = str(f'{str(coll[1])}x^{coll[0]} ')
		if coll[2]:
			coll[2] = str(f'+ {str(coll[2])}x ')
		if coll[3]:
			coll[3] = str(f'+ {coll[3]} ')
	else:
		coll = [0, '0']

	for i in coll[1:]:
		if i:
			res += i

	return res


nums_collection = get_random_coefficients(natural_power)

result = fill_formula(nums_collection)

path = '001.txt'
with open(path, 'w') as file_text:
	file_text.write(result)

print(f'рандомные коэффициенты: {nums_collection[1:4]}')
print(f'в файл {path} сохранена формула: {result}')

# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
