# моя единственная рекрсия. числа Фибоначчи:(тока считает неверно)

def fib(i):
    if i in [2]:
        return 1
    else:
        return (fib(i+1) + fib(i+1))
            
        

print(fib(0))



def f(result, n):
    if n in [5]:
        return result
    else:
        return f(result+str(n*n)+' ',n+1)

print(f('', 2))





















