def f1():
    print('helo world!')

def f2(sym, count = 3):
    print(sym * count)


def f3(f):
    n = 1
    for item in range(2, f + 1):
        n += item
    print(n)


def f4(sym, *nums):
    res = ''
    for item in nums:
        res += str(item) + ', '
    print(res, end='')


def f5(s):
    n = 1
    m = 2
    temp_result = 0
    for item in range(s):
        temp_result = n + m
        n = m
        m = temp_result
    print('\n', m)






