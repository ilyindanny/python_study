# # Задание 4:Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_pack(raw_data: str) -> str:
    """Упаковка данных в строку"""

    pack = [[1, raw_data[0]]]
    count = 1
    index = 0
    for i in range(1, len(raw_data)):
        if raw_data[i] == raw_data[index]:
            count += 1
            pack[-1][0] = count
            pack[-1][1] = raw_data[index]
        else:
            count = 1
            index = i
            pack.append([count, raw_data[index]])

    res = ''
    for i in pack:
        res += str(i[0]) + i[1]
    return res


def rle_unpack(packed_data: str) -> str:
    """Распаковка данных"""

    res = ''
    nums = ''
    for i in packed_data:
        if i.isdigit():
            nums += i
        else:
            for j in range(int(nums)):
                res += i
            nums = ''
    return res



path_1 = 'text.txt'
path_2 = '003 rle_pack.txt'
path_3 = '003 rle_unpack.txt'

with open(path_1) as data_file:
    data = data_file.readline()
    print(f'исходная строка: {data}')



result = rle_pack(data)
with open(path_2, 'w') as data_file:
    data_file.write(result)
print(f'в файл {path_2} добавлены упакованные данные: {result}')


with open(path_2) as data_file:
    data = data_file.readline()

result = rle_unpack(data)


with open(path_3, 'w') as data_file:
    data_file.write(result)
print(f'в файл {path_3} добавлены распакованные данные: {result}')










