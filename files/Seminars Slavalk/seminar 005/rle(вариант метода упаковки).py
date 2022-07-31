# # Задание 4:Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


data = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def rle_pack(data):
    result = ''
    count = 1
    index = 0
    for i in range(1, len(data)):
        if data[i] == data[index]:
            count += 1
            if i == len(data) - 1:
                result += data[index] + str(count)
                count = 1
                index = i
                
        else:
            result += data[index] + str(count)
            count = 1
            index = i

    return result
    
print(rle_pack(data))
        