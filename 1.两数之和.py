# 字典是哈希表的一种实现，效率更高。并且查询 key 的速度也要比查询 values 更快，因此第二段代码速度更快。复杂度都是O(n)。

nums = [3, 3]
target = 6
test = {}
for k, v in enumerate(nums):
    if target - v in test.values():
        print([nums.index(target - v), k])
    else:
        test[k] = v


# 以下代码更快
test = {}
for k, v in enumerate(nums):
    if target - v in test.keys():
        print([test[target - v], k])
    else:
        test[nums[k]] = k
