
# Строки соклиняются по умолчанию

s = 'Hello ' 'World' '!'
print(s)


# Округление для метода format()

print('{0: .3}'.format(1.1234567))


# Метрд format() может обрабатывать ключевые слова:

print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))


# Тройные кавычки это не только комментарии (PyCharm рекомендует три двойных кавычки для комментария), но и ограничение сложносоставного литерала:

s = '''текст
            текст'''
print(s)
# И наоборот, тут явное обозначение соединения строк (обозначается обратным слэшем):

s = '''текст \
        текст'''
print(s)

# если переносится строка с незакрытой скобкой, то обратный слэш можно не ставить.
        

# Точка с запятой ; это окончание логический строки. Но не рекомендуется писать как в этом примере:

a = 16; b = 3


# сдвиг влево или вправо. по сути сдвиг на 1 - это степени двойки:

a << 1
a >> 1


# время в пользовательском формате:

import time
print(time.strftime('%Y %m %d; %H:%M %S'))

# мировре время:

import datetime
datetime.datetime.now()


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



# Для получения параметров, переданных функции, в виде кортежа или словаря, 
# существуют специальные приставки «*» или «**» соответственно. 
# Это особенно полезно в случаях, когда функция может принимать переменное число параметров.

def powersum(power, *args):
    '''Возвращает сумму аргументов, возведённых в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
        return total

powersum(2, 3, 4)




# Функции exec() и eval() выполняют программу, указанную строкой:
exec('print("Здравствуй, Мир!")')
eval('2*3')


# Функция repr() возвращает строковое значение объекта

repr(lst)











