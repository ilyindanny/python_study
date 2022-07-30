# Выбрать уникальные элементы.

from random import randint

nums = [randint(0, 5) for x in range(5)]
print(nums)

stop_list = set()
result = set()
for i in nums:
    if i in result:
        stop_list.add(i)
    result.add(i)

result = result.difference(stop_list)

print(result)

# Второй вариант рещения задачи:
result = []
for i in nums:
    if nums.count(i) == 1:
        result.append(i)
print(result)

# Третий вариант:

result = [x for x in nums if nums.count(x) == 1]
print(result)
