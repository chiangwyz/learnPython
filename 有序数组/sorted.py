from sortedcontainers import SortedSet

ss = SortedSet([5, 1, 3, 3])
print(ss)  # 输出: SortedSet([1, 3, 5])

ss.add(2)
print(ss)  # 输出: SortedSet([1, 2, 3, 5])

ss.discard(3)
print(ss)  # 输出: SortedSet([1, 2, 5])

print(ss[1])  # 输出: 2
