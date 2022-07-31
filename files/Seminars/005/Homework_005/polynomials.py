# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# Например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55,
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66.




def get_coefficients(data: str) -> dict:
	"""Разбор многочлена"""
	data = data.replace('+ ', '+')
	data = data.replace('- ', '-')
	data = data.split()[:-2]

	if data[0][0] != '-':
		data[0] = '+' + data[0]

	res = {}
	count = 1

	for i in range(0, len(data)):
		for j in data[i][1:]:
			if j.isdigit():
				count += 1
			else:
				break
		if count < len(data[i]):
			res[data[i][count:]] = int(data[i][:count])
		else:
			res['nums'] = int(data[i][:count])

		count = 1

	return res


def sum_of_lists(a: dict, b: dict) -> str:
	"""Сложение"""
	sum_dict = b.copy()
	for l, m in a.items():
		if l in sum_dict:
			sum_dict[l] = sum_dict[l] + a[l]
		else:
			sum_dict[l] = m

	srt = sorted(sum_dict.keys(), reverse=True)
	sorted_dict = []
	for i in srt:
		sorted_dict.append([sum_dict[i], i])

	for i in range(1, len(sorted_dict)):
		if sorted_dict[i][0] < 0:
			sorted_dict[i][0] = ' - ' + str(abs(sorted_dict[i][0]))
		else:
			sorted_dict[i][0] = ' + ' + str(sorted_dict[i][0])

	res = ''
	for i in sorted_dict:
		for j in i:
			if j != 'nums' and i[0] != ' + 0':
				res += str(j)

	if res == '' or res[0] == '0':
		res = '0'
	else:
		res += ' = 0'

	return res


path1 = 'polynomials_1.txt'
path2 = 'polynomials_2.txt'
path3 = 'polynomials_result.txt'

with open(path1, 'r') as file:
	polynom_1 = file.readline()
with open(path2, 'r') as file:
	polynom_2 = file.readline()

print('многочлен a: ', polynom_1)
print('многочлен b: ', polynom_2)

polynom_1 = get_coefficients(polynom_1)
polynom_2 = get_coefficients(polynom_2)
result = str(sum_of_lists(polynom_1, polynom_2))

with open(path3, 'w') as file:
	file.write(result)

print(f'в файл {path3} сохранен результат: {result}')
