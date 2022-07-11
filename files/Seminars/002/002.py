# КНБ - вы играете с ботом, варианты раунда игры - победа 1 очко, проигрыш 0 очков, ничья 0.5 балла

import random

result1 = 0
result2 = 0

while True:
	x = random.randint(0, 3)
	a = input('введите К или Н или Б (либо q для выхода): ')
	if a != 'q':
		if x == 0:
			if a == 'Н':
				result1 += 1
				result2 += 0
			if a == 'Б':
				result1 += 0
				result2 += 1
		if x == 1:
			if a == 'К':
				result1 += 0
				result2 += 1

			if a == 'Б':
				result1 += 1
				result2 += 0
		if x == 2:
			if a == 'К':
				result1 += 1
				result2 += 0
			if a == 'Н':
				result1 += 0
				result2 += 1

	else:
		break
print(result1, result2)
