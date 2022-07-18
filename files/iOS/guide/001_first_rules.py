# комментарии начинаются символом решетки. hotkeys: Ctrl + /

# метод вызывается через точку (то есть как бы метод экземпляра). а статические методы тут тоже принимают аргументы и
# называются функции


# int(name) или str(name) - явное приведение типа
# print(int(input('введите число ')) + 10)

# print выводит через запятую разные типы данных
# также есть разделители слов, указывающиеся после запятой, sep='/' и отмена переноса строки end=' / ' (либо как раз
# перенос строки end='\n')указываются после переменных:

name = '1'
age = 2

print(name, age, sep=' / ')

print(name, end=' пробел ')
print(age, end='\n')  # тут курсор будет перенесен на следующую строчку

# табуляция
print('\t {0} \t and \t {1}'.format(name, age))

# ввод с консоли:

# name = input('введите что угодно...  ')  # тут в консоль выводится подсказка

# print(name)

# возведение в степень **
# целая часть от деления //

a = 11
b = 12
print(a / b)  # тут в любом случае приведение к float
print(a // b)  # тут результат деления нацело

# or and и not - логические операторы

# логический оператор:


if a < 1:
    print('true')
elif a == 1:  # elif можно использовать много раз
    print('true')
else:
    print('false')

# while, break, continue:
x = 0
while x <= 10:
    if x % 2 == 0:
        x += 1
        continue
    print(x)
    if x == 5:
        print('условие счетчика не выполнено')
        break
    x += 1
else:  # сработает только если счетчик досчитал и не сработал break
    print('условие счетчика выполнено')

# индекс символа строки можно указывать с конца (первая с конца это -1, а не -0):

text = "abcdef ghijkl"
print(text[-1])

# срезы: [1 : 4], или [ : 4], или [1 : ]. вторая цифра — это тот символ, который уже не печатается:
print(text[2: 4])

# длина (это функция):
print(len(text))

# поиск, возвращает индекс первой буквы (это метод, вызывается через точку):
text.find('a')

# разбиение на массив строк. разделитель по умолчанию — пробел (тоже метод, вызывается через точку):
print(text.split())

# проверка на число (true или false):
print(text.isdigit())

# приведение к нижнему илм верхнему регистру
# text.upper()
# text.lower()
# x = 0
# while input('введите b ').lower() != 'b':
#     print('more')

# вызов справки:
# help(str)
# или смотреть на pythonworld.ru

# желательный формат строки:
print('print: {1} и {0}!'.format(text, 'world'))

# списки это вроде массива. типы могут быть разные. объявляется так:

text_list = []
# или сразу с инициализацией:
text_list = ['abc', '123', 456]

# срез списка возвращает список:
text_list_cut = text_list[0: 2]
print(text_list_cut)

# добавление элемента в конец списка:
text_list.append('789')
print(text_list)

# добавление элемента в указанную позицию:
text_list.insert(2, 'abc')

# возвращает последний элемент, удаляя его из массива:
text_pop = text_list.pop()  # сейчас text_pop равен '789'
print(text_pop)

# возвращает указанный элемент по индексу, удаляя его из массива:
text_pop = text_list.pop(2)

# метод очищает весь список:
# text_list.clear()

# удаление элемента из списка:
text_list.remove(456)
print(text_list)

# удаление элемента по индексу:
del text_list[1]
print(text_list)

# функция возвращает длину списка:
print(len(text_list))

# форматирование:
# ' '.join(a) печатает массив ровнее
# print(*a) печатает массив как текст


# способ поиска одной строки в другой по срезу if b in a[i:i+len(b)]:

a = 'abcdefcd'
b = 'cd'
for i in range(len(a)):
    if b in a[i:i + len(b)]:
        print('+1')

# либо то же самое при помощи a.count(b):
res = a.count(b)
# можно со срезом:
print(a.count(b, 1, 5))
# либо метод find, но он вернет индекс, либо -1, если не нашел:
res = a.find(b)

# вот счетчик всех находок:
for i in range(len(a)):
    res = a.find(b, i, i + len(b))
    if res > 0:
        print('+1 ')

value = None  # объявление переменной без инициализации (именно с прописной буквы)

print(type(value))  # вывод в консоль типа переменной

a, b = 1, 2
print('{1} и {0}'.format(a, b))  # хороший способ форматирования строки

# print(f'{b} и {a}') интерполяция. тоже норм способ, но у меня в телефоне не работает

col = []  # так объявляется список
col = ['1', '2', '3']  # инициализация массива

# 9 im col - ищет 9 в col:
col = [3, 9, 4, 5, 2]
print(col)
print(9 in col)

a = int(input(
    'введите число '))  # ввод данных. в скобках функции можно указать сообщение. int конвертирует в целое,
# так как по умолчанию ввод возвращает строку

b = int(input('введите число '))
print(type(a / b))  # даже если тип ввода был указан как int, деление все равно преобразует в float

c = round(a / b)  # округление по математическим правилам
c = round(a / b, 1)  # указание количества знаков округления

a = a > b > c  # допускается неравенство с несколькими элементами.  сравнения соотносятся между собой. то есть в
# в данном примере C должна быть больше B

a = a > b or b < c  # дизъюнкция
a = a > b or not b < c  # похоже, что not инвертирует выражение
print(a)

# and - это логическое умножение, потому ято 1* 0 = 0
# соответственно приоритет and выше яем or, потому что оно умножение

# функция map() позволяет присваивать переменным элементы литерала, разделяя по указанному разделителю (по умолчанию
# по пробелу)
a, b = map(int, input('введите два числа через запятую: ').split(','))
col = list(map(int, input('введите несколько чисел через запятую: ').split(',')))  # а так вообще сразу список

# классно на ноль проверять выражения без приравнивания:
if a and b:
    print('ок')

# range(5) - это счетчик от 0 до 4
# range(5, 9) - это от 5 до 8
# range(2, 7, 2) - это от 2 до 6 с шагом 2
col = list(range(10))  # это заполнение списка по порядку

col = list(range(20, 9, -2))  # это заполнение задом наперед с шагом 2


# изменяемые только списки (из пройденного)
# следовательно, b = a[1,2,3] ссылается на ту же ячейку памяти
# если нужна именно копия, то нужно делать срез от нуля до конца: b = a[:]. присвоение по индексу b = a[2] тоже
# создает копию

# params:
def f(param, *args):
    for j in args:
        print(str(j), param, end='')


f(' 🌺 ', 1, 3, 9, 4, 6, 1)

# в Pycharm:
#   Shift - F6 переименование переменной
#   Ctrl-R поиск в файле
#   Ctrl-Shift-R поиск по всем файлам


#конструкция match (не раьотаем в моем мобильном компиляторе)
# match a:
#     case 2:
#         print()
#     case _:
#         print()

# говорят, exit() позволяет не выполнять код, написанный после. у меня программа простт вылетает после него.


# переменной можно задать тип так:
#testing_string: str = ''
# но в телефоне не работает


