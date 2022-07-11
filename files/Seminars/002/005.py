# КНБ от коллег

import random

num = None


def knb(num):
	bot = 0
	user = 0
	while bot < 1000 or user < 1000:
		num = input('Введите камень или ножницы или бумага\n')
		num_bot = random.randrange(1, 4)
		if num_bot == 1:
			print('Бот выбрал КАМЕНЬ')
			if num == 'камень':
				print('Ничья, каждый заработал по 0.5 очков')
				bot = bot + 0.5
				user = user + 0.5
				print(f'У Вас {user} - очков. У бота {bot} - очков')
			elif num == 'ножницы':
				print('Бот выиграл и получает 1 очко')
				bot = bot + 1
				print(f'У Вас {user} - очков. У бота {bot} - очков')
			elif num == 'бумага':
				print('Вы выиграли и получаете 1 очко')
				user = user + 1
				print(f'У Вас {user} - очков. У бота {bot} - очков')

		elif num_bot == 2:
			print('Бот выбрал НОЖНИЦЫ')
			if num == 'ножницы':
				print('Ничья, каждый заработал по 0.5 очков')
				bot = bot + 0.5
				user = user + 0.5
				print(f'У Вас {user} - очков. У бота {bot} - очков')
			elif num == 'бумага':
				print('Бот выиграл и получает 1 очко')
				bot = bot + 1
				print(f'У Вас {user} - очков. У бота {bot} - очков')
			elif num == 'камень':
				print('Вы выиграли и получаете 1 очко')
				user = user + 1
				print(f'У Вас {user} - очков. У бота {bot} - очков')

		elif num_bot == 3:
			print('Бот выбрал БУМАГУ')
			if num == 'бумага':
				print('Ничья, каждый заработал по 0.5 очков')
				bot = bot + 0.5
				user = user + 0.5
				print(f'У Вас {user} - очков. У бота {bot} - очков')
			elif num == 'камень':
				print('Бот выиграл и получает 1 очко')
				bot = bot + 1
				print(f'У Вас {user} - очков. У бота {bot} - очков')
			elif num == 'ножницы':
				print('Вы выиграли и получаете 1 очко')
				user = user + 1
				print(f'У Вас {user} - очков. У бота {bot} - очков')


knb(num)
