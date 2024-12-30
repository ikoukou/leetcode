# 找到指定数组中的零，并将其全部放到数组的最右边，题目要求不能复制数组，只能原地操作

nums = [4,2,4,0,0,3,0,5,1,0]

if len(nums) < 2:
    print(nums)
left = 0
right = 1
while left < len(nums) and right < len(nums):
    if nums[left] == 0:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    else:
        left += 1
        right += 1
print(nums)
