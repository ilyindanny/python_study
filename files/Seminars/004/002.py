
import random
from decimal import Decimal


s = list([random.randint(0, 5) for x in range(10)])
print(s)

s_odd = [x for x in s[1::2]]
print(s_odd)



def mult(s):
    s_mult = []
    length = len(s)

    for i in range(length // 2):
        s_mult.append(s[i] * s[length - i - 1])
    result = ''
    if len(s) % 2:
        result += 'список нечетный: \n'
    result += str(s_mult)
    return result


print(mult(s))






def rand():
    x = 0
    if random.randint(0, 3):
        x = round(random.random(), random.randint(0, 4))
    x = Decimal(str(x)) + Decimal(str(random.randint(0, 9)))
    
    return str(x)


s = list([rand() for x in range(8)])
print(s)


def find_minn_maxx(s):
    minn = 0
    maxx = 0
    new_s = []
    
    for i in s:
        if '.' in i:
            new_s.append(float('0.' + i.split('.')[1]))

    for i in range(len(new_s)):
        if new_s[i] > new_s[maxx]: maxx = i
        if new_s[i] < new_s[minn]: minn = i
    
    result = Decimal(str(new_s[maxx])) - Decimal(str(new_s[minn]))
    print('max {} - min {}'.format(new_s[maxx], new_s[minn]))
    print('разность min и max = {}'.format(result))



find_minn_maxx(s)




# revers





def b(x):
    n = x
    res = ''
    while n:
        res = str(n % 2) + res
        n //= 2
    
    print(x, ' - ', res)


b(3)



def fib(n):
    
    res_m = [0, 1]
    res = [0, 1]
    
    for i in range(n - 1):
        res_m.append(res_m[i] + res_m[i + 1] * -1)
    
    for i in range(n - 1):
        res.append(res[i] + res[i + 1])
    
    result = []
    for i in range(len(res_m) - 1, 0, -1):
        result.append(res_m[i])
    for i in res:
        result.append(i)
    
    print(*result)

fib(5)
    
        

def fib2(n):
    
    f = [0, 1]
    
    for i in range(2, n+1):
        f.append(f[i - 1] + f[i - 2])
    
    f.insert(0, 1)
    f.insert(0, -1)

    
    for i in range(0, n-2):
        f.insert(0, (f[1]) - (f[0]))
    
    
    print(f)
    return f
fib2(5)






