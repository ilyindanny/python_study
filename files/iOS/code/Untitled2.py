a = float(input('введите число '))

def first_num(x):    x = x * 10    x = x % 10    if x == 0:        print ('no')    else:        print(int(x))first_num(a)
