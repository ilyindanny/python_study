#  возвращает список str, проверяя, могут ли значения быть преобразованы в float:
def get_coll():
	digit = 1
	coll = []
	temp = 0
	while digit:
		try:
			coll = list(input('введите список вещественных чисел через пробел: ').split())
			#  проверка на правильный ввод
			only_int = 0
			for i in coll:
				temp = float(i)

				#  проверка. чисел с дробью не должно быть меньше двух:
				only_int += i.isdigit()
				1 / (only_int - len(coll))
				1 / (only_int - len(coll) + 1)
			digit = 0

		except:
			print('невозможно преобразовать в float или недостаточно дробных частей для вычисления')

	return coll


#  возвращает список str с минимальным и максимальным дробным числом (в целой части 0)

def find_max(coll):
	new_coll = []
	maxx = 0
	minn = 0

	#  если элемент содержит точку, он записывается в новый список float (в целой части 0):
	for i in range(len(coll)):
		if not coll[i].isdigit():
			new_coll.append(float('0.' + coll[i].split('.')[1]))

	#  поиск максимальной и минимальной дробной части:
	for j in range(len(new_coll)):
		if new_coll[j] > new_coll[maxx]:
			maxx = j
		if new_coll[j] < new_coll[minn]:
			minn = j

	result = [new_coll[maxx], new_coll[minn]]
	return get_int(result)


#  принимает массив из двух элементов макс и мин. поиск разности между дробными частями с обходом погрешности float

def get_int(coll):
	factor = 1

	# цикл вычисляет максимальный порядок дробного остатка:
	for i in coll:
		while i * factor != int(i * factor):
			factor *= 10

	return (coll[0] * factor - coll[1] * factor) / factor


num_collection = get_coll()

print(find_max(num_collection))

