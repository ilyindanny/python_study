
import datetime


# метод возвращает целое одноразрядное число:

def mono_random():
    nums = 0
    while nums < 999999999:
        try:
            nums += int(str(datetime.datetime.now())[-6:-1]) * int(str(datetime.datetime.now())[-5:])
    
    # из полученного числа забирается одна цифра по случайному индексу:
            result = int(str(nums)[-int(str(datetime.datetime.now())[-1])])
        except:
            continue
    return result



# метод возвращает целое число, в промежутке чисел, указанных в параметрах:

def multi_random(start, end):
    
    # создание списка пригодных пользователя чисел:
    col = []
    for i in range(start, end):
        col.append(i)
    
    # повторяющееся деление на два и рандомный выбор половины для последующего деления:
    a = 0
    b = len(col) - 1
    
    while b - a > 10:
        if mono_random() > 4:
            a = a + (b - a) // 2
        else:
            b = b - (b - a) // 2

    # когда остаток меньше десяти, число выбирается новым рендомом: 
    while True:
        f = mono_random()
        if f <= b - a:
            index = a + f
            break
                
    return(col[index])


# это добавка. создание на основн рендома двоичного числа и преобразование в десятичное число:



def f():
    n = []
    result = 0
    
    for i in range(20):
        n.append(multi_random(0, 2))
    print(n)
    
    for i in range(len(n)):
        if n[i] != 0:
            result += 2 ** (len(n) - i - 1)
    print(result)


f(n)



# альтернативный способ получения рандомного числа по методу time

'''
import time

def mult_t():
    a = list(str(time.time()).split('.'))
    return a[1]



import datetime

# метод возвращает целое одноразрядное число:

def mono_random():
    nums = 0
    while nums < 999999999:
        try:
            nums += int(mult_t()[-6:-1]) * int(mult_t()[-5:])
    
    # из полученного числа забирается одна цифра по случайному индексу:
            result = int(str(nums)[-int(mult_t()[-1])])
        except:
            continue
    return result
'''

