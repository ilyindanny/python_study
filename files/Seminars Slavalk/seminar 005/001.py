
# задача 1

s = '1 2 3 4 5 7 9'
    
a = list([int(x) for x in s.split()])

for i in range(len(a) - 1):
    if not a[i] == a[i + 1] - 1:
        print('{}'.format(a[i] + 1), end=' ')

print()


# задача 1 второй вариант

x = list(filter(lambda i: (a[i] - a[i - 1]) != 1, range(1, len(a))))

print(x[0] + 1)
    



# задача 2
        
s = '6 7 1 9 10 9'
a = list([int(x) for x in s.split()])


nums = ['|']
marker = 0

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        if marker == 0:
            nums.append(a[i - 1])
        nums.append(a[i])
        marker = 1
    else:
        if marker == 1:
            nums.append('|')   
        marker = 0


if nums[len(nums) - 1] == '|':
    del nums[len(nums) - 1]


result = []

for i in range(len(nums)):
    if nums[i] == '|':
        result.append([])
    else:
        result[len(result) - 1].append(nums[i])
        

print(*result)
















    
        