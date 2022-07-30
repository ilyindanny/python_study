"""
Заметки из книги A Byte of Python
"""

# Строки сочленяются по умолчанию:

s = 'Hello ' 'World' '!'
print(s)

# Округление для метода format():

print('{0: .3}'.format(1.1234567))

# Метод format() может обрабатывать ключевые слова:

print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))

# Тройные кавычки это не только комментарии (PyCharm рекомендует три двойных кавычки для комментария),
# но и ограничение сложносоставного литерала:

s = '''текст
текст'''
print(s)

# И наоборот, тут явное обозначение соединения строк (обозначается обратным слэшем):

s = '''текст \
текст'''
print(s)

# если переносится строка с незакрытой скобкой, то обратный слэш можно не ставить.

# Точка с запятой ; это окончание логической строки, но так писать не рекомендуется. Вот так не нужно:

a = 16; b = 3

# Сдвиг влево или вправо. По сути сдвиг на 1 - это степени двойки:

a << 1
a >> 1


# Зарезервированное слово global объявляет переменную с глобальной видимостью.
# Зарезервированное слово nonlocal объявляет переменную во вложенном методе с видимостью для основного метода.

# Обращение по именам при вызове метода:

def func(l, m=5, q=10):
	print('l', l, 'm', m, 'q', q)


func(4, q=11)


# Переменное число параметров.
# Как только присвоено все основное, остальное будет присваиваться параметру со звездочкой
# (кортеж, потому что нужна именно константа) или двумя звездочками (словарь))

def total(l, *numbers, **phonebook):
	print('a', l)

	# проход по всем элементам кортежа
	for single_item in numbers:
		print('single_item', single_item)

	# проход по всем элементам словаря
	for first_part, second_part in phonebook.items():
		print(first_part, second_part)


total(10, 1, 2, Jack=1123, John=2231)


# В методе после переменного числа параметров можно указать еще один параметр,
# но он обязательно будет параметром по ключу, иначе его не отделить от предыдущих значений.
# У такого параметра может быть указано значение по умолчанию, например extra_number=6,
# но передавать аргументы в такой параметр все равно можно только по ключу:


def total(initial=5, *numbers, extra_number=6):
	count = initial
	for number in numbers:
		count += number
	count += extra_number
	print(count)


total(10, 1, 2, 3, extra_number=50)


# total(10, 1, 2, 3)  # А это вызовет ошибку, поскольку не указано значение аргумента по умолчанию для 'extra_number'.


# Строки документации. Первая логическая строка функции — строка документации.
# В первой строчке основное название функции или основное действие, что она возвращает.
# Потом пустая строка.
# Потом в третьей строке подробное описание.
# Доступ к строке документации функции printMax можно получить с помощью атрибута этой функции
# (т.е. имени, принадлежащего ей) точки и __doc__ либо при помощи функции help(printMax)
# также функция help() попросту выводит те самые строки документации

def printMax(x: int) -> None:
	'''Заголовок. Что выводит функция.

	Это третья строка, в ней помещают описание функции.'''

	pass


print(printMax.__doc__)
help(printMax)

# Чтобы импортировать функцию randint() прямо в программу
# и не писать всякий раз random. при обращении к ней, можно воспользоваться выражением «from random import randint».
# Для импорта всех имён, использующихся в модуле random,
# можно выполнить команду «from random import *».
# Это работает для любых модулей.
# Но это ведет к риску пересечения имен,
# поэтому лучше все-таки писать import random, то есть вызывать функцию через имя_модуля.имя_функции

from random import randint

a = randint(2, 5)

# удаление переменной:
a = 5
del a

# время в пользовательском формате:

import time

print(time.strftime('%Y %m %d; %H:%M %S'))

# мировое время:

import datetime

datetime.datetime.now()

# Сырые строки. Вместо «C:\\Documents»  можно писать «r'C:\Documents'».
# Однако, не используйте «'C:\Documents'», так как в этом случае окажется,
# что вы пытаетесь применить неизвестную управляющую последовательность \D.

# Пример создания класса и метода:

class Person:
    def __init__(self, name):
        self.n = name
    def say_hi(self):
        print('Привет! Меня зовут', self.n)


p = Person('Swaroop')
p.say_hi()



# Пример класса и подкласса.
# Тут в основном классе как бы первая половина, а в подклассе вторая. в рещультате конда вызывается метод подкласса, его первая часть берется из класса, а вторая из подкласса:

class SchoolMember:
    '''Представляет любого человека в школе.'''
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))



g = Teacher('ivan', 34, 500000)
g.tell()



# Мой пример класса и подкласса:

class Customers:
    
    '''Создает клиента '''
    
    def __init__(self, name, tel):
        self.n = name
        self.t = tel
    
    def print_info(self):
        '''Первая часть метода печати '''
        print(self.n, self.t, end='')



class Visit(Customers):
    
    '''Создает обращение '''
    
    def __init__(self, name, tel, date):
        Customers.__init__(self, name, tel)
        self.d = date
    
    def print_info(self):
        '''Вторая часть метода печати '''
        Customers.print_info(self)
        print(',', self.d,)
        




visit_001 = Visit('Olga', '+7 (925) 785-21-78', '28.07.2022')

visit_001.print_info()


# Так напечатает только имя и тел из основного класса:
Customers.print_info(visit_001)




# Обработчик ошибок try.
# Блок else выполняется только если наконец получилось сделать без ошибок:

try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('ошибка EOF')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))



# Создание пользовательского класса исключения:

class ShortInputExc(Exception):
    
    '''Пользовательский класс исключения.'''
    
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputExc(len(text), 3)

except ShortInputExc as ex:
    print('ShortInputExc: Длина введённой строки -- {0}; ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))


#  После конструкции try возможны дополнительные действия в блоке finaly (независимо от исключения):

try:
    2 + 'f'
except:
    print(0)
finally:
    print('Дополнительные действия в любом случае')


# Таймер ожидания:

import time

time.sleep(5)


# Метод может возвращать более одного значения. При распаковке в переменные достаточно поставить звездочку, чтобы в одной переменной было присвоено все остальное:

def f():
    return ('a', 'b', 'c')

a, *b = f()

# Пример с Лямбдой и методом sort():

points = [{'x': 2, 'y': 3}, {'x': 1, 'y': 2}]
points.sort(key=lambda i: i['y'])
print(points)