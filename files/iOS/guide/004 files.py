# работа с файлами

colors = ['red ', 'green ', 'blue'] # это просто список для примеров

data = open('file.txt', 'w') # 'a' это  дозапись, 'w' перезапись заново, а 'r' - это чтение
data.writelines(colors) # разделителей не будет
data.write('\nLINE\n')
data.close()



# второй вариант как открыть. после этого блока связь с файлом разрывается автоматически

with open('file.txt', 'w') as data: # означает "воспринимать оператор как переменную data"
    data.write('LINE = 1\n')
    data.write('LINE = 2\n')


# третий вариант наверно

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print('{} line + data'.format(line))
data.close()

import file
file.f1()

# но можно указать "альяс" - это замена имени файла. указывается так:

import file as h
h.f2('!', 5) # вызов функции, умножающей строку на число. по умолчанию count = 3

# причем если в строку передать число, то оно умножится и вернется произведение. а если в функции поставить +,
# то складывать откажется:

h.f2(3,4)

# вызов функции, возвращающей факториал:

h.f3(5)

# вызов функции с кортежем:

h.f4('nums: ', 1,2,3,4,5)

# функция. прибавление суммы:

h.f5(5)