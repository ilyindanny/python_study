# # Задание 4:Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_pack(data: str) -> str:
    """упаковка данных в строку"""
    
    pack = [[1, data[0]]]
    count = 1
    index = 0
    for i in range(1, len(data)):
        if data[i] == data[index]:
            count += 1
            pack[-1][0] = count
            pack[-1][1] = data[index]
        else:
            count = 1
            index = i
            pack.append([count, data[index]])
    
    res = ''
    for i in pack:
        res += str(i[0]) + i[1]
    return res


def rle_unpack(data: str) -> str:
    """распаковка данных"""
    
    res = ''
    nums = ''
    for i in data:
        if i.isdigit():
            nums += i
        else:
            for j in range(int(nums)):
                res += i
            nums = ''
    return res



path_1 = 'text.txt'
path_2 = 'rle_pack.txt'
path_3 = 'rle_unpack.txt'

with open(path_1) as file:
    data = file.readline()
    print(data)



result = rle_pack(data)
with open(path_2, 'w') as file:
        file.write(result)
print('в файл {} добавлены упакованные данные: {}'.format(path_2, result))


with open(path_2) as file:
    data = file.readline()

result = rle_unpack(data)


with open(path_3, 'w') as file:
    file.write(result)
print('в файл {} добавлены распакованные данные: {}'.format(path_3, result))










