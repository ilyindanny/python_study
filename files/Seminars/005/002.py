
# 
from random import randint
k = 3

coefficients = [randint(0, 5) for i in range(k + 1)]
print(coefficients)

def fill_items(c, k):
    if k == 0:
        return str(c)
    elif k == 1:
        return str(c) + 'x'
    else:
        return str(c) + 'x^' + str(k)

# Мой вариант:
def get_exp(f, c, k):
    res = ''
    for i in range(k + 1):
        if c[i]:
            res += ' + ' + f(c[i], k)
        k -= 1
    return res[2:]+ ' = 0' 

# Второй вариант (из семинара). С нулем у первого коэффициента не пашет:

def get_exp2(f, c, k):
    
    res = [f(c, k) for (k, c) in enumerate(c) if c != 0]
    
    return ' + '.join(res[::-1]) + ' = 0'

result = get_exp(fill_items, coefficients, k)

print(result)