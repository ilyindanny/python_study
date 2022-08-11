# Создайте программу для игры в "Крестики-нолики".

# Это игра для двух игроков:

def set_map(n: int) -> list:
	"""Создание набора выигрышных строк"""
	map_01 = []

	for i in range(n + n + 2):
		map_01.append([0] * n)

	l = 1
	for i in range(n):
		for j in range(n):
			map_01[i][j] = l
			l += 1
	l = 1
	for i in range(n):
		for j in range(n, n + n):
			map_01[j][i] = l
			l += 1
	l = 1
	for i in range(n):
		for j in range(n + n, n + n + 1):
			map_01[j][i] = l
			l += n + 1
	l = n
	for i in range(n):
		for j in range(n + n + 1, n + n + 2):
			map_01[j][i] = l
			l += n - 1

	for i in range(len(map_01)):
		map_01[i] = set(map_01[i])

	return map_01


def win(m: set, map_02: list) -> bool:
	"""Проверка, выиграл или нет"""
	res = 0
	for i in map_02:
		if m >= i:
			res = i
	return res


def enter(s_1: list, s_2: list, player) -> list:
	"""Метод для ввода координаты и проверки ввода"""
	if player == 1:
		player = '1th'
	else:
		player = '2nd'

	done = 0
	n = 0
	while not done:
		n = int(input('you are {}. enter: '.format(player)))
		if n in s_1 or n in s_2:
			print('not like that')
		else:
			done = 1
	s_1.append(n)
	return s_1


def print_all(s_1: list, s_2: list):
	"""Вывод заполняющейся матрицы в консоль"""
	x = [0, '·', '·', '·', '·', '·', '·', '·', '·', '·']
	for i in range(1, len(x)):
		for l in s_1:
			if l == i:
				x[i] = 'x'
		for m in s_2:
			if m == i:
				x[i] = '0'

	print(
		'\n\t{}\t{}\t{}\n\n\t{}\t{}\t{}\n\n\t{}\t{}\t{}\n'.format(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))


matrix = 3
game_map = set_map(matrix)

s1 = []
s2 = []
count = matrix * matrix

while True:

	s1 = enter(s1, s2, 1)
	print_all(s1, s2)
	m1 = set(s1)
	result = win(m1, game_map)
	if result:
		print('1th won ', result)
		break
	count -= 1
	if count == 0:
		print('drawn game')
		break

	s2 = enter(s2, s1, 2)
	print_all(s1, s2)
	m2 = set(s2)
	result = win(m2, game_map)
	if result:
		print('2nd won ', result)
		break
	count -= 1
	if count == 0:
		print('drawn game')
		break
