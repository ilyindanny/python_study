# работа с файлами

import file as h
import file
import json
colors = ['red ', 'green ', 'blue']  # это просто список для примеров

# 'a' это  дозапись, 'w' перезапись заново, а 'r' - это чтение
data = open('file.txt', 'w')
data.writelines(colors)  # разделителей не будет
data.write('\nLINE\n')
data.close()


# второй вариант как открыть. после этого блока связь с файлом разрывается автоматически

#  как только появляется путь с обратным слжшем, нужно сразц же обозначать его как сырую строку. иначе слэш воспринимается как символ отмены соедующего символа:
#  r'files\iOS\guide\004 files.py'

with open('file.txt', 'w') as data:  # означает "воспринимать оператор как переменную data"
    data.write('LINE = 1\n')

# вариант открытия для файла json:


with open('file.json', 'w', encoding='utf-8') as data:
    data.write(json.dumps('LINE = 1\n', ensure_ascii=False))


# третий вариант наверно

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print('{} line + data'.format(line))
data.close()

file.f1()

# но можно указать "альяс" - это замена имени файла. указывается так:

h.f2('!', 5)  # вызов функции, умножающей строку на число. по умолчанию count = 3

# причем если в строку передать число, то оно умножится и вернется произведение. а если в функции поставить +,
# то складывать откажется:

h.f2(3, 4)

# вызов функции, возвращающей факториал:

h.f3(5)

# вызов функции с кортежем:

h.f4('nums: ', 1, 2, 3, 4, 5)

# функция. прибавление суммы:

h.f5(5)
