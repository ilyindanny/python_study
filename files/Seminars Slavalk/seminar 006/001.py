# Найти уникальные элементы в списке.
# Используется filter и comprehension.

nums = [1,2,3,2]


# 1:

s = list(filter(lambda x: nums.count(x) == 1, nums))
print(s)


# 2:

s = [x for x in nums if nums.count(x) == 1]
print(s)


# 3:

s = [nums[i] for i in range(len(nums)) if nums.count(nums[i]) == 1]
print(s)

