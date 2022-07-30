

# map
# в map передается функция без скобок

str_nums = '1 2 3 4 5 6 7 8'

nums = list(map(int, str_nums.split()))   # это итерируемый объект типа map
 

# а это comprehensions, возвращающий кортежи в список
# перед for должно быть написано только то, что непосредственно возвращается:

s = list([(i, i ** 2) for i in nums if i % 2 == 0])

print(type(s))
print(s)

# Еще один пример:

s = [input('enter: ') for i in range(2)]
print(s)

# Еще:

from math import factorial
s = [factorial(x) * (x + 1) for x in range(5)]
print(s)

# Еще пример.
# Преобразование в список с конвертацией в числовые форматы int или float:

text = '1 2 3 44 5'
lst = [int(x) for x in text.split()]

# Еще пример:

list_one = [2, 3, 4]
list_two = [2*i for i in list_one if i > 2]

print(list_two)


# это список:
nums = []
# это заполненный список. в квадратных скобках элементы через запятую:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# и comprehensions, видимо, то же список, потому что точно так же указывается в тех же квадратных скобках:
nums = [x for x in range(8)]
print(nums)

# То есть если в квадратных скобках, то внутри них формируется список. 
# А если в круглых скобках, то это генератор, который выдает по одному элементу 
# и потому перед нижно ставить list или tuple:

nums = tuple(x for x in range(8))
print(nums)



# функция filter(), которой передается в качестве аргумента lambda:

res = list(filter(lambda x: x % 2 == 0, nums))

# фильтр - это итерируемый объект. в скобки передается функция без скобок (то есть не вызывается) и данные.
# объект фильтра — это итерируемый объект. он сохраняет те элементы, для которых функция вернула True.
print(res)

# вот то же самое с отдельным методом вместо лямбды:

def f2(i):
    if i % 2 == 0:
        return True
    else:
        return False


nums = list(filter(f2, nums))
print(nums)














