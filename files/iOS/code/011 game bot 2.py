

import random

def set_map(n: int) -> set:

    map = []
    
    for i in range(n + n + 2):
        map.append([0] * n)
    
    l = 1
    for i in range(n):
        for j in range(n):
            map[i][j] = l
            l += 1
    l = 1
    for i in range(n):
        for j in range(n, n + n):
            map[j][i] = l
            l += 1
    l = 1
    for i in range(n):
        for j in range(n + n, n + n + 1):
            map[j][i] = l
            l += n + 1
    l = n
    for i in range(n):
        for j in range(n + n + 1, n + n + 2):
            map[j][i] = l
            l += n - 1
    
    
    for i in range(len(map)):
        map[i] = set(map[i])
    
    return map



def win(m: set, map: set) -> bool:
    result = 0
    for i in map:
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
            # нужные элементы на карте
        good_list = []
        for i in range(len(map)):
            count = 1
            for j in s1:
                if j in map[i]:
                    count = 0
            if count:
                good_list.append(map[i])
    
    
    # шаблон цифр для поиска
        nums = []
        for i in range(matrix * matrix):
            nums.append([i + 1, 0])
    
    
    # более встречающиеся цифры
        for i in good_list:
            for j in i:
                for k in range(len(nums)):
                    if j == nums[k][0]:
                        nums[k][1] += 1
    
        new_nums = []
        max = 0
    
        for i in range(len(nums)):
            if nums[i][1] > nums[max][1]:
                max = i
    
        new_nums.append(nums[max])
        del nums[max]
    
        max = new_nums[0][1]

        for i in range(len(nums)):
            if nums[i][1] == max:
                new_nums.append(nums[i])
        nums = []
        for i in new_nums:
            nums.append(i[0])
        

    
    
    # поиск на гуд-карте нужных цифр
    # в каком варианте больше всего нужных цифр
        best = []
        for i in range(len(good_list)):
            best.append([i, 0])
            for j in nums:
                if j in good_list[i]:
                    best[i][1] += 1
    
    
    
    
        nums = []
        max = 0
    
    # выбрать из лучших
    # вернет индексы нужных отрезков
        for i in range(len(best)):
            if best[i][1] > best[max][1]:
                max = i
    
        nums.append(best[max])
        del best[max]
    
        max = nums[0][1]

        for i in range(len(best)):
            if best[i][1] == max:
                nums.append(best[i])
        best = []
        for i in nums:
            best.append(i[0])
        
        
    
    
        index1 = random.randint(0, len(best)-1)
    
        three = list(good_list[index1])
    
        index2 = random.randint(0, 2)
    
        n = three[index2]
    
    
        
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
map = set_map(matrix)

s1 = []
s2 = []
count = matrix * matrix

while True:
    
    s1 = enter(s1, s2, 1)
    print_all(s1, s2)
    m1 = set(s1)
    result = win(m1, map)
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
    result = win(m2, map)
    if result:
        print('2nd won ', result)
        break
    count -= 1
    if count == 0:
        print('drawn game')
        break
