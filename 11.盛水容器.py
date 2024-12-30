# 给定一个数组，作为坐标轴的y轴值，序号作为坐标轴的x轴，视为容器的高和长，返回一个容积的最大值
# 以下方法对某些长数组会返回超时
height = [1,8,6,2,5,4,8,3,7]
maxV = 0
for i in range(len(height)):
    for j in range(i, len(height)):
        h = min(height[i], height[j])
        l = j - i
        maxV = max(h * l, maxV)
print(maxV)

height = [1,8,6,2,5,4,8,3,7]
maxV = 0

# 使用双指针法，重点在 if w * maxH < maxV: break ，当此时的指针间距也就是宽，与最长高度的乘积都无法比当前最大值大的时候，可以跳过所有循环
left = 0
right = len(height) - 1
maxH = max(height)
maxV = 0
while left != right:
    w = right - left
    if w * maxH < maxV:
        break
    h = min(height[left], height[right])
    maxV = max(maxV, h * (right - left))
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(maxV)

