# 尝试汇总常见排序算法和实现
# 冒泡排序 时间O(n^2) 稳定
# 从第一个元素开始，比较每一个相邻的元素，如果前者更大，那就做一次交换，继续比较每一个相邻的元素。完成一次循环后，从第二个元素以此类推
# 选择排序 时间O(n^2) 不稳定：[5, 5', 2]
# 从第一个元素开始，依次与后面所有的元素比较，找到更小的放到最前边。然后开始第二个元素，依次类推
# 插入排序 时间O(n^2) 稳定
# 将第一个元素看做有序序列，然后遍历所有元素，将后面的元素与有序序列里的每一个元素比较，插入到合适的位置。然后开始下一个元素
# 归并排序 时间O(Nlogn)
# 将数组二等分，然后递归，直到每个子数组只有两个元素，然后比较，再递归回来
# 快速排序 时间O(Nlogn) 但是常数比归并小
# 选择第一个值作为轴，遍历数组，将大于轴的和小于轴的值分别放在轴的两边，然后重复操作


# 冒泡排序 时间O(n^2) 稳定
# 从第一个元素开始，比较每一个相邻的元素，如果前者更大，那就做一次交换，继续比较每一个相邻的元素。完成一次循环后，从第二个元素以此类推
# num = [3, 5, 8, 1, 4, 6, 2, 7, 9]
# for i in range(len(num)):
#     for j in range(len(num) - 1):
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]
# print('the result is:', num)

# 选择排序 时间O(n^2) 不稳定：[5, 5', 2]
# 从第一个元素开始，依次与后面所有的元素比较，找到更小的放到最前边。然后开始第二个元素，依次类推
# num = [3, 5, 8, 1, 4, 6, 2, 7, 9]
# for i in range(len(num)):
#     for j in range(i+1, len(num)):
#         if num[i] > num[j]:
#             num[i], num[j] = num[j], num[i]
# print('the result is:', num)

# 插入排序 时间O(n^2) 稳定
# 将第一个元素看做有序序列，然后遍历所有元素，将后面的元素与有序序列里的每一个元素比较，插入到合适的位置。然后开始下一个元素
# num = [3, 5, 8, 1, 4, 6, 2, 7, 9]
# for i in range(1, len(num)):
#     for j in range(i):
#         if num[j] > num[i]:
#             num[i], num[j] = num[j], num[i]
# print('the result is:', num)

# 归并排序 时间O(Nlogn)
# 将数组二等分，然后递归，直到每个子数组只有两个元素，然后比较，再递归回来
# num = [3, 5, 8, 1, 4, 6, 2, 7, 9]
# def merge_sort(tup):
#     if len(tup) < 2:
#         return tup
#     mid = len(tup)//2
#     left = tup[:mid]
#     right = tup[mid:]
#     return merge(merge_sort(left), merge_sort(right))
# def merge(left, right):
#     res = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] > right[j]:
#             res.append(right[j])
#             j += 1
#         else:
#             res.append(left[i])
#             i += 1
#     if i < len(left):
#         res.extend(left[i:])
#     if j < len(right):
#         res.extend(right[j:])
#     return res
# print(merge_sort(num))

# 快速排序 时间O(Nlogn) 但是常数比归并小
# 选择第一个值作为轴，遍历数组，将大于轴的和小于轴的值分别放在轴的两边，然后重复操作
# num = [3, 5, 8, 1, 4, 6, 2, 7, 9]
# num = [6, 1, 2, 7, 9, 3, 4, 5, 8]
# def test(nums):
#     if len(nums) < 2:
#         return nums
#     mid = nums[0]
#     left = []
#     right = []
#     for i in nums[1:]:
#         if i > mid:
#             right.append(i)
#         else:
#             left.append(i)
#     return test(left) + [mid] + test(right)
# print(test(num))

