# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*
# приоритет операций стандартный.
#
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;


def get_user_input() ->str:
    """Принимает на ввод выражение, проверяет корректность и создает строку"""
    nums = ''
    flag = 1
    while flag:
        nums = input('Введите арифметическое выражение: ')
        for i in nums:
            if i in '0123456789+-*/^()' and ('*' in nums or '/' in nums or '+' in nums or '-' in nums):
                flag = 0
        if flag:
            print('Неверный ввод, используйте  + - * / ( ) и цифры')
    
    return nums


def get_list_from_str(nums: str) -> list:
    """Преобразует артфметическое выражение, заданное строкой, в список, цифры конвертирует в int"""
    res = []
    temp_collect_nums = ''
    
    for i in range(len(nums)):
        if nums[i] in '0123456789':
            temp_collect_nums += nums[i]
        else:
            if len(temp_collect_nums):
                res.append(int(temp_collect_nums))
            temp_collect_nums = ''
            res.append(nums[i])
    if len(temp_collect_nums):
                res.append(int(temp_collect_nums))
    
    return res


def math_operations(n: list) ->list:
    """Принимает выражение без скобок и производит арифметические действия. Возвращает результат вычисления"""
    nums = n[:]
    while len(nums) > 1:
        res = 0
        k = len(nums)
        l = len(nums)
        i = 0

        if '*' in nums or '/' in nums:
            if '*' in nums:
                k = nums.index('*')
            if '/' in nums:
                l = nums.index('/')
            if k < l:
                i = k
                res = nums[i-1] * nums[i+1]
            else:
                i = l
                res = nums[i-1] / nums[i+1]
            
        else:
            if '+' in nums:
                k = nums.index('+')
            if '-' in nums:
                l = nums.index('-')
            if k < l:
                i = k
                res = nums[i-1] + nums[i+1]
            else:
                i = l
                if i == 0:
                    res = nums[i+1] * -1
                else:
                    res = nums[i-1] - nums[i+1]
        
        # Если выражение является отрицательным числом в скобках, то возвращается отрицательное число:
        if i == 0:
            del nums[i:i+2]
            nums.insert(i, res)
        else:
            del nums[i-1:i+2]
            nums.insert(i-1, res)
    
    return nums


def find_result(n: list) ->list:
    """Принтмает список — арифметическое выражение. Передает методу вычисление в скобках, потом заменяет выражение в скобках на результат вычисления"""
    nums = n[:]
     
    while '(' in nums:
        
        index = [i for i in range(len(nums)) if nums[i] == '(' or nums[i] == ')']

        for i in range(len(index)-1):
            if nums[index[i]] == '(' and nums[index[i+1]] == ')':
                temp_res = math_operations(nums[index[i]+1:index[i+1]])
                nums = nums[:index[i]] + temp_res + nums[index[i+1]+1:]
                break
    
    nums = math_operations(nums)
    nums = nums[0]
    if nums < 0:
        nums = '({})'.format(nums)

    return nums


#user_input = get_user_input()
#user_input = '-21*(2*(21+32))-(22-2)-(-100)'
user_input = '224+34-16/4/2+(5-3*2-8/2)*2+56*34+16/(-4)'

nums_list = get_list_from_str(user_input)

result = find_result(nums_list)

print('{}={}'.format(user_input,result))

print('проверка методом eval():', eval(user_input))
