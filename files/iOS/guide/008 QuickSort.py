# Метод быстрой сортировки.

import random

nums = [4, 1, 6, 3, 2, 7, 8, 5]
print(nums)

# Первый вариант:

def quicksort1(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort1(s_nums) + e_nums + quicksort1(m_nums)

print(quicksort1(nums))


# Улучшенный вариант:

nums = [4, 1, 6, 3, 2, 7, 8, 5]

def quicksort2(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort2(l_nums) + e_nums + quicksort2(b_nums)

print(quicksort1(nums))





