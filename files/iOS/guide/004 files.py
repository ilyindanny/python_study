# работа с файлами



import json
colors = ['red ', 'green ', 'blue']  # это просто список для примеров

# 'a' это  дозапись, 'w' перезапись заново, а 'r' - это чтение
data = open('file.txt', 'w')
data.writelines(colors)  # разделителей не будет
data.write('\nLINE\n')
data.close()


# второй вариант как открыть. после этого блока связь с файлом разрывается автоматически


# пекомендуемый способ открытия файла.
# "альяс" - это замена имени файла на псевдоним (в примере это псевдоним data):

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



# Для имён, содержащих пробелы, необходимо использовать двойные кавычки внутри строки.


source = ['"C:\\My Documents"', 'C:\\Code']

# Если в строке адреса обратный слэш, то он воспринимается программой как знак отмены символа. Поэтому нужно использовать сырую строку:

source = r'files\iOS\guide\004 files.py'


# Пример созранения данных в файл при помощи встроенной библиотеки pickle. Сохранение в битовом формате данных. Такая запись в файл называется консервацией pickling, а извлечение данных из файла расконсервацией unpickling:

import pickle

# имя файла, в котором мы сохраним объект:

shoplistfile = 'shoplist.txt'

# список покупок:

shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл:

f = open(shoplistfile, 'wb')

pickle.dump(shoplist, f) # помещаем объект в файл f.close()

del shoplist # удаление переменной shoplist

