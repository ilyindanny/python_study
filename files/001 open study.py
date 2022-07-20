
'''
#  в телефоне не работает:

from pathlib import Path


path = Path('file.txt')

with open(path, 'a') as data:
    data.write('line+')
'''


# а вот так работает даже в телефоне!!!

import os

#  path = os.path.join('folder', 'file.txt')
path = os.path.join('folder', 'file.txt')

print (path)

with open(path, 'a') as data:
    data.write('line+')

















