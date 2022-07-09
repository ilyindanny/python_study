a = float(input('введите дробное число: '))

def find_digit(x):
    x = x * 10
    x = x % 10
    if x == 0:
        print ('no')
    else:
        print(int(x))

find_digit(a)


# мой новый вариант:

def find_digit():
    result = int(float(input('введите дробное число: ')) * 10 % 10)
    if result:
        print(result)
    else:
        print('нет')

find_digit()


# распечатать от -n до n

def col_from_n():
    n = int(input('введите число: '))
    col = list(range(n * -1, n + 1))
    return col

print(col_from_n())










