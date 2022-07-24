"""

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

path = 'data.txt'

with open(path, 'r') as file_games:
	data = file_games.read()

print('input\n{}\n'.format(data))

data = data.replace('\n', ';')
data_games = list(data.split(';'))


def get_result_list(d_gms):
	temp_list = []

	for i in range(1, len(d_gms), 2):
		temp_list.append(d_gms[i])

	temp_list = set(temp_list)
	temp_list = list(temp_list)

	result_games = []

	for i in temp_list:
		lst = [i]
		lst.append('0 0 0 0 0')
		result_games.append(lst)

	return result_games


def find_count(d_gms: list, res: list) -> list:
	for i in range(len(res)):
		count = 0
		for j in d_gms:
			if j in res[i][0]:
				count += 1
		res[i][1] = str(count) + res[i][1][1:]

	return res


def wins(d_gms, res):
	for i in range(len(res)):

		win = 0
		drawn = 0
		loss = 0

		for j in range(1, len(d_gms), 4):
			if d_gms[j] in res[i]:
				score = int(d_gms[j + 1]) - int(d_gms[j + 3])
				if score:
					if score > 0:
						win += 1
					else:
						loss += 1
				else:
					drawn += 1

			if d_gms[j + 2] in res[i]:
				score = int(d_gms[j + 3]) - int(d_gms[j + 1])
				if score:
					if score > 0:
						win += 1
					else:
						loss += 1
				else:
					drawn += 1
		sum_score = win * 3 + drawn

		r = str(win) + ' ' + str(drawn) + ' ' + str(loss) + ' ' + str(sum_score) + ' '
		res[i][1] = res[i][1][:2] + r

	return res


def output(res: list) -> str:
	output_res = ''

	for i in res:
		output_res += i[0] + ':' + i[1] + '\n'

	return output_res


results = get_result_list(data_games)

results = find_count(data_games, results)

results = wins(data_games, results)

result = output(results)

path = 'results.txt'

with open(path, 'w') as file_games:
	file_games.write(result)

print('output\nв файл {} добавлены результаты:\n{}'.format(path, result))
