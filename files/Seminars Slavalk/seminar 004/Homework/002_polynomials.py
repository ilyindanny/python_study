path1 = '002_polynomials_1.txt'
path2 = '002_polynomials_2.txt'
path3 = '002_polynomials_result.txt'


with open(path1, 'r') as file:
    a = file.readline()
with open(path2, 'r') as file:
    b = file.readline()


# разбор многочлена

def get_coefficients(data: str) -> list:
    
    data = data.replace('+ ', '+')
    data = data.replace('- ', '-')
    data = data.split()
    
    if data[0][0] != '-':
        data[0] = '+' + data[0]
    
    res = []
    count = 1
    
    for i in range(0, len(data) - 2):
        for j in data[i][1:]:
            if j.isdigit():
                count +=1
            else:
                break
        res.append(data[i][0] + data[i][1:count])
        if count < len(data[i]):
            res.append(data[i][count:])
        count = 1
    
    res.append(' = 0')
        
    return res


# сложение

def sum_of_lists(a: list, b: list) -> list:
    data = []
    for i in range(len(a)):
        try:
            if int(a[i]) + int(b[i]) > 0:
                data.append(' + ' + str(int(a[i]) + int(b[i])))
            else:
                data.append(' - ' + str(abs(int(a[i]) + int(b[i]))))
        except:
            data.append(a[i])
    
    
    if data[0][1] == '-':
        data[0] = '-' + data[0][3:]
    else:
        data[0] = data[0][3:]
    
    res = ''
    for i in data:
        res += i
    
    return res

print('многочлен a: ', a)
print('многочлен b: ', b)

a = get_coefficients(a)
b = get_coefficients(b)
result = str(sum_of_lists(a, b))

with open(path3, 'w') as file:
    file.write(result)

print(f'в файл {path3} сохранен результат: {result}')
