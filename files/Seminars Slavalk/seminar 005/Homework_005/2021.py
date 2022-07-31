# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота "интеллектом"

from random import randint
import time

player = randint(0, 1)
if player:
	print('вы начинаете')
else:
	print('начинает бот')

time.sleep(2)


def my_step(candy_left: int) -> int:
	"""По сути это и есть интеллект, который бы подошел и для бота тоже"""
	if candy_left % 29:
		return candy_left % 29
	else:
		return 28


def bot_step() -> int:
	"""А это просто рандомный бот. Смысла писать больше нет, так как выиграет все равно только первый ходящий"""
	return randint(0, 28)


candy = 2021

while candy > 0:

	if player:
		step = my_step(candy)
	else:
		step = bot_step()

	candy -= step

	if player:
		print('вы делаете ход на {}, конфет останется {}'.format(step, candy))
	else:
		print('бот делает ход на {}, конфет останется {}'.format(step, candy))

	if candy <= 0:
		if player:
			print('вы выиграли')
		else:
			print('выиграл бот')

	if player:
		player = 0
	else:
		player = 1
