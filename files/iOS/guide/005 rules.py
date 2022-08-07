#  int() — преобразование к целому числу в десятичной системе счисления
#  bin() — ... в двоичной
#  hex() — ...в шестнадцатеричной...


# функции возвращают минимальное и максимальное число в списке типа int:

lst = [1, 2, 3, 4]

min(lst)
max(lst)


# Type Hinting нужно добавлять. Тогда IDE сможет давать подсказки:

def f1(a: int, b: str) -> int:
    return a + int(b)


# Map.
# В map передается функция без скобок.

str_nums = '1 2 3 4 5 6 7 8'

nums = list(map(int, str_nums.split()))  # это итерируемый объект типа map.

# Comprehensions, возвращает список.
# Перед for должно быть написано только то, что непосредственно возвращается:

s = [(i, i ** 2) for i in nums if i % 2 == 0]

print(type(s))
print(s)

# Еще один пример:

s = [input('enter: ') for i in range(2)]
print(s)

# Еще:

from math import factorial

s = [factorial(x) * (x + 1) for x in range(5)]
print(s)

# Еще пример.
# Преобразование в список с конвертацией в числовые форматы int или float:

text = '1 2 3 44 5'
lst = [int(x) for x in text.split()]

# Еще пример:

list_one = [2, 3, 4]
list_two = [2 * i for i in list_one if i > 2]
print(list_two)

# Еще пример с comprehension:

s = [8, 5, 3, 2, 1, 1, 0, 1, 1, 2, 3, 5, 8]
a = [s[x] * -1 if x % 2 == 0 and x <= len(s) / 2 else s[x] for x in range(len(s))]
print(a)

# Еще пример:

s = tuple((i, i + 1) for i in range(7))
print(s)

# Это список:
nums = []
# Это заполненный список. в квадратных скобках элементы через запятую:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# И comprehensions, видимо, то же список, потому что точно так же указывается в тех же квадратных скобках:
nums = [x for x in range(8)]
print(nums)

# То есть если в квадратных скобках, то внутри них формируется список. 
# А если в круглых скобках, то это генератор, который выдает по одному элементу 
# и потому перед нужно ставить list или tuple:

nums = tuple(x for x in range(8))
print(nums)

# функция filter(), которой передается в качестве аргумента lambda:
# Фильтр - это итерируемый объект. В параметры передается функция без скобок (то есть она не вызывается) и данные.
# Объект фильтра — это итерируемый объект. Сохраняет те элементы, для которых функция вернула True.

res = list(filter(lambda x: x % 2 == 0, nums))
print(res)


# Вот то же самое с отдельным методом вместо лямбды:

def f2(i):
    if i % 2 == 0:
        return True
    else:
        return False


nums = list(filter(f2, nums))
print(nums)

# Еще пример с методом filter(). Первым параметром метода filter должен быть именно метод (без скобок):
s = [1, 2, 3.3, '4', '5']
s = list(filter(lambda i: type(i) == int, s))
print(s)

# Тернарный оператор:

f = lambda x: True if (x > 10) else False

# Функция map():

f = lambda x: 1 if (x % 2 == 0) else 2
r = list(map(f, s))

# Функция zip() собирает несколько объектов в один. к примеру можно создать из двух списков словарь:

n = [1, 2, 3, 4, 5]
m = ['a', 'b', 'c', 'd', 'e']

result = dict(zip(n, m))
print(result)

# Функция enumerate() нумерует с нуля список
result = list(enumerate(m))
print(result)

# Функция count() возвращает количество вхождений.
# Пример. Задача найти уникальные элементы в списке:
s = [x for x in nums if nums.count(x) == 1]

# Пример:
s = nums.count(5)


k = [(1,2), (3,4)]
l = [(1,2), (3,4)]

s = list(map(lambda x: x[0] * x[1], k))
print(s)

# То же самое:
s = [x[0] * x[1] for x in k]
print(s)

# Пример передачи в функцию кортеда через звездочку. Причем передать можео и список, просто распакуется он в кортеж (аргументы вроде всегда передаются параметру как константы):
def f(x, y):
    return x**y

s = [f(*x) for x in l]
print(s)

# Пример вложенных списков в comprehension:
s = [i * j for i in range(1,4) for j in range(1,4)]
print(s)

# Еще пример compehension с join(), split() и if в одной строке:

print(' '.join([i for i in input('enter words with "abc": ').lower().split() if 'abc' not in i]))


# Функция ord() возвращает номер символа в таблице utf-8:
n = ord('a')

# Функция chr() возвращает символ по номеру в таблице utf-8:
m = chr(97)

# Символ таблицы Юникод выводится вот так:

print('\u00B9')


