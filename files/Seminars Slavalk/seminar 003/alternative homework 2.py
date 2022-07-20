#  проверяет, могут ли значения быть преобразованы в float
#  возвращает список float только с дробными значениями и целой частью = 0


def get_coll():
    digit = 1
    new_coll = []
    while digit:
        try:
            coll = list(input('введите список вещественных чисел через пробел: ').split())
            #  проверка на правильный ввод и создание нового списка
            for i in coll:
                if not i.isdigit():
                    new_coll = float(i)
            digit = 0
        except:
            new_coll.clear()
            print('невозможно преобразовать в float')
    return new_coll




def find_max(coll):
    maxx = coll[0]
    minn = coll[0]
    factor = 1
    
    # цикл вычисляет максимальный порядок дробного остатка:
    for i in coll:
        while i * factor != int(i * factor):
            factor *= 10
            
    for i in range(len(coll)):
        coll[i] *= factor % factor

    #  поиск максимальной и минимальной дробной части:
    for j in coll:
        if j > maxx:
            maxx = j
        if j < minn:
            minn = j

    

    return (maxx * factor - minn * factor) / factor


num_collection = get_coll()

print(find_max(num_collection))
