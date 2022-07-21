#  проверяет, могут ли значения быть преобразованы в float
#  возвращает список float только с дробными значениями и целой частью = 0


def get_coll():
    digit = 1
    new_coll = []
    while digit:
        try:
            coll = list(input('введите список вещественных чисел через пробел: ').split())
            #  проверка на правильный ввод и создание нового списка
            not_zero = 0
            for i in coll:
                float(i)
                if not i.isdigit():
                    new_coll.append(float('0.' + i.split('.')[1]))
                    if float(i.split('.')[1]) > 0:
                        not_zero += 1
            1 / (len(new_coll) - 1) / not_zero  # деление на 0, если длина списка = 1, либо не было значащей части дроби
            digit = 0
        except:
            new_coll.clear()
            print('невозможно преобразовать в float, либо недостаточно дробных частей для вычисления')
    return new_coll


#  принимает список float, вычисляет мин и макс без погрешности float:


def find_max(coll):
    maxx = coll[0]
    minn = coll[0]
    factor = 1

    #  поиск максимальной и минимальной дробной части:
    for j in coll:
        if j > maxx:
            maxx = j
        if j < minn:
            minn = j

    # цикл вычисляет максимальный порядок дробного остатка:
    for i in minn, maxx:
        while i * factor != int(i * factor):
            factor *= 10

    return (maxx * factor - minn * factor) / factor


num_collection = get_coll()

print(find_max(num_collection))
