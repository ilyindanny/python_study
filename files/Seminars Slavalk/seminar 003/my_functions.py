# преобразование элементов списка в тип float
def make_float_collection():
	digit = 1
	col = []
	while digit:
		try:
			col = list(input('введите список вещественных чисел через пробел: ').split())
			for i in range(len(col)):
				col[i] = float(col[i])
				digit = 0
		except:
			print('невозможно преобразовать в float')
			col = []
	return col


# сумма элементов массива, стоящих на нечетных индексах
def get_sum(col: list):
	result = 0
	for i in range(0, len(col), 2):
		result += col[i]
	if result:
		print(result)
