# преобразование элементов списка в тип float
def make_float_collection():
    digit = 1
    col = []
    while digit:
        try:
            col = list(input('введите список вещественных чисел через пробел: ').split())
            for i in range(len(col)):
                col[i] = float(col[i])
                digit = 0
        except:
            print('невозможно преобразовать в float')
            col = []
    return col


# получение списка дробных частей чисел
def get_fractions():
    digit = 1
    new_col = []
    temp = 0
    while digit:
        try:
            col_1 = list(input('введите список вещественных чисел через пробел: ').split())
            for i in col_1:
                temp = float(i)  # проверка возможности преобразовать в float
                if float(i) != round(float(i), 0):  # проверка на наличие дроби
                    n = list(i.split('.'))  # список из целой части и дробной
                    new_col.append(float('0.' + n[1]))  # создание float элемента массива вида 0.01
                digit = 0
        except:
            print('невозможно преобразовать в float')
    return new_col


# сумма элементов массива, стоящих на нечетных индексах
def get_sum(col: list):
    result = 0
    clear_col = []
    for i in range(0, len(col), 2):
        clear_col.append(col[i])
        result += col[i]
    if result:
        print('на нечетных позициях элементы {}; ответ: {}'.format(clear_col, result))


# сумма элементов массива, стоящих на нечетных индексах
def get_sum_other(col: list):
    result = []
    pair_col = []
    n = 1
    for i in range(0, (len(col) + 1) // 2):
        result.append(col[i] * col[(len(col)) - n])
        n += 1
    print(result)


# поиск минимального и максимального элемента
def find_min_max(col_2):
    if len(col_2) > 0:
        find_max = col_2[0]
        find_min = col_2[0]
        for i in col_2:
            if find_max < i:
                find_max = i
            if find_min > i:
                find_min = i
        result = find_max - find_min
        if result:
            print(round(result, 6))


# преобразование десятичного числа в двоичное

def return_binary(numm):
    result = ''
    while numm > 0:
        result = str(numm % 2) + result
        numm //= 2
    print(result, '(2)')
