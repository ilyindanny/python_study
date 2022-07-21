#  список float

def get_coll():
    
    coll = []
    empty = 1
    while empty:
        try:
            coll = list(map(float, input('введите список вещественных чисел через пробел: ').split()))
            empty = 0
        except:
            coll.clear()
            print('неправильный ввод')
    return coll



#  метод вычисляет максимальный порядок дробного остатка:

def get_factor(coll):
    factor = 1
    for i in coll:
        while i * factor != int(i * factor):
            factor *= 10
    return factor




#  поиск мин и макс:

def find_max(coll, factor):
    
    maxx = coll[0]
    minn = coll[0]
    print(coll)
    print(factor, 'f')
    
    for i in range(len(coll)):
        print(round(coll[i]*factor), 'i rounded')
        coll[i] = (round(coll[i] * factor)) % factor
        
    print(coll, 'after')

    #  поиск максимальной и минимальной дробной части:
    
    for j in coll:
        if j > maxx:
            maxx = j
        if j < minn:
            minn = j

    return (maxx / factor - minn / factor)


num_collection = get_coll()

factor = get_factor(num_collection)

result = find_max(num_collection, factor)

#print(result)
