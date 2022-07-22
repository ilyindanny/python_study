
path1 = '002_polynoms_1.txt'
path2 = '002_polynoms_2.txt'
path3 = '002_polynoms_result.txt'


with open(path1, 'r') as file:
    a = file.readline()
with open(path2, 'r') as file:
    b = file.readline()


# поиск коэффициентов

def get_coefficients(data: list) -> list:
    
    data = data.split()[0:-2]
    if data[0] != '-':
        data.insert(0,'+')
    
    nums = []
    
    for i in range(1, len(data), 2):
        nums.append(data[i - 1])
        for j in data[i]:
            if j.isdigit():
                nums[len(nums) - 1] += j
            else:
                break
        for i in range(len(nums)):
            nums[i] = int(nums[i])
    return nums



# сложение

def sum_of_lists(a: list, b: list) -> list:
    
    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])
        
    return res



print('многочлен a: ', get_coefficients(a))
print('многочлен b: ', get_coefficients(b))

a = get_coefficients(a)    
b = get_coefficients(b)    
result = sum_of_lists(a, b)


with open(path3, 'w') as file:
    file.write(result)

print(f'в файл {path3} сохранен результат: {result}')
  