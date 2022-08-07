nums = [2,3,1,9,0]
print(nums)

def sort(nums, left, right):
    
    if left == right: return
    middle = left
    for i in range(left, right):
        if nums[i] <= nums[right - 1]:
            nums[i], nums[middle] = nums[middle], nums[i]
            middle +=1

    sort(nums, left, middle - 1)
    sort(nums, middle, right)

sort(nums, 0, len(nums))
print(nums)

