from sortedcontainers import SortedSet

# 创建一个空的 SortedSet
s = SortedSet()

# 创建一个有初始值的 SortedSet
s = SortedSet([5, 1, 3, 4, 2])
print(s)  # 输出: SortedSet([1, 2, 3, 4, 5])

s.add(6)
print(s)  # 输出: SortedSet([1, 2, 3, 4, 5, 6])

s.discard(3)
print(s)  # 输出: SortedSet([1, 2, 4, 5, 6])

print(s[0])  # 输出: 1
print(s[-1])  # 输出: 6

# 获取前两个元素
print(s[:2])  # 输出: SortedSet([1, 2])


# 自定义排序规则：按元素的负数排序
s = SortedSet([5, 1, 3, 4, 2], key=lambda x: -x)
print(s)  # 输出: SortedSet([5, 4, 3, 2, 1])
