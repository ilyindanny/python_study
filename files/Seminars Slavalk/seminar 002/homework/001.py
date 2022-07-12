# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
import random

num = input('введите число: ')


def sum_of_digit(n):
    result = 0
    for i in range(len(n)):
        if not n[i].isdigit():
            continue
        result += float(num[i])
    print(result)


sum_of_digit(num)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('введите число: '))


def mult_of_digit(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)


mult_of_digit(num)

# Задайте список из n чисел последовательности (1 + 1 / n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input('введите число: '))


def func(n):
    result = 0
    for i in range(1, n + 1):
        result += ((1 + 1 / i) ** i)
    print(round(result, 3))


func(num)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции вводит пользователь через пробел.

num = int(input('введите число: '))


def fill_list(n):
    col = []
    index = 1
    for i in range(n):
        col.append(random.randint(-n, n))
        index += 1
    print(col)
    return col


def get_user_nums(n):
    print('введите позиции через пробел (в диапазоне 0 до {}): '.format(n - 1), end='')
    user_nums = list(map(int, input().split()))
    return user_nums


def mult_num(col, user_nums):
    result = 1
    for i in user_nums:
        result *= col[i]
    print(result)


mult_num(fill_list(num), get_user_nums(num))

# Реализуйте алгоритм перемешивания списка.



def my_collection():
    n = int(input('введите размер коллекции: '))
    col = []
    for i in range(n):
        col.append(i)

    print('исходная коллекция: \t{}'.format(col))
    return col



def mix_collection(col):
    
    # коллекция с перемешанным списком
    new_col = []
    
    # список неиспользованных индексов в исходной коллекции
    index_list = []
    
    # заполнить список индексами от 0 до длины col - 1
    for i in range(len(col)):
        index_list.append(i)

    
    # наподнение нового списка с перемешиванием
    for i in range(len(col)):
        
        # рандомный индекс
        j = random.randint(0, len(index_list) - 1)
        
        # добавление в новую коллекцию случайного индекса
        new_col.append(index_list[j])
        
        # удаление использованного индекса из списка индексов
        index_list.remove(index_list[j])
    print('новая коллекция: \t\t{}'.format(new_col))


mix_collection(my_collection())
