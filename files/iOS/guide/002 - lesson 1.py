value = None # объявление переменной без инициализации (именно с прописной буквы)

print(type(value)) # вывод в консоль типа переменной

a, b = 1, 2
print('{1} и {0}'.format(a, b)) # хороший способ форматирования строки

# print(f'{b} и {a}') интерполяция. тоже норм способ, но у меня в телефоне не работает

col = [] # так объявляется список
col = ['1', '2', '3'] # инициализация массива

a = int(input('введите число ')) # ввод данных. в скобках функции можно указать сообщение. int конвертирует в целое, так как по умелчанию ввод возвращает строку

b = int(input('введите число '))
print(type(a / b)) # даже если тип ввода был указан как int, деление все равно преобразует в float

c = round(a / b) # округление по матеиатическим правилам
c = round(a / b, 1) # указание уоличества знаков округления

a = a > b > c # допускается неравенство с несколькими элеметами.  сравнения соотносятся между соьой. то есть в данном примере C должна быть больше B

a = a > b or b < c # дизъюнкция
a = a > b or not b < c # похоже, что not инвертирует выражение
print(a)

# and - это логическое умножение, потому ято 1* 0 = 0
# соответственно приоритет and выше яем or, потому что оно умножение

# функция map() позволяет присваивать переменным элементы литерала, разделяя по указанному разделителю (по умолчанию по пробелу)
a, b = map(int, input('введите два часла через запятую: ').split(','))
col = list(map(int, input('введите несколько чисел через запятую: ').split(','))) # а так вообще сразу список


# классно на ноль проверять выражения без приравнивания:
if a and b:
    print('ок')











