#  числа Фибоначчи:

def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


list = []

x = int(input('input: '))

for i in range (1, x + 1):
    list.append(fibo(i))
print (list)



#  моя единственная рекурсия:

def f(result, n):
    if n in [5]:
        return result
    else:
        return f(result+str(n*n)+' ',n+1)

print(f('', 2))

