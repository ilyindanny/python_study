
'''
#  в телефоне не работает:

from pathlib import Path


path = Path('file.txt')

with open(path, 'a') as data:
    data.write('line+')
'''


# а вот так работает даже в телефоне!!!

import os

path_1 = os.path.join('folder', 'data.txt')
with open(path_1, 'w') as data_1:
    data_1.write('Hello World!!!')




#  либо без библиотеки так:

path = 'folder/file.txt'

#  открыть, записать:
with open(path, 'w') as data:
    data.write('Hello World!!!')
    data.write('\n**************')
    data.write('\n--------------')

#  считать весь файл:
#with open(path, 'r') as data:
#    my_text = data.read()
#print(my_text)


#  считать пять символов:
#with open(path, 'r') as data:
#    my_text = data.read(5)
#  print(my_text)

#  считать все по строке:
with open(path, 'r') as data:
    for line in data:
        print(line)
    
#  считать по строке два раза:
with open(path, 'r') as data:
    print(data.readline())
    print(data.readline())
    
path_xcl = 'folder/tab_1.xlsx'
with open(path_xcl, 'r') as data:
    print(data.readline())
    print(data.readline())
    




