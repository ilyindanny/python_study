# создайте коллекцию 5-ю с результатами обработки списка:

collection = [6,4,2,9,8,5,3,1,7]

def f(coll):
    maxx = 0
    minn = 0
    average = 0
    
    for i in range(len(coll)):
        if coll[i] > coll[maxx]: maxx = i
            
        if coll[i] < coll[minn]: minn = i
        average += coll[i]
    
    average /= len(coll)
    
    dict = \
    {
        'максимальное число': coll[maxx],
        'минимальное число': coll[minn],
        'индекс максимального': maxx,
        'индекс минимального': minn,
        'среднее арифметическое': average
    }
    return dict


for i, j in f(collection).items():
    print(i, j)

text_for_file = ''
for i, j in f(collection).items():
    text_for_file += str((i, j)) + '\n'

with open('file.txt', 'w') as data:
    data.write(text_for_file)



# Задайте список из n чисел последовательности (1 + 1 / n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



num = int(input('\nзадайте число последовательности: '))

def f_formula(n):
    result = 0
    for i in range(1, n + 1):
        result += ((1 + 1 / i) ** i)
    print(round(result, 3))


f_formula(num)



# задайте список из n чисел Фибоначчи:

def fib(n):
    fbn = [0, 1]

    for i in range(n):
        fbn.append((fbn[i] + fbn[i + 1]))
    
    return fbn


n = int(input('задайте количество чисел Фибоначчи: '))

print(fib(n))

