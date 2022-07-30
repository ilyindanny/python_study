
import random

def set_map(n: int) -> set:

    my_map = []
    
    for i in range(n + n + 2):
        my_map.append([0] * n)
    
    l = 1
    for i in range(n):
        for j in range(n):
            my_map[i][j] = l
            l += 1
    l = 1
    for i in range(n):
        for j in range(n, n + n):
            my_map[j][i] = l
            l += 1
    l = 1
    for i in range(n):
        for j in range(n + n, n + n + 1):
            my_map[j][i] = l
            l += n + 1
    l = n
    for i in range(n):
        for j in range(n + n + 1, n + n + 2):
            my_map[j][i] = l
            l += n - 1
    
    
    for i in range(len(my_map)):
        my_map[i] = set(my_map[i])
    
    return my_map



def win(m: set, my_map: set) -> bool:
    result = 0
    for i in my_map:
        if m >= i:
            result = i
    return result



def enter(s1: list, s2: list, player) ->list:
    done = 0
    if player == 1:
        player = '1th'
    else:
        player = '2nd'
    
    while not done:
        n = int(input('you are {}. enter: '.format(player)))
        if n in s1 or n in s2:
            print('not like that')
        else:
            done = 1
    s1.append(n)
    return s1



def enter_bot(s1: list, s2: list, matrix) ->list:
    done = 0
    while not done:
        n = random.randint(1, matrix * matrix + 1)
        if n in s1 or n in s2:
            continue
        else:
            done = 1
    s1.append(n)
    return s1



def print_all(s1: list, s2: list):
    x =[0, '·', '·', '·', '·', '·', '·', '·', '·', '·'] 
    for i in range(1, len(x)):
        for l in s1:
            if l == i:
                x[i] = 'x'
        for m in s2:
            if m == i:
                x[i] = '0'
        
    
    print('\n\t{}\t{}\t{}\n\n\t{}\t{}\t{}\n\n\t{}\t{}\t{}\n'.format(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))           


matrix = 3
my_map = set_map(matrix)

s1 = []
s2 = []
count = matrix * matrix

while True:
    
    s1 = enter(s1, s2, 1)
    print_all(s1, s2)
    m1 = set(s1)
    result = win(m1, my_map)
    if result:
        print('1th won ', result)
        break
    count -= 1
    if count == 0:
        print('drawn game')
        break
    
    s2 = enter_bot(s2, s1, matrix)
    print_all(s1, s2)
    m2 = set(s2)
    result = win(m2, my_map)
    if result:
        print('2nd won ', result)
        break
    count -= 1
    if count == 0:
        print('drawn game')
        break
