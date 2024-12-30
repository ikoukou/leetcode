# 找到指定数组中最长的连续的数字的子串，返回其长度
# 以下代码运行失败，没有考虑到序列中间断裂的情况
nums = [1, 5, 2, 4, 3, 8, 9]

nums_sort = sorted(nums)
res = []
max_len = 0
for i in nums_sort:
    if len(res) == 0 or i == (res[-1] + 1):
        res.append(i)
    else:
        max_len = max(len(res), max_len)
        res = [i]
max_len = max(len(res), max_len)
print(max_len)

# 以下代码运行失败，测试长列表时导致系统超时
res = []
max_len = 0
pre = 0
for i in range(len(nums_sort)):
    if i >= pre:
        res.append(nums_sort[i])
        while (nums_sort[i] + 1 in nums_sort) and (nums_sort.index(nums_sort[i] + 1) > i):
            i = nums_sort.index(nums_sort[i] + 1)
            res.append(nums_sort[i])
        max_len = max(len(res), max_len)
        pre = i
        res = []
    else:
        pass
max_len = max(len(res), max_len)
print(max_len)

# 以下代码通过，占内存较高，且时间复杂度是Nlogn，因为使用了sorted()排序
res = []
dic = {}
max_len = 0
pre = nums_sort[0]
if len(nums) <= 1:
    print(len(nums))
for i in nums_sort:
    dic[i] = i
for i in dic.keys():
    if i >= pre:
        res.append(i)
        while i + 1 in dic.keys():
            res.append(i + 1)
            i += 1
        max_len = max(max_len, len(res))
        res = []
        pre = i
print(max_len)

# 以下代码使用set()方法，时间复杂度为O(n)
nums_set = set(nums)
max_len = 0
res = []
cur = 0
for num in nums_set:
    if num - 1 not in nums_set:
        cur = num
        res.append(num)
        while cur + 1 in nums_set:
            res.append(cur + 1)
            cur += 1
        max_len = max(max_len, len(res))
        res = []
print(max_len)
