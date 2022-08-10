
nums = ''
flag = 1

while flag:
    nums = input('enter: ')
    for i in nums:
        if i in '0123456789+-*/^()':
            flag = 0
    if flag:
        print('broken input')



def get_list(n: str) -> list:
    nums = []
    collect_nums = ''
    
    if n[0].isdigit:
        collect_nums = '+'
    
    for i in range(len(n)):
        if n[i] in '0123456789':
            collect_nums += n[i]
        else:
            if len(collect_nums):
                nums.append(collect_nums)
                collect_nums = ''
            nums.append(n[i])
    if len(collect_nums):
                nums.append(collect_nums)
    
    return nums

nums = get_list(nems)    
print(nums)


print(nums)





nums = '21*(2*(21+32))-(22-2)'
print(nums)

def get_list(n: str) -> list:
    nums = []
    collect_nums = ''

    for i in range(len(n)):
        if n[i] in '0123456789':
            collect_nums += n[i]
        else:
            if len(collect_nums):
                nums.append(collect_nums)
                collect_nums = ''
            nums.append(n[i])
    if len(collect_nums):
                nums.append(collect_nums)
    
    return nums


def math_operations(expression: str) -> str:
    k = (get_list(expression))
    print(k)
    res = 0
    for i in range(len(k)):
        if k[i] = '*':
            res = k[i]



n = nums
while '(' in n:
    index = [i for i in range(len(n)) if n[i] == '(' or n[i] == ')']

    for i in range(len(index)-1):
        if n[index[i]] == '(' and n[index[i+1]] == ')':
            
            math_operations(n[index[i]+1:index[i+1]])
            
            n = n[:index[i]] + n[index[i+1]+1:]
            break








        
    




















